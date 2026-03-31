def correlate(signals):
    reasons = []
    coordinated = False
    confidence = 0.2

    if "data_integrity_risk" in signals and "communications_disruption" in signals:
        coordinated = True
        reasons.append("integrity risk combined with communications disruption")
        confidence = max(confidence, 0.8)

    if "privilege_escalation_attempt" in signals and "access_anomaly" in signals:
        coordinated = True
        reasons.append("privilege escalation combined with access anomaly")
        confidence = max(confidence, 0.85)

    if "spread_detected" in signals and "system_instability" in signals:
        coordinated = True
        reasons.append("spread combined with instability")
        confidence = max(confidence, 0.75)

    return {
        "coordinated": coordinated,
        "confidence": confidence,
        "reasons": reasons
    }
