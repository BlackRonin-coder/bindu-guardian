import json
from guardian_loop import GuardianLoop
from guardian_context import apply_domain_bias
from signal_simulator import generate_signals
from safety_guardrails import adjust_for_safety
from correlation_engine import correlate
from early_warning import early_warning

DOMAINS = ["hospital", "university", "agency"]

loop = GuardianLoop()

for domain in DOMAINS:
    signals = generate_signals()
    result = loop.run(signals)
    correlation = correlate(signals)
    warning = early_warning(result["score"], correlation["correlation_confidence"])
    safety = adjust_for_safety(domain, result["action"])

    output = {
        "domain": domain,
        "signals": signals,
        "score": result["score"],
        "initial_action": result["action"],
        "final_action": safety["final_action"],
        "override": safety["override"],
        "override_reason": safety["reason"],
        "coordination_assessment": correlation,
        "early_warning": warning,
        "human_guidance": apply_domain_bias(domain, safety["final_action"])
    }

    print(f"\n=== {domain.upper()} BINDU PHASE 3 ===")
    print(json.dumps(output, indent=2))
