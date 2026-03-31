def prioritize_humans(domain, actions):
    if domain == "hospital":
        return actions + [
            "guarantee patient care systems active",
            "protect medication workflows"
        ]

    if domain == "university":
        return actions + [
            "maintain student access",
            "protect teaching continuity"
        ]

    if domain == "agency":
        return actions + [
            "preserve public access",
            "maintain emergency services"
        ]

    return actions
