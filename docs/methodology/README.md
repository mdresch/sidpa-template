# Stage methodology guides (template)

Operational **Stage … — Methodology Guide** documents for each chain stage, synced from `agent-learning` and aligned with `docs/chain-coverage.md` (Purpose blockquotes, overview tables, process steps, pitfalls, references).

Re-sync from a sibling `agent-learning` checkout (or specify `--source` / `AGENT_LEARNING_METHODOLOGY_DIR`):

```bash
python scripts/templify_methodology_from_agent_learning.py
# or:
python scripts/templify_methodology_from_agent_learning.py --source /path/to/agent-learning/docs/project-docs/Methodology
```

Instantiate by copying `Stage-NN-*-Methodology.template.md` to `docs/project-docs/Methodology/` (or your project path) and filling project-specific instances.

| Stage | Template | Primary gates / authority |
|---:|---|---|
| 1 | [Stage-01-Intent-Methodology.template.md](Stage-01-Intent-Methodology.template.md) | `approve-ideation` |
| 2 | [Stage-02-Hypothesis-Methodology.template.md](Stage-02-Hypothesis-Methodology.template.md) | `classify-hypothesis-status` |
| 3 | [Stage-03-Benefit-Methodology.template.md](Stage-03-Benefit-Methodology.template.md) | `approve-business-case`, `approve-benefits` |
| 4 | [Stage-04-Objective-Methodology.template.md](Stage-04-Objective-Methodology.template.md) | `approve-charter` |
| 5 | [Stage-05-Pillars-and-Architecture-Methodology.template.md](Stage-05-Pillars-and-Architecture-Methodology.template.md) | `approve-project-pillars`, `approve-adr` |
| 6 | [Stage-06-Requirement-Methodology.template.md](Stage-06-Requirement-Methodology.template.md) | `approve-adr`, `approve-brd`, `approve-fdd`, `approve-user-stories` |
| 7 | [Stage-07-Project-PMP-and-Baselines-Methodology.template.md](Stage-07-Project-PMP-and-Baselines-Methodology.template.md) | `approve-subsidiary-plan`, `approve-pmp` |
| 8 | [Stage-08-Implementation-Readiness-Methodology.template.md](Stage-08-Implementation-Readiness-Methodology.template.md) | `validate-intent-foundation` |
| 9 | [Stage-09-Deliverable-Methodology.template.md](Stage-09-Deliverable-Methodology.template.md) | `implement-story` |
| 10 | [Stage-10-Verification-Evidence-Methodology.template.md](Stage-10-Verification-Evidence-Methodology.template.md) | contract test suite |
| 11 | [Stage-11-Audit-Record-Methodology.template.md](Stage-11-Audit-Record-Methodology.template.md) | `approve-audit-record` |
| 12 | [Stage-12-Actual-Outcome-Methodology.template.md](Stage-12-Actual-Outcome-Methodology.template.md) | benefits / outcome comparison |
| 13 | [Stage-13-Observation-Methodology.template.md](Stage-13-Observation-Methodology.template.md) | raw capture (human review) |
| 14 | [Stage-14-Insight-Methodology.template.md](Stage-14-Insight-Methodology.template.md) | `resolve-kb-conflict` (reference; §3.2) |
| 15 | [Stage-15-Lesson-Learned-Methodology.template.md](Stage-15-Lesson-Learned-Methodology.template.md) | `resolve-kb-conflict` / human review |
| 16 | [Stage-16-Governance-Change-Methodology.template.md](Stage-16-Governance-Change-Methodology.template.md) | `classify-diff-type`, `escalate-diff-response` |
| 17 | [Stage-17-Adaptation-Plan-Methodology.template.md](Stage-17-Adaptation-Plan-Methodology.template.md) | `approve-adaptation-plan` |
| 18 | [Stage-18-Intent-Refinement-Methodology.template.md](Stage-18-Intent-Refinement-Methodology.template.md) | `approve-intent-refinement` |

New guide: start from [Stage-Methodology-SKELETON.template.md](Stage-Methodology-SKELETON.template.md) and the matching row in `docs/chain-coverage.md` §2.