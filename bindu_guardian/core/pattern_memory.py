PATTERN_MEMORY = {}

def store_pattern(signals):
    key = tuple(sorted(signals))
    if key not in PATTERN_MEMORY:
        PATTERN_MEMORY[key] = 0
    PATTERN_MEMORY[key] += 1
    return PATTERN_MEMORY[key]

def recall_pattern(signals):
    key = tuple(sorted(signals))
    return {
        "seen": key in PATTERN_MEMORY,
        "count": PATTERN_MEMORY.get(key, 0)
    }
