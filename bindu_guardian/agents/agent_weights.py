AGENT_WEIGHTS = {
    "clinical_guardian": 3,
    "identity_guardian": 2,
    "network_guardian": 2,
    "coordinator_guardian": 3
}

def get_agent_weight(agent_name):
    return AGENT_WEIGHTS.get(agent_name, 1)
