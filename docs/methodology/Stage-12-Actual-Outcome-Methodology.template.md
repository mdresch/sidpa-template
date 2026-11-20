---
artifact_type: "methodology_guide"
stage: "12"
stage_name: "Actual Outcome"
pmbok_process: "5.5 Validate Scope & Value Realization"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "none — empirical observation, baseline comparison against the Benefits Management Plan"
---

# Stage 12: Actual Outcome — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Telemetry & Benefits Statement. Process: Compare realized vs expected. Output: Impact deltas.

> **Purpose:** Compare the benefit this phase actually realized against what the Benefits Management Plan (Stage 4) said it would, honestly — including where it fell short — rather than treating delivery as automatically equal to value.

> **Alignment:** PMBOK 8 Process 5.5 Validate Scope & Value Realization.

> **Authority:** No TaskPolicy decides here. `docs/chain-coverage.md` §2 row 12 names this stage's lifecycle role as "Baseline Comparison" against production telemetry and the Benefits Statement — an empirical report, not a governed approval.

---

## 1. Overview

### 1.1 Position in the Chain

```
Stage 11 (Audit Record) — conformance evidence
    ↓
Stage 12 (Actual Outcome) — this stage
    ↓
Stage 13 (Observation) — raw telemetry this assessment draws on; Stage 4 (next phase) reads this stage's result as input
```

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| The Benefits Management Plan's stated targets | `docs/project-docs/Benefits-Management-Plan.md` | Yes |
| Production telemetry / realized metrics for the phase | Wherever the plan said it would be measured | Yes |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| Actual Outcome Assessment | `docs/project-docs/Status-Reports/Stage-12-Actual-Outcome-Assessment*.md` | No |
| Benefit Realization Review | `docs/project-docs/Status-Reports/Benefit-Realization-Review-Assessment.md` | No |

### 1.4 Success Criteria

Stage 12 is complete when:
- [ ] Every benefit the Benefits Management Plan named has a stated realized value (or an honest "not yet measurable, because...")
- [ ] The delta between expected and realized is stated plainly, not reframed as success
- [ ] The result is available for the next phase's Stage 4 to reconcile against before restating a target unchanged

---

## 2. Process

### Step 1: Pull the stated targets

From the current phase's Benefits Management Plan: what benefit, what metric, what measurement window.

### Step 2: Pull realized telemetry

Measure the actual value against that same metric and window. Where the window hasn't closed yet, say so explicitly rather than reporting an interim number as final.

### Step 3: State the delta honestly

Write the Actual Outcome Assessment: realized vs. expected, per benefit. A shortfall is reported as a shortfall — this feeds Stage 16 (Governance Change) if it implies a baseline problem, and the next phase's Stage 4 if it means a target needs revising.

### Step 4: Hand off

The next phase's Stage 3 (Benefit) reads this assessment before restating or revising its benefit targets (see Stage 3's own methodology, Step 2). Note: Stage 3/Benefit was renumbered from Stage 4 on 2026-11-12 — see [Intent-to-Outcome Chain Coverage](../chain-coverage.md) §0.

---


## 4. Validation

No dedicated validation script exists; the assessment is reviewed by checking it cites real metrics against the real Benefits Management Plan targets, not by running a command.

---

## 5. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| Treating "delivered" as automatically equal to "benefit realized" | Measure the actual stated metric, not just that the feature shipped |
| Reframing a shortfall as success | State the delta plainly; a shortfall is real information for Stage 4 and Stage 16 |
| Reporting an interim number as the final realized value | State explicitly when a measurement window hasn't closed |

---

## 6. References

- [Intent-to-Outcome Chain Coverage](../chain-coverage.md) — §2 row 12
- [Stage-12-Actual-Outcome-Assessment.md](../Status-Reports/Stage-12-Actual-Outcome-Assessment.md)
- [Stage-12-Actual-Outcome-Assessment-Phase2.md](../Status-Reports/Stage-12-Actual-Outcome-Assessment-Phase2.md)
- [Benefit-Realization-Review-Assessment.md](../Status-Reports/Benefit-Realization-Review-Assessment.md)
- [Stage 3: Benefit Methodology](Stage-03-Benefit-Methodology.template.md) — renamed 2026-11-12 (was Stage 4)
- [Stage 11: Audit Record Methodology](Stage-11-Audit-Record-Methodology.template.md)
- [Stage 13: Observation Methodology](Stage-13-Observation-Methodology.template.md)

---
