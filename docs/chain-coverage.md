# Intent-to-Outcome Chain — Full Document Validation and TaskPolicy Coverage

Source of the 18-stage chain concept: SocialEngage's `Intent-to-Outcome-Chain-and-TaskPolicy-Coverage.md` (Obsidian Brain wiki) and the SIDPA Project Management Lifecycle.

In enterprise software engineering and agentic governance (PMBOK 8 / SIDPA), every stage that yields a documented artifact requires a formal Bayesian validation gate. We start with a **Spark** and systematically trace intent through execution, verification, governance amendment, behavioral adaptation, and back to refined intent—closing the cognitive development lifecycle loop.

All document-approval policies operate under `DecisionAuthority.FULL` using multi-criteria Bayesian evaluation (`DecisionFrame`), with human adjudication mandated (`requires_human_approval: true`).

---

## 1. Complete 18-Stage Chain Coverage

| # | Chain Stage | Governed Document Artifact | Assigned TaskPolicy | Authority & Decision Shape | Lifecycle Role |
|---|---|---|---|---|---|
| 1 | **Intent** | `Spark-Capture.md`<br>`Ideation-Document.md` | `template-governance` / **`approve-ideation`** | `FULL`<br>(3 actions: approve, reject, request revision) | **Starts with a Spark.** Validates strategic motivation, grounded problem formulation, and initial scope before resources are committed. |
| 2 | **Objective** | `Project-Charter.md` | `template-governance` / **`approve-charter`** | `FULL`<br>(3 actions: approve, reject, request revision) | Validates project charter, sponsor authority, measurable objectives traced to benefits, and realistic scope boundaries without forcing premature subsidiary plans. |
| 3 | **Hypothesis** | `Ideation-Document.md`<br>(Hypothesis section / `HYP-*.md`) | `agent-learning-governance` / **`classify-hypothesis-status`** | `FULL`<br>(7 actions: advance to testing, mark validated, mark invalidated, etc.) | Evaluates falsifiable design assumptions and classifies status based on accumulated empirical test evidence. |
| 4 | **Benefit** | `Business-Case.md`<br>`Benefits-Statement.md` | `template-governance` / **`approve-business-case`** | `FULL`<br>(3 actions: approve, reject, request revision) | Validates business economics, ROI assumptions, risk assessments, and benefit-to-hypothesis linkage before authorizing project execution. |
| 5 | **Capability** | Capability Matrix / Catalog | *Automated Synthesis* | Deterministic mapping | Evaluates organizational and technical capabilities enabled by project deliverables (crystallized via synthesis scripts). |
| 6 | **Project** | Project Workspace & Structure | *Platform / Repo Setup* | Structural boundary | Establishes the bounded workspace, tooling configuration, and development environment (SIDPA template instance). |
| 7 | **Requirement** | Architecture & Specifications:<br>• `ADR-*.md`<br>• `BRD-*.md`<br>• `FDD-*.md`<br>• `user-stories/*.md` | `template-governance` /<br>• **`approve-adr`**<br>• **`approve-brd`**<br>• **`approve-fdd`**<br>• **`approve-user-stories`** | `FULL`<br>(3 actions each: approve, reject, request revision) | Independently validates each specification subtype against specialized architectural, business, functional, and user-story criteria. |
| 8 | **Work Package** | Epic / Sprint Backlog Entry | `template-governance` / **`validate-intent-foundation`** | `FULL`<br>(3 actions: accept, reject, flag) | Gates entry into the implementation pipeline, confirming the artifact foundation (ADR/BRD/FDD/Story) is sufficiently grounded. |
| 9 | **Deliverable** | Source Code & Release Artifacts | `implement-story` & `heal-contract-failure` | Direct Execution & Review | Implements stories against executable contracts and heals failures test-first. |
| 10 | **Verification Evidence** | Contract Tests & Execution Logs | Executable Test Suite | Input Evidence | Automated contract tests (`pytest`) provide empirical ground truth and feed into audit and approval gates. |
| 11 | **Audit Record** | `Audit-Register.md`<br>`Audit-Finding.md` | `template-governance` / **`approve-audit-record`** | `FULL`<br>(3 actions: approve, reject, request revision) | Formally validates audit findings, non-conformances, and architectural drift before logging to the official Audit Register. |
| 12 | **Actual Outcome** | Post-Delivery Impact Assessment | *Empirical Observation* | Baseline Comparison | Measures realized production outcomes against expected Benefits and Hypotheses. |
| 13 | **Observation** | Telemetry, Environment Gotchas | Knowledge Base Captures | Raw Input | Uninterpreted findings recorded from runtime telemetry and developer environments. |
| 14 | **Insight** | Synthesized Technical Findings | `obsidian-brain-ingestor` / **`resolve-kb-conflict`** | `FULL`<br>(trust existing, supersede, flag) | Decides whether new findings support, contradict, or supersede existing knowledge nodes. |
| 15 | **Lesson Learned** | Formalized Organizational Knowledge | `obsidian-brain-ingestor` / **`resolve-kb-conflict`** | `FULL`<br>(trust existing, supersede, flag) | Crystallizes actionable organizational learnings from verified insights. |
| 16 | **Governance Change** | Governance Amendments & Diffs | `template-governance` /<br>• **`classify-diff-type`**<br>• **`escalate-diff-response`** | Paired Pipeline:<br>• `FULL` (7 diff classes)<br>• `LOW` (3 escalation actions) | Automated governance change pipeline (ADR-007): paired diff classification and escalation bandit with ADR-005 progression comparison and ADR-006 evidence transport. |
| 17 | **Adaptation** | `Adaptation-Plan.md` | `template-governance` / **`approve-adaptation-plan`** | `FULL`<br>(3 actions: approve, reject, request revision) | Validates that governance amendments are operationalized into concrete behavioral adjustments, agent skills, and workflow rules. |
| 18 | **Intent Refinement** | `Intent-Refinement-Proposal.md` | `template-governance` / **`approve-intent-refinement`** | `FULL`<br>(3 actions: approve, reject, request revision) | Synthesizes adaptation results and empirical outcomes to update top-of-chain intent—closing the cognitive loop back to Stage 1. |

---

## 2. Document-Validation Action Shape Invariant

All document validation TaskPolicies in this template enforce the standard 3-action approval pattern:

1. `approve_<document>` — The document meets all quality, consistency, and governance criteria; approve to proceed to the next lifecycle stage.
2. `reject_<document>` — The document contains fundamental flaws, ungrounded assumptions, or unresolvable contradictions; reject outright.
3. `request_revision_before_decision` — The document requires specific clarifications, boundary refinements, or additional evidence before a final verdict can be reached.

### Authority and Human-in-the-Loop Safeguards
- Every document approval policy runs strictly on **`DecisionAuthority.FULL`** with Bayesian multi-criteria evaluation (`DecisionResolver`).
- **`requires_human_approval: true`** is permanently set across all approval policies. Automated agents recommend decisions with posterior confidence and margin, but human project leaders hold the final approval authority.

---

## 3. Directory Layout in This Template

```
sidpa-template/
├── docs/
│   ├── chain-coverage.md                         # This comprehensive coverage matrix
│   ├── project-docs/
│   │   ├── Spark-Capture.template.md              # Stage 1: Intent
│   │   ├── Ideation-Document.template.md          # Stage 1: Intent & Stage 3: Hypotheses
│   │   ├── Project-Charter.template.md            # Stage 2: Objective
│   │   ├── Business-Case.template.md              # Stage 4: Benefit
│   │   ├── Benefits-Statement.template.md         # Stage 4: Benefit
│   │   ├── Adaptation-Plan.template.md            # Stage 17: Adaptation
│   │   ├── Intent-Refinement-Proposal.template.md # Stage 18: Intent Refinement
│   │   ├── Business-Requirements/
│   │   │   └── BRD-TEMPLATE.md                    # Stage 7: Requirement
│   │   └── Functional-Design/
│   │       └── FDD-TEMPLATE.md                    # Stage 7: Requirement
│   ├── 07-architecture/
│   │   └── ADR-TEMPLATE.md                        # Stage 7: Requirement
│   ├── user-stories/
│   │   └── EPIC-TEMPLATE.md                       # Stage 7: Requirement
│   ├── registers/
│   │   ├── Audit-Register.template.md             # Stage 11: Audit Record
│   │   └── Story-Execution-Register.template.md   # Stage 9: Deliverable Tracking
│   └── policy-shapes/                             # Canonical JSON action shape specifications
│       ├── approve-ideation.actions.json
│       ├── approve-charter.actions.json
│       ├── classify-hypothesis-status.actions.json
│       ├── approve-business-case.actions.json
│       ├── approve-adr.actions.json
│       ├── approve-brd.actions.json
│       ├── approve-fdd.actions.json
│       ├── approve-user-stories.actions.json
│       ├── validate-intent-foundation.actions.json
│       ├── approve-audit-record.actions.json
│       ├── classify-diff-type.actions.json
│       ├── escalate-diff-response.actions.json
│       ├── approve-adaptation-plan.actions.json
│       └── approve-intent-refinement.actions.json
└── data/agent-learning/store/                     # Pre-declared policies and active pointers
    ├── active-policies/template-governance/
    └── policies/template-governance/
```
