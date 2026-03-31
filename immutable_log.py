import json
from datetime import datetime

LOG_FILE = "guardian_immutable_log.jsonl"

def write_immutable_log(event_type, payload):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "payload": payload
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return entry
