from AGENTS import capability_agent, legal_ethics_agent, policy_agent, risk_agent, source_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "source": source_agent.run(case),
        "capability": capability_agent.run(case),
        "policy": policy_agent.run(case),
        "legal_ethics": legal_ethics_agent.run(case),
        "risk": risk_agent.run(case),
    }
    governance = authorize("release_policy_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
