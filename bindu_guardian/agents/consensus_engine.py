from bindu_guardian.agents.agent_weights import get_agent_weight

ACTION_ORDER = {
    "observe": 0,
    "stabilize": 1,
    "isolate": 2,
    "escalate": 3
}

def build_consensus(agent_votes):
    weighted_totals = {
        "observe": 0,
        "stabilize": 0,
        "isolate": 0,
        "escalate": 0
    }

    for item in agent_votes:
        agent = item["agent"]
        vote = item["vote"]
        weight = get_agent_weight(agent)
        weighted_totals[vote] += weight

    winner = max(weighted_totals, key=weighted_totals.get)

    return {
        "agent_votes": agent_votes,
        "weighted_totals": weighted_totals,
        "consensus_action": winner
    }
