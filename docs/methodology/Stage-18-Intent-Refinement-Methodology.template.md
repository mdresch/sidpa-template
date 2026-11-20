---
artifact_type: "methodology_guide"
stage: "18"
stage_name: "Intent Refinement"
pmbok_process: "4.7 Close Project or Phase (Cognitive Feedback)"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "approve-intent-refinement (FULL authority)"
---

# Stage 18: Intent Refinement — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Stage 17 adaptations & phase review. Process: Strategic review of intent. Output: Catalyst for Phase N+1 Spark.

> **Purpose:** This document provides a comprehensive methodology for Stage 18 (Intent Refinement) of the Intent-to-Outcome chain. Stage 18 performs phase closure readiness evaluation, Bayesian hypothesis adjudication, and seeds the next phase with refined intent based on all realized outcomes and lessons learned.

> **Alignment:** PMBOK 8 Process 4.7 Close Project or Phase (Cognitive Feedback)

> **Authority:** FULL authority via `approve-intent-refinement` policy (3 actions: approve, reject, request revision)

> **Status:** **READY** - All inputs prepared from Stage 17

---

## 1. Stage 18 Overview

### 1.1 Purpose and Position in the Chain

Stage 18 is the **cognitive feedback gate** that closes Phase 1 and seeds Phase 2. It sits at the final position in the Intent-to-Outcome chain, performing strategic reflection and refinement based on all accumulated knowledge.

```
Stage 17 (Adaptation Plan)
    \u2193
Stage 18 (Intent Refinement) \u0014 Cognitive Feedback & Phase Closure
    \u2193
Phase 1 CLOSED \u0014 Phase 2 READY
```

**Key Responsibility:** Evaluate phase closure readiness, adjudicate hypotheses, and seed the next phase with refined intent based on realized outcomes.

**Cycle after the PMP is approved (Sponsor, 2026-11-11):** Stage 8 Implementation Readiness (the Implementation Authorization Notice gate), Stage 9 Execution (Deliverable), Stage 10 Verification (all contracts are run and passing), Stage 11 Audit Record, Stage 12 Actual Outcome Analysis, Stage 13 System Telemetry Review and Findings (Observation), Stage 14 Insights, Stage 15 Lessons Learned, Stage 16 Governance Change Analysis, Stage 17 Adaptation Plan Analysis, Stage 18 Intent Refinement Analysis, and back to Stage 1 Spark and Ideation.

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| Stage 17 Adaptation Plan | Stage 17 output | Yes |
| All Lessons Learned | Stage 15 output (LL-001 to LL-046) | Yes |
| All Governance Episodes | Stage 16 output | Yes |
| All Observations | Stage 13 output (OBS-001 to OBS-009) | Yes |
| All Insights | Stage 14 output (INSIGHT-001 to INSIGHT-004) | Yes |
| Current PMP Baseline | Project-Management-Plan.md | Yes |
| Phase Close Readiness | evaluate_phase_close_readiness() | Yes |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| Intent Refinement Proposal | `docs/governance/irp/` | Yes (via approve-intent-refinement) |
| Phase Close Decision | `docs/governance/decisions/` | Yes |
| Next Phase Spark | `docs/pmbok/Spark-Capture.md` | Yes |
| Next Phase Ideation | `docs/pmbok/Ideation-Document.md` | Yes |
| Updated PMP Baseline | Project-Management-Plan.md | Yes |
| Cumulative Lineage Kernel | `docs/governance/lineage/` | Yes |

### 1.4 Success Criteria

Stage 18 is complete when:
- [ ] Phase closure readiness is evaluated and approved
- [ ] All Stage 3 hypotheses are adjudicated to terminal states
- [ ] Intent Refinement Proposal is approved via `approve-intent-refinement`
- [ ] Next phase spark and ideation documents are generated
- [ ] PMP baseline is updated to PMP-BL-v1.0.1
- [ ] Cumulative Lineage Kernel is computed
- [ ] All changes are committed and pushed
- [ ] Project-Status-Register.md is updated

---

## 2. Intent Refinement Process (8-Step)

### Step 1: Readiness Audit

**Purpose:** Verify that all prerequisites for Stage 18 are met.

**Actions:**
1. Run `evaluate_phase_close_readiness()` to check:
   - All Stage 9 deliverables are accepted
   - Stage 11 audit records have no unresolved non-conformances
   - Stage 15 lessons learned are crystallized
   - Stage 16 governance changes are operationalized
   - Stage 17 adaptations are complete

2. Validate all required inputs exist:
   - All observations (OBS-001 to OBS-009)
   - All insights (INSIGHT-001 to INSIGHT-004)
   - All lessons (LL-001 to LL-046)
   - All governance episodes
   - Current PMP baseline

3. Verify test suite passes (1840 passed, 0 failures)

**Checklist:**
- [ ] `evaluate_phase_close_readiness()` returns READY
- [ ] All Stage 1-17 artifacts are committed
- [ ] All governance episodes are recorded
- [ ] Test suite passes with no regressions
- [ ] Project-Status-Register.md shows Stage 17 COMPLETED

**Validation Command:**
```bash
# Run readiness check
python -c "(legacy pmbok models — not in template).intent_refinement import evaluate_phase_close_readiness; result = evaluate_phase_close_readiness(); print(result.status)"

# Verify test suite
uv run pytest --ignore=tests/test_spark.py --ignore=tests/pmbok -q --tb=no
```

**Success Criteria:** ReadinessPreconditionError is NOT raised

---

### Step 2: Hypothesis Inventory

**Purpose:** Catalog all hypotheses from Phase 1 for adjudication.

**Actions:**
1. Extract all hypotheses from:
   - Stage 3 (Deliverable) acceptance criteria
   - Stage 9 (Deliverable) validation
   - Stage 12 (Actual Outcome) assessments
   - All observations, insights, and lessons

2. Create hypothesis inventory with:
   - Hypothesis ID
   - Source stage
   - Hypothesis statement
   - Current status
   - Bayes Factor (if available)
   - Related evidence

3. Verify all hypotheses have sufficient evidence for adjudication

**Template:**
```markdown
## Hypothesis Inventory

| ID | Source | Statement | Current Status | Bayes Factor | Evidence |
|---|---|---|---|---|---|
| HYP-001 | Stage 3 | [Statement] | Active | BF=5.2 | [Evidence] |
| HYP-002 | Stage 9 | [Statement] | Active | BF=12.4 | [Evidence] |
```

**Success Criteria:** All hypotheses cataloged with evidence

---

### Step 3: Bayes Factor Adjudication

**Purpose:** Adjudicate all hypotheses using empirical Bayes factors.

**Actions:**
1. For each hypothesis, compute Bayes Factor (BF10):
   - BF10 >= 10: VALIDATED (graduated to permanent architectural invariant)
   - BF10 <= 0.1: REFUTED (archived with negative reinforcement)
   - 0.1 < BF10 < 10: INCONCLUSIVE (requires further evaluation)

2. Run `resolve_hypothesis()` for each hypothesis
3. Run `adjudicate_hypothesis_batch()` for batch processing
4. Apply recurrence depth guard (max 3 cycles)

**Adjudication Rules:**
- VALIDATED hypotheses become permanent architectural invariants
- REFUTED hypotheses are archived with negative reinforcement learning penalty
- INCONCLUSIVE hypotheses at cycle 3 (d=2) are collapsed to REFUTED

**Success Criteria:** 100% of hypotheses resolve to terminal states (VALIDATED or REFUTED)

---

### Step 4: Low-Pass Damping

**Purpose:** Apply low-pass filter to smooth outcome deltas and eliminate strategic whiplash.

**Actions:**
1. Compute rolling outcome deltas using exponential moving average:
   - ΘN+1 = βΘN + (1-β)∇L
   - β ∈ [0.6, 0.85] (damping factor)
   - Bias-corrected warmup for initial generations (N < 3)

2. Apply `LowPassOutcomeDampingFilter` to all outcome metrics
3. Validate damping eliminates strategic whiplash

**Success Criteria:** All outcome deltas are smoothed within acceptable bounds

---

### Step 5: Strategic Pivot Capacity Validation

**Purpose:** Ensure proposed strategic pivots don't exceed operational adaptation capacity.

**Actions:**
1. Run `validate_strategic_pivot_capacity()` to check:
   - Pivots_max <= ceil(C_adapt / 2)
   - No StrategicWhiplashError is raised

2. Validate S3-S4 Homeostatic Capacity Balance

**Success Criteria:** All strategic pivots are within capacity limits

---

### Step 6: Intent Refinement Proposal

**Purpose:** Create formal Intent Refinement Proposal with all findings.

**Actions:**
1. Create `IRP-20261106-001-Phase-1-Intent-Refinement-Proposal.md`
2. Include:
   - Phase closure readiness results
   - Hypothesis adjudication results
   - Low-pass damping results
   - Strategic pivot capacity validation
   - Refined intent for Phase 2
   - Baseline update (PMP-BL-v1.0.0 → PMP-BL-v1.0.1)

**Template:**
```markdown
---
artifact_type: "intent_refinement_proposal"
proposal_id: "IRP-20261106-001"
baseline_from: "PMP-BL-v1.0.0"
baseline_to: "PMP-BL-v1.0.1"
version: "1.0"
date: "2026-11-06"
---

# Intent Refinement Proposal: IRP-20261106-001

## Phase 1 Closure & Phase 2 Seeding

### Readiness Audit
[Results from Step 1]

### Hypothesis Adjudication
[Results from Step 3]

### Low-Pass Damping
[Results from Step 4]

### Strategic Pivot Capacity
[Results from Step 5]

### Refined Intent for Phase 2
[Refined intent statement]
```

**Success Criteria:** Proposal validates against IntentRefinementProposalPayload schema

---

### Step 7: Approval Gate

**Purpose:** Obtain FULL authority approval for the Intent Refinement Proposal.

**Actions:**
1. Submit proposal to `approve-intent-refinement` policy
2. Policy performs multi-criteria Bayesian evaluation
3. Human approval required (requires_human_approval: true)
4. Policy can: approve, reject, or request revision

**Approval Criteria:**
- All steps 1-6 completed successfully
- Proposal validates against schema
- All hypotheses adjudicated to terminal states
- Strategic pivot capacity within limits
- Low-pass damping applied successfully

**Success Criteria:** Proposal approved via `approve-intent-refinement`

---

### Step 8: Phase Seeding

**Purpose:** Seed Phase 2 with refined intent.

**Actions:**
1. Run `(project phase-close / seed tooling — not shipped in sidpa-template) --mode seed-next` to:
   - Generate Phase 2 `Spark-Capture.md`
   - Generate Phase 2 `Ideation-Document.md`
   - Populate with approved directives
   - Increment baseline to PMP-BL-v1.0.1

2. Run `(project phase-close / seed tooling — not shipped in sidpa-template) --mode close` to:
   - Prune ephemeral worktrees
   - Archive Phase 1 artifacts
   - Update Project-Status-Register.md

3. Compute `CumulativeLineageKernel` for project generations

4. **Final step (Sponsor, 2026-11-11):** bump or create the new PMP baseline (Phase 2 to Phase 3: `PMP-BL-v1.2.0`) as one of the last Stage 18 actions, after the lineage kernel and the Project-Status-Register update. Until then the current baseline stays in force. The subsidiary plans move with the baseline: the roll-up into the Project Management Plan starts from the Spark and runs in this order: Spark, Ideation, Benefits Statement, Business Case, Stakeholder Register, Project Charter, the Pillars Exercise, ADRs, BRD, FDD, User Stories, the Foundational Baseline Management packs, the subsidiary plans, then the Project Management Plan. The Stakeholder Register is a prerequisite to the Project Charter, and it is sufficient as long as it names the Sponsor and the Project Manager, the people who sign the Charter; the Charter exists to formally designate the authority assigned to the Project Manager to operate and bring the project to completion, so without those two named there is no reason to draft it (Sponsor, 2026-11-11). A small start on the Stakeholder Engagement Plan is based on the same register, and is not a prerequisite to the Charter. Once the Phase 3 Charter, ADRs, BRD, FDD and user stories are drafted, scope, schedule, resource and cost are revisited and rolled up as one package for the Sponsor to approve the Phase 3 work (GC-P2-06, GC-P2-07).

**Success Criteria:**
- Phase 2 spark and ideation documents generated
- PMP baseline updated
- Cumulative Lineage Kernel computed
- Phase 1 formally closed

---
