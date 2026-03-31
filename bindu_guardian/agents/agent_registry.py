AGENTS = {
    "clinical_guardian": {
        "domain": "hospital",
        "focus": ["medication_workflows", "clinical_access", "critical_care"]
    },
    "identity_guardian": {
        "domain": "hospital",
        "focus": ["identity_access", "privilege_changes", "login_anomalies"]
    },
    "network_guardian": {
        "domain": "hospital",
        "focus": ["network_segments", "spread_detection", "communications_disruption"]
    },
    "coordinator_guardian": {
        "domain": "hospital",
        "focus": ["shared_awareness", "decision_fusion", "human_routing"]
    }
}
