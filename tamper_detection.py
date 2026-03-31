def detect_tamper(signals, actor_role):
    suspicious = False
    reasons = []

    if "privilege_escalation_attempt" in signals:
        suspicious = True
        reasons.append("privilege escalation signal present")

    if actor_role == "unknown_actor":
        suspicious = True
        reasons.append("unknown actor attempted action")

    return {
        "tamper_suspected": suspicious,
        "reasons": reasons
    }
