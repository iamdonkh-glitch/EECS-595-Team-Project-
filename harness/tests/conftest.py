import os
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
MOH = os.path.join(CODE, "third_party", "moh")
FIXTURE = os.path.join(HERE, "fixtures", "ROPE")
sys.path.insert(0, CODE)


@pytest.fixture(scope="session")
def moh():
    """moh's own evaluation module (needs PIL). Imported from the clone, not our copy."""
    sys.path.insert(0, MOH)
    import evaluation
    return evaluation


SUBS = ["AAAAB", "BAAAA", "heterogenous", "homogenous", "mixed"]


@pytest.fixture
def entries():
    """validation fixture entries by subset"""
    from rope_runner.data import load_subset
    return {s: load_subset(FIXTURE, "validation", s) for s in SUBS}


@pytest.fixture
def png_root(tmp_path):
    """Write a 4x4 PNG at every fixture entry's path so moh's Image.open works."""
    from PIL import Image
    from rope_runner.data import image_path, load_subset
    root = str(tmp_path / "ROPE")
    for sp in ["train", "validation"]:
        for e in [e for s in SUBS for e in load_subset(FIXTURE, sp, s)]:
            p = image_path(root, e)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            Image.new("RGB", (4, 4)).save(p)
    return root
