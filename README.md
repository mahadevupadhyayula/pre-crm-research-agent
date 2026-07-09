# Pre-CRM Research Agent

Pre-CRM Research Agent is an AI workflow for researching, scoring, and qualifying leads before they enter a CRM.

The core product question is:

> Is this lead worth pursuing, and how should we approach them?

## Why this project exists

Most sales teams treat CRM as the place where sales work starts. In many B2B workflows, that is too late.

When every lead is added to CRM before qualification, the CRM becomes noisy. Poor-fit leads sit beside high-fit leads, outreach becomes generic, and sales teams waste time cleaning, filtering, and deprioritizing records that should never have entered the pipeline.

Pre-CRM Research Agent creates a structured intelligence layer before CRM entry.

It helps teams:

- reduce manual prospect research time
- evaluate fit against a defined ICP
- detect likely pain points and buying signals
- generate a clear lead score
- create better outreach angles
- prepare CRM-ready notes only for leads worth pursuing

## Target users

- B2B founders
- sales teams
- outbound agencies
- RevOps consultants
- lead generation businesses
- recruiters
- consultants
- SaaS startups
- small teams doing manual prospect research

## Core workflow

```text
Lead / company input
  -> ICP context
  -> company research extraction
  -> company signal context
  -> ICP evaluation and score
  -> human review gate
  -> CRM-ready payload
  -> outreach task
  -> learning update
```

## Main outputs

- lead score
- ICP fit summary
- company research summary
- likely pain points
- buying triggers
- decision-maker relevance
- suggested outreach angle
- personalized email / LinkedIn draft direction
- CRM-ready notes
- recommended next action

## Design principle

Evidence first. Signal extraction second. Evaluation third. Human approval fourth. CRM action fifth.

This keeps the system from prematurely qualifying bad-fit companies and makes a clear distinction between observed facts and AI-generated hypotheses.

## Repository structure

```text
/docs
  workflow-architecture.md
  scoring-rubric.md
  prompt-chain.md
  implementation-roadmap.md

/schemas
  state-object.json

/examples
  sample-lead-input.json

/src/pre_crm_research_agent
  __init__.py
  workflow.py
  scoring.py
```

## Current status

Current implementation status: `workflow contract + documentation skeleton`.

This repo currently includes:

- project overview
- workflow architecture
- master state object
- prompt chain
- scoring rubric
- sample input
- lightweight Python workflow/scoring constants
- implementation roadmap

Next implementation steps are to connect concrete research agents, web/enrichment adapters, review queue, CRM payload generation, outreach task creation, persistence, and evaluation tests.

## Source resources

This project is based on the planning resources:

- Pre-CRM Research Agent — Researching, Scoring, and Qualifying Leads Before CRM Entry
- Pre-CRM Evaluation Workflow
