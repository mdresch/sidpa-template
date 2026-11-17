---
name: pmbok-planning
description: How to draft the nine PMBOK 8 subsidiary management plans from their skeletons, approve them through the per-plan gate, and synthesize the integrated Project Management Plan, using the ADR-012 content contract and the ADR-013 approval sequence.
---

# Skill: pmbok-planning (SIDPA template)

This template no longer ships a plan-generation engine. The earlier SQLite, FastAPI and `orchestrate_pmbok.py` tooling was removed, following the decision in `agent-learning` ADR-034 to retire it in favor of a small pure-Python module. Until that module exists in your project, plans are drafted by a person or an LLM working from the skeletons in `docs/project-docs/management-plans/`. The standards, gates and registers below do not depend on a generator.

## The sequence (draft, approve, formalize)

1. **Draft** each plan from its `*.template.md` skeleton (`scripts/init_project.py` copies them to `.md`). Order follows the dependency graph in each plan's `depends_on`: Scope first, then Schedule, then Cost, then the plans that depend on them.
2. **Approve** each plan routed `full_plan` through `approve-subsidiary-plan` (one policy, parameterized by `plan_id`, human approval permanent). A plan routed `pmp_section` is drafted under `docs/project-docs/.staging/pmp-sections/` and is not approved separately.
3. **Formalize** the integrated `Project-Management-Plan.md` only when every `full_plan` is approved and not stale, every `pmp_section` is present and not a stub, and every `not_applicable` plan has an approved tailoring rationale. Then run `approve-pmp`.

## The content contract (every plan)

- **Frontmatter** with the keys in the skeleton: `plan_id`, `plan_name`, `pmbok_edition`, `pmbok_focus_area`, `primary_pmbok_domain`, `secondary_pmbok_domains`, `legacy_process`, `route`, `generator`, `version`, `baseline_id`, `cycle_id`, `owner_role`, `depends_on`, `inputs`, `outputs`, `governance_policy`. Flat keys, quoted strings, string lists only. Domains come from the closed set Governance, Scope, Schedule, Finance, Stakeholders, Resources, Risk.
- **Three literal headings:** `## 1. Intent, Alignment & Boundaries`, `## 2. Domain Mechanics & Standards`, `## 3. Governance, Control & Decision Rights`. Plan-specific content goes in subsections under them. Renaming a top-level heading raises a structural flag.
- **Out-of-scope list** in section 1. If nothing is excluded, write `None: <rationale of at least 10 words>`. A placeholder-only item (TBD, TBC, FIXME, N/A) does not count.
- **Floors and caps** are word-count flags, not blocks. Count words in the body below the frontmatter with the regex `\b[^\W_]+(?:['’][^\W_]+)?\b`, excluding code blocks and HTML comments. Contractions count as one word and hyphenated terms as two.
- **Plan tiers:** Tier 1 (Scope, Schedule, Cost) cannot be `not_applicable` without a recorded rationale and sponsor confirmation. Tier 2 (Risk, Quality) and Tier 3 (Resource, Stakeholder Engagement, Communications, Procurement) may be, with an approved tailoring rationale.

## What blocks and what only flags

- **Blocks approval (technical integrity):** `generator: stub` or `mock`, unexpanded template tokens (TBD or TODO in square brackets), a missing file, or frontmatter that cannot be parsed.
- **Flags, resolved by a recorded human rationale:** word count below the floor or above the cap, a missing or thin out-of-scope list, a missing required subsection, metadata that does not match the tailoring matrix or the Cycle Register.

## Baselines, cycles and staleness

- Every approved PMP gets a baseline identifier `PMP-BL-vX.Y.Z`. Plans, ADRs, BRDs, FDDs and stories carry `baseline_id` and `cycle_id`.
- A **cycle** (`CYC-NNN`, recorded in `docs/registers/Cycle-Register.md`) is one pass through the loop. A baseline is the approved result of a cycle, not the cycle itself.
- Changing a plan marks every plan that depends on it, directly or through another plan, as stale until it is re-verified. Changing a leaf plan invalidates nothing else.
- Hashes for approvals are computed over the file content with `cycle_id` and `baseline_id` excluded, and are stored in episode metadata and the Cycle Register, never inside the file.

## Adaptation and rollback

When an approved Stage 17 `Adaptation-Plan.md` names plans to revise, open a new cycle in the Cycle Register, revise only the named plans, re-approve them and anything stale, then run `approve-pmp`. To roll back, restore the prior baseline from `docs/project-docs/management-plans/history/<baseline_id>/` and record the cycle as `ROLLED_BACK`.
