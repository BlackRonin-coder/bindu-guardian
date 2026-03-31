def should_escalate(score, correlation_conf, tamper, authorized):
    signals = 0

    if score > 0.7:
        signals += 1

    if correlation_conf > 0.6:
        signals += 1

    if tamper["tamper_suspected"]:
        signals += 1

    if not authorized:
        signals += 1

    return {
        "signal_count": signals,
        "escalate": signals >= 3  # require strong agreement
    }
