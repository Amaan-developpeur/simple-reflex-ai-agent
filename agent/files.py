from pathlib import Path
import os

def image_paths(base_dir=None):
    if base_dir is None:
        # Go up 2 levels: agent/ → project root → parent of project
        base_dir = Path(__file__).resolve().parent.parent.parent / "split" / "val"

    print(f"📂 Looking in: {base_dir}")
    if not base_dir.exists():
        raise FileNotFoundError(f"❌ Directory not found: {base_dir}")

    image_paths = []
    for class_folder in os.listdir(base_dir):
        class_path = base_dir / class_folder
        for filename in os.listdir(class_path):
            image_paths.append(str(class_path / filename))

    return image_paths
