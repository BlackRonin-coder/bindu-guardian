import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from correlation_engine import correlate
from early_warning import early_warning
from safety_guardrails import adjust_for_safety
from guardian_context import apply_domain_bias
from temporal_analyzer import TemporalAnalyzer
from pattern_memory import PatternMemory

DOMAINS = ["hospital", "university", "agency"]

memory = PatternMemory()
timelines = {d: TemporalAnalyzer() for d in DOMAINS}

for domain in DOMAINS:
    signals = generate_signals()

    weighted_score = evaluate_weighted(signals)
    timelines[domain].add_score(weighted_score)
    trend = timelines[domain].trend()

    memory.record(signals)
    recall = memory.recall(signals)

    correlation = correlate(signals)
    warning = early_warning(weighted_score, correlation["correlation_confidence"])

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

    if trend["worsening"] and action in ["observe", "reinforce"]:
        action = "stabilize"

    safety = adjust_for_safety(domain, action)

    print(f"\n=== {domain.upper()} BINDU PHASE 5 ===")
    print(json.dumps({
        "signals": signals,
        "weighted_score": weighted_score,
        "trend": trend,
        "pattern_memory": recall,
        "correlation": correlation,
        "warning": warning,
        "initial_action": action,
        "final_action": safety["final_action"],
        "override": safety["override"],
        "guidance": apply_domain_bias(domain, safety["final_action"])
    }, indent=2))
