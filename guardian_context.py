def apply_domain_bias(domain, action):
    if domain == "hospital":
        if action in ["isolate", "restore"]:
            return "Ensure patient safety. Maintain critical care systems."
        if action == "stabilize":
            return "Limit system usage. Continue essential medical services."

    if domain == "university":
        if action in ["isolate", "restore"]:
            return "Protect identity systems. Secure research data."
        if action == "stabilize":
            return "Restrict platform access. Maintain core teaching."

    if domain == "agency":
        if action in ["isolate", "restore"]:
            return "Secure systems immediately. Preserve public function."
        if action == "stabilize":
            return "Limit operations. Maintain essential services."

    return "Monitor and proceed safely."
