import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / "logs" / "guardian_log.jsonl"

def write_log(event_type, payload):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "payload": payload
    }

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return entry
