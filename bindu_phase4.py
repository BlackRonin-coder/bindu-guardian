import json
from weighted_evaluator import evaluate_weighted
from correlation_engine import correlate
from early_warning import early_warning
from safety_guardrails import adjust_for_safety
from guardian_context import apply_domain_bias
from signal_simulator import generate_signals

DOMAINS = ["hospital", "university", "agency"]

for domain in DOMAINS:
    signals = generate_signals()

    weighted_score = evaluate_weighted(signals)
    correlation = correlate(signals)
    warning = early_warning(weighted_score, correlation["correlation_confidence"])

    # derive action from weighted score
    if weighted_score < 0.2:
        action = "observe"
    elif weighted_score < 0.4:
        action = "reinforce"
    elif weighted_score < 0.6:
        action = "stabilize"
    elif weighted_score < 0.8:
        action = "isolate"
    elif weighted_score < 0.95:
        action = "restore"
    else:
        action = "escalate"

    safety = adjust_for_safety(domain, action)

    print(f"\n=== {domain.upper()} BINDU PHASE 4 ===")
    print(json.dumps({
        "signals": signals,
        "weighted_score": weighted_score,
        "initial_action": action,
        "final_action": safety["final_action"],
        "override": safety["override"],
        "correlation": correlation,
        "warning": warning,
        "guidance": apply_domain_bias(domain, safety["final_action"])
    }, indent=2))
