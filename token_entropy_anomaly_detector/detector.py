"""Core Token Entropy Anomaly Detector implementation."""
import math
import re
from collections import Counter
from typing import Dict, Any


class AnomalyReport:
    def __init__(self, is_anomalous: bool, entropy: float, reason: str = ""):
        self.is_anomalous = is_anomalous
        self.entropy = entropy
        self.reason = reason


class TokenEntropyAnomalyDetector:
    def __init__(self, min_safe_entropy: float = 1.2, max_safe_entropy: float = 4.8):
        self.min_safe_entropy = min_safe_entropy
        self.max_safe_entropy = max_safe_entropy

    def calculate_entropy(self, text: str) -> float:
        if not text:
            return 0.0
        counts = Counter(text)
        total = float(len(text))
        return -sum((c / total) * math.log2(c / total) for c in counts.values())

    def analyze(self, text: str) -> AnomalyReport:
        if not text.strip():
            return AnomalyReport(False, 0.0, "Empty text")

        h = self.calculate_entropy(text)

        # Check for repetitive delimiter flood
        if len(text) > 30 and (text.count("=") > len(text) * 0.4 or text.count("-") > len(text) * 0.5):
            return AnomalyReport(True, h, "Delimiter flood attack pattern detected")

        # Check for high-entropy obfuscation
        if h > self.max_safe_entropy and len(text) > 40:
            return AnomalyReport(True, h, f"Excessive entropy ({h:.2f} bits) suggests encoded payload")

        return AnomalyReport(False, h, "Safe normal distribution")
