import random

POSSIBLE_SIGNALS = [
    "access_anomaly",
    "system_instability",
    "data_integrity_risk",
    "spread_detected",
    "communications_disruption",
    "privilege_escalation_attempt",
    "unexpected_shutdown",
    "slow_system_response"
]

def generate_signals():
    count = random.randint(1, 5)
    return random.sample(POSSIBLE_SIGNALS, count)

if __name__ == "__main__":
    print(generate_signals())
