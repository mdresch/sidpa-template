---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Planning"
pmbok_process: "4.2 Develop Project Management Plan"
pmp_baseline: "PMP-BL-v1.0.0"
lifecycle_stage: "Stage 6 (Project)"
governance_policy: "approve-pmp"
inputs:
  - "Project-Charter.md"
  - "docs/project-docs/management-plans/*.md"
process: "Integrate subsidiary management plans, establish baselines, define governance gates"
outputs:
  - "Project-Management-Plan.md"
---

# Project Management Plan (PMP) — SIDPA Project

> **PMBOK 8 Process:** `4.2 Develop Project Management Plan` (Planning)  
> **Governance Policy:** `approve-pmp` | **Lifecycle Stage:** `Stage 6 (Project)`  
> **Baseline Identifier:** `PMP-BL-v1.0.0`  
> **Inputs:** Project-Charter.md, Subsidiary Management Plans  
> **Process:** Integrate subsidiary management plans, establish baselines, define governance gates  
> **Outputs:** Project-Management-Plan.md

## 1. Executive Summary & Baselines
- **Project Title:** SIDPA Project
- **Baseline ID:** `PMP-BL-v1.0.0`
- **Scope Baseline:** Pending; summarize the approved scope boundary and Charter trace after its plan gate.
- **Schedule Baseline / Progressive Elaboration:** Pending; establish milestones and evidence-based durations after the Scope baseline is approved.
- **Cost Baseline / Progressive Elaboration:** Pending; establish authorized funding after required scope, schedule, resource, and procurement inputs are approved.

### 1.1 Foundation Baseline Roll-up Register

This register is the PMP-level roll-up of the Scope, Schedule, Resource, and Cost foundation packs. Keep each row pending until its foundation artifacts, pack roll-up, and parent management plan have their required human approvals.

| Domain | Parent management plan | Foundation pack manifest | Baseline ID | Pack / plan status | Parent-plan approval reference |
|---|---|---|---|---|---|
| Scope | [Scope Management Plan](management-plans/Scope-Management-Plan.md) | [Scope Foundation Pack](management-plans/scope-baseline/Scope-Foundation-Pack-Manifest.md) | Pending | Pending | Pending |
| Schedule | [Schedule Management Plan](management-plans/Schedule-Management-Plan.md) | [Schedule Foundation Pack](management-plans/schedule-baseline/Schedule-Foundation-Pack-Manifest.md) | Pending | Pending | Pending |
| Resource | [Resource Management Plan](management-plans/Resource-Management-Plan.md) | [Resource Foundation Pack](management-plans/resource-baseline/Resource-Foundation-Pack-Manifest.md) | Pending | Pending | Pending |
| Cost | [Cost Management Plan](management-plans/Cost-Management-Plan.md) | [Cost Foundation Pack](management-plans/cost-baseline/Cost-Foundation-Pack-Manifest.md) | Pending | Pending | Pending |

For each approved row, record the baseline identifier, approved manifest/version and artifact-hash reference, parent-plan approval episode, and any accepted constraints. Pack generation or completion alone is not PMP approval evidence. Keep blocked or pending rows visible; do not infer approval.

## 2. Integrated Subsidiary Management Plans

### 2.5.1 Scope Management Plan
**Document Link:** [management-plans/Scope-Management-Plan.md](management-plans/Scope-Management-Plan.md)
- **Summary:** Formulated Scope Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.6.1 Schedule Management Plan
**Document Link:** [management-plans/Schedule-Management-Plan.md](management-plans/Schedule-Management-Plan.md)
- **Summary:** Formulated Schedule Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.7.1 Cost Management Plan
**Document Link:** [management-plans/Cost-Management-Plan.md](management-plans/Cost-Management-Plan.md)
- **Summary:** Formulated Cost Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.8.1 Quality Management Plan
**Document Link:** [management-plans/Quality-Management-Plan.md](management-plans/Quality-Management-Plan.md)
- **Summary:** Formulated Quality Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.9.1 Resource Management Plan
**Document Link:** [management-plans/Resource-Management-Plan.md](management-plans/Resource-Management-Plan.md)
- **Summary:** Formulated Resource Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.10.1 Communications Management Plan
**Document Link:** [management-plans/Communications-Management-Plan.md](management-plans/Communications-Management-Plan.md)
- **Summary:** Formulated Communications Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.11.1 Risk Management Plan
**Document Link:** [management-plans/Risk-Management-Plan.md](management-plans/Risk-Management-Plan.md)
- **Summary:** Formulated Risk Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.12.1 Procurement Management Plan
**Document Link:** [management-plans/Procurement-Management-Plan.md](management-plans/Procurement-Management-Plan.md)
- **Summary:** Formulated Procurement Management Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

### 2.13.2 Stakeholder Engagement Plan
**Document Link:** [management-plans/Stakeholder-Engagement-Plan.md](management-plans/Stakeholder-Engagement-Plan.md)
- **Summary:** Formulated Stakeholder Engagement Plan addressing Formalize PMBOK 8 planning baselines, Generate verified subsidiary management plans, Integrate into Project Management Plan (PMP)....

The four baseline rows in §1.1 roll up through their approved parent plans. Foundation manifests remain the detailed artifact registers; this PMP records the approved plan-level baseline and its approval evidence.

## 3. Feedback Loop from Adaptation
When an **Adaptation Plan** (Stage 17) is approved, this PMP and its subsidiary plans are updated with tailored operational changes evaluated through the Governance Change Impact Matrix, which in turn trigger refined ADRs, BRDs, FDDs, and Stories for the next cycle. Prior baselines are archived to `management-plans/history/{baseline_id}/`.

## 4. Governance Authorization
This integrated PMP must be formally evaluated and approved via `approve-pmp` (`FULL` Bayesian authority, `requires_human_approval: true`) before technical specifications (ADR, BRD, FDD, Stories) are finalized. All downstream technical requirements must record `pmp_baseline: 'PMP-BL-v1.0.0'` (Invariant 6). Prior baselines remain recoverable from history archives (Invariant 7).
