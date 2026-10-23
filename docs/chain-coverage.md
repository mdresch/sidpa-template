# Intent-to-Outcome Chain — what this template covers, honestly

Source of the 18-stage chain concept: SocialEngage's own `Intent-to-Outcome-Chain-and-TaskPolicy-Coverage.md` (Obsidian Brain wiki). This document restates only what's needed to scope this template — read the source directly for the full picture, including stages this template deliberately leaves out.

## Pre-declared in this template (real, converged shape; zero episodes; idle until a real case feeds it)

| Chain stage | Policy | Shape confirmed by |
|---|---|---|
| Hypothesis (Stage 3) | `classify-hypothesis-status` | Literally shared `agent_id`/`task_id` across two real codebases (`agent-learning-governance`) — the strongest convergence signal in this log |
| Requirement (ADR) (Stage 7) | `approve-adr` | Independently converged, ADPA + SocialEngage + agent-learning |
| Requirement (BRD) (Stage 7) | `approve-brd` | Independently converged, ADPA + SocialEngage + agent-learning |
| Requirement (FDD) (Stage 7) | `approve-fdd` | Independently converged, ADPA + SocialEngage + agent-learning |
| Requirement (Story) (Stage 7) | `approve-user-stories` | **Partially converged** — SocialEngage's own shape (`mark_ready`/`mark_blocked`) differs from ADPA's (`approve_user_stories`/`reject_user_stories`). Both included in `docs/policy-shapes/`; not resolved into one. See `root-cause-log.md`. |
| Requirement → Work Package (Stage 8) | `validate-intent-foundation` | Independently converged, ADPA + SocialEngage + agent-learning. Confirmed `full` authority only — a learned low-authority version hit a hard entropy ceiling on real data. |
| Governance Change (Stage 16) | `classify-diff-type` (FULL) & `escalate-diff-response` (LOW) | Independently converged, SocialEngage + agent-learning (ADR-007 / PR #2). Full-authority 7-action diff classifier across 3 operational tiers paired with low-authority 3-action escalation bandit, gated by ADR-005 progression comparison and ADR-006 evidence transport. |

## Explicitly not pre-declared — named as real, open gaps instead

| Chain stage | Status | Why not pre-declared |
|---|---|---|
| Intent, Objective, Benefit, Capability (Stages 1, 2, 4, 5) | No policy anywhere | SocialEngage's own assessment: Capability is correctly excluded (an automatically-crystallized artifact, not a planning decision); Benefit may not be separable from Hypothesis; Objective/Intent have no evidence yet distinguishing them as separate judgment calls. Don't build three policies to look thorough when the evidence doesn't support separating them. |
| Deliverable (code/output acceptance) (Stage 9) | No TaskPolicy, by design | Handled by `implement-story`/`heal-contract-failure` and human review directly — not every real decision needs to be a TaskPolicy. |
| Verification Evidence (Stage 10) | No TaskPolicy, by design | Read as *input* to other decisions (e.g., contract-test results feed `approve-adr`'s own evidence), not itself decided on. |
| Observation → Insight → Lesson Learned (Stages 13–15) | Partially covered, cross-project | SocialEngage's `resolve-kb-conflict` lives under a shared knowledge-base-ingestor agent, not a per-project one. If this project has access to a shared knowledge base, integrate; don't rebuild. |
| Adaptation → Intent Refinement (Stages 17–18) | **Uncovered everywhere** | Stage 16 is now mechanized and closed via paired diff classification/escalation. The final closing loop (Adaptation → Intent Refinement — how validated governance amendments adapt execution workflows and refine top-of-chain intent) remains the active frontier. |
| Audit Record (Stage 11) | No TaskPolicy anywhere (yet) — but the **register** to record findings in does exist (`docs/registers/Audit-Register.template.md`) | ADPA's own `classify-audit-finding` is a *different*, narrower thing — classifying one ADR-vs-code drift finding, not a formal Audit Record stage of this chain. A register to hold real findings in is zero-evidence to provide (it's just a place to write things down); a policy to classify them automatically is not — that's why one exists here and the other doesn't yet. |

## Project-specific policies, not pre-declared, pattern documented instead

`classify-audit-finding` and `validate-plan-dependency` (both real, both built for ADPA) are **not** in this template's pre-declared set — their decision shapes are specific to problems ADPA actually hit (a drifted ADR found via sample audit; a PM-plan dependency chain), not independently reconfirmed by a second real project. See `root-cause-log.md` for the pattern behind each, so a new project can recognize its own version of the same trigger rather than copy ADPA's specific shape uncritically.
