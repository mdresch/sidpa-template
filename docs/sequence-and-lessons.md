# Sequence & Lessons — order that actually mattered, confirmed the hard way

Every rule below was learned by hitting it, not derived in the abstract. Cited against the real projects (ADPA, SocialEngage, Enterprise Work Hierarchy) that surfaced it, so a future reader can go check the primary source rather than trust this summary alone.

---

## 1. Governance-document order

1. **Spark → Ideation → Business Case → Benefits Statement → Charter.** Benefits Statement before Charter, not after — PMBOK 8 confirms the Benefits Plan is a Charter *input*, not a follow-on (ADPA, corrected after an earlier draft had them in the wrong order).
2. **Charter before the Pillars Exercise before the 9 subsidiary management plans.** Obvious in principle; the real trap is treating the Charter as a PMP (Project Management Plan) — it isn't one. The PMP is an *integration* document, built only after every subsidiary plan is grounded in concrete work packages. Don't draft a PMP early thinking it's the Charter's natural next step.
3. **Pillars Exercise bridges Charter to Architecture.** Right after the Project Charter is approved, execute the **Pillars Exercise** (`docs/07-architecture/PILLARS-EXERCISE.md`) to decompose the project into 4–6 mutually exclusive, collectively exhaustive architectural and functional pillars.
4. **100% ADR Pillar Coverage Invariant.** For each identified pillar, draft high-level foundational ADRs. The set of initial ADRs must provide 100% full coverage across every identified pillar before proceeding to requirements. No architectural pillar may be left floating or unassigned.
5. **Hypothesis before Requirement.** A Hypothesis (falsifiable design assumption) gets tested and its status updated *before* it becomes an ADR (a Requirement-stage artifact). `classify-hypothesis-status` sits here; `approve-adr` sits one stage later. Don't skip straight to drafting an ADR from an untested Hypothesis.

---

## 2. ADR → BRD → FDD → Story order & Work Package Derivation

6. **ADR before BRD before FDD before Story, strictly.** Each cites the one before it and does not restate it. An FDD that re-derives its own ADR's reasoning instead of citing it is a sign something was drafted out of order.
7. **User Stories ARE the Work Packages for Subsidiary Plans.** Schedule (6.1) and Cost (7.1) plans cannot be front-loaded against speculative estimates; they require real duration and resource commitments. The User Stories decomposed from FDDs with testable Acceptance Criteria (BDD) *are* the PMBOK Work Packages (5.4 WBS). Once User Stories exist, they provide the real story points, velocity, and task items needed to synthesize:
   - **Scope Management Plan (5.1)**
   - **Schedule Management Plan (6.1)**
   - **Cost Management Plan (7.1)**
   - **Resource Management Plan (9.1)**
   into the integrated **Project Management Plan (4.2)**.
8. **Not every Accepted ADR produces a Story.** Confirmed twice: an ADR whose every real decision is "record a convention for future work" (no current build target) produces zero code-shaped stories, and that's the correct output, not a gap to fill by inventing one (ADPA, ADR-032/Epic 3; FDD-032 names this explicitly as "no current build target").
9. **A drafted Story can still turn out not to be code-shaped.** Running `implement-story` against it is how you find out — not by reasoning about it in advance. When that happens, reclassify (a Governance Exercise register, or equivalent), don't force a lighter-weight Story template into existence for a category of one (ADPA, Story 1.1 → GOV-EX-001).

---

## 3. The pipeline-entry gate

10. **`validate-intent-foundation` sits between "the documents are approved" and "it's safe to start `implement-story`."** These are genuinely different questions. A Story can have an Accepted ADR, an Accepted BRD, an Accepted FDD, and still not be the right moment to start real code — e.g., a named prerequisite elsewhere is still open. Don't treat document approval as implicit permission to start building (ADPA + SocialEngage, independently converged).
11. **This gate does not learn from aggregate statistics — it reasons per instance.** SocialEngage's own low-authority learned version of this exact decision hit a hard entropy ceiling (~42% probability) on real positive-only data and could never earn autonomy no matter how much evidence accumulated. Don't re-attempt a learned version of this specific decision; `full` authority, reasoned via a decision frame, from the start.
12. **Validate the gate itself against a deliberately-wrong case before trusting it on real ones.** A policy that only ever sees cases that should pass can't demonstrate it discriminates. Build one invented, obviously-ungrounded case (no real ADR/BRD/FDD behind it at all) and confirm it loses before registering any real episode (ADPA: the "Story 9.9" red-team case; SocialEngage: "hypothetical MongoDB ADR, correctly rejected").

---

## 4. Code-implementation order

13. **Worktree isolation is justified by real multi-contributor state, not assumed.** Check `git log` for actual distinct contributors before deciding whether per-story worktree isolation is worth the overhead for this project.
14. **Confirm the real base branch before the first worktree, not after a failed command.** `main` is a default assumption, not a fact — ADPA's real default branch had a project-specific name, discovered via a failed `git worktree add`.
15. **A worktree does not inherit installed dependencies.** `git worktree add` gives you the files, not `node_modules`. Confirm and fix this before the first test run, not after a confusing failure that looks like a missing-package bug.
16. **Direct-push-to-default-branch skips more than a compliance checkbox.** PR review (automated reviewers, a second pair of eyes) catches things a solo local check cannot. Even with no CI gate forcing it, prefer a real PR over a direct merge once more than one contributor exists (ADPA, corrected after Story 1.2's own direct push).
17. **A pending commit-hash placeholder needs a real backfill step.** If the implementation and its log entry must be committed together before the commit's own hash is known, the `pending` placeholder needs something — a human remembering, or a pre-commit hook — to actually resolve it, or it stays wrong forever.

---

## 5. Governance-mechanism-building order (meta-level)

18. **Only build a TaskPolicy where a real, repeating judgment call is already evidenced.** Every policy in this methodology's real history was built *after* hitting the same kind of decision more than once — never pre-built in anticipation. See `docs/root-cause-log.md` for exactly which real case justified each one.
19. **Declaring a policy's shape (actions, decision context) is not the same as fabricating evidence for it.** A policy can sit idle — zero episodes, baseline logits at 0.0 — once its *shape* is independently confirmed by more than one real project (see `docs/policy-shapes/`). What must never happen: running a decision against invented support/confidence numbers, or registering a fake episode. This template's own policies follow this rule: declared, idle, never fed fake data.
20. **A requires_human_approval mistake is a real, repeatable failure mode — default to `true` for any decision with a known human-approval rule, and correct down later with evidence, not the reverse.** ADPA's own `approve-adr` was built with `requires_human_approval: false` initially and had to be corrected after the resolver's own autonomy logic would have bypassed a real governance rule. Every later policy in this methodology defaulted to `true` from the start because of that one correction.

---

## 6. Universal Agent Artifact Quality Assurance Directives

When AI agents or subagents generate any governance document, they must adhere to these five quality invariants:

1. **Negative Scope Boundary ("What this is not yet"):**  
   Every early-stage document (Spark, Ideation, Charter) MUST explicitly declare what is intentionally excluded and deferred to downstream stages. Never collapse architecture or implementation details into an intent document.
2. **Problem-Before-Solution Discipline:**  
   Articulate the mechanical friction and organizational failure mode in concrete, unsanitized terms before introducing the capability or technical premise.
3. **Standardized PMBOK 8 / IPO Frontmatter:**  
   Every generated governance document must begin with YAML frontmatter specifying: `pmbok_edition`, `pmbok_process_group`, `pmbok_process`, `lifecycle_stage`, `governance_policy`, `inputs`, `process`, and `outputs`.
4. **Non-Duplication Principle:**  
   Never re-derive or restate the reasoning of an upstream document. ADR cites Charter/Pillars; BRD cites ADR; FDD cites BRD; Stories cite FDD; PMP subsidiary plans ingest User Story work packages.
5. **No Template Clutter:**  
   Clean up blank `*.template.md` files upon creating target documents to maintain a pristine, production-grade project documentation tree.

---

## 7. The chain's known, real, open ends

21. **Observation → Insight → Lesson Learned is a cross-project concern, not a per-project one to rebuild.** SocialEngage's own `resolve-kb-conflict` lives under a shared knowledge-base-ingestor agent, not under the project's own governance namespace. If a project has access to a shared knowledge base, integrate with it; don't build a project-local copy of this stage without evidence the shared one doesn't fit.
22. **Adaptation → Intent Refinement remains uncovered everywhere, including in the most mature real precedent.** No project in this methodology's real history has a working shape for "did an accepted change actually change behavior, and should that refine the original Intent/Hypothesis." Don't invent one here — watch for a real first case, the same discipline every other policy in this chain was built by.
