def apply_preemptive_logic(action, escalation):
    if not escalation["preempt"]:
        return action

    if action in ["observe"]:
        return "reinforce"
    if action in ["reinforce"]:
        return "stabilize"
    if action in ["stabilize"]:
        return "isolate"
    if action in ["isolate"]:
        return "restore"

    return action
