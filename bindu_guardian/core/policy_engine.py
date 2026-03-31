def enforce_policy(action, domain, system_actions, policy):
    violations = []

    if "no_uncontrolled_autonomy" in policy["hard_constraints"]:
        if action == "escalate" and "external_incident_response" not in system_actions:
            violations.append("missing external oversight")

    if "no_blunt_shutdown_of_life_critical_services" in policy["hard_constraints"]:
        if "shutdown_all" in system_actions:
            violations.append("illegal shutdown")

    if violations:
        return {
            "approved": False,
            "violations": violations,
            "override_action": "stabilize"
        }

    return {
        "approved": True,
        "violations": []
    }
