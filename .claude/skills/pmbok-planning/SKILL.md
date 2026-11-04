---
name: pmbok-planning
description: Orchestrates PMBOK 8 subsidiary management plans, architectural pillars, and synthesizes the integrated Project Management Plan (PMP) with agent-learning decision validation gates.
---

# PMBOK Planning Skill

This skill orchestrates the generation, synthesis, architectural framing, and adaptation of PMBOK 8 subsidiary management plans and the overarching Project Management Plan (PMP) for projects initialized from `sidpa-template`.

---

## Supported Workflows

### 1. The Post-Charter Pillars Exercise & Architecture Sequence
After `Project-Charter.md` is approved by `approve-charter`:
1. Execute the **Pillars Exercise** ([`docs/07-architecture/PILLARS-TEMPLATE.md`](../../docs/07-architecture/PILLARS-TEMPLATE.md)) to identify 4–6 foundational project pillars.
2. Draft foundational high-level ADRs covering **100% of identified pillars** (no pillar left unaddressed).
3. Draft the **BRD** citing the ADRs.
4. Draft the **FDD** citing the BRD.
5. Decompose the FDD into concrete **User Stories** (Work Packages) with BDD acceptance criteria.

### 2. Full Planning & Subsidiary Plan Orchestration

**Foundation Pack tailoring — a project-size decision, not a universal requirement.** Before drafting any subsidiary plan, decide whether it actually needs a Foundation Pack (`docs/project-docs/management-plans/<domain>-baseline/foundation/` — e.g. `Schedule-Basis-of-Estimates.md`, `Schedule-Network-Phase1.md`, each gated through its own Stage 6.B sequence) populated as a pre-commit step first. Only drop into that granular tier when the subsidiary plan document itself cannot hold the level of detail the project genuinely needs — e.g. a complex multi-team schedule that needs a real CPM network and basis-of-estimates before the plan's own prose can be written responsibly, not drafted around. A small project can rely on the subsidiary plan (or even the integrated PMP alone) to carry every required answer directly, with **no Foundation Pack at all** — do not populate one "for completeness" when the plan's own prose already answers everything required of it. (Known gap: `scripts/orchestrate_pmbok.py` currently generates a "Foundation Baseline Roll-up" section referencing a pending Foundation Pack for every subsidiary plan regardless of whether one is actually warranted — if a project skips the Foundation Pack tier for a plan, that generated section needs manual removal, not left as a dangling "Pending" reference.)

Once User Stories (Work Packages) exist, they provide the real duration data, story points, and resource commitments needed to synthesize the Schedule (6.1), Cost (7.1), Scope (5.1), and Resource (9.1) plans into the integrated `Project-Management-Plan.md`:

```powershell
python scripts/orchestrate_pmbok.py --mode full --charter docs/project-docs/Project-Charter.md
```

*(Add `--mock` for offline / stub execution without external LLM keys).*

### 3. Closed-Loop Adaptation Regeneration
Executed when an `Adaptation-Plan.md` (Stage 17) evaluates governance amendments via the **Governance Change Impact Matrix** and identifies specific subsidiary plans requiring revision after a Stage 16 Governance Change.

```powershell
python scripts/orchestrate_pmbok.py --mode adapt --adaptation-plan docs/project-docs/Adaptation-Plan.md
```

This scans the checklist in `Adaptation-Plan.md`:
- `[x] Scope Management Plan` $\rightarrow$ regenerates `5.1`
- `[x] Schedule Management Plan` $\rightarrow$ regenerates `6.1`
- `[x] Cost Management Plan` $\rightarrow$ regenerates `7.1`
- `[x] Quality Management Plan` $\rightarrow$ regenerates `8.1`
- `[x] Resource Management Plan` $\rightarrow$ regenerates `9.1`
- `[x] Communications Management Plan` $\rightarrow$ regenerates `10.1`
- `[x] Risk Management Plan` $\rightarrow$ regenerates `11.1`
- `[x] Procurement Management Plan` $\rightarrow$ regenerates `12.1`
- `[x] Stakeholder Engagement Plan` $\rightarrow$ regenerates `13.2`

It regenerates only the checked plans, updates `docs/project-docs/management-plans/`, archives prior baselines to `management-plans/history/{baseline_id}/`, and re-synthesizes `docs/project-docs/Project-Management-Plan.md`.

### 4. Decision Validation Gate Verification
After synthesis, the integrated PMP must be validated via `approve-pmp`:

```powershell
agent-learn task-policy-decide --agent-id <project-name>-governance --task-id approve-pmp
```

### 5. PMP Baseline Versioning & Traceability Invariant (Invariant 6)
Every approved PMP receives an immutable SemVer identifier (`PMP-BL-v1.0.0`, `PMP-BL-v1.1.0`). All downstream technical requirements (ADRs, BRDs, FDDs, Stories) must reference the active baseline:
```yaml
---
pmp_baseline: "PMP-BL-v1.0.0"
---
```

### 6. Deterministic Rollback Protocol (Invariant 7)
If downstream execution triggers regressions, atomic rollback restores the prior approved baseline from archive and penalizes the escalation bandit:
```powershell
python scripts/orchestrate_pmbok.py --mode rollback --to-baseline PMP-BL-v1.0.0
```

### 7. Phase Next Evolutionary Seeding (Stage 18 -> Stage 1)

**Planning-round size is a hybrid agile/waterfall tailoring decision, scaled to uncertainty — not a fixed batch size.** Don't try to fix every problem in one go, especially the genuinely unknown, high-uncertainty ones. Well-understood, already-evidenced work can be safely batch-planned further ahead; genuinely novel, unevidenced work should not be pre-committed into the same upfront batch as its well-understood neighbors. If a phase's own batch turns out to contain an epic like that, an already-approved Epic can simply be marked `Deferred` to the next phase (the Epic itself stays `Approved` — only its execution window moves) rather than forcing it to execute before its own unknowns are ready to be tackled; close the current phase around its remaining, lower-uncertainty scope instead.

When Stage 18 Intent Refinement completes with a disposition of `phase_handoff` and receives full Bayesian governance approval (`approve-intent-refinement`), run the orchestrator in `seed-next` mode to mechanically scaffold Phase $N+1$:

```powershell
python scripts/orchestrate_pmbok.py --mode seed-next --refinement-proposal docs/project-docs/Intent-Refinement-Proposal.md
```

### 8. Administrative Decommissioning (Stage 18 Project Termination)
If Stage 18 outcome evaluation concludes that the project's strategic intent is fully realized or non-viable (`disposition_type: project_termination`), run the orchestrator in `decommission` mode:

```powershell
python scripts/orchestrate_pmbok.py --mode decommission --refinement-proposal docs/project-docs/Intent-Refinement-Proposal.md
```
