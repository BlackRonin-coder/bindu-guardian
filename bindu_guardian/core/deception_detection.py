def detect_deception(signals, correlation, trust):
    suspicion = 0
    reasons = []

    if correlation["coordinated"] and not trust["trusted"]:
        suspicion += 2
        reasons.append("coordinated signals from untrusted actor")

    if "privilege_escalation_attempt" in signals and "normal_operation" in signals:
        suspicion += 1
        reasons.append("conflicting signals detected")

    if len(signals) >= 4 and correlation["confidence"] < 0.5:
        suspicion += 1
        reasons.append("high signal volume with low correlation confidence")

    level = "low"
    if suspicion >= 2:
        level = "medium"
    if suspicion >= 3:
        level = "high"

    return {
        "suspicion_score": suspicion,
        "level": level,
        "reasons": reasons
    }
