import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from action_executor import execute_action
from human_priority import prioritize_humans

from bindu_guardian.core.policy_loader import load_policy
from bindu_guardian.core.policy_engine import enforce_policy

DOMAIN = "hospital"

signals = generate_signals()
score = evaluate_weighted(signals)

action = "observe"
if score > 0.4:
    action = "stabilize"
if score > 0.7:
    action = "isolate"
if score > 0.9:
    action = "escalate"

system_actions = execute_action(DOMAIN, action)

policy = load_policy()
check = enforce_policy(action, DOMAIN, system_actions, policy)

if not check["approved"]:
    action = check["override_action"]
    system_actions = execute_action(DOMAIN, action)

human_safe_actions = prioritize_humans(DOMAIN, system_actions)

print("\n=== BINDU GUARDIAN RUNTIME ===")
print(json.dumps({
    "signals": signals,
    "score": score,
    "final_action": action,
    "policy_approved": check["approved"],
    "violations": check["violations"],
    "system_actions": system_actions,
    "human_safe_actions": human_safe_actions
}, indent=2))
