"""Claim-type → criterion map for PR-gate triage replay (IMP-017).

Vendored slice of agent-learning's triage_replay: only the mapping the gate needs.
"""

from __future__ import annotations

from collections.abc import Mapping

CLAIM_TO_CRITERION_MAP: Mapping[str, str] = {
    "crash risk": "correctness",
    "logic error": "correctness",
    "test gap": "test_coverage",
    "documentation": "implementation_quality",
    "style": "implementation_quality",
    "confirmation": "correctness",
}


def map_claim_to_criterion(claim_type: str) -> str:
    """Map a finding claim type to a standardized DecisionFrame criterion."""
    clean = claim_type.strip().lower()
    return CLAIM_TO_CRITERION_MAP.get(clean, "correctness")
