HIGH_RISK = {
    "privilege_escalation_attempt",
    "data_integrity_risk",
    "spread_detected"
}

MEDIUM_RISK = {
    "access_anomaly",
    "communications_disruption"
}

LOW_RISK = {
    "slow_system_response"
}

def classify_signal(signal):
    if signal in HIGH_RISK:
        return "high"
    if signal in MEDIUM_RISK:
        return "medium"
    return "low"
