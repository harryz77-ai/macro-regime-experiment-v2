import unittest
import pandas as pd

import runner


class TestRunnerCore(unittest.TestCase):
    def test_rule_engine_identifies_r2_stress(self):
        features = {
            "us10y_level": 5.1,
            "us30y_level": 5.6,
            "us10y_20d_change_bp": 40.0,
            "us30y_20d_change_bp": 45.0,
            "dxy_20d_return": 4.0,
            "spy_20d_return": -7.0,
            "qqq_20d_return": -8.0,
            "iwm_spy_20d_relative": -4.0,
            "eem_spy_20d_relative": -5.0,
            "tlt_20d_return": -5.0,
            "hyg_20d_return": -4.0,
            "hy_oas_20d_change_bp": 90.0,
            "ig_oas_20d_change_bp": 30.0,
            "sovereign_spread_change_bp": 50.0,
        }
        result = runner.classify_regime(features, previous_regime=None)
        self.assertEqual(result["top_regime"], "R2")
        self.assertAlmostEqual(sum(result["posterior_probability"].values()), 1.0, places=8)

    def test_rule_engine_identifies_r3_repair(self):
        features = {
            "us10y_level": 3.8,
            "us30y_level": 4.1,
            "us10y_20d_change_bp": -40.0,
            "us30y_20d_change_bp": -35.0,
            "dxy_20d_return": -2.0,
            "spy_20d_return": 5.0,
            "qqq_20d_return": 6.0,
            "iwm_spy_20d_relative": 1.0,
            "eem_spy_20d_relative": 1.0,
            "tlt_20d_return": 6.0,
            "hyg_20d_return": 1.0,
            "hy_oas_20d_change_bp": -30.0,
            "ig_oas_20d_change_bp": -10.0,
        }
        result = runner.classify_regime(features, previous_regime=None)
        self.assertEqual(result["top_regime"], "R3")
        self.assertAlmostEqual(sum(result["posterior_probability"].values()), 1.0, places=8)

    def test_student_t_filter_graceful_fallback_on_small_panel(self):
        panel = pd.DataFrame({
            "us10y_20d_change_bp": [1.0, 2.0, 3.0],
            "dxy_20d_return": [0.1, 0.2, 0.3],
        })
        result = runner.run_student_t_filter(panel, previous_regime=None, temperature=1.25, min_rows=80)
        self.assertFalse(result["diagnostics"]["used"])
        self.assertAlmostEqual(sum(result["probability"].values()), 1.0, places=8)

    def test_change_point_score_graceful_fallback_on_small_panel(self):
        panel = pd.DataFrame({"us10y_20d_change_bp": [1.0, 2.0, 3.0]})
        result = runner.robust_change_point_score(panel)
        self.assertFalse(result["used"])
        self.assertEqual(result["risk_level"], "not_available")


if __name__ == "__main__":
    unittest.main()
