---
plan_id: "procurement-management"
plan_name: "Procurement Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Finance"
secondary_pmbok_domains:
  - "Resources"
  - "Governance"
legacy_process: "12.1 Plan Procurement Management"
route: "full_plan"
generator: "human"
version: "0.1.0"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
owner_role: "Project Manager"
depends_on: 
  - "scope-management"
  - "cost-management"
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/management-plans/Scope-Management-Plan.md"
  - "docs/project-docs/management-plans/Cost-Management-Plan.md"
outputs:
  - "docs/project-docs/management-plans/Procurement-Management-Plan.md"
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

# Procurement Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter, Scope and Cost traceability for planned acquisitions. <write here>
- Acquisition classes: open-source libraries, hosted services, tooling licences, contracted work as applicable. <write here>
- Out-of-scope procurement boundaries. <write here>

## 2. Domain Mechanics & Standards

- Make-or-buy criteria: capability fit, total cost, maintenance burden, lock-in, data exposure, and how they are weighed. <write here>
- Dependency intake rule: a new third-party runtime dependency or external service needs a recorded justification covering the need, alternatives (including doing without), licence, maintenance status and exit path. <write here>
- Supplier selection criteria and evidence. <write here>
- Contract and licence checks before adoption: licence compatibility, usage limits, data handling and retention, change-of-terms rights. <write here>
- Supplier performance monitoring and exit conditions. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Project Manager owns the plan. Acquisitions above the threshold declared here need Sponsor authorization. <write here>
- An acquisition that changes the Cost envelope or a stage budget goes through integrated change control. <write here>
- Review cadence: each acquisition decision and phase close. <write here>
