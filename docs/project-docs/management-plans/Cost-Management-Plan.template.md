---
plan_id: "cost-management"
plan_name: "Cost Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Finance"
secondary_pmbok_domains:
  - "Governance"
legacy_process: "7.1 Plan Cost Management"
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
  - "docs/project-docs/management-plans/Cost-Management-Plan.md"
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

# Cost Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter, Scope and Schedule traceability for the envelope and funding stages. <write here>
- Management envelope: total ceiling, unit (currency or a defined effort unit) and approving authority. <write here>
- Out-of-scope cost boundaries (for example costs borne by another budget). <write here>

## 2. Domain Mechanics & Standards

- Cost categories: each category with an owner and a measurement source (people effort, compute, external model or API usage, tooling and licences as applicable). <write here>
- Estimating basis per category and its accuracy range. <write here>
- Staged funding: funding released per milestone or phase with the release condition. <write here>
- Contingency and management reserve held separately, with release authority. Contingency references identified risks. <write here>
- Cost baseline: the approved staged budget at the approval date, excluding management reserve. <write here>
- Burn-rate control: how actual spend is compared with plan, and the reporting interval. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Project Manager owns cost baseline compliance. Envelope increases need the Sponsor. <write here>
- Variance tolerance (defaults; a stricter Charter tolerance takes precedence): stage variance within +/-10% and inside contingency is at PM discretion. Beyond that, any envelope change, or any reserve release goes through integrated change control. <write here>
- Downstream invalidation: an approved change marks Risk and Procurement `STALE_DEPENDENCY`. <write here>
