def predict_escalation(score, trend, correlation_conf):
    risk = score + (0.5 * correlation_conf)

    if trend["worsening"]:
        risk += 0.2

    if risk > 1.0:
        risk = 1.0

    if risk > 0.85:
        return {"level": "critical", "preempt": True}
    elif risk > 0.65:
        return {"level": "high", "preempt": True}
    elif risk > 0.4:
        return {"level": "moderate", "preempt": False}
    else:
        return {"level": "low", "preempt": False}
