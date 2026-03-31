OUTCOMES = []

def record_outcome(domain, signals, action, success=True):
    OUTCOMES.append({
        "domain": domain,
        "signals": signals,
        "action": action,
        "success": success
    })

def get_history():
    return OUTCOMES
