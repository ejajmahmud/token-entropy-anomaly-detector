"""Unit tests for token-entropy-anomaly-detector."""
import unittest
from token_entropy_anomaly_detector.detector import TokenEntropyAnomalyDetector


class TestTokenEntropyAnomalyDetector(unittest.TestCase):
    def test_clean_text_normal(self):
        d = TokenEntropyAnomalyDetector()
        rep = d.analyze("Standard English prompt with natural character distributions.")
        self.assertFalse(rep.is_anomalous)

    def test_delimiter_flood_anomaly(self):
        d = TokenEntropyAnomalyDetector()
        rep = d.analyze("------------------------------------------------------------")
        self.assertTrue(rep.is_anomalous)
        self.assertIn("Delimiter", rep.reason)
