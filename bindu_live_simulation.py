import json
from guardian_loop import GuardianLoop
from guardian_context import apply_domain_bias
from signal_simulator import generate_signals

DOMAINS = ["hospital", "university", "agency"]

loop = GuardianLoop()

for domain in DOMAINS:
    signals = generate_signals()

    result = loop.run(signals)

    print(f"\n=== LIVE {domain.upper()} SIMULATION ===")
    print(json.dumps({
        "domain": domain,
        "signals": signals,
        "score": result["score"],
        "action": result["action"],
        "response": result["response"],
        "human_guidance": apply_domain_bias(domain, result["action"])
    }, indent=2))
