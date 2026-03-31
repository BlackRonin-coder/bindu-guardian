def explain_decision(situation, mapped_response, trend, pressure):
    situation_type = situation["situation_type"]
    reason = situation["reason"]
    action = mapped_response["recommended_action"]

    explanation = (
        f"Guardian classified this as {situation_type.replace('_', ' ')} "
        f"because {reason}. "
        f"Trend status: {trend['trend']}. "
        f"Combined high-risk pressure: {pressure['combined_high_risk_pressure']}. "
        f"Recommended action: {action}."
    )

    return {
        "plain_english": explanation
    }
