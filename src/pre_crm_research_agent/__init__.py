"""Pre-CRM Research Agent package."""

from .workflow import (
    ALLOWED_FINAL_ACTIONS,
    ALLOWED_HUMAN_DECISIONS,
    DECISION_THRESHOLDS,
    SCORING_WEIGHTS,
    STATE_SECTIONS,
    WORKFLOW_GOAL,
    WORKFLOW_NAME,
    WORKFLOW_STEPS,
    should_trigger_pre_crm_research,
)
from .scoring import classify_fit_level, recommend_final_action

__all__ = [
    "ALLOWED_FINAL_ACTIONS",
    "ALLOWED_HUMAN_DECISIONS",
    "DECISION_THRESHOLDS",
    "SCORING_WEIGHTS",
    "STATE_SECTIONS",
    "WORKFLOW_GOAL",
    "WORKFLOW_NAME",
    "WORKFLOW_STEPS",
    "should_trigger_pre_crm_research",
    "classify_fit_level",
    "recommend_final_action",
]
