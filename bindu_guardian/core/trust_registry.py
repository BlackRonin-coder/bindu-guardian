TRUST_REGISTRY = {
    "hospital": {
        "trusted_roles": [
            "clinical_safety_lead",
            "it_incident_lead",
            "executive_on_call"
        ]
    },
    "university": {
        "trusted_roles": [
            "identity_admin",
            "it_incident_lead",
            "executive_on_call"
        ]
    },
    "agency": {
        "trusted_roles": [
            "security_manager",
            "it_incident_lead",
            "executive_on_call"
        ]
    }
}

def get_trusted_roles(domain):
    return TRUST_REGISTRY.get(domain, {}).get("trusted_roles", [])
