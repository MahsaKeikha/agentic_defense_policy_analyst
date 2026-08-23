"""Fail-closed governance for F147 Agentic Defense Policy Analyst.

This reference system is limited to high-level policy analysis. It does not
provide operational targeting, weapon construction, evasion, or actionable
harm-enabling assistance.
"""

PROTECTED_ACTIONS = {
    "authorize_use_of_force",
    "approve_operational_plan",
    "select_or_prioritize_target",
    "authorize_weapon_employment",
    "issue_operational_command",
    "external_operational_distribution",
}

REQUIRED_REVIEWS = (
    "source_quality_reviewed",
    "capability_context_reviewed",
    "policy_options_reviewed",
    "legal_ethics_reviewed",
    "civilian_harm_reviewed",
    "escalation_risk_reviewed",
    "classification_release_reviewed",
    "qualified_policy_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "operational force, targeting, weapon-employment, command, or operational-distribution action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required defense-policy review", "missing": missing}
    checks = {
        "source_reliability_gap": "material source reliability, freshness, corroboration, or provenance uncertainty unresolved",
        "classified_sensitive_gap": "classification, controlled-information, operational-security, privacy, or release-status issue unresolved",
        "operationalization_risk": "analysis would materially enable targeting, weapon construction, evasion, force employment, or other actionable harm",
        "legal_ethics_gap": "material domestic-law, international-law, rules, authority, human-rights, or ethical question unresolved",
        "civilian_harm_risk": "material civilian protection, humanitarian, proportionality, discrimination, or downstream harm concern unresolved",
        "escalation_strategic_risk": "material escalation, misperception, alliance, deterrence, proliferation, crisis-stability, or strategic-risk issue unresolved",
        "bias_alternative_gap": "material analytic bias, missing alternative hypothesis, adversarial assumption, or uncertainty treatment unresolved",
        "provenance_documentation_gap": "source, assumption, estimate, scenario, option, legal basis, or decision provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "defense-policy governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "high-level defense-policy support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
