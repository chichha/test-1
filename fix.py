"""
Fix CardList.json: set each card's "id" to its object key.

Usage:
    python fix_card_ids.py CardList.json
"""

import json
import sys

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "CardList.json"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for key, card in data.items():
        card["id"] = key

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Fixed {len(data)} cards in {path}")

if __name__ == "__main__":
    main()