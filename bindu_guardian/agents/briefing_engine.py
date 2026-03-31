def build_briefing(situation, mapped_response, override, temporal):
    return {
        "executive_brief": {
            "situation_type": situation["situation_type"],
            "why": situation["reason"],
            "recommended_action": mapped_response["recommended_action"],
            "message": mapped_response["message"],
            "override_active": override["override"] or temporal["override"]
        }
    }
