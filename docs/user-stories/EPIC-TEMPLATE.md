---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Planning"
pmbok_process: "5.4 Create WBS & Backlog Elaboration"
pmp_baseline: "PMP-BL-v<X.Y.Z>"
lifecycle_stage: "Stage 6 (Requirement: Story)"
governance_policy: "approve-user-stories"
inputs:
  - "FDD-*.md"
  - "BRD-*.md"
  - "ADR-*.md"
process: "Decompose solution requirements into testable user stories with explicit acceptance criteria"
outputs:
  - "user-stories/epic-*.md"
  - "Testable User Stories"
---

# Epic <N>: <Title>

> **PMBOK 8 Process:** `5.4 Create WBS & Backlog Elaboration` (Planning)  
> **Governance Policy:** `approve-user-stories` | **Lifecycle Stage:** `Stage 6 (Requirement: Story)`  
> **Inputs:** FDD-*.md, BRD-*.md, ADR-*.md  
> **Process:** Decompose solution requirements into testable user stories with explicit acceptance criteria  
> **Outputs:** user-stories/epic-*.md, Testable User Stories


**Source ADR:** [ADR-<NNN>](../07-architecture/ADR-<NNN>-<slug>.md)
**Source BRD/FDD:** [BRD-<NNN>](../project-docs/Business-Requirements/BRD-<NNN>-<slug>.md) / [FDD-<NNN>](../project-docs/Functional-Design/FDD-<NNN>-<slug>.md)

**Governing Baseline:** `PMP-BL-v<X.Y.Z>` (Invariant 6)

## Story <N>.1 — <title>

**Status:** Ready (not yet run through `implement-story`) — or Blocked, naming the real blocker (a blocker that is a baseline defect is named by its BFI id; see Baseline Feedback below)
**As** <role>, **I want** <capability>, **so that** <reason>.

**Acceptance Criteria:**
- $AC_0$: <concrete, contract-testable condition>

## Baseline Feedback (Stage 7-8 → 6)
<While writing or reviewing this document, did you find that it contradicts, or cannot be satisfied by, the approved baseline (the PMP, a subsidiary plan, the Charter, or an upstream document)? Raise each contradiction as a BFI-NNN in the PMP's Pending Baseline Feedback table (PMP §3.3) and cite it here by id and by the documents it concerns. Do not fix the baseline inside this document, and do not open an Adaptation Plan: that is the Stage 17 route and needs evidence from executed work. "None found" is a valid entry.>

| BFI | Contradiction (cite the documents) | Status |
|---|---|---|
| None found | | |

<A story that cannot proceed because of an open BFI names it in its Status line, for example `Blocked by BFI-003 (awaiting Steering Committee approval of the Baseline Revision Package)`. Do not invent an "adaptation" to unblock it.>

## If this epic has zero code-shaped stories

That's a valid, correct output — not a gap. State why plainly (cite the FDD section that explains it), the same way the source projects' own Epic-3-equivalent does. Do not invent a story to fill this template.

## Before running `implement-story` on any story here

Run `validate-intent-foundation` first (see `docs/policy-shapes/validate-intent-foundation.json`) — document approval and pipeline-entry readiness are different questions. Record the real recommendation and the real human sign-off in this story's own Status line once it clears, the same way the source projects do.
