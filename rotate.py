"""
Rotate Mission card images (MSS*) by 90 degrees.

Usage:
    python rotate_missions.py [images_folder]

Default folder: naruto_cards/images
"""

import sys
from pathlib import Path
from PIL import Image

def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("images")

    if not folder.exists():
        print(f"Folder not found: {folder}")
        sys.exit(1)

    rotated = 0
    for filepath in sorted(folder.iterdir()):
        if filepath.stem.startswith("MSS 04") and filepath.suffix.lower() in (".webp", ".png", ".jpg", ".jpeg"):
            print(f"  Rotating: {filepath.name}")
            img = Image.open(filepath)
            img = img.rotate(-90, expand=True)
            img.save(filepath)
            rotated += 1

    print(f"\nDone. {rotated} images rotated.")

if __name__ == "__main__":
    main()