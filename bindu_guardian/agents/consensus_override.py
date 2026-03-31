def apply_override(consensus_action, pressure_info):
    if pressure_info["threshold_exceeded"]:
        return {
            "final_action": "isolate",
            "override": True,
            "reason": "combined high-risk pressure exceeded threshold"
        }

    return {
        "final_action": consensus_action,
        "override": False,
        "reason": "consensus accepted"
    }
