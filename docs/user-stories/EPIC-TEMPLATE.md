# Epic <N>: <Title>

**Source ADR:** [ADR-<NNN>](../07-architecture/ADR-<NNN>-<slug>.md)
**Source BRD/FDD:** [BRD-<NNN>](../project-docs/Business-Requirements/BRD-<NNN>-<slug>.md) / [FDD-<NNN>](../project-docs/Functional-Design/FDD-<NNN>-<slug>.md)

## Story <N>.1 — <title>

**Status:** Ready (not yet run through `implement-story`) — or Blocked, naming the real blocker
**As** <role>, **I want** <capability>, **so that** <reason>.

**Acceptance Criteria:**
- $AC_0$: <concrete, contract-testable condition>

## If this epic has zero code-shaped stories

That's a valid, correct output — not a gap. State why plainly (cite the FDD section that explains it), the same way the source projects' own Epic-3-equivalent does. Do not invent a story to fill this template.

## Before running `implement-story` on any story here

Run `validate-intent-foundation` first (see `docs/policy-shapes/validate-intent-foundation.json`) — document approval and pipeline-entry readiness are different questions. Record the real recommendation and the real human sign-off in this story's own Status line once it clears, the same way the source projects do.
