---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Planning"
pmbok_process: "5.3 Define Scope & Architectural Strategy"
lifecycle_stage: "Stage 5 (Pillars & Architecture)"
governance_policy: "approve-project-pillars"
inputs:
  - "Project-Charter.md"
  - "PILLARS-EXERCISE.md"
  - "Spark-Capture.md"
  - "Ideation-Document.md"
  - "Business-Case.md"
  - "Benefits-Management-Plan.md"
process: "Roll up approved pillars into topic statements with primary ADR assignments"
outputs:
  - "Project-Pillars.md"
---

# Project Pillars — <project name>

> **Governance Policy:** `approve-project-pillars` | **Lifecycle Stage:** `Stage 5 (Pillars & Architecture)`  
> **Sources:** Spark, Ideation, Business Case, Benefits Management Plan, and the [Pillars Exercise](../07-architecture/PILLARS-EXERCISE.md).

## Pillars

Each pillar is a **durable topic**, not a one-shot slot. Many ADRs may address the same pillar over the project lifetime.

### <Pillar name>
- **Statement:** <one-sentence scope>
- **Sources:** <Spark / Ideation / Business Case sections>
- **An ADR addresses this pillar when:** <criterion>

## Primary assignment

| ADR | Primary topic pillar |
|---|---|
| ADR-001 | <pillar name> |

## Not a pillar

<Document classes and tooling routes that intentionally bypass Stage 5/6 — conventions, not accidents.>

## Amendment log

| Date | Author | Change |
|---|---|---|
| <date the project starts> | <name> | Initial approval candidate. |