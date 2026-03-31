def adjust_for_safety(domain, action):
    # Critical override rules

    if domain == "hospital":
        if action in ["isolate", "restore"]:
            return {
                "final_action": "stabilize",
                "reason": "Isolation may disrupt critical care",
                "override": True
            }

    return {
        "final_action": action,
        "reason": "No safety override",
        "override": False
    }
