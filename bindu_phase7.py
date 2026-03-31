import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from correlation_engine import correlate
from early_warning import early_warning
from safety_guardrails import adjust_for_safety
from guardian_context import apply_domain_bias
from temporal_analyzer import TemporalAnalyzer
from pattern_memory import PatternMemory
from escalation_predictor import predict_escalation
from preemptive_actions import apply_preemptive_logic
from action_executor import execute_action
from human_priority import prioritize_humans

DOMAINS = ["hospital", "university", "agency"]

memory = PatternMemory()
timelines = {d: TemporalAnalyzer() for d in DOMAINS}

for domain in DOMAINS:
    signals = generate_signals()

    score = evaluate_weighted(signals)
    timelines[domain].add_score(score)
    trend = timelines[domain].trend()

    memory.record(signals)
    recall = memory.recall(signals)

    correlation = correlate(signals)

    if score < 0.2:
        action = "observe"
    elif score < 0.4:
        action = "reinforce"
    elif score < 0.6:
        action = "stabilize"
    elif score < 0.8:
        action = "isolate"
    elif score < 0.95:
        action = "restore"
    else:
        action = "escalate"

    escalation = predict_escalation(score, trend, correlation["correlation_confidence"])
    action = apply_preemptive_logic(action, escalation)

    safety = adjust_for_safety(domain, action)

    system_actions = execute_action(domain, safety["final_action"])
    human_safe_actions = prioritize_humans(domain, system_actions)

    print(f"\n=== {domain.upper()} BINDU PHASE 7 ===")
    print(json.dumps({
        "signals": signals,
        "score": score,
        "trend": trend,
        "correlation": correlation,
        "escalation": escalation,
        "final_action": safety["final_action"],
        "system_actions": system_actions,
        "human_safe_actions": human_safe_actions,
        "guidance": apply_domain_bias(domain, safety["final_action"])
    }, indent=2))
