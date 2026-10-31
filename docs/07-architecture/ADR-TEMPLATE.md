---
pmbok_edition: "PMBOK 8"
pmbok_process_group: "Planning"
pmbok_process: "5.3 Define Scope & Systems Architecture Planning"
pmp_baseline: "PMP-BL-v<X.Y.Z>"
lifecycle_stage: "Stage 7 (Requirement: Architecture)"
governance_policy: "approve-adr"
inputs:
  - "Project-Charter.md"
  - "PILLARS-EXERCISE.md"
  - "Ideation-Document.md (Hypotheses)"
process: "Formulate architectural decisions per pillar, evaluate trade-off alternatives, specify consequences"
outputs:
  - "ADR-*.md"
---

# ADR <NNN>: <Title>

> **PMBOK 8 Process:** `5.3 Define Scope & Systems Architecture Planning` (Planning)  
> **Governance Policy:** `approve-adr` | **Lifecycle Stage:** `Stage 7 (Requirement: Architecture)`  
> **Inputs:** Project-Charter.md, PILLARS-EXERCISE.md, Ideation-Document.md (Hypotheses)  
> **Process:** Formulate architectural decisions per pillar, evaluate trade-off alternatives, specify consequences  
> **Outputs:** ADR-*.md

**Governing Baseline:** `PMP-BL-v<X.Y.Z>` (Invariant 6)  
**Governing Pillar:** `<PIL-0N: Pillar Name>` (traced to PILLARS-EXERCISE.md)

---

## 1. Executive Brief
<One paragraph: what's real today, what gap this closes, what the decision actually is. State it as a finding, not a proposal — if you haven't verified the "what's real today" part against actual code/docs yet, you're not ready to write this section.>

## 2. Pillar & Strategic Alignment
- **Pillar Covered:** `<PIL-0N: Pillar Name>`
- **Charter Objectives Addressed:** `<Objective 1, Objective 2>`
- **Hypotheses Addressed:** `<HYP-NNN>`
- **Downstream Artifacts:** This ADR serves as the direct prerequisite input to `<BRD-NNN>` and `<FDD-NNN>`, which decompose into User Stories (Work Packages).

## 3. Status
**Proposed (<date>)** — awaiting <real approver>'s explicit review and sign-off, per <this project's own governance rule, cited>.

<Do not write "Accepted" here until that sign-off actually happened. If this project has a real `approve-adr` policy, its recommendation goes here too, once run — but the recommendation is an input to the decision, never a substitute for it. Say so explicitly, every time.>

## 4. Context
<Real, cited facts only. Every claim needs a file path, a line number, a command output, or an explicit "not independently verified, named as plausible" caveat. If a reviewer's claim turns out wrong when checked, say what you checked and what you found — don't just fix it silently.>

## 5. Decision
<Numbered subsections. Each decision should be traceable to a fact in §4. Name what you are NOT deciding (explicitly out of scope) as clearly as what you are.>

### 5.N Review triggers (if any apply)
<Only include this if a real, nameable future event would make this ADR's own facts stale — e.g. "revisit before first production deployment." Don't invent a generic review cadence; tie it to something concrete.>

## 6. Alternatives Considered
| Alternative | Reason for rejection |
|---|---|
| <a real alternative that was actually considered> | <the real reason, not a strawman> |

## 7. Consequences
### Positive
### Negative
<Negative consequences are not optional filler — if you can't think of a real one, you probably haven't scrutinized the decision enough yet.>

## 8. References
<Every file this ADR cites, as a real link/path. Link related ADRs. Cite PILLARS-EXERCISE.md and the gap-tracking document that justified writing this ADR in the first place.>
