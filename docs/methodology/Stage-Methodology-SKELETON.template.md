---
artifact_type: "methodology_guide"
stage: "<N>"
stage_name: "<Chain stage name>"
pmbok_process: "<PMBOK 8 process or chain label>"
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "<primary TaskPolicy id(s)>"
---

# Stage <N>: <Chain stage name> — Methodology Guide

> **Purpose:** <One paragraph: what this stage proves and which artifact it leaves behind.>

> **Alignment:** <PMBOK 8 process group / process.>

> **Authority:** <FULL / LOW authority via named policies; human approval rules.>

> **Lifecycle IPO (template):** Inputs: … Process: … Output: … (from `docs/chain-coverage.md` §2.)

---

## 1. Overview

### 1.1 Position in the Chain

```
<prior stage>
    ↓
Stage <N> — this stage
    ↓
<next stage>
```

### 1.2 Inputs

| Input | Source | Mandatory |
|---|---|---|
| <artifact or signal> | `<path>` | Yes / If applicable |

### 1.3 Outputs

| Output | Destination | Governed |
|---|---|---|
| <artifact> | `<path>` | Yes / No (via `<policy>`) |

### 1.4 Success Criteria

Stage <N> is complete when:
- [ ] <observable criterion tied to gates and registers>

---

## 2. Process

### Step 1: <verb phrase>

<Actions and handoff notes.>

### Step 2: <verb phrase>

<Gate: run policy; record episode only on explicit human instruction (LL-040).>

---

## 4. Validation

```bash
# Project-specific checks — cite contract tests or grep guards here.
```

---

## 5. Common Pitfalls

| Pitfall | Mitigation |
|---|---|
| <common mistake> | <fix> |

## 6. References

- [Intent-to-Outcome chain coverage](../chain-coverage.md) — §2 row <N>, §3 feedback loops as applicable
- [Sequence and lessons](../sequence-and-lessons.md)
- Related stage guides under `docs/methodology/`