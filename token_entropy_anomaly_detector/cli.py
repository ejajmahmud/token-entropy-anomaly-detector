"""CLI for token-entropy-anomaly-detector."""
import sys
import argparse
from .detector import TokenEntropyAnomalyDetector


def main():
    parser = argparse.ArgumentParser(description="Token Entropy Anomaly Detector CLI")
    parser.add_argument("--demo", action="store_true", help="Run entropy anomaly detector demo")
    args = parser.parse_args()

    if args.demo:
        detector = TokenEntropyAnomalyDetector()
        clean = "Please write a Python function that parses JSON files."
        attack = "=========================================================================="
        obfuscated = "aGVsbG8gd29ybGQgdGhpcyBpcyBhbiBleGFtcGxlIG9mIGEgbG9uZyBlbmNvZGVkIHBheWxvYWQgd2hpY2ggaGFzIGhpZ2ggZW50cm9weQ=="

        for sample in [clean, attack, obfuscated]:
            rep = detector.analyze(sample)
            print(f"[*] Text: '{sample[:30]}...' -> Anomalous: {rep.is_anomalous} (H={rep.entropy:.2f}, Reason: {rep.reason})")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
