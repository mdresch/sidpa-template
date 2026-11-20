---
artifact_type: "methodology_guide"
stage: "13"
stage_name: "Observation"
pmbok_process: "4.5 Monitor & Control Project Work"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "none — raw observation capture; human_review, no decision policy declared"
---

# Stage 13: Observation — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Runtime telemetry & findings. Process: Record raw facts. Output: Observation log (§3.2).

> **Purpose:** Record what was actually seen — what ran, when, the evidence — with no interpretation and no fix attached, so Stage 14 has raw facts to synthesize rather than someone's conclusion already baked in.

> **Alignment:** PMBOK 8 Process 4.5 Monitor & Control Project Work.

> **Authority:** No TaskPolicy decides here. `docs/chain-coverage.md` §2 row 13 names this stage's role as "Raw Input" / Knowledge Base Captures. **Authority in the project:** `human_review` — the repository has not declared the `resolve-kb-conflict` shape the idealized chain assumes starting at Stage 14, so there is no policy at this stage either; a human reviews and accepts, changes, or drops each observation.

---

## 1. Overview

### 1.1 Position in the Chain

```
Stage 11-12 (Audit Record, Actual Outcome) and runtime telemetry
    ↓
Stage 13 (Observation) — this stage — raw, uninterpreted facts
    ↓
Stage 14 (Insight) — synthesizes causal significance from these observations
```

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| Runtime telemetry, review findings, test-run anomalies | Wherever they actually occurred (CI, `implementation-log.md` review-triage entries per ADR-036, manual notice) | Yes |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| Observation notes | `docs/observations/OBS-NNN.md` (one file per observation) | No (human-reviewed, no episode) |
| Systems Telemetry Review and Findings note (phase-level roll-up) | `docs/project-docs/Status-Reports/Stage-13-Systems-Telemetry-Review-and-Findings.md` | No |

### 1.4 Success Criteria

Stage 13 is complete, for a phase, when:
- [ ] Every real anomaly, drift, or environment gotcha noticed during the phase has a corresponding `OBS-NNN.md`
- [ ] Each observation states only what was seen, when, and the evidence — no interpretation, no proposed fix
- [ ] The phase's roll-up note exists and names every `OBS-NNN` it covers

---

## 2. Process

### Step 1: Write the observation as pure fact

One `OBS-NNN.md` per distinct thing noticed: store location, a dependency on legacy code, status drift between two sources, a review-triage finding from `implementation-log.md` (ADR-036 `review_triage`). State what was seen and the evidence. Do not explain why it happened or what to do about it — that is Stage 14's job, deliberately kept separate.

### Step 2: Roll up at phase close

Write or update the phase's Systems Telemetry Review and Findings note, listing every `OBS-NNN` the phase produced.

### Step 3: Hand to Stage 14

Stage 14 reads these observations and may ask for more detail, but does not edit them to fit its own interpretation — an observation is evidence, not a draft of the insight.

---


## 4. Validation

```bash
ls docs/observations/OBS-*.md | wc -l
grep -n "review_triage" implementation-log.md | head -10
```

---

## 5. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| Writing an interpretation or a fix into an observation | Keep Stage 13 to pure fact; interpretation is Stage 14's job |
| Citing chain-coverage.md §3.2's 2026-10-27 snapshot as current | Verify against `docs/observations/` directly; the note is stale |
| Skipping the phase roll-up note | Stage 15/16/18 readiness checks look for it, not just the individual `OBS-NNN` files |

---

## 6. References

- [Intent-to-Outcome Chain Coverage](../chain-coverage.md) — §2 row 13, §3.2 (dated 2026-10-27, now partially stale — see §3 above)
- [ADR-036: Learning Methodology Examples Ledger and Review Triage Loop](../../adr/ADR-036-learning-methodology-examples-ledger-and-review-triage-loop.md)
- [Stage-13-Systems-Telemetry-Review-and-Findings.md](../Status-Reports/Stage-13-Systems-Telemetry-Review-and-Findings.md)
- [Stage 14: Insight Methodology](Stage-14-Insight-Methodology.template.md)
- [Stage 15: Lesson Learned Methodology](Stage-15-Lesson-Learned-Methodology.template.md) — §Step 1's input table for both phases

---
