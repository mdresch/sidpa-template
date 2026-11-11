---
plan_id: "resource-management"
plan_name: "Resource Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Resources"
secondary_pmbok_domains:
  - "Governance"
legacy_process: "9.1 Plan Resource Management"
route: "full_plan"
generator: "human"
version: "0.1.0"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
owner_role: "Project Manager"
depends_on: 
  - "scope-management"
  - "schedule-management"
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/management-plans/Scope-Management-Plan.md"
  - "docs/project-docs/management-plans/Schedule-Management-Plan.md"
outputs:
  - "docs/project-docs/management-plans/Resource-Management-Plan.md"
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

# Resource Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter, Scope and Schedule traceability for resource needs. <write here>
- Resource classes: human roles, autonomous agents, tooling and environment assets. <write here>
- Out-of-scope resource boundaries. <write here>

## 2. Domain Mechanics & Standards

- Role catalogue: responsibilities, accountable owner and decision rights per role. <write here>
- Allocation and capacity per role per timebox, with the basis for the capacity figure. <write here>
- Agent work boundaries: work classes an agent may perform and the human role that stays accountable. No agent holds a decision reserved for a human. <write here>
- Tooling and environment assets with owner and acquisition lead time. <write here>
- Acquisition and release: how a resource is added or released and who approves it. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Project Manager owns the plan. Role owners come from the Stakeholder Register. <write here>
- Capacity conflicts: who decides between descoping and rescheduling. Both are integrated change control events. <write here>
- Review cadence: each timebox boundary. <write here>
