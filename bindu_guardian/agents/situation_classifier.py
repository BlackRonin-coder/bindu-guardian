def classify_situation(consensus, pressure, trend):
    action = consensus["consensus_action"]
    high_pressure = pressure["threshold_exceeded"]
    rising = trend["rising"]
    trend_name = trend["trend"]

    if not high_pressure and action == "observe" and trend_name in ["stable", "easing", "insufficient_data"]:
        return {
            "situation_type": "false_alarm",
            "reason": "low pressure and no rising threat pattern"
        }

    if not high_pressure and action in ["observe", "stabilize"] and trend_name == "stable":
        return {
            "situation_type": "transient_incident",
            "reason": "limited disruption without sustained high-risk pressure"
        }

    if high_pressure and not rising:
        return {
            "situation_type": "coordinated_attack",
            "reason": "high-risk pressure exceeded threshold"
        }

    if rising:
        return {
            "situation_type": "slow_burn_attack",
            "reason": "high-risk pressure is increasing over time"
        }

    return {
        "situation_type": "transient_incident",
        "reason": "default safe classification"
    }
