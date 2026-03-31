def adjust_for_pattern(correlation, pattern_info):
    if pattern_info["seen"] and pattern_info["count"] >= 3:
        return {
            "pattern_escalation": True,
            "reason": "repeated coordinated pattern"
        }

    return {
        "pattern_escalation": False,
        "reason": "no repeated pattern"
    }
