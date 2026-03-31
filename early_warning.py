def early_warning(score, correlation_confidence):
    pressure = round((score * 0.7) + (correlation_confidence * 0.3), 2)

    if pressure < 0.35:
        warning = "low"
    elif pressure < 0.6:
        warning = "elevated"
    elif pressure < 0.8:
        warning = "high"
    else:
        warning = "critical"

    return {
        "warning_level": warning,
        "combined_pressure": pressure
    }
