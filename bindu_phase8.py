import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from correlation_engine import correlate
from early_warning import early_warning
from safety_guardrails import adjust_for_safety
from guardian_context import apply_domain_bias
from escalation_predictor import predict_escalation
from preemptive_actions import apply_preemptive_logic
from action_executor import execute_action
from human_priority import prioritize_humans
from identity_guard import authorize
from tamper_detection import detect_tamper

DOMAINS = {
    "hospital": "clinical_safety_lead",
    "university": "identity_admin",
    "agency": "unknown_actor"
}

for domain, actor_role in DOMAINS.items():
    signals = generate_signals()

    score = evaluate_weighted(signals)
    correlation = correlate(signals)
    warning = early_warning(score, correlation["correlation_confidence"])

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

    escalation = predict_escalation(
        score,
        {"worsening": warning["warning_level"] in ["high", "critical"]},
        correlation["correlation_confidence"]
    )

    action = apply_preemptive_logic(action, escalation)

    auth = authorize(domain, actor_role, action)
    tamper = detect_tamper(signals, actor_role)

    if tamper["tamper_suspected"] or not auth["authorized"]:
        action = "escalate"

    safety = adjust_for_safety(domain, action)
    system_actions = execute_action(domain, safety["final_action"])
    human_safe_actions = prioritize_humans(domain, system_actions)

    print(f"\n=== {domain.upper()} BINDU PHASE 8 ===")
    print(json.dumps({
        "signals": signals,
        "score": score,
        "correlation": correlation,
        "warning": warning,
        "predicted_escalation": escalation,
        "authorization": auth,
        "tamper_detection": tamper,
        "final_action": safety["final_action"],
        "system_actions": system_actions,
        "human_safe_actions": human_safe_actions,
        "guidance": apply_domain_bias(domain, safety["final_action"])
    }, indent=2))
