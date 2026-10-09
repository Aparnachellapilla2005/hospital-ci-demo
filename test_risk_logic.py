import unittest

from risk_logic import predict_risk


class TestRiskLogic(unittest.TestCase):

    def test_low_risk_case(self):
        result = predict_risk(24.9, 100)
        self.assertEqual(result, "LOW RISK")

    def test_high_risk_due_to_bmi(self):
        result = predict_risk(32.0, 100)
        self.assertEqual(result, "HIGH RISK")

    def test_high_risk_due_to_glucose(self):
        result = predict_risk(24.9, 180)
        self.assertEqual(result, "HIGH RISK")


if __name__ == "__main__":
    unittest.main()
