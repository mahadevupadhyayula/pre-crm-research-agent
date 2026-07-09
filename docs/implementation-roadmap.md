# Implementation Roadmap

## Current repo scope

This repository incorporates the Pre-CRM Research Agent as a standalone project package.

Included now:

- project overview
- workflow architecture
- state object contract
- prompt chain
- scoring rubric
- sample lead input
- lightweight Python workflow constants
- deterministic scoring helpers
- implementation roadmap

## Phase 1: Contract and demo workflow

Goal: make the project understandable and runnable as a controlled workflow skeleton.

Tasks:

- [x] Add README
- [x] Add workflow architecture
- [x] Add state object contract
- [x] Add scoring rubric
- [x] Add prompt chain
- [x] Add sample input
- [x] Add lightweight Python workflow constants
- [x] Add deterministic scoring helper
- [ ] Add basic CLI demo run
- [ ] Add unit tests for scoring and decision logic

## Phase 2: Agent implementations

Goal: connect workflow stages to concrete agent implementations.

Agents to add:

- ICP Context Agent
- Company Signal Research Agent
- ICP Evaluation Agent
- Human Review Gate Agent
- CRM Payload Agent
- Outreach Task Agent
- Learning Update Agent

Each agent should produce structured outputs and update only its allowed state section.

## Phase 3: Data and tool adapters

Goal: support realistic inputs and downstream actions.

Adapters:

- Google Sheets / CSV input adapter
- web research adapter
- enrichment adapter
- CRM duplicate check adapter
- CRM payload adapter
- outreach task adapter
- review queue adapter

## Phase 4: Persistence and auditability

Goal: persist workflow runs, evaluation decisions, human review status, CRM payloads, and learning updates.

Data stores:

- workflow state repository
- lead evaluation repository
- human review repository
- CRM payload repository
- outreach task repository
- learning memory repository

## Phase 5: Evaluation layer

Goal: test scoring reliability and output quality.

Evaluation areas:

- ICP score consistency
- evidence grounding
- hallucination / unsupported claim checks
- outreach angle relevance
- human approval rate
- rejected-lead analysis
- score vs downstream outcome correlation

## Phase 6: UI and portfolio demo

Goal: turn the workflow into a clear portfolio demo.

Suggested demo flow:

1. Upload or paste a lead list.
2. Select or define ICP criteria.
3. Run research and scoring.
4. Review lead intelligence cards.
5. Approve / reject / research more.
6. Generate CRM payload and outreach task.
7. Show learning update after outcome.

## Definition of implemented

This workflow should be marked `Implemented` only when it satisfies all five criteria:

1. Trigger exists.
2. Orchestration is sequenced by the workflow runner.
3. At least one action/tool path is runnable.
4. Outcomes are analyzed/scored after execution.
5. State/outcomes are persisted for resume/audit.

Until all five are true, keep the status as `Partial` or `Workflow Contract`.
