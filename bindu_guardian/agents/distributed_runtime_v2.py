import json
from signal_simulator import generate_signals
from bindu_guardian.agents.agent_registry import AGENTS
from bindu_guardian.agents.agent_signal_share import share_signals, fuse_shared_signals
from bindu_guardian.agents.decision_fusion import decide_from_fusion

shared_packets = []

for agent_name in AGENTS:
    signals = generate_signals()
    packet = share_signals(agent_name, signals)
    shared_packets.append(packet)

fused = fuse_shared_signals(shared_packets)
decision = decide_from_fusion(fused["fused_signals"])

print("\n=== BINDU GUARDIAN DISTRIBUTED RUNTIME V2 ===")
print(json.dumps({
    "agents": list(AGENTS.keys()),
    "fusion_result": fused,
    "decision": decision
}, indent=2))
