def vote_from_signals(signals):
    count = len(signals)

    vote = "observe"
    if count >= 2:
        vote = "stabilize"
    if count >= 4:
        vote = "isolate"
    if count >= 5:
        vote = "escalate"

    return vote
