import json
from guardian_loop import GuardianLoop

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

    print(f"\n=== {profile['domain'].upper()} ===")
    print(json.dumps({
        "domain": profile["domain"],
        "bias": profile["human_message_bias"],
        "signals": profile["signals"],
        "score": result["score"],
        "action": result["action"],
        "response": result["response"],
    }, indent=2))
