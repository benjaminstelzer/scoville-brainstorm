from __future__ import annotations

import unittest

from normalize_output import normalize


class NormalizeOutputTests(unittest.TestCase):
    def test_flattens_clusters_and_strips_process_signature(self) -> None:
        answer = {
            "activation": {"activated": True},
            "process": {"actual_generators": 5},
            "constraints": {"preserved": ["C1"], "violated": []},
            "research": {"sources_read": ["research/a.md"]},
            "idea_map": [
                {
                    "cluster": "event flow",
                    "candidates": [
                        {
                            "id": "i1",
                            "title": "Deferred merge",
                            "mechanism": "append locally then merge",
                            "prior_art": {
                                "label": "Adaptation",
                                "closest_match": "event sourcing",
                            },
                            "load_bearing_risk": "merge explosion",
                            "cheapest_falsification_experiment": "replay a conflict fixture",
                        }
                    ],
                }
            ],
            "shortlist": {"best_practical_leverage": "i1"},
            "traps": [{"reason": "Scoville Brainstorm-shaped padding"}],
            "deepened_directions": [
                {
                    "id": "i1",
                    "mechanism": "append locally then merge",
                    "closest_analogue": "event sourcing",
                    "exact_difference": "client-owned merge",
                    "benefit": "offline progress",
                    "load_bearing_risk": "merge explosion",
                    "cheapest_falsification_experiment": "replay a conflict fixture",
                }
            ],
            "decision_point": {"status": "awaiting_human_selection"},
        }
        result = normalize(answer, "ABC")
        self.assertNotIn("process", result)
        self.assertEqual(result["ideas"][0]["prior_art_label"], "Adaptation")
        self.assertEqual(result["ideas"][0]["falsification"], "replay a conflict fixture")
        self.assertEqual(result["deepened_directions"][0]["load_bearing_risk"], "merge explosion")
        self.assertEqual(result["traps"][0]["reason"], "[skill]-shaped padding")

    def test_preserves_negative_control(self) -> None:
        answer = {
            "activation": {"activated": False, "reason_code": "known_root_cause"},
            "response": {"answer_type": "canonical_fix"},
            "side_effects": {"files_read": []},
        }
        result = normalize(answer, "DEF")
        self.assertFalse(result["activation"])
        self.assertEqual(result["reason_code"], "known_root_cause")


if __name__ == "__main__":
    unittest.main()
