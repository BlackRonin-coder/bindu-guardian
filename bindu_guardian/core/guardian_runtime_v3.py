import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from action_executor import execute_action
from human_priority import prioritize_humans

from bindu_guardian.core.policy_loader import load_policy
from bindu_guardian.core.policy_engine import enforce_policy
from bindu_guardian.core.trust_engine import evaluate_actor
from bindu_guardian.core.self_protection import evaluate_self_protection
from bindu_guardian.core.immutable_log import write_log

DOMAIN = "hospital"
ACTOR_ROLE = "unknown_actor"

signals = generate_signals()
score = evaluate_weighted(signals)

action = "observe"
if score > 0.4:
    action = "stabilize"
if score > 0.7:
    action = "isolate"
if score > 0.9:
    action = "escalate"

trust = evaluate_actor(DOMAIN, ACTOR_ROLE)

if not trust["trusted"] and action in ["isolate", "restore", "escalate"]:
    action = "stabilize"

policy = load_policy()

self_protection = evaluate_self_protection(trust, score, signals)

system_actions = execute_action(DOMAIN, action)

check = enforce_policy(action, DOMAIN, system_actions, policy)

if not check["approved"]:
    action = check["override_action"]
    system_actions = execute_action(DOMAIN, action)

human_safe_actions = prioritize_humans(DOMAIN, system_actions)

log_entry = write_log("guardian_runtime_v3", {
    "domain": DOMAIN,
    "actor_role": ACTOR_ROLE,
    "signals": signals,
    "score": score,
    "trust": trust,
    "self_protection": self_protection,
    "final_action": action
})

print("\n=== BINDU GUARDIAN RUNTIME V3 ===")
print(json.dumps({
    "domain": DOMAIN,
    "actor_role": ACTOR_ROLE,
    "signals": signals,
    "score": score,
    "trust": trust,
    "self_protection": self_protection,
    "final_action": action,
    "policy_approved": check["approved"],
    "violations": check["violations"],
    "system_actions": system_actions,
    "human_safe_actions": human_safe_actions,
    "log_entry": log_entry
}, indent=2))
