# Do Multimodal Reasoning Models Talk Themselves into Hallucination? Self-Induced Inertia in Multi-Object Recognition

Oct 26, 2026 · @Carl Song

We test whether RL-trained multimodal reasoning models amplify or correct self-induced inertia in multi-object recognition. We measure it on ROPE and try to reduce it with a per-object GRPO reward.

## Why this project

Reasoning-trained VLMs now think at length before they answer, and nobody knows whether that thinking talks them into mistakes they would otherwise avoid. ROPE lets us test this cleanly, and we found no work that runs it on reasoning models.

### What a ROPE item looks like

*Illustrative example, not an actual ROPE item.* A dining-room photo has five numbered red boxes: boxes 1–4 are chairs and box 5 is the table, an AAAAB item. The model answers `obj1: … obj5: …`, picking each label from a candidate list.

- **Correct:** chair, chair, chair, chair, dining table
- **Inertia error:** chair, chair, chair, chair, **chair**

### The gap: self-induced inertia

Prior work plants a misleading text cue beside the image, such as a hint that names a wrong answer ([Sánchez Villegas et al., 2026](https://arxiv.org/abs/2604.14888)). In an AAAAB item nobody plants anything. The pull comes from the model's own four "chair" answers.

Long reasoning could go either way:

- **Amplify:** `<think>Boxes 1–4 are chairs around the table; box 5 is by the table, so probably another chair.</think> obj5: chair`
- **Correct:** `<think>Boxes 1–4 are chairs. Wait, box 5 is larger and flat; it is the table.</think> obj5: dining table`

Which one wins is our core question. It matters beyond ROPE: real scenes hold many objects, and the same paper found fluent reasoning can look visually grounded while following the cue, so these errors are hard to spot.

### Why same-base model pairs

MiMo-VL-7B-RL comes from the SFT model through one more post-training stage (MORL), so the gap between them is mostly RL ([Xiaomi, 2025](https://arxiv.org/abs/2506.03569)). That is testing one student before and after a training camp, not comparing students from two schools. Unrelated models would mix in different bases, data, and image resolutions.

- **MiMo-VL-7B SFT vs RL:** what RL training does to inertia. A hypothetical reading: 20% inertia for SFT and 35% for RL would mean RL amplifies it.
- **Qwen3-VL-8B Instruct vs Thinking:** what turning thinking on does.

Together the pairs separate "RL changed the weights" from "the model just thinks longer."

### Why a per-object reward

Take the chairs-and-table item and four made-up sampled answers. GRPO's advantage is (reward − group mean) / group standard deviation.

| Sample | Answer (obj1–5) | Correct | All-or-nothing: reward → advantage | Per-object: reward → advantage |
| --- | --- | --- | --- | --- |
| r1 | chair chair chair chair table | 5/5 | 1 → +1.5 | 1.0 → +0.99 |
| r2 | chair chair chair chair chair | 4/5 (inertia) | 0 → −0.5 | 0.8 → +0.20 |
| r3 | chair chair sofa chair table | 4/5 | 0 → −0.5 | 0.8 → +0.20 |
| r4 | chair stool sofa chair chair | 2/5 | 0 → −0.5 | 0.4 → −1.39 |

- **All-or-nothing** punishes r2 (one error) as hard as r4 (three errors). If no sample gets 5/5, every reward is 0 and the item teaches nothing.
- **Per-object** gives partial credit, so almost every item carries signal.
- **Catch:** r2's inertia error still earns a positive advantage. An inertia penalty, such as −0.5 when B is labeled A, drops r2's reward to 0.3 and makes its advantage negative.

Rewards come straight from COCO/ADE20K annotations, so no human or LLM judge is needed.

### Why it fits a course project

- **Cheap:** single-GPU jobs, about 60–100 A40 GPU-hours in total (our estimate).
- **Clean scoring:** labels come from a candidate list, so accuracy is automatic.
- **Four natural angles:** one research question per member (see Team).
- **Specific feedback:** ROPE comes from the instructor's lab.

For the 2-page submission, this section shrinks to two or three sentences inside Problem.

## Problem

Reasoning-trained VLMs gain on math and chart benchmarks, but they look at the image less as their reasoning grows longer ([Liu et al., 2025](https://arxiv.org/abs/2505.21523); [Tian et al., 2026](https://arxiv.org/abs/2509.25848)). Their early commitments also tend to be reinforced rather than revised during reasoning, and misleading text cues sway them ([Sánchez Villegas et al., 2026](https://arxiv.org/abs/2604.14888)). We ask whether a model's **own** earlier answers cause the same inertia when it labels several objects in one image.

1. **RQ1.** On ROPE, do reasoning versions hallucinate more or less than non-reasoning versions of the same base model, split by object-class composition?
2. **RQ2.** On the Adversarial split (AAAAB), how often is the fifth object labeled A, and does longer reasoning raise or lower that rate?
3. **RQ3.** Which errors does reasoning change: invented classes, classes borrowed from other objects in the image, or inertia?
4. **RQ4 (stretch).** Does GRPO with a per-object reward reduce inertia without hurting general reasoning?

## Approach

We compare same-base model pairs with and without reasoning post-training, using ROPE's probes plus two of our own.

- **Model pairs:** [MiMo-VL-7B](https://arxiv.org/abs/2506.03569) SFT vs RL; [Qwen3-VL-8B](https://openrouter.ai/models/qwen/qwen3-vl-8b-thinking) Instruct vs Thinking. Optional: one API model with adjustable reasoning effort.
- **Probes:** ROPE Default (all five objects in one turn) and Single-object (one object per turn). A prefix probe gives the true labels of objects 1–4 and asks only for object 5. A budget sweep caps thinking at several lengths.
- **Metrics:** per-object accuracy, plus three error types: *invented* (a class absent from the image), *borrowed* (the class of another object in the image), and *inertia* (on AAAAB, object 5 labeled A). We also check think–answer consistency: does the reasoning name the same class as the final answer?
- **Fix (RQ4):** build ROPE-style training images from COCO and ADE20K annotations, disjoint from ROPE's test images. Train a 3B VLM with [GRPO](https://arxiv.org/abs/2402.03300) under a per-object reward versus an all-or-nothing reward, and check [MathVista](https://arxiv.org/abs/2310.02255) for regressions.

## Data

[ROPE](https://arxiv.org/abs/2407.06192) is the test set. Its images come from [MSCOCO](https://arxiv.org/abs/1405.0312) (panoptic annotations) and [ADE20K](https://arxiv.org/abs/1608.05442), each with five objects marked by numbered red boxes. Models pick each label from a candidate list, so scoring is automatic.

- **Subsets:** Homogeneous (AAAAA), Heterogeneous (ABCDE), Adversarial (AAAAB), and In-the-Wild (mixed classes, random order).
- **Splits:** Seen and Unseen, following the source datasets' original train/val split; about 10k rows on [HuggingFace](https://huggingface.co/datasets/sled-umich/ROPE).
- **Training data (RQ4):** COCO and ADE20K annotations, excluding every ROPE image.
- **Open question:** how the HuggingFace train/validation splits map to Seen/Unseen.

## Related work

We found no prior work testing ROPE on reasoning models (search as of Oct 26, 2026); the closest papers each cover one piece.

| Work | Finding | What we add |
| --- | --- | --- |
| [ROPE](https://arxiv.org/abs/2407.06192) (Chen et al., NeurIPS 2024) | Multi-object queries cause more hallucination; class composition drives shortcuts | Reasoning models released after ROPE |
| [POPE](https://arxiv.org/abs/2305.10355) (Li et al., EMNLP 2023) | Probes whether single objects exist | Several objects with controlled class order |
| [RH-Bench](https://arxiv.org/abs/2505.21523) (Liu et al., 2025) | Longer reasoning lowers attention to the image | Isolates inertia from earlier object labels |
| [VAPO](https://arxiv.org/abs/2509.25848) (Tian et al., ICLR 2026) | RL reasoning harms basic recognition | Per-object error types, not overall accuracy |
| [Reasoning Dynamics](https://arxiv.org/abs/2604.14888) (Sánchez Villegas et al., COLM 2026) | Answer inertia; misleading text cues sway models | Inertia from the model's own outputs |
| [MM-THEBench](https://arxiv.org/abs/2601.22735) (Huang et al., 2026) | Hallucination inside reasoning traces | Controlled multi-object compositions |
| [DO-Bench](https://arxiv.org/abs/2604.22822) (Wang et al., 2026) | Separates perception errors from text-prior errors | The same split for multiple objects and reasoning models |
| [MIOH](https://arxiv.org/abs/2608.30653) (Min et al., CVPR 2026) | Object hallucination across several images | Several objects within one image |

## Plan

The evaluation study (RQ1–RQ3) is the core; RQ4 starts only after the main runs finish.

1. **Oct 27–Nov 2:** pilot MiMo-VL SFT vs RL on 100 images per subset (Default, Single-object); confirm output parsing and a measurable gap.
2. **Nov 3–15:** evaluation harness; full runs for both model pairs on all subsets (RQ1).
3. **Nov 16–29:** budget sweep, prefix probe, and error taxonomy (RQ2, RQ3); GRPO data and first training runs (RQ4).
4. **Nov 30–Dec 6:** analysis and slides for the Dec 7 and Dec 9 presentations.
5. **Dec 7–16:** final runs, error analysis, and the report due Dec 16.

Fallbacks: if RQ4 slips, RQ1–RQ3 stand alone. If the pilot shows no gap between versions, the budget sweep becomes the main axis.

## Team

Four members, one research question each. Names go in the OpenReview form, not the blind PDF.

| Member | Owns | Question |
| --- | --- | --- |
| Member 1 | Evaluation harness and paired-model runs | RQ1 |
| Member 2 | Budget sweep and think–answer consistency | RQ2 |
| Member 3 | Error taxonomy; object size, salience, and frequency analysis | RQ3 |
| Member 4 | GRPO training data, rewards, and runs | RQ4 |

Open question: Team ID (needed for submission).

## References

- Chen, X., Ma, Z., et al. 2024. [Multi-Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2407.06192). NeurIPS.
- Huang, Z., Yao, Z., et al. 2026. [MM-THEBench: Do Reasoning MLLMs Think Reasonably?](https://arxiv.org/abs/2601.22735) arXiv.
- Li, Y., Du, Y., et al. 2023. [Evaluating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2305.10355). EMNLP.
- Lin, T.-Y., Maire, M., et al. 2014. [Microsoft COCO: Common Objects in Context](https://arxiv.org/abs/1405.0312). ECCV.
- Liu, C., Xu, Z., et al. 2025. [More Thinking, Less Seeing? Assessing Amplified Hallucination in Multimodal Reasoning Models](https://arxiv.org/abs/2505.21523). arXiv.
- Lu, P., Bansal, H., et al. 2024. [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://arxiv.org/abs/2310.02255). ICLR.
- Min, J., Kim, C., et al. 2026. [Fine-Grained Multi Image Object Hallucination Benchmark](https://arxiv.org/abs/2608.30653). CVPR.
- Sánchez Villegas, D., Lewis-Lim, S., Aletras, N., and Elliott, D. 2026. [Reasoning Dynamics and the Limits of Monitoring Modality Reliance in Vision-Language Models](https://arxiv.org/abs/2604.14888). COLM.
- Shao, Z., Wang, P., et al. 2024. [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300). arXiv.
- Tian, X., Zou, S., et al. 2026. [More Thought, Less Accuracy? On the Dual Nature of Reasoning in Vision-Language Models](https://arxiv.org/abs/2509.25848). ICLR.
- Wang, J., Chen, J., et al. 2026. [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822). arXiv.
- Xiaomi LLM-Core Team. 2025. [MiMo-VL Technical Report](https://arxiv.org/abs/2506.03569). arXiv.
- Zhou, B., Zhao, H., et al. 2019. [Semantic Understanding of Scenes through the ADE20K Dataset](https://arxiv.org/abs/1608.05442). IJCV.
