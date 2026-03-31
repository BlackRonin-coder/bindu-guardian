import json

with open("signal_weights.json", "r", encoding="utf-8") as f:
    WEIGHTS = json.load(f)

def evaluate_weighted(signals):
    score = 0.0

    for s in signals:
        score += WEIGHTS.get(s, 0.1)

    return round(min(score, 1.0), 2)
