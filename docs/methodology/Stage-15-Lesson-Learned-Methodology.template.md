---
artifact_type: "methodology_guide"
stage: "15"
stage_name: "Lesson Learned"
pmbok_process: ""
version: "1.0"
date: ""
owner: "<project maintainer>"
governance_policy: "resolve-kb-conflict (reference shape; human_review until initialized)"
---

# Stage 15: Lesson Learned — Methodology Guide

> **Lifecycle IPO (template):** Inputs: Verified insights. Process: Crystallize actionable knowledge. Output: Lessons Learned register (§3.2).

> **Purpose:** Transform verified insights into formalized organizational knowledge that can be ingested into Obsidian brain knowledge graphs, improving project procedures and methodologies.

> **Authority:** the chain designs Stage 14 around a LOW-authority `resolve-kb-conflict` policy (trust existing, supersede, or flag). This repository declares no such shape and has recorded no such decision, so Stages 13 to 15 are `human_review` here: the assistant drafts, and the maintainer accepts or drops every entry. No episode is created for them.

---

## 1. Overview

Stage 15 crystallizes actionable knowledge from verified insights (Stage 14, Insights) derived from raw observations (Stage 13, Observation, run in Phase 2 as the Systems Telemetry Review and Findings). This completes the knowledge path and transforms lessons into high-quality knowledge graph entries for Obsidian brain ingestion.

### Knowledge Pipeline

```
Stage 13 (Observation) 
    ↓ Raw facts, no interpretation  
Stage 14 (Insight) 
    ↓ Synthesized understanding, causal analysis  
Stage 15 (Lesson Learned) 
    ↓ Actionable invariants, formalized knowledge  
    ↓ Knowledge Graph Entry (Obsidian Brain)
```

---

## 2. Process

### Step 1: Verify Stage 13 & 14 Completeness

**Where the inputs live.** The forms differ by phase, and Stage 15 reads whichever the phase produced:

| Phase | Stage 13 (Observation) | Stage 14 (Insight) |
|---|---|---|
| Phase 1 (worked example below) | One file per observation: `docs/observations/OBS-001.md` to `OBS-009.md` | One file per insight: `docs/insights/INSIGHT-001.md` to `INSIGHT-004.md` |
| Phase 2 | A review note, `Status-Reports/Stage-13-Systems-Telemetry-Review-and-Findings.md` (REP-STAGE13-OBSERVATION-PHASE2), and one file per observation: `docs/observations/OBS-010.md` to `OBS-019.md` | A review note, `Status-Reports/Stage-14-Insights-Phase2.md` (REP-STAGE14-INSIGHT-PHASE2), with a baseline-findings table, and one file per insight: `docs/insights/INSIGHT-005.md` to `INSIGHT-011.md` (the note calls them `INSIGHT-P2-01` to `P2-07`) |

An insight that contradicts an approved document is a baseline finding for Stage 16 and does not become a lesson. A lesson cites the insight id and, through it, the observation sections. The Phase 1 walk-through that follows keeps its original ids.


---

### Step 2: Insight-to-Lesson Crystallization

**For each INSIGHT-NNN, create LL-NNN:**

| Insight | Lesson | Knowledge Base Action | Tier Propagation |
|---------|--------|----------------------|------------------|
| INSIGHT-001: Phase 1 blocked by evidence | LL-044: External Evidence Dependency | Trust existing + link | Tier 1-3 |
| INSIGHT-002: Story status in two places | LL-045: Single Source of Truth | Trust existing + link | Tier 1-3 |
| INSIGHT-003: Stage 18 tooling in legacy tree | LL-043: Legacy Code Dependency | Flag for human decision | Tier 1-3 |
| INSIGHT-004: Gate evidence split | LL-046: Dual Evidence Storage | Trust existing + flag | Tier 1-3 |

**Crystallization Template:**
```markdown
### LL-XXX — [Descriptive Title]
- **Identifier:** `LL-XXX`
- **Date:** 2026-11-05
- **Phase:** Phase 1 / Stage 15
- **Epic / Source:** Derived from INSIGHT-NNN (OBS-AAA, OBS-BBB)
- **Scope:** [Universal Process / Repository Architecture / Universal Testing / etc.]
- **Tier 2/3 Propagation Target:** [Where this lesson applies]
- **The Trap:** [What problem was observed]
- **The Root Cause:** [Why it happened]
- **Actionable Invariant:** [Concrete rule to prevent recurrence]
```


---

### Step 3: Knowledge Graph Entry Creation (Obsidian Brain Format)

**Obsidian Brain Ingestion Requirements:**
- Unique ID mapping: `LL-###` → `Lesson-nnnn`
- Structured YAML frontmatter
- Tag-based categorization
- Cross-reference links

**Knowledge Graph Entry Template:**

```markdown
# (Extended template omitted — port detail from agent-learning when instantiating.)
```

---

### Step 4: Quality Assurance Checklist

**✅ Required Fields (ADR-010 §4.3):**
- [ ] Identifier: `LL-###` format
- [ ] Title: Descriptive summary
- [ ] The Trap: What was observed
- [ ] The Root Cause: Underlying mechanism
- [ ] The Rule: Actionable invariant
- [ ] Tier 2/3 Propagation Target: Where to apply

**✅ Quality Criteria:**
- [ ] **Specific**: Addresses one clear problem
- [ ] **Actionable**: Provides concrete prevention rule
- [ ] **Universal**: Applies beyond single incident
- [ ] **Testable**: Can verify rule prevents recurrence
- [ ] **Propagatable**: Clear Tier 2/3 targets

**✅ Validation:**
```bash
# Parse validation
uv run pytest tests/test_lessons_learned.py -v

# Schema validation
python -c "from src.agent_learning.lessons_learned import load_lessons_learned_register; entries = load_lessons_learned_register(); print(f'Valid: {len(entries)} lessons')"
```

---

### Step 5: Cross-Reference Linking

**Link all related artifacts:**

```markdown
## References
- **Observations**: [[OBS-001]], [[OBS-004]], [[OBS-005]]
- **Insights**: [[INSIGHT-001]]
- **Hypotheses**: [[HYP-AL-008]], [[HYP-AL-009]]
- **ADRs**: [[ADR-010]]
- **Documents**: [[Benefits-Management-Plan]], [[Project-Charter]]
```

**Bidirectional Links:**
- Add lesson references to observations and insights
- Link lessons to affected ADRs and hypotheses
- Reference lessons in governance documents

---

### Step 6: Tier Propagation Strategy

| Tier | Location | Purpose | Example |
|------|----------|---------|---------|
| **Tier 1** | Lessons-Learned-Register.md | Historical record | LL-044 entry |
| **Tier 2** | `.claude/skills/*/SKILL.md` | Agent guidance | Add data check to Step 0 |
| **Tier 3** | `sidpa-template/*` | Cross-project | testing/data-dependencies.md |

**Propagation Checklist:**
- [ ] Tier 1: Entry added to register
- [ ] Tier 2: Skill updated with lesson reference
- [ ] Tier 3: Template updated (requires human approval)

---

### Step 7: Obsidian Brain Ingestion

**Ingestion Script:** `obsidian-second-brain/scripts/ingest-agent-learning.mjs`

**Ingestion Process:**
1. **Transform** LL-### entries to Lesson-nnnn format
2. **Map** relationships between observations, insights, lessons
3. **Tag** with appropriate categories
4. **Link** to existing knowledge base nodes
5. **Validate** knowledge graph integrity

**Ingestion Command:**
```bash
# From obsidian-second-brain directory
node scripts/ingest-agent-learning.mjs \
  --source /workspace/github__mdresch__agent-learning \
  --output vault/agent-learning \
  --stage 15
```

**Expected Output:**
```
Ingesting Stage 15 lessons...
✓ LL-044 → Lesson-0044 (External Evidence Dependency)
✓ LL-045 → Lesson-0045 (Single Source of Truth)
✓ LL-046 → Lesson-0046 (Dual Evidence Storage)
✓ LL-043 → Lesson-0043 (Legacy Code Dependency)
...
Knowledge graph updated: 4 new nodes, 12 new edges
```

---

### Step 8: Knowledge Graph Quality Metrics

**Graph Metrics to Track:**
- **Node Degree**: Number of connections per lesson
- **Centrality**: Importance in knowledge network
- **Clustering**: Related lessons grouped together
- **Coverage**: % of project knowledge captured

**Target Metrics:**
- Each lesson: ≥3 cross-references
- Each lesson: ≥1 Tier 2 propagation
- Graph density: 0.3-0.5 (well-connected)
- Orphan nodes: 0

---
