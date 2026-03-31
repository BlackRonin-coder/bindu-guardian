def self_protect(domain, tamper_detection, authorization):
    if tamper_detection["tamper_suspected"]:
        return {
            "self_protection_triggered": True,
            "guardian_mode": "hardened",
            "actions": [
                "freeze non-essential control changes",
                "require dual authorization for critical actions",
                "write immutable incident log"
            ]
        }

    if not authorization["authorized"]:
        return {
            "self_protection_triggered": True,
            "guardian_mode": "restricted",
            "actions": [
                "deny direct control request",
                "allow monitoring only",
                "write immutable incident log"
            ]
        }

    return {
        "self_protection_triggered": False,
        "guardian_mode": "normal",
        "actions": [
            "continue guarded operation"
        ]
    }
