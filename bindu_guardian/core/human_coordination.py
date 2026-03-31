def coordination_message(domain, action, notify):
    return {
        "message": f"{action.upper()}: notify {', '.join(notify)}",
        "priority": "people_first"
    }
