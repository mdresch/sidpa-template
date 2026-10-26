---
plan_id: "quality-management"
plan_name: "Quality Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Governance"
secondary_pmbok_domains:
  - "Scope"
legacy_process: "8.1 Plan Quality Management"
route: "full_plan"
generator: "human"
version: "0.1.0"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
owner_role: "Quality Assurance Lead"
depends_on: 
  - "scope-management"
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/management-plans/Scope-Management-Plan.md"
outputs:
  - "docs/project-docs/management-plans/Quality-Management-Plan.md"
governance_policy: "approve-subsidiary-plan"
---

<!--
Plan Tier 2 (Governance and Control). Delete this comment block when the plan is written.
Route: full_plan | pmp_section | not_applicable. The route must match the tailoring matrix. For a pmp_section, move the file to docs/project-docs/.staging/pmp-sections/, set governance_policy to "approve-pmp" and keep the three headings.
Word count (body below the frontmatter, excluding code blocks and HTML comments): pmp_section 160 to 800 words, full_plan 650 to 5000 words. Outside the range raises a governance flag, not a block.
Out-of-scope items: list at least 1 for a pmp_section or 2 for a full_plan distinct items, or write `None: <rationale of at least 10 words>`. A placeholder-only item (TBD, TBC, FIXME, N/A) does not count.
Tier 2 plans may be `not_applicable` with an approved tailoring rationale.
Unexpanded template tokens (TBD or TODO written in square brackets) and generator: stub or mock block approval. Use <angle-bracket> prompts while drafting and replace every one before approval.
Keep the three headings below exactly as written. Other headings go under them as subsections.
-->

# Quality Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter and Scope traceability: map quality objectives to the Scope acceptance criteria and Definition of Done. <write here>
- Quality objectives: measurable objectives appropriate to the project. <write here>
- Out-of-scope quality boundaries (verification activities not performed). <write here>

## 2. Domain Mechanics & Standards

- Quality gates: each gate names its lifecycle point, pass criteria, required evidence and gate owner. <write here>
- Verification criteria and coverage: required test or review types, what a coverage figure measures, and the minimum accepted value. <write here>
- Nonconformance handling: how a failed gate is recorded, triaged and returned to work. <write here>
- Quality metrics with collection source and the threshold that triggers action. <write here>
- Continuous improvement link: where recurring defects are recorded for lessons learned. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Quality Assurance Lead owns the plan and gate definitions. Deliverable acceptance authority stays as in the Scope plan. <write here>
- Waivers: a waived criterion needs a recorded rationale and the named waiver authority. Waivers are never silent. <write here>
- Review cadence: each gate and phase close. <write here>
