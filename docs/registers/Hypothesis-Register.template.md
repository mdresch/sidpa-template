---
register: "hypothesis-register"
pmbok_edition: "PMBOK 8"
lifecycle_stage: "Stage 2 (Hypothesis)"
governance_policy: "classify-hypothesis-status"
inputs:
  - "Spark-Capture.md"
  - "Ideation-Document.md"
process: "Track falsifiable design assumptions and empirical status updates"
outputs:
  - "Hypothesis-Register.md"
---

# Hypothesis Register — <project name>

> **Lifecycle Stage:** `Stage 2 (Hypothesis)`  
> **Governance Policy:** `classify-hypothesis-status` (shared `agent-learning-governance` policy shape)  
> **Inputs:** [Spark-Capture.md](../project-docs/Spark-Capture.md), [Ideation-Document.md](../project-docs/Ideation-Document.md)  
> **Purpose:** Hypothesis tracking continues here on its own cadence after Stage 1 (`approve-ideation`) closes, so reclassifying a hypothesis does not require reopening Ideation.

## How to use this register

One row or subsection per `HYP-<project>-NNN`. Append **Update** lines with dates; never rewrite the original statement. Run `classify-hypothesis-status` when a test outcome is real enough to classify — do not set status by feel.

| ID | Type | Statement | Falsification criteria | Status |
|---|---|---|---|---|
| **HYP-<project>-001** | <ValueHypothesis \| TechnicalHypothesis \| …> | <falsifiable statement> | <what evidence would invalidate it> | Formulated |

## Amendment log

| Date | Author | Change |
|---|---|---|
| <date the project starts> | <name> | Initial register opened from Ideation. |