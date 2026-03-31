from collections import Counter

def correlate(signals):
    c = Counter(signals)

    coordinated = False
    reasons = []

    if "access_anomaly" in c and "spread_detected" in c:
        coordinated = True
        reasons.append("access anomaly combined with spread")

    if "data_integrity_risk" in c and "communications_disruption" in c:
        coordinated = True
        reasons.append("integrity risk combined with communications disruption")

    if "privilege_escalation_attempt" in c and "access_anomaly" in c:
        coordinated = True
        reasons.append("privilege escalation combined with access anomaly")

    confidence = 0.3
    if coordinated:
        confidence = 0.8

    return {
        "coordinated_attack_likely": coordinated,
        "reasons": reasons,
        "correlation_confidence": confidence
    }
