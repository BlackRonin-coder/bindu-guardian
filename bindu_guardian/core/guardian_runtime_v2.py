import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import json
from signal_simulator import generate_signals
from weighted_evaluator import evaluate_weighted
from action_executor import execute_action
from human_priority import prioritize_humans

from bindu_guardian.core.policy_loader import load_policy
from bindu_guardian.core.policy_engine import enforce_policy
from bindu_guardian.core.trust_engine import evaluate_actor

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

system_actions = execute_action(DOMAIN, action)

policy = load_policy()
check = enforce_policy(action, DOMAIN, system_actions, policy)

if not check["approved"]:
    action = check["override_action"]
    system_actions = execute_action(DOMAIN, action)

human_safe_actions = prioritize_humans(DOMAIN, system_actions)

print("\n=== BINDU GUARDIAN RUNTIME V2 ===")
print(json.dumps({
    "domain": DOMAIN,
    "actor_role": ACTOR_ROLE,
    "signals": signals,
    "score": score,
    "trust": trust,
    "final_action": action,
    "policy_approved": check["approved"],
    "violations": check["violations"],
    "system_actions": system_actions,
    "human_safe_actions": human_safe_actions
}, indent=2))
