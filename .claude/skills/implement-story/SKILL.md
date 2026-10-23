# Skill: implement-story (SIDPA template)

Generalized from two independently-converged real implementations (SocialEngage's original, ADPA's own adaptation of it). The loop itself transferred unchanged between those two; only a few concrete facts (base branch name, test-file location convention, isolation mechanism) turned out to be project-specific. **This file is the loop. Each new project confirms or corrects the project-specific facts on its own first real story, the same way ADPA did — do not assume this template's placeholder values are already correct for a new project.**

## Before first use: confirm, don't assume

- **Base branch name** for worktrees. (ADPA's real default branch was not `main` — confirmed the hard way, via a failed `git worktree add`.)
- **Isolation mechanism.** SocialEngage used per-run ephemeral database clones; ADPA used two persistent Docker containers instead (`*-test` ephemeral, `*-dev` persistent). Confirm what this project actually has before assuming either shape.
- **Contract file location convention.** SocialEngage used `contracts/epic-<N>/`; ADPA's real convention turned out to be `server/src/__tests__/modules/<module>/`. Check for an existing convention before inventing one.
- **Language and test runner.** The loop below is written Node/Jest-first (SocialEngage, ADPA). A Python/pytest project (agent-learning) uses a flat `tests/test_<module>.py`, runs through its own venv, and needs that venv set up in each new worktree.
- **Where contract fixtures live.** If contracts test against real artifacts (result files, sample documents), they must be **committed** under a stable path such as `tests/fixtures/<module>/`. Never the repo root, never untracked.
- **Whether a mechanical enforcement layer exists** (a pre-commit hook, a CI gate tying code changes to a contract). If none exists yet, say so explicitly in this file's own copy for the new project — it changes how load-bearing Step 3 below is (see `heal-contract-failure`'s own note on this).

## The loop — mandatory, in order, for every story

### 0. Worktree provisioning
```bash
git worktree add ../<project>-story-<X.Y> -b feat/story-<X.Y> <confirmed-base-branch>
cd ../<project>-story-<X.Y>
```
If the worktree doesn't inherit dependencies automatically (confirmed real issue: `git worktree add` doesn't install `node_modules`), fix that before Step 5, not after a confusing test-runner failure.

### 1. Ingest the specification pyramid & check scope
- **User Story** (wherever this project's epics live): confirm `Status: Ready`, never `Blocked`. Note Acceptance Criteria.
- **Source ADR**: read in full, including any amendment.
- **BRD**: business rules.
- **FDD**: technical schemas, error codes, prerequisite gates.

*Hierarchy rule:* ADR > BRD/FDD > User Story. If a story has **no** entry at this level at all — not even a Blocked one — that is itself a real finding (see "When Step 1 fails outright" below), not a reason to skip ahead.

### 2. State intent
```
Intent: Story <X.Y> — <title> (ADR-<NNN>)
Scope: touches <file list>
Contract to encode: <paraphrase of the Acceptance Criteria being tested>
Explicitly out of scope: <named adjacent work NOT touched this pass>
```

### 3. Write the contract (RED)
One test per Acceptance Criterion, header comment naming its Story and ADR. Confirm the project's real contract-location convention (see "Before first use" above) before writing the first one.

### 4. Derive or update the component `SKILL.md`
Governing ADRs/Stories, contract files, load-bearing constraints, real call-site relationships.

### 5. Implement (GREEN)
Minimal code only — no speculative generalization.

### 6. Validate
Run the story's contract, then its epic's contract suite.

### 7. Commit & log
`implementation-log.md`: one entry per completed story, append-only, never edited. If the implementation and its own log entry must be committed together before the commit's hash is known, use a `pending` placeholder, backfilled by whichever commit runs next (or by a pre-commit hook that resolves it automatically, if one exists — confirmed real in at least one of the two source projects).

### 8. Open a PR, don't merge directly
Direct-push-to-default-branch was tried once (ADPA's real Story 1.2) and found to bypass real branch-protection value, not just a compliance checkbox — PR review triggers scrutiny no local check can provide. Push the branch, open the PR, tear down the worktree only after it actually merges upstream.

## When Step 1 fails outright — not every "story" is code-shaped

Confirmed twice, independently, by actually running this loop rather than assuming: a story can turn out to have no code deliverable at all (an operational/data-verification exercise), or an *epic* can turn out to have zero story-shaped entries in it at all (every real decision in its source ADR was a convention for future work, not a current build target). Neither is a flaw in the loop — it's the loop correctly refusing to force a template onto work that doesn't have that shape. **Reclassify, don't force**: if the project has a Governance-Exercise-style register for "a real-world prerequisite check with no code deliverable," use it. If it doesn't yet, that absence is itself worth naming before inventing a lighter-weight story variant for a category of one.

## Before entering this loop at all: a real gate exists

`validate-intent-foundation` (see the template's policy shapes) decides whether an already-accepted ADR/BRD/FDD/Story chain is grounded enough to enter this loop in the first place — distinct from approving the *content* of those documents (that's `approve-adr`/`approve-brd`/`approve-fdd`/`approve-user-stories`'s job). Confirmed necessary the hard way: a learned, low-authority version of this gate hit a hard entropy ceiling on positive-only data and could never earn autonomy, no matter how much evidence accumulated — this is a `full`-authority, reasoned-per-instance decision, not something to default to a shortcut on.

## Lessons from agent-learning Story 5.1 (first Python run of this loop)

Story 5.1 ran this loop without the skill installed in the repo and drifted in four places. Each is now a rule above or below:

1. **Fixtures read from the untracked repo root** made the contract pass locally and fail on a clean clone. Verify the contract in a fresh `git clone` of the branch before opening the PR.
2. **Step 0 (worktree) skipped** and the branch cut in place. Not fatal on a solo repo, but it is how untracked clutter ended up in the same tree as the story.
3. **Step 4 (component `SKILL.md`) skipped.** With no mechanical layer, nothing caught it; it was backfilled later. Treat it as a Definition-of-done item, not a nicety.
4. **Log hash went stale after `git commit --amend`.** The `pending` backfill covers a *later* commit, not an amend. After any amend, re-read `git log -1` and fix the entry's hash.

Also: install this skill into the new project's `.claude/skills/` **before** its first story, not after.

## Definition of done

Contract exists and passes; epic's contract suite still passes; `SKILL.md` current; traceability (ADR/BRD/FDD/Story) still accurate; a real `implementation-log.md` entry exists, hash `pending` or resolved; contract fixtures are committed and the contract passes on a clean clone.
