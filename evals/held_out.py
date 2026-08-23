"""Held-out governance scenarios for F147."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"source_reliability_gap": True}, False),
    (base() | {"classified_sensitive_gap": True}, False),
    (base() | {"operationalization_risk": True}, False),
    (base() | {"legal_ethics_gap": True}, False),
    (base() | {"civilian_harm_risk": True}, False),
    (base() | {"escalation_strategic_risk": True}, False),
    (base() | {"bias_alternative_gap": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_policy_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F147 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
