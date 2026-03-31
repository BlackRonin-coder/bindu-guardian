import json
from guardian_loop import GuardianLoop
from guardian_context import apply_domain_bias

with open("escalation_matrix.json", "r", encoding="utf-8") as f:
    ESCALATION = json.load(f)

with open("continuity_profiles.json", "r", encoding="utf-8") as f:
    CONTINUITY = json.load(f)

FILES = [
    "hospital_guardian.json",
    "university_guardian.json",
    "agency_guardian.json",
]

loop = GuardianLoop()

for path in FILES:
    with open(path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    result = loop.run(profile["signals"])
    domain = profile["domain"]
    action = result["action"]

    output = {
        "domain": domain,
        "score": result["score"],
        "action": action,
        "system_response": result["response"],
        "human_guidance": apply_domain_bias(domain, action),
        "notify": ESCALATION[domain][action],
        "preserve": CONTINUITY[domain]["preserve"],
        "restrict": CONTINUITY[domain]["restrict"],
        "fallback": CONTINUITY[domain]["fallback"]
    }

    print(f"\n=== {domain.upper()} BINDU PHASE 2 ===")
    print(json.dumps(output, indent=2))
