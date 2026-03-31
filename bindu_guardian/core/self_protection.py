def evaluate_self_protection(trust, score, signals):
    trigger = False
    reasons = []

    if not trust["trusted"] and score >= 0.7:
        trigger = True
        reasons.append("untrusted actor during high pressure")

    if "privilege_escalation_attempt" in signals:
        trigger = True
        reasons.append("privilege escalation attempt detected")

    if "data_integrity_risk" in signals:
        trigger = True
        reasons.append("integrity risk may affect guardian trust base")

    mode = "normal"
    actions = ["continue monitored operation"]

    if trigger:
        mode = "hardened"
        actions = [
            "freeze nonessential control changes",
            "require dual authorization for critical actions",
            "write immutable incident record"
        ]

    return {
        "triggered": trigger,
        "mode": mode,
        "reasons": reasons,
        "actions": actions
    }
