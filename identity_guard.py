TRUSTED_ROLES = {
    "hospital": ["clinical_safety_lead", "it_incident_lead", "executive_on_call"],
    "university": ["identity_admin", "it_incident_lead", "executive_on_call"],
    "agency": ["security_manager", "it_incident_lead", "executive_on_call"]
}

def authorize(domain, actor_role, action):
    trusted = TRUSTED_ROLES.get(domain, [])
    allowed = actor_role in trusted

    return {
        "actor_role": actor_role,
        "action": action,
        "authorized": allowed,
        "reason": "trusted role" if allowed else "untrusted role"
    }
