from collections import Counter

def learn_from_history(history):
    action_success = Counter()

    for entry in history:
        key = (tuple(sorted(entry["signals"])), entry["action"])
        if entry["success"]:
            action_success[key] += 1

    return action_success

def suggest_action(signals, learned_patterns):
    key_prefix = tuple(sorted(signals))

    best = None
    best_score = 0

    for (pattern, action), score in learned_patterns.items():
        if pattern == key_prefix and score > best_score:
            best = action
            best_score = score

    return best
