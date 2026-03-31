from signal_tiers import classify_signal

def should_escalate_v2(signals, correlation_conf, tamper, authorized):
    score = 0

    for s in signals:
        tier = classify_signal(s)

        if tier == "high":
            score += 2
        elif tier == "medium":
            score += 1
        else:
            score += 0.5

    if correlation_conf > 0.6:
        score += 1

    if tamper["tamper_suspected"]:
        score += 1

    if not authorized:
        score += 1

    return {
        "weighted_signal_score": score,
        "escalate": score >= 5
    }
