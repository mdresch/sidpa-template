---
name: intent-refinement
description: Stage 18 Intent Refinement for a SIDPA project: phase-close readiness, hypothesis adjudication, damped strategic change, and hand-off to the next cycle. Process guidance only; the earlier Python module was removed with the legacy tooling.
---

# Skill: intent-refinement (SIDPA template)

This skill describes Stage 18 as a process. The earlier code (`pmbok.models.intent_refinement`) was removed with the legacy tooling. If your project needs the readiness check, hypothesis adjudication or damping filter as code, build them as small pure functions with contract tests through `implement-story`, using the rules below as the contract.

## Readiness before Stage 18 can proceed

- Every Stage 9 deliverable is accepted.
- No Stage 11 audit record has an unresolved non-conformance.
- Stage 15 lessons learned are recorded for the phase (an entry, or a no-new-lessons sign-off).

## The gate

`approve-intent-refinement` runs under full authority with permanent human approval. The Intent Refinement Proposal records the disposition (`phase_handoff` or `project_termination`), the evidence, and the baseline it refines.

## Hypotheses

- Every Stage 3 hypothesis ends in a terminal state before Stage 18 closes: validated (graduates into an architectural invariant), refuted (archived), or collapsed.
- Adjudicate with Bayes factors where evidence supports it: a factor of 10 or more validates, 0.1 or less refutes.
- A hypothesis may be refined for at most two generations. On the third, an inconclusive hypothesis collapses to refuted because its budget is spent. A generation is not a cycle: the generation counter and the `CYC-NNN` counter are separate.

## Damping and capacity

- Smooth rolling outcome deltas before they drive a strategic change, so one noisy period does not cause whiplash. A bias-corrected exponential moving average with a smoothing factor between 0.6 and 0.85 is the starting point.
- Rate-limit strategic pivots against what the operation can absorb. After a major charter revision, require at least one complete delivery and audit cycle under the new baseline before the next refinement proposal.

## Hand-off

- `phase_handoff`: seed the next phase's Spark and Ideation from the approved directives, open a new cycle in the Cycle Register, and increment the baseline.
- `project_termination`: prune ephemeral worktrees, revoke temporary credentials, release test runners, and close the open cycle.
- Record refinement proposals, frames, evaluations and sign-offs as episode metadata. Add no new store record type.
