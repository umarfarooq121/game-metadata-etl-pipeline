import json
from pathlib import Path


MANIFEST_PATH = Path("images/downloads/image_manifest.json")


def load_image_manifest():
    if not MANIFEST_PATH.exists():
        return {}

    with MANIFEST_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_image_manifest(manifest):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)

    with MANIFEST_PATH.open("w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=4)