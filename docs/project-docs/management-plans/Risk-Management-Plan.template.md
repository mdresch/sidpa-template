---
plan_id: "risk-management"
plan_name: "Risk Management Plan"
pmbok_edition: "PMBOK 8"
pmbok_focus_area: "Planning"
primary_pmbok_domain: "Risk"
secondary_pmbok_domains:
  - "Governance"
  - "Finance"
legacy_process: "11.1 Plan Risk Management"
route: "full_plan"
generator: "human"
version: "0.1.0"
baseline_id: "<target-baseline-id>"
cycle_id: "CYC-001"
owner_role: "Risk Lead"
depends_on: 
  - "scope-management"
  - "schedule-management"
  - "cost-management"
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/management-plans/Scope-Management-Plan.md"
  - "docs/project-docs/management-plans/Schedule-Management-Plan.md"
  - "docs/project-docs/management-plans/Cost-Management-Plan.md"
outputs:
  - "docs/project-docs/management-plans/Risk-Management-Plan.md"
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

# Risk Management Plan — <project name>

## 1. Intent, Alignment & Boundaries

- Charter and baseline traceability: which Scope, Schedule and Cost elements are in the assessed exposure. <write here>
- Risk appetite per objective area (scope, schedule, cost, quality, governance integrity). <write here>
- Out-of-scope risk boundaries (categories not managed here). <write here>

## 2. Domain Mechanics & Standards

- Risk taxonomy: the categories used to classify risks. <write here>
- Probability-impact scale: defined bands per objective area and the rule that combines them into a rating. Ratings must be reproducible from the scale. <write here>
- Risk register contract: location and minimum fields (identifier, description, category, probability, impact, rating, owner, response, status, trigger). <write here>
- Response strategies: avoid, mitigate, transfer, accept or escalate, and when each applies. <write here>
- Contingency link to the Cost plan and buffers in the Schedule plan. <write here>

## 3. Governance, Control & Decision Rights

- Accountability: the Risk Lead owns the register. Risk owners are roles from the Stakeholder Register. <write here>
- Escalation thresholds: a risk at or above the high band, or threatening a baseline tolerance, goes to the Sponsor. Accepting it is a recorded decision. <write here>
- Review cadence: each timebox boundary and when an upstream baseline changes. <write here>
