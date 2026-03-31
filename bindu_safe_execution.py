import json
from guardian_loop import GuardianLoop
from guardian_context import apply_domain_bias
from signal_simulator import generate_signals
from safety_guardrails import adjust_for_safety

DOMAINS = ["hospital", "university", "agency"]

loop = GuardianLoop()

for domain in DOMAINS:
    signals = generate_signals()

    result = loop.run(signals)

    safety = adjust_for_safety(domain, result["action"])

    print(f"\n=== SAFE {domain.upper()} EXECUTION ===")
    print(json.dumps({
        "domain": domain,
        "signals": signals,
        "initial_action": result["action"],
        "final_action": safety["final_action"],
        "override": safety["override"],
        "reason": safety["reason"],
        "response": result["response"],
        "human_guidance": apply_domain_bias(domain, safety["final_action"])
    }, indent=2))
