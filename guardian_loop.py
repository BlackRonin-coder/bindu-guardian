import json
from datetime import datetime

THREAT_LADDER = [
    "observe",
    "reinforce",
    "stabilize",
    "isolate",
    "restore",
    "escalate"
]


class GuardianLoop:
    def __init__(self):
        self.history = []

    def log(self, event, data):
        self.history.append({
            "time": datetime.now().isoformat(),
            "event": event,
            "data": data
        })

    def evaluate(self, signals):
        score = 0

        if "access_anomaly" in signals:
            score += 0.2
        if "system_instability" in signals:
            score += 0.2
        if "data_integrity_risk" in signals:
            score += 0.3
        if "spread_detected" in signals:
            score += 0.3

        score = round(min(score, 1.0), 2)
        return score

    def choose_action(self, score):
        if score < 0.2:
            return "observe"
        elif score < 0.4:
            return "reinforce"
        elif score < 0.6:
            return "stabilize"
        elif score < 0.8:
            return "isolate"
        elif score < 0.95:
            return "restore"
        else:
            return "escalate"

    def respond(self, action):
        responses = {
            "observe": "Monitoring system. No action required.",
            "reinforce": "Reminder: follow safe procedures.",
            "stabilize": "Restricting risky operations.",
            "isolate": "Segmenting affected systems.",
            "restore": "Restoring trusted state.",
            "escalate": "Alerting human leadership."
        }
        return responses[action]

    def run(self, signals):
        score = self.evaluate(signals)
        action = self.choose_action(score)
        response = self.respond(action)

        result = {
            "signals": signals,
            "score": score,
            "action": action,
            "response": response
        }

        self.log("decision", result)
        return result


if __name__ == "__main__":
    loop = GuardianLoop()

    test_signals = [
        "access_anomaly",
        "data_integrity_risk",
        "spread_detected"
    ]

    result = loop.run(test_signals)

    print("\n=== GUARDIAN RESULT ===")
    print(json.dumps(result, indent=2))
