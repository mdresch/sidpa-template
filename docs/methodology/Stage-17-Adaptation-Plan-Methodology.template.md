---
artifact_type: "methodology_guide"
stage: "17"
stage_name: "Adaptation Plan"
pmbok_process: "4.6 Perform Integrated Change Control (Tailoring)"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "approve-adaptation-plan (FULL authority)"
---

# Stage 17: Adaptation Plan — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Validated Stage 16 change & outcomes. Process: Tailor PMP via impact matrix. Output: Impacted plan list.

> **Purpose:** This document provides a comprehensive methodology for Stage 17 (Adaptation Plan) of the Intent-to-Outcome chain. Stage 17 operationalizes governance changes from Stage 16 into executable skills, workflows, and tailored project management plan updates.

> **Alignment:** PMBOK 8 Process 4.6 Perform Integrated Change Control (Tailoring)

> **Authority:** FULL authority via `approve-adaptation-plan` policy (3 actions: approve, reject, request revision)

> **Authority in the project:** the policy's gate computes a recommendation; the decision of record is the Project Sponsor's, given in words and registered with `task-policy-adjudicate` and `task-episode-register`. An agent drafts the plan and runs the steps; it never adjudicates, registers an approval, or edits a generated plan by hand. There is no separate technical-review or project-manager sign-off beyond the Sponsor (the Charter names one decision-maker).

> **One adaptation per phase.** A phase runs Stage 16 and Stage 17 once, at its close (Sponsor, 2026-11-10: "close Phase 2 once instead of multiple times"). Stage 17 therefore carries everything Stage 16 approved plus what it deferred; a standalone package for one change is kept as an input, not run on its own.

---

## 1. Stage 17 Overview

### 1.1 Purpose and Position in the Chain

Stage 17 is the **operationalization gate** that transforms approved governance changes into actionable adaptations. It sits at the boundary between **Monitoring & Controlling** (Stage 16) and **Closing / Strategic Feedback** (Stage 18).

```
Stage 16 (Governance Change)
    \u2193
Stage 17 (Adaptation Plan) \u0014 Operationalize
    \u2193
Stage 18 (Intent Refinement) \u0014 Strategic Feedback
```

**Key Responsibility:** Take validated governance changes and make them operational through skills updates, workflow modifications, and tailored PMP updates.

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| Approved Governance Changes | Stage 16 output | Yes |
| Baseline Revision Packages (BRPs) | Stage 16 output | If applicable |
| Subsidiary Plan Amendments (SPAs) | Stage 16 output | If applicable |
| Current Skills | `.claude/skills/` | Yes |
| Current Workflows | `.claude/skills/` | Yes |
| Current PMP | Project-Management-Plan.md | Yes |
| Governance Episodes | `docs/policy-shapes/episodes/` and the governance store (`data/agent-learning/store/`) | Yes |
| Stage 16 assessment | `docs/project-docs/Status-Reports/Stage-16-Governance-Change-*.md`, approved | Yes |
| Change requests and their decisions | `docs/governance/change-requests/` | Yes |
| Earlier change packages kept as inputs | `docs/project-docs/Adaptation-Plans/` | If any |
| Registers | Lessons Learned and Continuous Improvement, for the dispositions Stage 16 set | Yes |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| Updated Skills | `.claude/skills/` | No (but version controlled) |
| Updated Workflows | `.claude/skills/` | No (but version controlled) |
| Tailored PMP | Project-Management-Plan.md | Yes (via approve-adaptation-plan) |
| Adaptation Plan Document | `docs/project-docs/Adaptation-Plans/ADP-YYYYMMDD-NNN-<title>.md` (the integrated `docs/project-docs/Adaptation-Plan.md` is produced by the planning tooling after approval) | Yes |
| Updated Governance Episodes | `docs/policy-shapes/episodes/` | Yes |

### 1.4 Success Criteria

Stage 17 is complete when:
- [ ] All Stage 16 governance changes are operationalized
- [ ] All skills and workflows are updated
- [ ] All PMP tailoring is complete
- [ ] Adaptation Plan document is approved via `approve-adaptation-plan`
- [ ] All changes are committed and pushed
- [ ] Project-Status-Register.md is updated

---

## 2. Adaptation Plan Process (8-Step)

### Step 1: Input Validation

**Purpose:** Ensure all required inputs from Stage 16 are available and valid.

**Actions:**
1. Verify Stage 16 assessment is complete and marked COMPLETED
2. Confirm all BRPs and SPAs are prepared and approved
3. Verify current skills and workflows are accessible
4. Confirm current PMP baseline is accessible
5. Verify governance episodes from Stage 16 are recorded

**Checklist:**
- [ ] Stage 16 assessment exists and is marked COMPLETED
- [ ] All BRPs have required approvals (or are in review)
- [ ] All SPAs have required approvals (or are in review)
- [ ] Current skills directory exists and is valid
- [ ] Current PMP is accessible and valid
- [ ] All Stage 16 episodes are recorded

**Validation Commands** (the Stage 16 assessment is marked `APPROVED` in its frontmatter status; Stage 16 writes no per-lesson episode files named `classify-diff-type-LL-*.json`):
```bash
# Stage 16 assessment approved
grep -n "^status:" docs/project-docs/Status-Reports/Stage-16-Governance-Change-*.md

# Change requests exist and record their decisions
ls docs/governance/change-requests/ && grep -n "Decision status\|Project Sponsor |" docs/governance/change-requests/CR-*.md

# Skills and the PMP
ls .claude/skills/ && head -30 docs/project-docs/Project-Management-Plan.md | grep "PMP-BL-v"

# The store the approval will be registered in (LL-040): print it, count its files
echo "${AGENT_LEARNING_LOCAL_STORE_DIR:-./data/agent-learning/store}"
```
Open items that Stage 16 deferred (for example F3 and F4) are carried as deferrals in the plan; they are not silently dropped.

---

### Step 2: Change Inventory

**Purpose:** Create a complete inventory of all governance changes that need to be operationalized.

**Inventory Template:**
```markdown
## Governance Change Inventory

### From Stage 16 Assessment: [REP-GC-...]

| Change ID | Source | Type | Status | Priority | Owner |
|---|---|---|---|---|---|
| GC-001 | LL-043 | Structural | BRP Approved | High | [Name] |
| GC-002 | LL-046 | Process | SPA Approved | High | [Name] |
| GC-003 | LL-044 | Process | Direct | Medium | [Name] |
| GC-004 | LL-045 | Process | Direct | Medium | [Name] |

### Detailed Changes

#### GC-001: [Change Name]
- **Source:** LL-043
- **Type:** Structural/Architectural
- **BRP:** BRP-20261106-001
- **Description:** [Detailed description]
- **Affected Components:** [List]
- **Operationalization Requirements:** [List]
- **Success Criteria:** [List]
```


---

### Step 3: Impact Mapping

**Purpose:** Map each governance change to the specific skills, workflows, and PMP sections that need to be updated.

**Impact Mapping Template:**
```yaml
change_id: GC-001
source: LL-043
change_type: structural
affected_skills:
  - .claude/skills/implement-story/SKILL.md
  - .claude/skills/governance/SKILL.md
affected_workflows:
  - workflows/stage-18.yml
affected_pmp_sections:
  - Scope Management Plan
  - Schedule Management Plan
  - Quality Management Plan
operationalization_steps:
  - Step 1: [description]
  - Step 2: [description]
success_criteria:
  - Criterion 1: [description]
  - Criterion 2: [description]
validation_methods:
  - Test 1: [description]
  - Test 2: [description]
```

**Current Impact Mapping:**

#### GC-001: Stage 18 Tooling Migration (from LL-043)
```yaml
change_id: GC-001
source: LL-043
change_type: structural
affected_skills:
  - .claude/skills/implement-story/SKILL.md
  - .claude/skills/governance/SKILL.md
affected_workflows:
  - .claude/skills/stage-18/SKILL.md (new)
affected_pmp_sections:
  - Project-Management-Plan.md (baseline update)
  - Scope-Management-Plan.md
  - Schedule-Management-Plan.md
  - Quality-Management-Plan.md
operationalization_steps:
  - Update implement-story to reference new tooling location
  - Create new stage-18 skill for intent refinement
  - Update governance skill to handle new module structure
  - Update PMP baseline to PMP-BL-v1.0.1
success_criteria:
  - All Stage 18 functionality works in new location
  - All tests pass
  - CI pipeline includes new tests
validation_methods:
  - Run Stage 18 tooling in new location
  - Verify CI passes with new tests
  - Validate governance episodes are created correctly
```

#### GC-002: Evidence Management Synchronization (from LL-046)
```yaml
change_id: GC-002
source: LL-046
change_type: process
affected_skills:
  - .claude/skills/governance/SKILL.md
affected_workflows:
  - N/A
associated_scripts:
  - scripts/governance/sync_episodes.py
  - scripts/governance/validate_episodes.py
  - scripts/governance/backfill_episodes.py
affected_pmp_sections:
  - Governance-Management-Plan.md
operationalization_steps:
  - Update governance skill to write episodes to repository first
  - Create sync script to copy episodes to external store
  - Create validation script to check for discrepancies
  - Create backfill script for missing episodes
  - Update Governance-Management-Plan.md with new policies
success_criteria:
  - All governance decisions recorded in repository
  - All repository episodes synchronized to external store
  - No discrepancies between sources
  - All upstream gates have episodes
validation_methods:
  - Run validation script
  - Verify all episodes exist in both locations
  - Check for missing episodes
```

#### GC-003: External Evidence Dependency (from LL-044)
```yaml
change_id: GC-003
source: LL-044
change_type: process
affected_skills:
  - .claude/skills/implement-story/SKILL.md
affected_documentation:
  - sidpa-template/testing/data-dependencies.md
operationalization_steps:
  - Add data dependency check to implement-story Step 0
  - Create guidance document for hypothesis validation
  - Update testing template with data dependency section
success_criteria:
  - All hypotheses have documented data dependencies
  - Test environment has mock data for validation
  - No hypotheses blocked by missing data
validation_methods:
  - Check hypothesis tracking for data dependencies
  - Verify mock data exists for all test scenarios
```

#### GC-004: Single Source of Truth for Story Status (from LL-045)
```yaml
change_id: GC-004
source: LL-045
change_type: process
affected_skills:
  - .claude/skills/implement-story/SKILL.md
affected_scripts:
  - scripts/phase_rollup.py
  - scripts/update_story_status.py (new)
affected_documentation:
  - sidpa-template/governance/story-status-management.md
operationalization_steps:
  - Automate story status updates in implementation-log.md
  - Derive epic file status from implementation-log.md
  - Add validation to detect and flag drift
  - Update phase_rollup.py to enforce single source
  - Create automation script for status synchronization
success_criteria:
  - Story status maintained in single canonical location
  - All other representations derived from canonical source
  - No drift between epic files and implementation-log.md
validation_methods:
  - Run phase_rollup.py with --check
  - Verify no status-drift rows
  - Check that all status updates are automated
```

---

### Step 4: Skill and Workflow Updates

**Purpose:** Update the actual skills and workflows to implement the governance changes.

**Update Process:**

#### For Each Skill Update:

1. **Create feature branch**
   ```bash
   git checkout -b feature/adaptation-[change-id]
   ```

2. **Identify specific changes**
   - Review the impact mapping for the change
   - Identify exact lines/sections to modify
   - Document current state

3. **Implement changes**
   - Make minimal, focused changes
   - Follow existing patterns and conventions
   - Add comments explaining changes (if necessary)

4. **Update tests**
   - Update existing tests for modified behavior
   - Add new tests for new functionality
   - Ensure all tests pass

5. **Document changes**
   - Update skill documentation
   - Add change log entry
   - Update cross-references

**Skill Update Template:**
```markdown
## Skill Update: [Skill Name]

**Change ID:** GC-XXX
**Source:** LL-XXX
**Date:** YYYY-MM-DD
**Author:** [Name]

### Changes Made

1. **Section [X]** - [Description of change]
   - **Before:** [old code/text]
   - **After:** [new code/text]
   - **Rationale:** [why this change was made]

2. **Section [Y]** - [Description of change]
   - **Before:** [old code/text]
   - **After:** [new code/text]
   - **Rationale:** [why this change was made]

### Tests Updated

- [ ] test_1.py - Updated to test new behavior
- [ ] test_2.py - Added new test for feature X

### Validation

- [ ] All existing tests pass
- [ ] All new tests pass
- [ ] Manual testing completed
- [ ] Code review completed
```

**Current Skill Updates Required:**

1. **implement-story/SKILL.md**
   - Add data dependency check (GC-003)
   - Automate story status updates (GC-004)

2. **governance/SKILL.md**
   - Update to write episodes to repository first (GC-002)
   - Add evidence sync check (GC-002)

3. **New: stage-18/SKILL.md**
   - Create new skill for intent refinement (GC-001)

---

### Step 5: PMP Tailoring

**Purpose:** Update the Project Management Plan and subsidiary plans to reflect the operationalized changes.

**Generated plans are regenerated, never hand-edited.** The PMP and the nine subsidiary plans come from `(project phase-close / seed tooling — not shipped in sidpa-template)` (`--mode adapt --adaptation-plan <plan>`) and the `pmbok-planning` skill. A standard that must hold in every run goes in the template, then the plans are regenerated. Hand-authored approved documents named by the plan (the Charter, Business Case, Benefits Management Plan, Ideation Document) change through their own approved amendment, accepted by the Sponsor, and are listed in the plan with that route. **Baseline versioning** follows ADR-008 §4.6.1 and ADR-037: an execution adaptation is a minor increment (`PMP-BL-v1.1.0` to `PMP-BL-v1.2.0`); the numbers in the example below are from Phase 1.

**PMP Update Process:**

1. **Update baseline version**
   - From: PMP-BL-v1.0.0
   - To: PMP-BL-v1.0.1 (for BRP-20261106-001)
   - Or: PMP-BL-v1.1.0 (if major changes)

2. **Update affected subsidiary plans**
   - Scope-Management-Plan.md
   - Schedule-Management-Plan.md
   - Quality-Management-Plan.md
   - Governance-Management-Plan.md

3. **Document changes**
   - Add change log entry
   - Update version history
   - Update cross-references

**PMP Tailoring Template:**
```markdown
## PMP Tailoring: [Change ID]

**BRP/SPA:** [Document ID]
**From Version:** PMP-BL-vX.Y.Z
**To Version:** PMP-BL-vA.B.C
**Date:** YYYY-MM-DD
**Author:** [Name]

### Changes to Project-Management-Plan.md

| Section | Change | Rationale |
|---|---|---|
| Baseline Version | Updated from vX.Y.Z to vA.B.C | Reflects approved changes |
| Scope | [Description] | [Rationale] |
| Schedule | [Description] | [Rationale] |

### Changes to Subsidiary Plans

#### Scope-Management-Plan.md
- [Change 1 description]
- [Change 2 description]

#### Schedule-Management-Plan.md
- [Change 1 description]
- [Change 2 description]

### Validation

- [ ] All cross-references updated
- [ ] All version numbers consistent
- [ ] All changes approved
```

**Current PMP Tailoring:**

1. **From BRP-20261106-001:**
   - Update baseline from PMP-BL-v1.0.0 to PMP-BL-v1.0.1
   - Update Scope-Management-Plan.md with new work packages
   - Update Schedule-Management-Plan.md with migration timeline
   - Update Quality-Management-Plan.md with test coverage requirements

2. **From SPA-20261106-001:**
   - Update Governance-Management-Plan.md with new policies
   - Add evidence management procedures
   - Add synchronization requirements

---

### Step 6: Adaptation Plan Document

**Purpose:** Create the formal Adaptation Plan document that consolidates all changes and serves as the input for approval.

**Adaptation Plan Template:**
```markdown
# (Extended template omitted — port detail from agent-learning when instantiating.)
```

---

### Step 7: Validation

**Purpose:** Validate that all changes are correctly implemented and working as expected.

**Validation Checklist:**

#### Skill Validation
- [ ] All skill updates are committed
- [ ] All skill tests pass
- [ ] All skill changes are documented
- [ ] All cross-references are valid

#### Workflow Validation
- [ ] All workflow updates are committed
- [ ] All workflow tests pass
- [ ] All workflow changes are documented

#### PMP Validation
- [ ] All PMP updates are committed
- [ ] All version numbers are consistent
- [ ] All cross-references are valid
- [ ] All changes are approved

#### Integration Validation
- [ ] All skills work together correctly
- [ ] All workflows execute properly
- [ ] All PMP changes are reflected in operations

**Validation Commands** (the scripts `validate_pmp.py`, `validate_links.py` and `validate_episodes.py` do not exist in this repository):
```bash
uv run pytest                                  # the whole suite, no --ignore
uv run pytest tests/test_governance_baseline.py tests/test_stage16_amend.py tests/test_lessons_learned.py
# plan consistency: the plan-lint and plan-approval-gate skills, run by the planning tooling
python (project phase-close / seed tooling — not shipped in sidpa-template) --mode adapt --adaptation-plan <plan>   # only after approval
```
Run the suite with `AGENT_LEARNING_LOCAL_STORE_DIR` pointing at a temporary directory until IMP-063 lands: the suite writes fixture episodes into the configured store.

---

### Step 8: Approval and Completion

**Purpose:** Submit the Adaptation Plan for approval and complete Stage 17.

**Approval Process:**

1. **Merge the plan as a draft.** The plan document is committed with `status: draft`. Implementation work it lists is done in separate PRs, each merged through `scripts/pr_gate.py` after every required workflow has concluded (LL-060) and the whole suite has passed.
2. **Decision.** The Sponsor reads the plan. Run `task-policy-decide` for `approve-adaptation-plan`, show the gate's recommendation, and wait. On the Sponsor's explicit words run `task-policy-adjudicate` and `task-episode-register`, after printing the store path and its file count before and after (LL-040).
3. **Record.** Put the decision, its date and the episode id in the plan and in the Project-Status-Register. A gate that was missed is not approved afterwards; record the gap and run the gate going forward.
4. **Finalize.** Regenerate the PMP and plans with the tooling, commit, and mark Stage 17 COMPLETED only when the work the plan authorizes is merged.

**Completion Checklist:**
- [ ] All skill and workflow updates are committed
- [ ] All PMP updates are committed
- [ ] Adaptation Plan document is approved
- [ ] All validation tests pass
- [ ] Project-Status-Register.md is updated
- [ ] All artifacts are pushed to repository

---

---

## 5. Common Pitfalls and Mitigations

###1 Pitfalls

| Pitfall | Description | Mitigation |
|---|---|---|
| Incomplete inventory | Missing some governance changes | Use Stage 16 assessment as source of truth |
| Incorrect impact mapping | Wrong skills/workflows identified | Review with technical lead, trace all dependencies |
| Breaking changes | Skill updates break existing functionality | Run all tests, validate before and after |
| Inconsistent PMP | Version numbers or references don't match | Use PMP validation script, manual review |
| Missing documentation | Changes not documented | Use templates, require documentation for all changes |
| Scope creep | Adding unrelated changes | Stick to governance changes from Stage 16 |
| Validation gaps | Not all scenarios tested | Use comprehensive test suite, manual testing |

###2 Mitigation Strategies

1. **Use Templates:** Always use the provided templates for consistency
2. **Follow Checklists:** Complete all checklist items before submitting
3. **Automate Validation:** Run validation scripts before submission
4. **Peer Review:** Have another team member review changes
5. **Incremental Updates:** Make small, focused changes
6. **Document Everything:** Document all changes, no matter how small
7. **Test Thoroughly:** Run all tests, including edge cases
8. **Trace to Source:** Always link changes to specific governance changes

---

## 6. References

###1 Internal References

- [Intent-to-Outcome Chain Coverage](../chain-coverage.md)
- [Project Status Register](../Project-Status-Register.md)
- [Stage 16 Governance Change Assessment](../Status-Reports/Stage-16-Governance-Change-Assessment.md)
- [Stage 16 Methodology](../Methodology/Stage-16-Governance-Change-Methodology.md)
- [Stage 18 Methodology](Stage-18-Intent-Refinement-Methodology.md) (to be created)

###2 External References

- PMBOK 8: Project Management Body of Knowledge, 8th Edition
- PMI: Project Management Institute standards
- ISO 21500: Guidance on Project Management

###3 Related Methodologies

- [Stage 15 Methodology](../Methodology/Stage-15-Lesson-Learned-Methodology.md)
- [Stage 16 Methodology](../Methodology/Stage-16-Governance-Change-Methodology.md)

---
