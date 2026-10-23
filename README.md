# SIDPA Template

A reusable scaffold for the governance-and-build methodology developed across `agent-learning`, `ADPA`, and `SocialEngage`: Spark → Ideation → Business Case → Benefits Statement → Charter → subsidiary plans → ADR → BRD → FDD → Story → `implement-story` → `heal-contract-failure`, gated at the right points by real `agent_learning` TaskPolicies.

**This repo contains no project-specific content.** It is a shape, not a case study. Every policy in it is real and initialized but genuinely idle — zero episodes, baseline logits at 0.0 — because it would be a real mistake (caught once already, see `docs/root-cause-log.md`) to pre-fabricate evidence just to make the template look more complete than it honestly is.

## What's here

- **`docs/sequence-and-lessons.md`** — the real, hard-won ordering rules, each cited against the real project that surfaced it. Read this first.
- **`docs/chain-coverage.md`** — honest mapping of the full Intent-to-Outcome chain: what this template pre-declares, what it deliberately doesn't, and why.
- **`docs/root-cause-log.md`** — why each of the six pre-declared policies actually got built, and the one real place the source projects *didn't* converge (`approve-user-stories` vs. `approve-story`). This is the template's own living lessons-learned mechanism — it grows when a project using this template discovers it needs a policy neither source project had, not on a schedule.
- **`docs/policy-shapes/`** — the raw action-set JSON for all six pre-declared policies, plus the one documented-but-not-initialized alternate shape.
- **`docs/07-architecture/ADR-TEMPLATE.md`**, **`docs/project-docs/Business-Requirements/BRD-TEMPLATE.md`**, **`.../Functional-Design/FDD-TEMPLATE.md`**, **`docs/user-stories/EPIC-TEMPLATE.md`** — document shells matching the real, proven structure, each with inline notes on the mistakes already made once so a new project doesn't repeat them.
- **`docs/project-docs/*.template.md`** — Spark Capture through Project Charter, same treatment.
- **`.claude/skills/implement-story/SKILL.md`**, **`.claude/skills/heal-contract-failure/SKILL.md`** — the real build/healing loop, generalized from two independently-converged implementations, with an explicit "confirm first" section naming what turned out to be project-specific rather than universal.
- **`data/agent-learning/store/`** — the six real, idle policies themselves, ready to copy into a new project's own store.
- **`docs/registers/Story-Execution-Register.template.md`**, **`.../Audit-Register.template.md`** — the two real central registers, genuinely empty (no pre-loaded findings), each naming why no TaskPolicy governs it yet and what real trigger would justify building one.

## Using this for a new project

1. Copy the document templates and skills into the new project; rename placeholders.
2. Copy `data/agent-learning/store/active-policies/` and `.../policies/` into the new project's own store — then **rename the `template-governance` agent_id** to match that project's real convention (e.g. `<project>-governance`). Leave `agent-learning-governance`/`classify-hypothesis-status` as-is; that namespace is shared on purpose.
3. Follow `docs/sequence-and-lessons.md`'s ordering. Don't skip `validate-intent-foundation` between document-approval and `implement-story`.
4. When a real case needs a policy this template doesn't have, build it the same evidence-first way every policy here was built — then add the trigger that justified it to `docs/root-cause-log.md`, here in the template, not just in the new project's own docs. That's how this stays a living template instead of a frozen snapshot.

## What this deliberately does not do

It does not cover the chain's true open ends (Adaptation → Intent Refinement, uncovered everywhere; Observation → Lesson Learned, a cross-project concern belonging to a shared knowledge base, not rebuilt here). See `docs/chain-coverage.md` for the honest accounting. Building a shape for either of those without a real first case would repeat the exact mistake this template exists to avoid.
