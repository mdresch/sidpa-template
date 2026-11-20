---
artifact_type: "methodology_guide"
stage: "1"
stage_name: "Intent"
pmbok_process: "Pre-Project: Strategic Need Identification"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "approve-ideation (FULL authority)"
---

# Stage 1: Intent — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Trigger event / strategic driver. Process: Validate intent. Output: Approved Ideation.

> **Renumbered 2026-11-12** (Sponsor decision): the Initiating group's stage numbers now match real execution order. Old Stage 2 (Objective) is now Stage 4; old Stage 3 (Hypothesis) is now Stage 2; old Stage 4 (Benefit) is now Stage 3. Stage 1 (Intent) and Stage 5 (Pillars) are unchanged. See [Intent-to-Outcome Chain Coverage](../chain-coverage.md) §0 for the full crosswalk and why. A document dated before 2026-11-12 that says "Stage 2", "Stage 3", or "Stage 4" means the **old** numbering — read it against that crosswalk, not against this guide's current numbers.

> **Purpose:** Capture the strategic trigger for a new phase (the Spark) and refine it into a falsifiable, scoped Ideation Document before any Charter, Business Case, or architecture work begins. Ideation is a whiteboard/brainstorm pass on the Spark, not a governance document in disguise: it stays lightweight by design, carrying only the trigger, the executive summary, and the measurable objectives — not hypothesis evidence (Stage 2), stakeholder taxonomy (Stage 4), scope/WBS (Stage 7), ADR rationale (Stage 5), or framework research (the research library, LL-044). Each of those has its own real home; Ideation references them, it does not restate them.

> **Alignment:** PMBOK 8 Pre-Project, Strategic Need Identification.

> **Authority:** FULL authority via `approve-ideation` (3 actions: `approve_ideation`, `reject_ideation`, `request_revision_before_decision`).

> **Authority in the project:** the Charter names one decision-maker, the Project Sponsor and Maintainer (<project maintainer>). An agent drafts the Spark and the Ideation Document and may run the policy's recommendation, but the Sponsor's words are the decision of record, registered with `task-policy-adjudicate` and `task-episode-register`. The agent never registers an approval on the Sponsor's behalf.

---

## 1. Overview

### 1.1 Position in the Chain

Stage 1 opens every phase and is the point Stage 18 (Intent Refinement) writes back into at phase close.

```
Stage 18 (Intent Refinement, prior phase)
    ↓  seeds
Stage 1 (Intent) — this stage
    ↓
Stage 2 (Hypothesis) classifies the HYP-AL-NNN rows this stage writes or carries
    ↓
Stage 3 (Benefit) drafts the Business Case and Benefits Management Plan on that classified evidence
    ↓
Stage 4 (Objective) drafts the Charter on top of Stage 3's output
```

This is a strict line, not a fan-out, and now reads in plain number order: `1 → 2 → 3 → 4`. The Business Case is built in neither Stage 1 nor Stage 4 — it is Stage 3's output, and Stage 4 cannot start until Stage 3 (which itself waits on Stage 2) is done.

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| The strategic trigger | A Stage 18 Intent Refinement Proposal (phase 2+), or a first-principles need (phase 1) | Yes |
| Prior phase's carried-over hypotheses and deferred items | The prior phase's Intent Refinement Proposal and Phase Carry-Over Backlog (`phase-rollup` skill) | If phase 2+ |
| Realized outcomes and lessons from the prior phase | `Lessons-Learned-Register.md`, `Continuous-Improvement-Register.md` | If phase 2+ |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| Spark Capture | `docs/project-docs/Spark-Capture.md` | Yes (via `approve-ideation`, bundled with Ideation) |
| Ideation Document | `docs/project-docs/Ideation-Document.md` | Yes (via `approve-ideation`) |

### 1.4 Success Criteria

Stage 1 is complete when:
- [x] `Spark-Capture.md` names the trigger, the strategic driver, and (phase 2+) what it carries over from the prior phase's close — `Spark-Capture.md` v3.0, `SPARK-P3-001` to `004`
- [x] `Ideation-Document.md` §1 states the executive summary, strategic boundaries, and measurable KPI bounds — unchanged through the v1.16–v1.20 rewrite
- [x] `Hypothesis-Register.md` (Stage 2's own document, since 2026-11-12) states every hypothesis this phase carries or introduces — 13 active carried hypotheses plus `HYP-AL-028`; 6 withdrawn (§2 there)
- [x] `approve-ideation` has run and the Sponsor's decision is recorded — twice: v1.15 (episode `c60c7021`), then the v1.16–v1.20 restructuring (episode `d526e945`)
- [x] Project-Status-Register.md names the new Spark/Ideation version and the episode id — updated 2026-11-12

**Stage 1 COMPLETED, 2026-11-12.**

---

## 2. Process

### Step 1: Capture the Spark

Write or update `Spark-Capture.md`. A first-phase Spark states the trigger from first principles. A phase-2+ Spark states what the prior phase's Intent Refinement Proposal (Stage 18) handed forward: carried-over hypotheses, deferred governance items, and Phase Carry-Over Backlog entries. Version the file (the Phase 3 seed, for example, is `Spark-Capture.md` v3.0, seeded 2026-11-11 from `IRP-20261111-001`).

### Step 2: Draft or amend the Ideation Document

`Ideation-Document.md` carries:
- §1 Executive Summary & Strategic Boundary Definitions, and Core Project Objectives & Measurable KPI Bounds.
- §2.1 Learning Methodologies Landscape (which methodologies exist and their maturity — stays here, it is not a hypothesis). §2.2's hypothesis tables moved to `Hypothesis-Register.md` on 2026-11-12 (Stage 2's own document, see Step 2 there); a new hypothesis gets a new id there (never reused), a carried hypothesis keeps its id and prior status.
- A dated "Updated" line in the header metadata block naming what changed and why, in the same style as the existing entries (for example the 2026-11-11 Phase 3 seeding line that names `IRP-20261111-001`, `PCD-20261111-001`, `CLK-20261111-001`, and the new `HYP-AL-028`).

Never invent a hypothesis to fill a gap; a hypothesis exists because a real design assumption needs testing (ADR-024 methodology selection depends on this).

### Step 3: Submit for `approve-ideation`

Run the policy's recommendation (`task-policy-decide`), show it to the Sponsor, and wait for their words. On the Sponsor's explicit instruction, run `task-policy-adjudicate` then `task-episode-register`, printing the store path and its file count before and after (LL-040).

### Step 4: Record and hand off

Record the decision, its date, and the episode id in `Project-Status-Register.md` §1 (Current Orientation) and §2 (Phase Status). Stage 2 (Hypothesis) reads the now-approved Ideation Document next. Stage 4 (Objective) does **not** start here — it waits for Stage 3 (Benefit), which itself waits for Stage 2: a Stage's predecessor is whatever the dependency graph actually names, not inferred from stage number order alone — though after the 2026-11-12 renumbering, for Stages 1-4 the two now agree.

---


## 4. Validation

```bash
grep -n "^## " docs/project-docs/Spark-Capture.md
grep -n "^### SECTION\|HYP-AL-" docs/project-docs/Ideation-Document.md | head -40
```
No dedicated schema-validation script exists for these two files in this repository; review against `approve-ideation`'s own action descriptions (strategic motivation, falsifiable hypotheses, grounded scope) and against `docs/policy-shapes/approve-ideation.actions.json`.

---

## 5. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| Treating a seeded Spark/Ideation as already approved | Check Project-Status-Register.md §1, not the file's existence |
| Inventing a hypothesis to justify scope already decided elsewhere | A hypothesis is a real, falsifiable design assumption (Stage 2); scope decisions belong in §1, not §2 |
| Dropping a carried-over hypothesis's id when re-stating it | Carried hypotheses keep their `HYP-AL-NNN` id and prior status; only a new assumption gets a new id |

---

## 6. References

- [Intent-to-Outcome Chain Coverage](../chain-coverage.md) — §0 renumbering crosswalk, §2 row 1, §4 `approve-ideation`
- [Project-Status-Register.md](../Project-Status-Register.md) — §1, §2
- [Spark-Capture.md](../Spark-Capture.md)
- [Ideation-Document.md](../Ideation-Document.md)
- [Stage 18: Intent Refinement Methodology](Stage-18-Intent-Refinement-Methodology.template.md) — the stage that seeds this one
- [Stage 2: Hypothesis Methodology](Stage-02-Hypothesis-Methodology.template.md)

---
