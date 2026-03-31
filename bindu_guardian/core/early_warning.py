def early_warning(score, signal_count):
    warning = {
        "level": "none",
        "message": "system stable"
    }

    if score >= 0.4 and signal_count >= 2:
        warning = {
            "level": "watch",
            "message": "instability forming"
        }

    if score >= 0.7 and signal_count >= 3:
        warning = {
            "level": "high",
            "message": "likely escalation forming"
        }

    return warning
