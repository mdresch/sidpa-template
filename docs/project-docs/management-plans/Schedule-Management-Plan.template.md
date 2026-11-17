---
plan_id: "schedule-management"
plan_name: "Schedule Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Schedule"
secondary_pmbok_domains:
  - "Governance"
legacy_process: "6.1 Plan Schedule Management"
route: "full_plan"
generator: "human"
version: "0.1.0"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
owner_role: "Project Manager"
depends_on: 
  - "scope-management"
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/management-plans/Scope-Management-Plan.md"
outputs:
  - "docs/project-docs/management-plans/Schedule-Management-Plan.md"
governance_policy: "approve-subsidiary-plan"
---

<!--
Plan Tier 1 (Baseline-Substantiating). Delete this comment block when the plan is written.
Route: full_plan | pmp_section | not_applicable. The route must match the tailoring matrix. For a pmp_section, move the file to docs/project-docs/.staging/pmp-sections/, set governance_policy to "approve-pmp" and keep the three headings.
Word count (body below the frontmatter, excluding code blocks and HTML comments): pmp_section 180 to 750 words, full_plan 700 to 4500 words. Outside the range raises a governance flag, not a block.
Out-of-scope items: list at least 2 for a pmp_section or 4 for a full_plan distinct items, or write `None: <rationale of at least 10 words>`. A placeholder-only item (TBD, TBC, FIXME, N/A) does not count.
`not_applicable` raises `FLAG: OMISSION_OF_BASE_PLAN`.
Unexpanded template tokens (TBD or TODO written in square brackets) and generator: stub or mock block approval. Use <angle-bracket> prompts while drafting and replace every one before approval.
Keep the three headings below exactly as written. Other headings go under them as subsections.
-->

# Schedule Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter and Scope traceability: map the horizon and milestones to Charter objectives and Scope epics. <write here>
- Planning horizon: what is scheduled in detail, and what is held at milestone level only. <write here>
- Out-of-scope scheduling boundaries (for example date commitments beyond the detailed horizon). <write here>

## 2. Domain Mechanics & Standards

- Milestone register: each milestone names parent epic(s), an objectively verifiable exit condition and a target window. <write here>
- Timebox and sequencing model: timebox length and cadence, predecessor relationships between epics, and the sequence that fixes the earliest completion. <write here>
- Duration estimation basis: method, unit, whether estimates are ranges, and the confidence rule beyond the detailed horizon. <write here>
- Schedule baseline: the approved milestone register and timebox plan at the approval date. <write here>
- Buffers: where schedule contingency is held and who may consume it. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Project Manager owns schedule baseline compliance. <write here>
- Variance tolerance (defaults; a stricter Charter tolerance takes precedence): a non-critical-path slip of at most 2 working days is at PM discretion. A larger slip, any critical-path slip, or a changed exit condition goes through integrated change control. <write here>
- Review cadence: each timebox boundary and phase close. <write here>
- Downstream invalidation: an approved change marks Cost, Resource and Risk `STALE_DEPENDENCY`; Procurement follows through Cost. <write here>
