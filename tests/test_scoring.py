import unittest

from scholarfit.scoring import score_item, score_items, summarize_constructs


class RuleScoringTests(unittest.TestCase):
    def test_sjt_scoring(self):
        item = {
            "id": "T1",
            "type": "situational_judgment",
            "scoring": {"A": {"research_self_efficacy.debugging": 2}},
        }
        result = score_item(item, "A")
        self.assertEqual(result.scores["research_self_efficacy.debugging"], 2)

    def test_ranking_scoring(self):
        item = {
            "id": "T2",
            "type": "ranking",
            "scoring": {
                "position_weights": [2, 1, 0],
                "options": {
                    "A": {"research_behavior.systematicity": 1},
                    "B": {"stress_recovery.restoration": 1},
                },
            },
        }
        result = score_item(item, ["A", "B"])
        self.assertEqual(result.scores["research_behavior.systematicity"], 2)
        self.assertEqual(result.scores["stress_recovery.restoration"], 1)

    def test_summary_confidence(self):
        items = [
            {"id": "A", "type": "situational_judgment", "scoring": {"X": {"motivation.intrinsic": 1}}},
            {"id": "B", "type": "situational_judgment", "scoring": {"X": {"motivation.intrinsic": 1}}},
            {"id": "C", "type": "situational_judgment", "scoring": {"X": {"motivation.intrinsic": 1}}},
        ]
        result = score_items(items, {"A": "X", "B": "X", "C": "X"})
        summary = summarize_constructs(result)
        self.assertEqual(summary["motivation.intrinsic"]["confidence"], "medium")


if __name__ == "__main__":
    unittest.main()
