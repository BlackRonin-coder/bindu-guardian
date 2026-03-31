import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from correlation_engine import correlate
from action_executor import execute_action
from human_priority import prioritize_humans
from confidence_gate_v2 import should_escalate_v2
from outcome_tracker import record_outcome, get_history
from learning_engine import learn_from_history, suggest_action

DOMAIN = "agency"

signals = generate_signals()

score = evaluate_weighted(signals)
correlation = correlate(signals)

action = "observe"
if score > 0.4:
    action = "stabilize"
if score > 0.7:
    action = "isolate"

gate = should_escalate_v2(signals, correlation["correlation_confidence"], {"tamper_suspected": False}, True)

if gate["escalate"]:
    action = "escalate"

history = get_history()
learned = learn_from_history(history)
suggested = suggest_action(signals, learned)

if suggested:
    action = suggested

system_actions = execute_action(DOMAIN, action)
human_safe_actions = prioritize_humans(DOMAIN, system_actions)

record_outcome(DOMAIN, signals, action, success=True)

print("\n=== BINDU PHASE 12 (LEARNING) ===")
print(json.dumps({
    "signals": signals,
    "chosen_action": action,
    "learned_patterns": len(learned),
    "system_actions": system_actions,
    "human_safe_actions": human_safe_actions
}, indent=2))
