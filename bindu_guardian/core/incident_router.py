ROUTING_TABLE = {
    "hospital": {
        "observe": ["local_monitoring"],
        "stabilize": ["it_duty", "ward_lead"],
        "isolate": ["it_incident_lead", "clinical_safety_lead"],
        "escalate": ["it_incident_lead", "clinical_safety_lead", "executive_on_call"]
    }
}

def route_incident(domain, action):
    routes = ROUTING_TABLE.get(domain, {})
    recipients = routes.get(action, ["local_monitoring"])
    return {
        "domain": domain,
        "action": action,
        "notify": recipients
    }
