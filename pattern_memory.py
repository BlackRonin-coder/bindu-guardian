from collections import Counter

class PatternMemory:
    def __init__(self):
        self.counter = Counter()

    def record(self, signals):
        key = tuple(sorted(signals))
        self.counter[key] += 1

    def recall(self, signals):
        key = tuple(sorted(signals))
        seen = self.counter[key]
        return {
            "pattern": list(key),
            "seen_count": seen,
            "familiar": seen > 0
        }
