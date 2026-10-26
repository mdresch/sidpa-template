---
plan_id: "scope-management"
plan_name: "Scope Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Scope"
secondary_pmbok_domains:
  - "Governance"
legacy_process: "5.1 Plan Scope Management"
route: "full_plan"
generator: "human"
version: "0.1.0"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
owner_role: "Project Manager"
depends_on: []
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/Ideation-Document.md"
  - "docs/project-docs/Business-Case.md"
outputs:
  - "docs/project-docs/management-plans/Scope-Management-Plan.md"
governance_policy: "approve-subsidiary-plan"
---

<!--
Plan Tier 1 (Baseline-Substantiating). Delete this comment block when the plan is written.
Route: full_plan | pmp_section | not_applicable. The route must match the tailoring matrix. For a pmp_section, move the file to docs/project-docs/.staging/pmp-sections/, set governance_policy to "approve-pmp" and keep the three headings.
Word count (body below the frontmatter, excluding code blocks and HTML comments): pmp_section 180 to 750 words, full_plan 700 to 4500 words. Outside the range raises a governance flag, not a block.
Out-of-scope items: list at least 2 for a pmp_section or 4 for a full_plan distinct items, or write `None: <rationale of at least 10 words>`. A placeholder-only item (TBD, TBC, FIXME, N/A) does not count.
`not_applicable` raises `FLAG: OMISSION_OF_BASE_PLAN` and needs a recorded rationale and sponsor confirmation.
Unexpanded template tokens (TBD or TODO written in square brackets) and generator: stub or mock block approval. Use <angle-bracket> prompts while drafting and replace every one before approval.
Keep the three headings below exactly as written. Other headings go under them as subsections.
-->

# Scope Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter traceability: map the scope to the Charter's objectives, high-level requirements and success metrics. <write here>
- In-scope boundary: itemize major features, architectural deliverables, code modules and test suites authorized. <write here>
- Out-of-scope boundary: itemize what is strictly excluded from this phase. <write here>

## 2. Domain Mechanics & Standards

- WBS hierarchy: Project Phase > Epic > User Story > Work Package or Commit. <write here>
- WBS dictionary (required for `full_plan`): each deliverable names acceptance criteria, owner role and parent epic. <write here>
- Scope baseline: the approved scope statement, the WBS and story mapping, and the acceptance criteria in the user stories. <write here>
- Requirements traceability (required for `full_plan`): business goals to functional specifications to tests. <write here>
- Deliverable acceptance: a Definition of Done that is testable or objectively verifiable. A qualitative criterion needs a named validation method. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Project Manager is accountable for scope baseline compliance. <write here>
- Variance tolerance: unplanned additions of at most 1 story point, or localized refactoring that affects no public interface, approved deliverable, architectural decision or acceptance criterion, are at PM discretion. Anything larger goes through integrated change control. <write here>
- Downstream invalidation: an approved Scope baseline change marks Schedule, Cost and every plan that depends on Scope as `STALE_DEPENDENCY`. <write here>
