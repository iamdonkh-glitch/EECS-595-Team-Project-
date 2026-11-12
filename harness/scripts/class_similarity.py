"""NEW. Cosine similarity between the class names of each ROPE candidate list, for the counterfactual
probe's near / far choice of the wrong class C (run.py --cf-class near|far).

  python harness/scripts/class_similarity.py <dir of all-mpnet-base-v2> > harness/configs/class_similarity.json

Embeds every class name of the four 50-class lists (Seen/Unseen x COCO/ADE) with
sentence-transformers/all-mpnet-base-v2 at the revision below: mean pooling over tokens, then L2
normalisation, as the model's own sentence-transformers config does. Writes
{"model", "revision", "lists": {"<split>/<data_source>": {"classes": [...], "cos": [[...], ...]}}},
cosines rounded to 4 decimals. Runs on CPU in seconds.
"""
import json
import os
import sys

import torch
from transformers import AutoModel, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from rope_runner.constant import TRAIN_CLASSES, VALIDATION_CLASSES  # noqa: E402

MODEL = "sentence-transformers/all-mpnet-base-v2"
REVISION = "e8c3b32edf5434bc2275fc9bab85f82640a19130"


def embed(names, tok, model):
    batch = tok(names, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        out = model(**batch).last_hidden_state
    mask = batch["attention_mask"].unsqueeze(-1).float()
    vec = (out * mask).sum(1) / mask.sum(1)
    return torch.nn.functional.normalize(vec, dim=1)


def main(model_dir):
    tok = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModel.from_pretrained(model_dir).eval()
    parts = []
    for split, table in (("train", TRAIN_CLASSES), ("validation", VALIDATION_CLASSES)):
        for src, names in table.items():
            names = [n.lower() for n in names]
            v = embed(names, tok, model)
            rows = ",\n      ".join(json.dumps([round(x, 4) for x in row]) for row in (v @ v.T).tolist())
            parts.append(f'  "{split}/{src}": {{\n    "classes": {json.dumps(names)},\n'
                         f'    "cos": [\n      {rows}\n    ]\n  }}')
    # one matrix row per line keeps the file readable and diffable
    print('{\n "model": "%s",\n "revision": "%s",\n "lists": {\n%s\n }\n}'
          % (MODEL, REVISION, ",\n".join(parts)))


if __name__ == "__main__":
    main(sys.argv[1])
