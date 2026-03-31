def detect_escalation_pressure(weighted_totals):
    pressure = weighted_totals.get("isolate", 0) + weighted_totals.get("escalate", 0)

    return {
        "combined_high_risk_pressure": pressure,
        "threshold_exceeded": pressure >= 5
    }
