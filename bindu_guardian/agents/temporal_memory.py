from collections import deque

TEMPORAL_HISTORY = deque(maxlen=6)

def record_cycle(weighted_totals):
    TEMPORAL_HISTORY.append(dict(weighted_totals))
    return list(TEMPORAL_HISTORY)

def get_history():
    return list(TEMPORAL_HISTORY)
