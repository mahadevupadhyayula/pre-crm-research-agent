"""
Workflow contract for the Pre-CRM Research Agent.

This module keeps the project logic explicit and importable while the full
agent, orchestration, persistence, and integration layers are built out.
"""

from __future__ import annotations

WORKFLOW_NAME = "pre_crm_research_workflow"

WORKFLOW_GOAL = (
    "Research, score, and qualify leads before CRM entry so GTM teams can "
    "avoid CRM clutter, prioritize better-fit accounts, and generate "
    "approval-ready outreach tasks."
)

WORKFLOW_STEPS = [
    "icp_context_agent",
    "company_signal_research_agent",
    "icp_evaluation_agent",
    "human_review_gate_agent",
    "crm_payload_agent",
    "outreach_task_agent",
    "learning_update_agent",
]

STATE_SECTIONS = [
    "company_input",
    "icp_context",
    "company_research_notes",
    "company_signal_context",
    "pre_crm_evaluation",
    "human_review",
    "crm_payload",
    "outreach_task",
    "learning_update",
    "state_log",
]

SCORING_WEIGHTS = {
    "firmographic_icp_fit": 20,
    "sales_motion_fit": 20,
    "gtm_pain_intensity": 25,
    "tool_data_readiness": 15,
    "urgency_trigger_strength": 10,
    "buyer_accessibility": 10,
}

DECISION_THRESHOLDS = {
    "strong_fit": "80-100",
    "good_fit": "65-79",
    "unclear_fit": "50-64",
    "poor_fit": "below 50",
}

ALLOWED_FINAL_ACTIONS = [
    "add_to_crm",
    "research_more",
    "add_to_watchlist",
    "manual_review",
    "reject",
]

ALLOWED_HUMAN_DECISIONS = [
    "approve_add_to_crm",
    "reject",
    "research_more",
    "add_to_watchlist",
    "manual_review_later",
]

PRE_CRM_RESEARCH_TRIGGER_EVENTS = {
    "pre_crm_research",
    "lead_research",
    "company_intake",
    "manual_pre_crm",
}


def should_trigger_pre_crm_research(raw_data: dict) -> bool:
    """Return true when a lead/company should enter the pre-CRM research workflow."""

    workflow_id = str(raw_data.get("workflow_id", "")).strip().lower()
    if workflow_id == WORKFLOW_NAME:
        return True

    trigger_event = str(raw_data.get("trigger_event", "")).strip().lower()
    if trigger_event in PRE_CRM_RESEARCH_TRIGGER_EVENTS:
        return True

    if bool(raw_data.get("pre_crm_research_required")):
        return True

    has_company_identity = bool(
        raw_data.get("company_name")
        or raw_data.get("website_url")
        or raw_data.get("linkedin_company_url")
    )
    has_intake_signal = bool(
        raw_data.get("icp_context")
        or raw_data.get("target_geography")
        or raw_data.get("outreach_goal")
        or raw_data.get("notes_from_user")
    )

    return has_company_identity and has_intake_signal
