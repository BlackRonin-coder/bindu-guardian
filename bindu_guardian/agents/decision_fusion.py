def decide_from_fusion(fused_signals):
    score = len(fused_signals)

    action = "observe"

    if score >= 2:
        action = "stabilize"
    if score >= 4:
        action = "isolate"
    if score >= 5:
        action = "escalate"

    return {
        "fused_signal_count": score,
        "recommended_action": action
    }
