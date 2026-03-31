from containment_strategy import containment_plan

def execute_action(domain, action):
    if action == "observe":
        return ["log activity"]

    if action == "reinforce":
        return ["increase monitoring", "verify access logs"]

    if action == "stabilize":
        return ["limit system changes", "alert IT staff"]

    if action == "isolate":
        return ["segment affected systems", "block suspicious access"]

    if action == "restore":
        return ["reset affected systems", "verify integrity"]

    if action == "escalate":
        return containment_plan(domain, action)

    return ["no_action"]
