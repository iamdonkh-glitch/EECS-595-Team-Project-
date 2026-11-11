"""ROPE data loading.

Pieces marked MOH are copied from sled-group/moh @ 9483f2e4a69a90aee339b2305c1f5866daeba1a0
(data_handler.py, evaluation.py, image_processor.py). The moh repo has no license file:
attribution only, do not redistribute.
"""
import json
import os

from .constant import TRAIN_CLASSES, VALIDATION_CLASSES

SPLITS = {"train": "Seen", "validation": "Unseen"}

# MOH: data_handler.py DataHandler.load_data, json_files list (verbatim).
JSON_FILES = [
    "AAAAB_data.json",
    "BAAAA_data.json",
    "merged_heterogenous_data.json",
    "merged_homogenous_data.json",
    "merged_mixed_data.json"
]

# MOH: data_handler.py DataHandler.file2folder, file2folder_dict (verbatim).
# Our CLI subset names are moh's folder names.
file2folder_dict = {
    "AAAAB_data.json": "AAAAB",
    "BAAAA_data.json": "BAAAA",
    "merged_heterogenous_data.json": "heterogenous",
    "merged_homogenous_data.json": "homogenous",
    "merged_mixed_data.json": "mixed"
}
SUBSETS = list(file2folder_dict.values())
folder2file = {v: k for k, v in file2folder_dict.items()}


def load_subset(dataset_path, split, subset):
    """Load one JSON file. Same file layout as moh DataHandler.load_data(split)[file]."""
    if split not in SPLITS:
        raise ValueError(f"split must be train or validation, got {split}")
    with open(os.path.join(dataset_path, split, folder2file[subset]), "r") as f:
        return json.load(f)


def image_path(dataset_path, entry):
    # MOH: evaluation.py process_entry: `self.dataset_path + entry["folder"].replace("jpg", "png")`
    # (verbatim; `folder` points at the bbox/ PNG, so the model sees boxes drawn on the image).
    path = dataset_path + entry["folder"].replace("jpg", "png")
    # NEW: the HF train.zip unpacks to train/images/ while the JSONs say train/image/
    # (validation unpacks to image/). Fall back to the plural folder when it exists.
    if not os.path.exists(path):
        alt = path.replace("/image/", "/images/", 1)
        if os.path.exists(alt):
            return alt
    return path


def load_image(path):
    from PIL import Image
    image = Image.open(path)
    # MOH: image_processor.py ImageProcessor.preprocess_image (verbatim body).
    if image.mode == "RGBA":
        image = image.convert("RGB")
    return image


def get_class_list(data_type, dataset_name):
    """MOH: evaluation.py *_generate_prompt class-list branch (verbatim, self.data_type -> data_type)."""
    if data_type == 'train':
        if dataset_name == "COCO":
            class_list = ", ".join(TRAIN_CLASSES["COCO"])
        elif dataset_name == "ADE":
            class_list = ", ".join(TRAIN_CLASSES["ADE"])
        else:
            raise ValueError(f"Unknown dataset: {dataset_name}")
    else:
        if dataset_name == "COCO":
            class_list = ", ".join(VALIDATION_CLASSES["COCO"])
        elif dataset_name == "ADE":
            class_list = ", ".join(VALIDATION_CLASSES["ADE"])
        else:
            raise ValueError(f"Unknown dataset: {dataset_name}")
    return class_list


def candidates(split, data_source):
    """The 50-class candidate list as a Python list (same order as moh)."""
    return (TRAIN_CLASSES if split == "train" else VALIDATION_CLASSES)[data_source]


def iter_items(dataset_path, split, subset, limit=None):
    """Yield (entry_idx, image_id, entry). entry_idx is the position in the JSON file;
    image_id is the PNG stem. Note: validation/mixed has two PNGs that appear twice with
    different object lists (entries 184/1170 and 256/1171), so (image_id, entry_idx) is the key."""
    entries = load_subset(dataset_path, split, subset)
    if limit is not None:
        entries = entries[:limit]
    for idx, entry in enumerate(entries):
        stem = os.path.splitext(os.path.basename(entry["folder"]))[0]
        yield idx, stem, entry


def gold_labels(entry):
    # moh compares against entry["objects"][i]["name"].lower()
    return [o["name"].lower() for o in entry["objects"]]
