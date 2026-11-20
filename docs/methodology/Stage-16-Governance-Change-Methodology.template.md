---
artifact_type: "methodology_guide"
stage: "16"
stage_name: "Governance Change"
pmbok_process: "4.6 Perform Integrated Change Control"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "classify-diff-type (FULL), escalate-diff-response (LOW)"
---

# Stage 16: Governance Change — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Lessons & proposed diffs. Process: Classify & escalate. Output: Governed baseline update.

> **Purpose:** This document provides a comprehensive methodology for Stage 16 (Governance Change) of the Intent-to-Outcome chain. Stage 16 processes lessons learned and insights to identify, classify, and escalate necessary changes to the project's governance baseline, architectural decisions, and process documentation.

> **Alignment:** PMBOK 8 Process 4.6 Perform Integrated Change Control

> **Authority:** FULL authority for `classify-diff-type`, LOW authority for `escalate-diff-response`

> **Authority in the project:** the Charter names one decision-maker, the Project Sponsor and Maintainer (<project maintainer>). There is no standing Steering Committee, so every "Steering Committee" or "Project Manager" approval below is given by the Sponsor and recorded as such (as in CR-20261109-001, CR-20261109-002 and CR-20261110-001). An agent classifies and drafts; it never accepts, approves or applies a governance change on its own, and it never backfills or re-scores a gate that was missed (record the gap; any exception is a dated human waiver).

> **Scope of a pass:** a Stage 16 pass covers the whole Lessons Learned Register and the whole Continuous Improvement Register, not only the lessons flagged in Stage 15. A lesson or improvement that earlier passes never triaged is triaged now (Step 2).

---

## 1. Stage 16 Overview

### 1.1 Purpose and Position in the Chain

Stage 16 sits at the **Monitoring & Controlling** process group, acting as the **gatekeeper for baseline evolution**. It receives input from Stage 15 (Lesson Learned) and produces outputs that feed into Stage 17 (Adaptation Plan).

```
Stage 15 (Lesson Learned)
    \u2193
Stage 16 (Governance Change)  Classify & Escalate
    \u2193
Stage 17 (Adaptation Plan)  Operationalize
```

**Key Responsibility:** Determine whether a lesson learned requires a change to the governed baseline, and if so, what type of change and at what authority level.

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| Approved Lessons Learned | Stage 15 output | Yes |
| Flagged Lessons | Stage 15 assessment | Yes |
| Current Baseline | PMP-BL-vX.Y.Z | Yes |
| Existing ADRs | docs/adr/ | Yes |
| Governance Episodes | docs/policy-shapes/episodes/ | Yes |
| Audit Register | docs/registers/Audit-Register.md | Yes |
| Project Charter | docs/project-docs/Project-Charter.md | Yes |
| Continuous Improvement Register | docs/project-docs/Continuous-Improvement-Register.md | Yes |
| Baseline findings from Stage 14 | the "Baseline findings" table of the Stage 14 note | Yes |
| Open change requests | docs/governance/change-requests/ | Yes |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| Classified Diffs | Stage 16 assessment | No |
| Escalation Decisions | Stage 16 assessment | No |
| Baseline Revision Package (BRP) | Stage 17 input | Yes (if Steering Committee) |
| Subsidiary Plan Amendments | Stage 17 input | Yes (if PM authority) |
| Updated Governance Episodes | docs/policy-shapes/episodes/ | Yes |

### 1.4 Success Criteria

Stage 16 is complete when:
- [ ] All flagged lessons from Stage 15 are classified
- [ ] All classified diffs have escalation decisions
- [ ] All required governance amendments are prepared
- [ ] All decisions are recorded as governance episodes
- [ ] Project-Status-Register.md is updated

---

## 2. Governance Change Process (8-Step)

### Step 1: Input Validation

**Purpose:** Ensure all required inputs are available and valid before processing.

**Actions:**
1. Verify Stage 15 assessment is complete and approved
2. Confirm all flagged lessons are documented in Lessons-Learned-Register.md
3. Verify current baseline (PMP-BL-vX.Y.Z) is accessible
4. Confirm Project Charter approval limits are documented
5. Verify governance policies (`classify-diff-type`, `escalate-diff-response`) are operational

**Checklist:**
- [ ] Stage 15 assessment exists and is marked COMPLETED
- [ ] All flagged lessons have complete entries in Lessons-Learned-Register.md
- [ ] Current baseline version is documented
- [ ] Charter approval limits are defined
- [ ] Governance policies are available and tested

**Validation Commands** (Stage 15 for Phase 1 ends in the words `STAGE 15 COMPLETE`; for Phase 2 the maintainer's acceptance is recorded in the Stage 15 note):
```bash
# Stage 15 is complete and accepted
grep -n "accepted\|COMPLETE" docs/project-docs/Status-Reports/Stage-15-*.md

# Every lesson parses, and the last id is the one expected
uv run python -c "from agent_learning.lessons_learned import load_lessons_learned_register as l; e=l(); print(len(e), e[-1].id)"

# Baseline and policies
head -30 docs/project-docs/Project-Management-Plan.md | grep "PMP-BL-v"
ls docs/policy-shapes/classify-diff-type.actions.json docs/policy-shapes/escalate-diff-response.actions.json

# The store the governance commands will write to (LL-040): print it, count its files
echo "${AGENT_LEARNING_LOCAL_STORE_DIR:-./data/agent-learning/store}"
```
Check that `AGENT_LEARNING_LOCAL_STORE_DIR` points at the project's store before any command that registers an episode. `(stage16_amend tooling when IMP-062 lands)` does not print or check it yet.

---

### Step 2: Triage of the whole registers

**Purpose:** Separate lessons and improvements that need a governance change from those that need a direct fix or none, and find those no earlier pass triaged.

**2a. Coverage of the Lessons Learned Register.** For every `LL-###`, read its Tier 2/3 target and place it in one bucket:

| Bucket | Meaning |
|---|---|
| A. Tier 1 only | No propagation owed. |
| B. Tier 2/3 target, rule found there | Applied. Confirm by reading the target, not only by finding the id. |
| C. Tier 2/3 target, rule not found | Not applied. A finding, because LL-041 requires the Tier 2 edit in the same PR as the entry. |

An id search is a lead, not proof (a rule can sit in a skill without its id, an id in a test proves nothing). Read the named target. Tier 3 (`sidpa-template`) is outside the repository; list it as proposed, never as done.

**2b. Coverage of the Continuous Improvement Register.** For every `IMP-###` whose disposition is `In-Flight Candidate`, read the change it names in the code and mark it implemented, partly, or open. An entry that says it awaits Stage 16/17 and was never evaluated is a finding. Check the numbering for gaps and the dispositions for stale labels; do not change a status on the agent's reading alone.

**2c. Identifier integrity.** Check that each id cited in earlier stage documents (assessments, SPAs, BRPs, adaptation plans) names the lesson or improvement the register holds under that id. A mismatch is a baseline finding corrected through the amendment tooling; nothing is re-scored.

**2d. Classification of what needs a change.**

| Lesson or improvement impact | Requires governance change? | Action |
|---|---|---|
| Architectural (affects code structure) | Yes | Stage 16 |
| Process (affects how work is done) | Yes | Stage 16 |
| Documentation (clarification only) | No | Direct fix, traced |
| Tooling (automation only) | No | Direct fix, traced (a story or an `IMP`) |
| Scope (new features) | Yes | Stage 16 |
| Schedule (timeline changes) | Yes | Stage 16 |
| Cost (budget changes) | Yes | Stage 16 |
| Quality (standards changes) | Yes | Stage 16 |

**Triage Questions:**
1. Does this lesson require a change to the approved baseline?
2. Does it affect architectural decisions (ADRs)?
3. Does it require updates to governance policies, skills or templates?
4. Does it impact project scope, schedule, or cost?
5. Can it be resolved through documentation or tooling changes only?
6. Does the lesson conflict with a rule already in force (for example two skill steps that disagree)? Settle the conflict in the same change as the addition.

**Output:** Coverage table for both registers, and the list of items requiring Stage 16 processing, each with its route (Step 3).

---

### Step 3: Diff Classification (classify-diff-type)

**Purpose:** Classify each governance change by its structural type to determine the appropriate handling.

**Policy:** `classify-diff-type` (FULL authority)

**Two classifications, used for two different things.** The diff types below label a *proposed change* so that it can be routed and escalated. The `classify-diff-type` policy classifies an *edit to an approved document* into one of seven actions: `new_superseding_adr`, `amendment_log_entry`, `correction_note`, `clarification_section`, `provenance_note`, `pending_supersession_note`, `supersession_update`. Use the diff type here; use the policy's action only when an approved document is edited (route 1 below). The policy's lifecycle actions (`new_superseding_adr`, `pending_supersession_note`, `supersession_update`) mean the change is more than an amendment: stop and use the ADR route.

**Routes by artifact.** The artifact decides the tooling, not the diff type:

| # | Artifact changed | Route | Evidence it leaves |
|---|---|---|---|
| 1 | An approved ADR, BRD, FDD or user story | ADR-007: edit uncommitted, `(stage16_amend propose/accept when available) propose <doc>`, a human reads the classification, then `accept <doc> --by "<name>" --summary "..."` on the human's explicit instruction; commit the document, the manifest and the `docs/policy-shapes/` files together. `tests/test_governance_baseline.py` must pass. | Episode in `docs/policy-shapes/episodes/`, the `Amended <date> at Stage 16 ...` line in the document, a refreshed manifest |
| 2 | A skill under `.claude/skills/` (Tier 2), a script, a workflow, a process document | A manual Change Request `CR-YYYYMMDD-NNN` under `docs/governance/change-requests/` with the exact proposed text, a Sponsor decision recorded in it, then one PR that applies the edit and cites the request (LL-041). The whole suite must pass. | The request, its decision record, the PR |
| 3 | The PMP and generated subsidiary plans | Regenerate from the `pmbok-planning` tooling and templates; never hand-edit a generated plan. A standard that must hold in every run belongs in the template. | The regenerated plan and its baseline id |
| 4 | The baseline itself (scope, schedule, cost, a new baseline id) | Baseline Revision Package (Step 6); versioning per ADR-008 §4.6.1 and ADR-037. | `BRP-...` document, new `PMP-BL` id |
| 5 | A register entry (`LL`, `IMP`) | Append-only. A correction is a new dated entry; an id is never reused or renumbered. | The register |
| 6 | A stage assessment or methodology note (a Status Report, this guide) | Direct edit with a change-log line; these are working documents. | Git history |

**Diff Type Taxonomy:**

#### 1. Structural Diffs (Architectural Changes)
- **Definition:** Changes that affect the project's architectural structure
- **Examples:** Adding/removing modules, changing package structure, migrating code
- **Authority:** Typically requires Steering Committee approval
- **Version Impact:** Minor or major version increment

#### 2. Process Diffs (Governance Procedure Changes)
- **Definition:** Changes to how governance is performed
- **Examples:** Evidence management, approval workflows, documentation standards
- **Authority:** Typically within PM authority
- **Version Impact:** Patch version or subsidiary plan update

#### 3. Content Diffs (Documentation Changes)
- **Definition:** Changes to documentation content only
- **Examples:** Clarifications, corrections, additions
- **Authority:** Typically within PM authority
- **Version Impact:** Patch version

#### 4. Dependency Diffs (External Package Changes)
- **Definition:** Changes to external dependencies
- **Examples:** Version bumps, package additions/removals
- **Authority:** Varies by impact
- **Version Impact:** Patch or minor version
- **First, check the pillar trigger.** A brand-new dependency already needs an explicit ADR (ADR-034 Invariant 1). A version bump or an incoming upstream fork-sync change that meets the same bar — a public-API change, a dropped Python version, a major-version boundary, or anything Invariant 1 would reject as new — is not a plain Dependency Diff: it goes through the Stage 5 pillar check and the full ADR → BRD → FDD → Stories → Schedule Task chain first (Stage 5 Methodology §2 Step 6, proposed 2026-11-12, methodology-level only). Only a bump or sync that does not meet that bar stays here as an ordinary Dependency Diff.

#### 5. Configuration Diffs (Settings Changes)
- **Definition:** Changes to configuration files
- **Examples:** CI configuration, environment settings
- **Authority:** Typically within PM authority
- **Version Impact:** Patch version

#### 6. Scope Diffs (Feature Changes)
- **Definition:** Changes to project scope
- **Examples:** New features, removed features, changed requirements
- **Authority:** Typically requires Steering Committee approval
- **Version Impact:** Major version increment

#### 7. Schedule Diffs (Timeline Changes)
- **Definition:** Changes to project timeline
- **Examples:** Extended deadlines, accelerated delivery
- **Authority:** Varies by magnitude
- **Version Impact:** Typically no version change

**Classification Template:**
```yaml
lesson_id: LL-XXX
diff_type: [structural|process|content|dependency|configuration|scope|schedule]
subtype: [specific subtype]
evidence_basis: [execution|design_time]
affected_artifacts: [list of files/directories]
scope: [migration|update|addition|removal|refactoring]
impact: [low|medium|high]
confidence: [low|medium|high]
classification_timestamp: "YYYY-MM-DD"
classifier: classify-diff-type
rationale: "Detailed explanation of classification"
```

**Classification Rules:**
1. **Start with the most specific type** - If a change affects architecture, classify as structural even if it also affects process
2. **Consider evidence basis** - `execution` for changes derived from executed work, `design_time` for changes found during design review
3. **Assess impact** - High impact changes typically require higher authority
4. **Document rationale** - Always include clear reasoning for the classification

---

### Step 4: Impact Assessment

**Purpose:** Assess the impact of each classified diff to inform escalation decisions.

**Impact Dimensions:**

#### Technical Impact
- **Code Complexity:** Does it increase or decrease complexity?
- **Test Coverage:** Does it require new tests?
- **Performance:** Does it affect performance characteristics?
- **Security:** Does it introduce security considerations?
- **Maintainability:** Does it affect code maintainability?

#### Process Impact
- **Workflow Changes:** Does it change how work is performed?
- **Tooling Changes:** Does it require new or modified tools?
- **Training:** Does it require team training?
- **Documentation:** Does it require documentation updates?

#### Governance Impact
- **Policy Changes:** Does it require changes to governance policies?
- **Approval Authority:** Does it change who can approve what?
- **Audit Trail:** Does it affect auditability?
- **Compliance:** Does it affect compliance requirements?

#### Business Impact
- **Cost:** Does it have cost implications?
- **Schedule:** Does it affect timelines?
- **Scope:** Does it change project scope?
- **Risk:** Does it introduce new risks?

**Impact Assessment Template:**
```yaml
lesson_id: LL-XXX
diff_type: [from Step 3]
technical_impact:
  complexity: [increase|decrease|neutral]
  test_coverage: [new_tests_required|existing_sufficient|reduced]
  performance: [improved|degraded|neutral]
  security: [improved|degraded|neutral]
  maintainability: [improved|degraded|neutral]
process_impact:
  workflow: [changed|unchanged]
  tooling: [new_required|modified|unchanged]
  training: [required|not_required]
  documentation: [required|not_required]
governance_impact:
  policy_changes: [required|not_required]
  approval_authority: [changed|unchanged]
  audit_trail: [affected|unchanged]
  compliance: [affected|unchanged]
business_impact:
  cost: [increase|decrease|neutral]
  schedule: [extended|accelerated|neutral]
  scope: [changed|unchanged]
  risk: [new_risks|reduced_risks|neutral]
overall_impact: [low|medium|high]
```

---

### Step 5: Escalation Decision (escalate-diff-response)

**Purpose:** Determine the appropriate authority level for each classified diff.

**Policy:** `escalate-diff-response` (LOW authority, human decides)

**Escalation Matrix:**

| Diff Type | Impact | Authority Level | Action |
|---|---|---|---|
| Structural | High | Steering Committee | Baseline Revision Package |
| Structural | Medium | Steering Committee | Baseline Revision Package |
| Structural | Low | Project Manager | Subsidiary Plan Amendment |
| Process | High | Steering Committee | Baseline Revision Package |
| Process | Medium | Project Manager | Subsidiary Plan Amendment |
| Process | Low | Project Manager | Subsidiary Plan Amendment |
| Scope | Any | Steering Committee | Baseline Revision Package |
| Schedule | High | Steering Committee | Baseline Revision Package |
| Schedule | Medium/Low | Project Manager | Subsidiary Plan Amendment |
| Content | Any | Project Manager | Direct update or Subsidiary Plan |
| Dependency | High | Steering Committee | Baseline Revision Package |
| Dependency | Medium/Low | Project Manager | Subsidiary Plan Amendment |
| Configuration | Any | Project Manager | Direct update |

**Authority Limits (from Project Charter):**
- **Project Manager Authority:** Changes within approved scope, schedule, and budget
- **Steering Committee Authority:** Changes to scope, major schedule changes, budget changes > X%, architectural changes
- **Project Sponsor Authority:** Project charter changes, major scope changes

**Who decides here.** The matrix names roles from the PMBOK model. In the project each of them is the Project Sponsor (see Authority above). The `escalate-diff-response` policy runs at LOW authority and its classifier's human-approval gate halts before it, so the human's decision is the decision of record. Write the decision into the request or the document it concerns; do not infer an approval from silence or from a later instruction.

**Escalation Template:**
```yaml
lesson_id: LL-XXX
diff_type: [from Step 3]
escalation_level: [project_manager|steering_committee|project_sponsor]
action: [direct_update|subsidiary_plan_amendment|baseline_revision_package]
evidence_basis: [execution|design_time]
threshold_exceeded: [true|false]
charter_approval_limit: [exceeded|within]
required_approvals: [list of roles]
decision_timestamp: "YYYY-MM-DD"
escalator: escalate-diff-response
rationale: "Detailed explanation of escalation decision"
```

**Escalation Decision Tree:**

```
Does the change exceed Charter approval limits?
  \u2192 Yes: Escalate to Steering Committee
  \u2192 No: Is it within PM authority?
    \u2192 Yes: Escalate to Project Manager
    \u2192 No: Escalate to Project Sponsor
```

**Charter Approval Limit Check:**
- Review Project Charter for specific limits
- Check ADR-037 for versioning rules
- Consult governance policies for thresholds

---

### Step 6: Governance Amendment Preparation

**Purpose:** Prepare the necessary documentation for approved governance changes.

Prepare the document that matches the route chosen in Step 3. Route 1 needs no separate package (the amendment tooling produces the evidence). Route 2 needs a Change Request. A BRP or an SPA is used only when the baseline or a subsidiary plan changes; existing examples are `docs/governance/brp/` and `docs/governance/spa/`. Prepare, do not apply: nothing here is applied before the decision is recorded.

#### Baseline Revision Package (BRP) - For Steering Committee

**Required Contents:**
1. **Revised PMP** - Updated Project Management Plan
2. **Changed Plans** - All affected subsidiary management plans
3. **Standard Set** - Core project documents:
   - Spark-Capture.md
   - Ideation-Document.md
   - Business-Case.md
   - Benefits-Statement.md
   - Stakeholder-Register.md
   - Project-Charter.md (if amended)
4. **Change Documentation** - Detailed description of changes
5. **Impact Assessment** - Technical, process, governance, business impacts
6. **Risk Assessment** - New risks introduced by changes
7. **Rollback Plan** - How to revert if issues arise

**Versioning Rules (ADR-037):**
- Design-time revisions: PMP-BL-v1.0.x (patch increment)
- Execution-time adaptations: PMP-BL-v1.1.0 (minor increment)
- Major architectural changes: PMP-BL-v2.0.0 (major increment)

**BRP Template:** use your project's BRP artifact pattern; full example lives in agent-learning.

---


### Step 7: Decision Recording

**Purpose:** Record every governance decision so it can be audited and replayed.

**Use the tooling; do not hand-write episodes.** Episodes are `Episode` records created by the commands, not JSON written by hand:

| Decision | How it is recorded |
|---|---|
| An edit to an approved ADR, BRD, FDD or story | `stage16_amend.py propose`, then `accept`: frame, result and measurements under `docs/policy-shapes/`, the episode in `docs/policy-shapes/episodes/` (for example `amend-adr-005-cr002b-episode.json`), the Status line in the document, and a refreshed governance baseline (`scripts/governance_baseline.py`) |
| A decision on a change request | The decision table inside the request, with the date and the words of the decision as given by the human |
| A classification by `classify-diff-type` or an escalation by `escalate-diff-response` outside the amendment route | `agent-learn-ext task-policy-decide`, then `task-policy-adjudicate`, then `task-episode-register`, in that order |

**Rules:**
1. Before any `task-policy-decide`, `task-policy-adjudicate` or `task-episode-register`, resolve and print the store path and count its files before and after (LL-040). Only `task-episode-register` writes a file.
2. An agent never runs `accept` and never registers an approval on a human's behalf.
3. A gate that was missed is not approved afterwards. Record the gap in the assessment; run the gate going forward; an exception is a dated human waiver.
4. Never edit `tests/governance_baseline.json` by hand.
5. Stages 13 to 15 have no episodes here (they are `human_review`); a Stage 16 decision on their output is the first episode.

**Recording order:** decide, record in the request or document, commit together with the evidence files, run `tests/test_governance_baseline.py` and the whole suite.

---

### Step 8: Stage Completion and Handoff

**Purpose:** Finalize Stage 16 and prepare for Stage 17.

**Completion Checklist:**
- [ ] Every lesson and every in-flight improvement has a coverage line (Step 2), not only the flagged ones
- [ ] Id mismatches in earlier documents are listed (Step 2c)
- [ ] All flagged lessons from Stage 15 are classified
- [ ] All classified diffs have escalation decisions
- [ ] Each change has a route (Step 3) and its evidence
- [ ] All required BRPs are prepared and submitted
- [ ] All required subsidiary plan amendments are prepared and submitted
- [ ] All decisions are recorded as the route requires (Step 7); none is recorded by an agent for a human
- [ ] Project-Status-Register.md is updated to mark Stage 16 as COMPLETED
- [ ] Stage 16 assessment document is complete and approved
- [ ] All artifacts are committed to repository

**One adaptation per phase.** The phase close runs Stage 16 and Stage 17 once, as one adaptation; Stage 17 receives everything Stage 16 approved, plus what it deferred to Phase Next.

**Handoff to Stage 17:**
1. Create Stage 17 assessment document
2. Reference all approved governance changes from Stage 16
3. Identify operationalization requirements
4. Prepare adaptation plan
5. Submit for approval via `approve-adaptation-plan`

**Stage 16 Completion Template:**
```markdown
## Stage 16 Completion Summary

### Processing Summary
- **Lessons Processed:** X
- **Flagged for Governance Change:** Y
- **Classified Diffs:** Y
- **Escalation Decisions:** Y
- **BRPs Created:** A
- **Subsidiary Plan Amendments:** B

### Decisions Made
| Lesson ID | Diff Type | Escalation Level | Action | Status |
|---|---|---|---|---|
| LL-XXX | structural | steering_committee | BRP | Approved/Pending |
| LL-YYY | process | project_manager | SPA | Approved/Pending |

### Next Steps
1. [Stage 17 action 1]
2. [Stage 17 action 2]

### Approval
- [ ] Stage 16 Assessment Approved
- [ ] Project-Status-Register.md Updated
- [ ] All artifacts committed
```

---

---

## 5. Common Pitfalls and Mitigations

###1 Pitfalls

| Pitfall | Description | Mitigation |
|---|---|---|
| Over-classification | Classifying everything as structural | Use the classification matrix, start with most specific type |
| Under-escalation | Not escalating high-impact changes | Always check charter approval limits |
| Incomplete documentation | Missing rationale for decisions | Use templates, require rationale for all decisions |
| Inconsistent versioning | Wrong version numbers | Follow ADR-037 versioning rules |
| Missing episodes | Decisions not recorded | Automate episode generation, validate before completion |
| Scope creep | Adding unrelated changes to BRP | Stick to the specific lesson being addressed |
| Analysis paralysis | Over-analyzing simple changes | Set time limits for classification and escalation |

###2 Mitigation Strategies

1. **Use Templates:** Always use the provided templates for consistency
2. **Follow Checklists:** Complete all checklist items before submitting
3. **Automate Validation:** Run validation scripts before submission
4. **Peer Review:** Have another team member review classifications and escalations
5. **Timebox Decisions:** Set time limits for classification and escalation decisions
6. **Document Assumptions:** Clearly document any assumptions made during classification
7. **Trace to Evidence:** Always link decisions to specific evidence

---

## 6. References

###1 Internal References

- [Intent-to-Outcome Chain Coverage](../chain-coverage.md)
- [Project Status Register](../Project-Status-Register.md)
- [Lessons Learned Register](../Lessons-Learned-Register.md)
- [ADR-010: Lessons Learned Crystallization and Register](../adr/ADR-010-lessons-learned-crystallization-and-register.md)
- [ADR-034: Decommission pmbok/ Directory](../adr/ADR-034-decommission-pmbok-directory.md)
- [ADR-037: Design-Time vs Execution-Time Feedback Loops](../adr/ADR-037-design-time-vs-execution-time-feedback-loops.md)
- [Stage 15 Lesson Learned Methodology](Stage-15-Lesson-Learned-Methodology.template.md)

###2 External References

- PMBOK 8: Project Management Body of Knowledge, 8th Edition
- PMI: Project Management Institute standards
- ISO 21500: Guidance on Project Management

###3 Related Methodologies

- [Stage 15 Methodology](Stage-15-Lesson-Learned-Methodology.template.md)
- [Stage 17 Methodology](Stage-17-Adaptation-Plan-Methodology.md) (to be created)
- [Stage 18 Methodology](Stage-18-Intent-Refinement-Methodology.md) (to be created)

---
