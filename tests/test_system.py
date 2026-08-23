from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("source", "capability", "policy", "legal_ethics", "risk"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_policy_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_high_level_package_can_release():
    assert authorize("release_policy_support_package", approved_context())["allowed"] is True


def test_source_reliability_gap_blocks():
    assert authorize("release_policy_support_package", approved_context() | {"source_reliability_gap": True})["allowed"] is False


def test_operationalization_risk_blocks():
    assert authorize("release_policy_support_package", approved_context() | {"operationalization_risk": True})["allowed"] is False


def test_legal_ethics_gap_blocks():
    assert authorize("release_policy_support_package", approved_context() | {"legal_ethics_gap": True})["allowed"] is False


def test_civilian_harm_risk_blocks():
    assert authorize("release_policy_support_package", approved_context() | {"civilian_harm_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
