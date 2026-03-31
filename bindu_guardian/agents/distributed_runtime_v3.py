import json
from signal_simulator import generate_signals
from bindu_guardian.agents.agent_registry import AGENTS
from bindu_guardian.agents.agent_signal_share import share_signals, fuse_shared_signals
from bindu_guardian.agents.agent_vote import vote_from_signals
from bindu_guardian.agents.consensus_engine import build_consensus

shared_packets = []
agent_votes = []

for agent_name in AGENTS:
    signals = generate_signals()
    packet = share_signals(agent_name, signals)
    shared_packets.append(packet)

    vote = vote_from_signals(signals)
    agent_votes.append({
        "agent": agent_name,
        "vote": vote,
        "signals": signals
    })

fused = fuse_shared_signals(shared_packets)
consensus = build_consensus(agent_votes)

print("\n=== BINDU GUARDIAN DISTRIBUTED RUNTIME V3 ===")
print(json.dumps({
    "fusion_result": fused,
    "consensus": consensus
}, indent=2))
