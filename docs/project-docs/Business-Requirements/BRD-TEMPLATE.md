---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Planning"
pmbok_process: "5.2 Collect Requirements & 5.3 Define Scope"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
lifecycle_stage: "Stage 7 (Requirement: Business)"
governance_policy: "approve-brd"
inputs:
  - "Project-Charter.md"
  - "Project-Management-Plan.md (Scope Management Plan)"
process: "Define functional and non-functional business requirements and stakeholder rules"
outputs:
  - "BRD-*.md"
---

# BRD-<NNN>: <Title>

> **PMBOK 8 Process:** `5.2 Collect Requirements & 5.3 Define Scope` (Planning)  
> **Governance Policy:** `approve-brd` | **Lifecycle Stage:** `Stage 7 (Requirement: Business)`  
> **Inputs:** Project-Charter.md, Project-Management-Plan.md (Scope Management Plan)  
> **Process:** Define functional and non-functional business requirements and stakeholder rules  
> **Outputs:** BRD-*.md


**Source ADR:** [ADR-<NNN>](../../07-architecture/ADR-<NNN>-<slug>.md) — <its real status>
**Governing Baseline:** `<baseline_id>` · **Cycle:** `<cycle_id>` (see the Cycle Register)
**Status:** Draft — business rules derived from an Accepted ADR, not yet built
**Stakeholders:** <the real ones. If there's no formal Product Owner or separate business stakeholder, say that plainly rather than inventing a role.>

## Business Need
<Why this matters in business terms, grounded in the source ADR's own §3. Don't restate the ADR's technical content — translate it.>

## Business Rules (BRU)
- **BRU-<NNN>-01**: <rule>, citing the specific ADR section it comes from.
<Every rule traces to a specific ADR section. A BRD that invents a rule the ADR doesn't actually support is drifting from its own source.>

## Stakeholder Success Metrics
<Named honestly. "Not measurable yet" is a correct, valid entry if that's the truth — don't invent a number to fill the cell.>

| Metric | Current state |
|---|---|

## Baseline Feedback (Stage 7-8 → 6)
<While writing or reviewing this document, did you find that it contradicts, or cannot be satisfied by, the approved baseline (the PMP, a subsidiary plan, the Charter, or an upstream document)? Raise each contradiction as a BFI-NNN in the PMP's Pending Baseline Feedback table (PMP §3.3) and cite it here by id and by the documents it concerns. Do not fix the baseline inside this document, and do not open an Adaptation Plan: that is the Stage 17 route and needs evidence from executed work. "None found" is a valid entry.>

| BFI | Contradiction (cite the documents) | Status |
|---|---|---|
| None found | | |

## Out of Scope
<What the source ADR itself already excludes — don't introduce a new exclusion here that the ADR didn't name.>
