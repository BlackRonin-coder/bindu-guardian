def share_signals(agent_name, signals):
    return {
        "agent": agent_name,
        "signals": signals,
        "signal_count": len(signals)
    }

def fuse_shared_signals(shared_packets):
    fused = []
    for packet in shared_packets:
        fused.extend(packet["signals"])

    unique_signals = sorted(set(fused))
    return {
        "shared_packets": len(shared_packets),
        "fused_signals": unique_signals,
        "fused_count": len(unique_signals)
    }
