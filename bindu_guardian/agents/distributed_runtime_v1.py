import json
from signal_simulator import generate_signals
from bindu_guardian.agents.agent_registry import AGENTS
from bindu_guardian.agents.agent_signal_share import share_signals, fuse_shared_signals

shared_packets = []

for agent_name in AGENTS:
    signals = generate_signals()
    packet = share_signals(agent_name, signals)
    shared_packets.append(packet)

fused = fuse_shared_signals(shared_packets)

print("\n=== BINDU GUARDIAN DISTRIBUTED RUNTIME V1 ===")
print(json.dumps({
    "agents": list(AGENTS.keys()),
    "shared_packets": shared_packets,
    "fusion_result": fused
}, indent=2))
