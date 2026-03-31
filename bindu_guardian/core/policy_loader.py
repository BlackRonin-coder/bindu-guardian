import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_policy():
    with open(ROOT / "policies" / "core_policy.json", "r", encoding="utf-8") as f:
        return json.load(f)
