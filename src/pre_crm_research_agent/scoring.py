"""Deterministic scoring helpers for Pre-CRM Research Agent."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FinalActionRecommendation:
    """Decision recommendation returned after ICP scoring."""

    fit_level: str
    decision: str
    reason: str
    human_review_required: bool = True


def classify_fit_level(total_score: int) -> str:
    """Classify a 0-100 ICP score into a fit level."""

    if total_score < 0 or total_score > 100:
        raise ValueError("total_score must be between 0 and 100")

    if total_score >= 80:
        return "strong_fit"
    if total_score >= 65:
        return "good_fit"
    if total_score >= 50:
        return "unclear_fit"
    return "poor_fit"


def _normalize_confidence(value: str | None) -> str:
    return str(value or "low").strip().lower()


def recommend_final_action(
    *,
    total_score: int,
    buyer_access_confidence: str | None,
    pain_evidence_confidence: str | None,
    has_conflicting_signals: bool = False,
) -> FinalActionRecommendation:
    """Recommend the final workflow action from score and evidence confidence.

    This helper intentionally keeps the decision deterministic. LLM agents can
    generate evidence and notes, but the final action should be auditable.
    """

    fit_level = classify_fit_level(total_score)
    buyer_confidence = _normalize_confidence(buyer_access_confidence)
    pain_confidence = _normalize_confidence(pain_evidence_confidence)

    if has_conflicting_signals:
        return FinalActionRecommendation(
            fit_level=fit_level,
            decision="manual_review",
            reason="Conflicting signals require human review before CRM action.",
        )

    if total_score >= 80 and buyer_confidence in {"medium", "high"}:
        return FinalActionRecommendation(
            fit_level=fit_level,
            decision="add_to_crm",
            reason="Strong ICP score and sufficient buyer access evidence.",
        )

    if total_score >= 80:
        return FinalActionRecommendation(
            fit_level=fit_level,
            decision="research_more",
            reason="Strong ICP score, but buyer access is not sufficiently validated.",
        )

    if total_score >= 65 and pain_confidence == "high":
        return FinalActionRecommendation(
            fit_level=fit_level,
            decision="manual_review",
            reason="Good ICP score with strong pain evidence; human approval should decide CRM entry.",
        )

    if total_score >= 65:
        return FinalActionRecommendation(
            fit_level=fit_level,
            decision="research_more",
            reason="Good ICP score, but more evidence is needed before CRM entry.",
        )

    if total_score >= 50:
        return FinalActionRecommendation(
            fit_level=fit_level,
            decision="add_to_watchlist",
            reason="Unclear fit; keep the company available for later research or nurture.",
        )

    return FinalActionRecommendation(
        fit_level=fit_level,
        decision="reject",
        reason="Poor ICP fit based on the available evidence.",
    )
