import json
from guardian_loop import GuardianLoop
from guardian_context import apply_domain_bias

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

    context_message = apply_domain_bias(profile["domain"], result["action"])

    print(f"\n=== {profile['domain'].upper()} (CONTEXT-AWARE) ===")
    print(json.dumps({
        "domain": profile["domain"],
        "action": result["action"],
        "system_response": result["response"],
        "human_guidance": context_message
    }, indent=2))
