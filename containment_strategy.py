def containment_plan(domain, action):
    if action != "escalate":
        return ["standard containment"]

    if domain == "hospital":
        return [
            "isolate infected segments",
            "lock admin privileges",
            "maintain patient systems",
            "allow clinical access only"
        ]

    if domain == "university":
        return [
            "isolate research systems",
            "lock bulk account actions",
            "maintain teaching systems"
        ]

    if domain == "agency":
        return [
            "isolate sensitive databases",
            "lock privilege escalation",
            "maintain public services"
        ]

    return ["generic containment"]
