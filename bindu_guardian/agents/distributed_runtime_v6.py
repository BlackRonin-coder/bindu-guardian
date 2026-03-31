import json
from signal_simulator import generate_signals
from bindu_guardian.agents.agent_registry import AGENTS
from bindu_guardian.agents.agent_signal_share import share_signals, fuse_shared_signals
from bindu_guardian.agents.agent_vote import vote_from_signals
from bindu_guardian.agents.consensus_engine import build_consensus
from bindu_guardian.agents.escalation_pressure import detect_escalation_pressure
from bindu_guardian.agents.consensus_override import apply_override
from bindu_guardian.agents.temporal_memory import record_cycle, get_history
from bindu_guardian.agents.trend_analysis import analyse_trend
from bindu_guardian.agents.temporal_override import apply_temporal_override
from bindu_guardian.agents.situation_classifier import classify_situation
from bindu_guardian.agents.response_mapper import map_response

for cycle in range(1, 4):
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

    pressure = detect_escalation_pressure(consensus["weighted_totals"])
    override = apply_override(consensus["consensus_action"], pressure)

    record_cycle(consensus["weighted_totals"])
    trend = analyse_trend(get_history())
    temporal = apply_temporal_override(override["final_action"], trend)

    situation = classify_situation(consensus, pressure, trend)
    mapped = map_response(situation["situation_type"])

    print(f"\n=== BINDU GUARDIAN DISTRIBUTED RUNTIME V6 / CYCLE {cycle} ===")
    print(json.dumps({
        "fusion_result": fused,
        "consensus": consensus,
        "pressure_analysis": pressure,
        "override": override,
        "trend_analysis": trend,
        "temporal_override": temporal,
        "situation": situation,
        "mapped_response": mapped
    }, indent=2))
