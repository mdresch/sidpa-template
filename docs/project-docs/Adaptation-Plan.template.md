---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Monitoring & Controlling / Adaptive Closing"
pmbok_process: "4.6 Perform Integrated Change Control & Tailoring"
lifecycle_stage: "Stage 17 (Adaptation)"
governance_policy: "approve-adaptation-plan"
inputs:
  - "Stage 16 Governance Amendments (ADR Diffs)"
  - "Audit-Register.md findings"
process: "Operationalize governance changes into behavioral/skill updates and tailor management plan updates"
outputs:
  - "Adaptation-Plan.md"
  - "Updated Project Management Plan"
---

# Adaptation Plan

> **PMBOK 8 Process:** `4.6 Perform Integrated Change Control & Tailoring` (Monitoring & Controlling / Adaptive Closing)  
> **Governance Policy:** `approve-adaptation-plan` | **Lifecycle Stage:** `Stage 17 (Adaptation)`  
> **Inputs:** Stage 16 Governance Amendments (ADR Diffs), Audit-Register.md findings  
> **Process:** Operationalize governance changes into behavioral/skill updates and tailor management plan updates  
> **Outputs:** Adaptation-Plan.md, Updated Project Management Plan


**Source:** [Governance Change Log / ADR Diff]
**Governance Policy:** `approve-adaptation-plan`

## Triggering Governance Change
<Reference the specific validated ADR/BRD amendment, supersession, or policy update from Stage 16 that necessitates behavioral or process adaptation.>

## Scope of Behavioral / Tooling Adaptation
- **Workflow / Process Adjustments:** <What steps in the engineering, review, or operational workflow are modified?>
- **Agent Skill / Tooling Updates:** <What agent skills, hooks, or system prompts require revision to enforce the updated governance?>
- **Environmental / Configuration Changes:** <Any CI/CD, linter, or sandbox environment modifications.>

## Tailored Subsidiary Management Plan Updates (Feeding back to PMP)
Identify which subsidiary management plans require updates as a direct result of this adaptation:
- [ ] **Scope Management Plan:** <Updates to scope boundaries or change control>
- [ ] **Requirements Management Plan:** <Updates to requirement validation criteria or traceability>
- [ ] **Risk Management Plan:** <New risks, altered severity, or revised mitigation strategies>
- [ ] **Quality Management Plan:** <New contract test requirements or verification checks>
- [ ] **Resource Management Plan:** <Updated agent skill definitions, prompts, or authority limits>
- [ ] **Communications Management Plan:** <Modified reporting, audit, or notification rules>
- [ ] **Schedule / Cost Plans:** <Adjusted timeline or resource allocation>

*Any checked plan triggers an update to `Project-Management-Plan.md`, which cascades into refined ADRs, BRDs, FDDs, and User Stories for the subsequent development cycle.*

## Verification & Rollout Gates
<Measurable criteria confirming the adaptation is successfully operating in practice without causing regressions.>

## What this is not yet
This is Stage 17 (Adaptation). It executes the operational and behavioral changes required by an already-approved Stage 16 Governance Change. Do not redefine core strategic intent here -- that belongs in Stage 18 Intent Refinement.
