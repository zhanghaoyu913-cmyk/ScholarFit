import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ItemBankTests(unittest.TestCase):
    def test_chapter_files_have_ten_items(self):
        chapter_files = sorted((ROOT / "item_bank").glob("chapter_*.json"))
        self.assertEqual(len(chapter_files), 8)
        total = 0
        for path in chapter_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(len(payload["items"]), 10, path.name)
            total += len(payload["items"])
        self.assertEqual(total, 80)

    def test_item_ids_are_unique(self):
        ids = []
        for path in sorted((ROOT / "item_bank").glob("chapter_*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            ids.extend(item["id"] for item in payload["items"])
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
