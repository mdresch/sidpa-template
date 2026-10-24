---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Closing"
pmbok_process: "4.7 Close Project or Phase & Strategic Cognitive Feedback"
pmp_baseline: "PMP-BL-v<X.Y.Z>"
refinement_id: "IR-PROP-v<X.Y.Z>"
lifecycle_stage: "Stage 18 (Intent Refinement)"
governance_policy: "approve-intent-refinement"
inputs:
  - "docs/project-docs/Project-Management-Plan.md"
  - "docs/project-docs/Adaptation-Plan.md"
  - "Actual Outcomes (Stage 12)"
  - "Audit-Register.md"
  - "Lessons Learned Register"
process: "Synthesize empirical outcomes and adaptations to refine top-of-chain intent and resolve hypotheses for subsequent project phases"
outputs:
  - "docs/project-docs/Intent-Refinement-Proposal.md"
  - "docs/project-docs/Spark-Capture.vNext.md"
---

# Intent Refinement Proposal — <Project Name>

> **PMBOK 8 Process:** `4.7 Close Project or Phase & Strategic Cognitive Feedback` (Closing)  
> **Governance Policy:** `approve-intent-refinement` | **Lifecycle Stage:** `Stage 18 (Intent Refinement)`  
> **Governing Baseline:** `PMP-BL-v<X.Y.Z>` | **Refinement ID:** `IR-PROP-v<X.Y.Z>`  
> **Inputs:** Project-Management-Plan.md, Adaptation-Plan.md, Actual Outcomes (Stage 12), Audit-Register.md, Lessons Learned  
> **Process:** Synthesize empirical outcomes and adaptations to refine top-of-chain intent and resolve hypotheses  
> **Outputs:** Intent-Refinement-Proposal.md (Catalyst for next Spark Capture)

---

## 1. Executive Evaluation Brief
<Concise summary of phase achievements, realized business value, and strategic variance against original intent.>

---

## 2. Outcome Delta Evaluation Matrix (Stage 12 vs. Stage 4)
| Objective / Expected Benefit (Stage 4) | Target Baseline Metric | Actual Realized Metric (Stage 12) | Delta / Variance | Causal Factor (Stage 11/15) | Strategic Directive (Stage 18) |
|---|---|---|---|---|---|
| *<Metric 1>* | *<Target>* | *<Observed>* | *<Variance>* | *<Root cause from audits/lessons>* | *<Maintain / Pivot / Retire>* |
| *<Metric 2>* | *<Target>* | *<Observed>* | *<Variance>* | *<Root cause from audits/lessons>* | *<Maintain / Pivot / Retire>* |

---

## 3. Hypothesis Adjudication Register (Stage 3 Terminal Adjudication)
| Hypothesis ID | Statement | Empirical Test Evidence (Stage 10/12) | Terminal Disposition | Strategic Impact / Graduation |
|---|---|---|---|---|
| `HYP-001` | *<Statement>* | *<Pytest / benchmark / telemetry log ref>* | `VALIDATED` / `REFUTED` / `REFINED` | *<Graduated to core principle / Retired / Reformulated as HYP-001.1>* |
| `HYP-002` | *<Statement>* | *<Pytest / benchmark / telemetry log ref>* | `VALIDATED` / `REFUTED` / `REFINED` | *<Graduated to core principle / Retired / Reformulated as HYP-002.1>* |

---

## 4. Strategic Pivots & Lessons Learned Synthesis
- **Refined Problem Statement:** <How has our understanding of the core problem evolved through real execution?>
- **Updated Strategic Motivation:** <What new priorities, boundary conditions, or goals supersede the original spark/ideation?>
- **Retired Premises:** <What assumptions or capabilities are formally decommissioned based on negative evidence?>

---

## 5. Phase N+1 Spark Directives (Generational Handoff)
- **Primary Catalyst for Phase N+1:** <What specific opportunity or gap initiates the next turn of the 18-stage wheel?>
- **Targeted Capabilities:** <What new capabilities or modules should the subsequent Project Charter authorize?>
- **Parent Refinement Linkage:** `parent_refinement: "IR-PROP-v<X.Y.Z>"` (ensures cross-generational traceability).

---

## 6. Governance Authorization
This Intent Refinement Proposal must be formally evaluated and approved via `approve-intent-refinement` (`FULL` Bayesian authority, `requires_human_approval: true`). Upon approval, this proposal closes the current phase baseline and initializes `Spark-Capture.vNext.md`.
