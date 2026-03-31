def apply_temporal_override(current_action, trend_info):
    if trend_info["rising"] and current_action in ["observe", "stabilize"]:
        return {
            "final_action": "isolate",
            "override": True,
            "reason": "rising high-risk pressure over time"
        }

    return {
        "final_action": current_action,
        "override": False,
        "reason": "no temporal override"
    }
