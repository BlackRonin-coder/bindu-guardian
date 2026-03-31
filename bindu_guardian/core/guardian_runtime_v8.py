import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from action_executor import execute_action
from human_priority import prioritize_humans

from bindu_guardian.core.policy_loader import load_policy
from bindu_guardian.core.policy_engine import enforce_policy
from bindu_guardian.core.trust_engine import evaluate_actor
from bindu_guardian.core.self_protection import evaluate_self_protection
from bindu_guardian.core.early_warning import early_warning
from bindu_guardian.core.correlation_engine import correlate
from bindu_guardian.core.pattern_memory import store_pattern, recall_pattern
from bindu_guardian.core.pattern_awareness import adjust_for_pattern
from bindu_guardian.core.deception_detection import detect_deception
from bindu_guardian.core.deception_response import adjust_for_deception
from bindu_guardian.core.incident_router import route_incident
from bindu_guardian.core.human_coordination import coordination_message

DOMAIN = "hospital"
ACTOR_ROLE = "unknown_actor"

signals = generate_signals()
score = evaluate_weighted(signals)
warning = early_warning(score, len(signals))
correlation = correlate(signals)

pattern_info = recall_pattern(signals)
store_pattern(signals)
pattern_adjustment = adjust_for_pattern(correlation, pattern_info)

trust = evaluate_actor(DOMAIN, ACTOR_ROLE)
deception = detect_deception(signals, correlation, trust)

action = "observe"
if score > 0.4:
    action = "stabilize"
if score > 0.7:
    action = "isolate"
if score > 0.9:
    action = "escalate"

if correlation["coordinated"] and correlation["confidence"] >= 0.8:
    action = "isolate"

if pattern_adjustment["pattern_escalation"]:
    action = "isolate"

deception_adjustment = adjust_for_deception(action, deception)
action = deception_adjustment["adjusted_action"]

if not trust["trusted"] and action in ["restore", "escalate"]:
    action = "stabilize"

self_protection = evaluate_self_protection(trust, score, signals)

system_actions = execute_action(DOMAIN, action)

policy = load_policy()
check = enforce_policy(action, DOMAIN, system_actions, policy)

if not check["approved"]:
    action = check["override_action"]
    system_actions = execute_action(DOMAIN, action)

human_safe_actions = prioritize_humans(DOMAIN, system_actions)
routing = route_incident(DOMAIN, action)
coordination = coordination_message(DOMAIN, action, routing["notify"])

print("\n=== BINDU GUARDIAN RUNTIME V8 ===")
print(json.dumps({
    "signals": signals,
    "score": score,
    "early_warning": warning,
    "correlation": correlation,
    "pattern_memory": pattern_info,
    "deception": deception,
    "trust": trust,
    "self_protection": self_protection,
    "final_action": action,
    "system_actions": system_actions,
    "human_safe_actions": human_safe_actions,
    "routing": routing,
    "coordination": coordination
}, indent=2))
