"""NEW (moh has no vLLM / Qwen3-VL / MiMo-VL handler). vLLM wrapper plus think-tag stripping.

vLLM and transformers are imported lazily so the pure-Python parts (strip_think, the fake
model used by --dry-run and the tests) run on CPU without them.
"""
import os

from .prompts import chat_messages

THINK_OPEN, THINK_CLOSE = "<think>", "</think>"
_TRAILING_SPECIAL = ("<|im_end|>", "<|endoftext|>")


def strip_think(text, think_prefilled=False):
    """Split a generation into (trace, answer, closed).
    closed=True   a </think> was emitted: answer = text after the LAST </think>.
    closed=False  thinking was open (<think> emitted, or prefilled by the chat template as in
                  Qwen3-VL-Thinking) but never closed: everything is trace, answer is "".
    closed=None   no thinking at all (Instruct, /no_think without tags): answer = whole text."""
    t = text
    for s in _TRAILING_SPECIAL:
        t = t.replace(s, "")
    if THINK_CLOSE in t:
        trace, ans = t.rsplit(THINK_CLOSE, 1)
        if THINK_OPEN in trace:
            trace = trace.split(THINK_OPEN, 1)[1]
        return trace.strip(), ans.strip(), True
    if THINK_OPEN in t or think_prefilled:
        return t.split(THINK_OPEN, 1)[-1].strip(), "", False
    return "", t.strip(), None


def expand(path):
    os.environ.setdefault("MODELS_DIR", os.path.expanduser("~/cse595/models"))
    return os.path.expandvars(os.path.expanduser(path))


def sampling_dict(model_cfg, greedy, seed):
    if greedy:
        return {"mode": "greedy", "temperature": 0.0, "seed": seed}
    d = {"mode": "recommended", **model_cfg["sampling"], "seed": seed}
    return d


class VLLMModel:
    """Offline vLLM engine. Prompts are rendered with the model's own HF chat template and
    sent as raw strings, so continuations (truncate-and-close) are exact string prefixes."""

    def __init__(self, name, model_cfg, defaults, greedy=False, seed=0, prefix_caching=None):
        """prefix_caching: None = vLLM's default (on in vLLM 0.11's V1 engine), True/False = force."""
        from transformers import AutoProcessor
        from vllm import LLM
        self.name, self.cfg = name, model_cfg
        self.path = expand(model_cfg["path"])
        self.family = model_cfg["family"]
        self.thinking = bool(model_cfg.get("thinking", False))
        self.processor = AutoProcessor.from_pretrained(self.path)
        kw = dict(
            model=self.path,
            dtype=defaults.get("dtype", "bfloat16"),
            # ROPE_MAX_MODEL_LEN / ROPE_GPU_MEM_UTIL (set by scripts/run.sbatch from the card's
            # memory) override the config so a 40 GB card does not OOM.
            max_model_len=int(os.environ.get("ROPE_MAX_MODEL_LEN") or model_cfg.get("max_model_len", defaults["max_model_len"])),
            gpu_memory_utilization=float(os.environ.get("ROPE_GPU_MEM_UTIL") or defaults.get("gpu_memory_utilization", 0.90)),
            limit_mm_per_prompt=defaults.get("limit_mm_per_prompt", {"image": 1}),
            seed=seed,
        )
        if prefix_caching is not None:
            kw["enable_prefix_caching"] = bool(prefix_caching)
        self.prefix_caching = prefix_caching
        if model_cfg.get("mm_processor_kwargs"):
            kw["mm_processor_kwargs"] = model_cfg["mm_processor_kwargs"]
        self.llm = LLM(**kw)
        self.tokenizer = self.llm.get_tokenizer()
        self.sampling = sampling_dict(model_cfg, greedy, seed)

    def render(self, text):
        return self.processor.apply_chat_template(
            chat_messages(text, self.family), tokenize=False, add_generation_prompt=True)

    def count_tokens(self, text):
        return len(self.tokenizer.encode(text, add_special_tokens=False)) if text else 0

    def generate(self, prompts, images, max_tokens, stop=None):
        """Returns list of (text, n_generated_tokens, finish_reason, n_prompt_tokens,
        n_cached_prompt_tokens). Prompt tokens include the image placeholder tokens; cached =
        vLLM's prefix-cache hits (None when vLLM does not report it).
        stop: optional list of stop strings; the matched string is kept in the text (NEW, used
        to end the thinking stage at </think> before an assistant-turn prefill).
        max_tokens: one cap for all prompts, or a list with one cap per prompt (NEW, used for the
        answer stage after an assistant-turn prefill)."""
        from vllm import SamplingParams
        s = {k: v for k, v in self.sampling.items() if k != "mode"}
        if stop:
            s.update(stop=list(stop), include_stop_str_in_output=True)
        if isinstance(max_tokens, (list, tuple)):
            sp = [SamplingParams(max_tokens=int(n), skip_special_tokens=False, **s) for n in max_tokens]
        else:
            sp = SamplingParams(max_tokens=max_tokens, skip_special_tokens=False, **s)
        reqs = [{"prompt": p, "multi_modal_data": {"image": im}} for p, im in zip(prompts, images)]
        outs = self.llm.generate(reqs, sp, use_tqdm=True)
        return [(o.outputs[0].text, len(o.outputs[0].token_ids), o.outputs[0].finish_reason,
                 len(o.prompt_token_ids or []), getattr(o, "num_cached_tokens", None)) for o in outs]


class FakeModel:
    """CPU stand-in for --dry-run and tests: answers with the gold labels in moh's format,
    wrapped in a <think> block, so the full pipeline (render, strip, parse, score, write,
    resume) runs without a GPU. answer_for[(rendered_prompt, image)] = answer text; in --dry-run
    the "image" is the image path, so identical prompts for different images stay distinct."""

    family = "qwen3vl"
    thinking = True  # always wraps its answer in <think>...</think>

    def __init__(self, name="fake", think_tokens=40, prefix_caching=None):
        self.name, self.path, self.think_tokens = name, "fake://", think_tokens
        self.prefix_caching = prefix_caching
        self.sampling = {"mode": "fake"}
        self.answer_for = {}  # (prompt, image) -> answer text

    def render(self, text):
        return f"<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>{text}<|im_end|>\n<|im_start|>assistant\n"

    def count_tokens(self, text):
        return len(text.split())

    def _cached(self, p, im, earlier):
        """Simulated prefix cache: longest shared word prefix with an earlier prompt in this
        batch on the same image (only when prefix caching is on)."""
        if not self.prefix_caching:
            return 0
        w, best = p.split(), 0
        for q, qim in earlier:
            if qim != im:
                continue
            n = 0
            for a, b in zip(w, q.split()):
                if a != b:
                    break
                n += 1
            best = max(best, n)
        return best

    def generate(self, prompts, images, max_tokens, stop=None):
        caps = list(max_tokens) if isinstance(max_tokens, (list, tuple)) else [max_tokens] * len(prompts)
        out = [self._generate_one(p, im, n, stop) for p, im, n in zip(prompts, images, caps)]
        earlier = []
        for i, (p, im) in enumerate(zip(prompts, images)):
            out[i] = out[i] + (self.count_tokens(p), self._cached(p, im, earlier))
            earlier.append((p, im))
        return out

    def _generate_one(self, p, im, max_tokens, stop=None):
        head = p.split("<|im_start|>assistant\n")[0] + "<|im_start|>assistant\n"
        tail = p[len(head):]
        if tail:  # continuation: after a forced close, or after an assistant-turn prefill
            body = self.answer_for.get((head, im), "")
            done = tail.rsplit("</think>", 1)[-1].lstrip("\n") if "</think>" in tail else tail
            if done and body.startswith(done):
                body = body[len(done):]
            if self.count_tokens(body) > max_tokens:  # keep the leading space: "obj5:" + " dog"
                lead = body[:len(body) - len(body.lstrip())]
                return (lead + " ".join(body.split()[:max_tokens]), max_tokens, "length")
            return (body, self.count_tokens(body), "stop")
        ans = self.answer_for.get((p, im), "")
        think = " ".join(["hmm"] * self.think_tokens)
        full = f"<think>\n{think}\n</think>\n\n{ans}"
        for s in stop or []:
            if s in full:
                full = full[:full.index(s) + len(s)]
        toks = full.split()
        if len(toks) > max_tokens:
            return (" ".join(toks[:max_tokens]), max_tokens, "length")
        return (full, len(toks), "stop")
