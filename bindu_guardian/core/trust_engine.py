from bindu_guardian.core.trust_registry import get_trusted_roles

def evaluate_actor(domain, actor_role):
    trusted_roles = get_trusted_roles(domain)
    trusted = actor_role in trusted_roles

    return {
        "domain": domain,
        "actor_role": actor_role,
        "trusted": trusted,
        "reason": "trusted role" if trusted else "role not trusted for critical control"
    }
