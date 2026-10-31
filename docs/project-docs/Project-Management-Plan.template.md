---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Planning"
pmbok_process: "4.2 Develop Project Management Plan"
pmp_baseline: "PMP-BL-v1.0.0"
lifecycle_stage: "Stage 6 (Project)"
governance_policy: "approve-pmp"
inputs:
  - "Project-Charter.md"
  - "Subsidiary management plans (Scope, Risk, Quality, etc.)"
process: "Integrate subsidiary management plans, establish baselines, define governance gates"
outputs:
  - "Project-Management-Plan.md"
---

# Project Management Plan (PMP)

> **PMBOK 8 Process:** `4.2 Develop Project Management Plan` (Planning)  
> **Governance Policy:** `approve-pmp` | **Lifecycle Stage:** `Stage 6 (Project)`  
> **Baseline Identifier:** `PMP-BL-v1.0.0`  
> **Inputs:** Project-Charter.md, Subsidiary management plans (Scope, Risk, Quality, etc.)  
> **Process:** Integrate subsidiary management plans, establish baselines, define governance gates  
> **Outputs:** Project-Management-Plan.md


**Source:** [Project-Charter.md](Project-Charter.md)
**Governance Policy:** `approve-pmp`

**This is the integrated Project Management Plan, formalized after the Project Charter is approved and before technical specifications (ADR, BRD, FDD, User Stories) are drafted.**

## 1. Executive Summary & Baselines
- **Scope Baseline:** Pending; summarize the approved scope boundary and Charter trace after its plan gate.
- **Schedule Baseline / Progressive Elaboration:** Pending; establish milestones and evidence-based durations after the Scope baseline is approved.
- **Cost Baseline / Progressive Elaboration:** Pending; establish authorized funding after required scope, schedule, resource, and procurement inputs are approved.
- **Baseline ID:** `PMP-BL-v1.0.0` (Invariant 6)

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
- **Scope Management Plan:** How requirements and scope changes are evaluated and controlled.
- **Requirements Management Plan:** Traceability chain from Charter to ADR/BRD/FDD/Stories.
- **Risk Management Plan:** Risk register, probability/impact scoring, and mitigation protocols.
- **Quality Management Plan:** Contract-test criteria, zero-drift verification, and regression prevention rules.
- **Resource Management Plan:** Roles, responsibilities, and agent authority tiers.
- **Communications Management Plan:** Project transparency, PR reviews, and audit log cadence.
- **Stakeholder Engagement Plan:** Human approval gates and escalation pathways.

The four baseline rows above are integrated through their approved parent plans. Foundation manifests remain the detailed artifact registers; the PMP records the approved plan-level baseline and its approval evidence.

## 3. Feedback Loop from Adaptation
When an **Adaptation Plan** (Stage 17) is approved, this PMP and its subsidiary plans are updated with tailored operational changes, which in turn trigger refined ADRs, BRDs, FDDs, and Stories for the next cycle.

## What this is not yet
This document integrates governance and operational plans. It does NOT contain code architecture or solution logic—those belong in ADRs, BRDs, and FDDs, which are drafted only after this PMP is approved.
