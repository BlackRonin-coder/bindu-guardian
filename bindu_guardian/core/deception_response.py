def adjust_for_deception(action, deception):
    if deception["level"] == "high":
        return {
            "adjusted_action": "stabilize",
            "override": True,
            "reason": "high deception risk"
        }

    if deception["level"] == "medium" and action == "escalate":
        return {
            "adjusted_action": "isolate",
            "override": True,
            "reason": "moderate deception risk"
        }

    return {
        "adjusted_action": action,
        "override": False,
        "reason": "no significant deception"
    }
