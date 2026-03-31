def analyse_trend(history):
    if len(history) < 2:
        return {
            "trend": "insufficient_data",
            "high_risk_series": [],
            "rising": False
        }

    series = []
    for item in history:
        high_risk = item.get("isolate", 0) + item.get("escalate", 0)
        series.append(high_risk)

    rising = series[-1] > series[0] and (series[-1] - series[0]) >= 2

    if rising:
        trend = "rising_high_risk_pressure"
    elif series[-1] < series[0]:
        trend = "easing"
    else:
        trend = "stable"

    return {
        "trend": trend,
        "high_risk_series": series,
        "rising": rising
    }
