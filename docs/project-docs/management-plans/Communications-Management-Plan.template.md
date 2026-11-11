---
plan_id: "communications-management"
plan_name: "Communications Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Stakeholders"
secondary_pmbok_domains:
  - "Governance"
legacy_process: "10.1 Plan Communications Management"
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
  - "docs/project-docs/management-plans/Communications-Management-Plan.md"
governance_policy: "approve-subsidiary-plan"
---

<!--
Plan Tier 3 (Execution Support). Delete this comment block when the plan is written.
Route: full_plan | pmp_section | not_applicable. The route must match the tailoring matrix. For a pmp_section, move the file to docs/project-docs/.staging/pmp-sections/, set governance_policy to "approve-pmp" and keep the three headings.
Word count (body below the frontmatter, excluding code blocks and HTML comments): pmp_section 150 to 800 words, full_plan 600 to 5000 words. Outside the range raises a governance flag, not a block.
Out-of-scope items: list at least 1 for a pmp_section or 2 for a full_plan distinct items, or write `None: <rationale of at least 10 words>`. A placeholder-only item (TBD, TBC, FIXME, N/A) does not count.
Tier 3 plans may be `not_applicable` with an approved tailoring rationale.
Unexpanded template tokens (TBD or TODO written in square brackets) and generator: stub or mock block approval. Use <angle-bracket> prompts while drafting and replace every one before approval.
Keep the three headings below exactly as written. Other headings go under them as subsections.
-->

# Communications Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter and Scope traceability for reporting obligations and notices. <write here>
- Audience list by role, referencing the Stakeholder Register. <write here>
- Out-of-scope communication boundaries. <write here>

## 2. Domain Mechanics & Standards

- Communication matrix: for each flow the audience, information, purpose, channel, cadence or trigger and owner role. <write here>
- Decision recording rule: a decision communicated is recorded in the governance record (episode metadata or a version-controlled artifact). The channel message is a pointer, not the record. <write here>
- Status report format: progress against milestones, spend against the stage, top risks, decisions needed. <write here>
- Escalation path: sequence and time limits for an urgent issue. <write here>
- Confidentiality classes. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Project Manager owns the plan. Every flow has an owner role. <write here>
- Which messages need approval before release, and by whom. <write here>
- Review cadence: each phase boundary and when the Stakeholder Register changes materially. <write here>
