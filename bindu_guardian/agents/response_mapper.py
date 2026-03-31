def map_response(situation_type):
    mapping = {
        "false_alarm": {
            "recommended_action": "observe",
            "message": "Monitor only. No disruptive action."
        },
        "transient_incident": {
            "recommended_action": "stabilize",
            "message": "Stabilize locally and keep services running."
        },
        "coordinated_attack": {
            "recommended_action": "isolate",
            "message": "Contain affected systems and protect critical functions."
        },
        "slow_burn_attack": {
            "recommended_action": "isolate",
            "message": "Preempt escalation and contain before spread increases."
        }
    }

    return mapping.get(situation_type, {
        "recommended_action": "observe",
        "message": "Fallback safe response."
    })
