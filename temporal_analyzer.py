from collections import deque

class TemporalAnalyzer:
    def __init__(self, maxlen=6):
        self.history = deque(maxlen=maxlen)

    def add_score(self, score):
        self.history.append(score)

    def trend(self):
        if len(self.history) < 2:
            return {
                "trend": "insufficient_data",
                "delta": 0.0,
                "worsening": False
            }

        delta = round(self.history[-1] - self.history[0], 2)

        if delta > 0.15:
            label = "worsening"
        elif delta < -0.15:
            label = "improving"
        else:
            label = "stable"

        return {
            "trend": label,
            "delta": delta,
            "worsening": delta > 0.15
        }
