## Learned User Preferences

- Do not vend or maintain the full `agent-learning` codebase inside `sidpa-template`; that product stays in its own repository (a local clone under gitignored `agent-learning/` is only for comparison).
- Defer building a dedicated CLI for template-governance work until IMP-062 and IMP-007 are actually required; continue other templification without it first.

## Learned Workspace Facts

- `sidpa-template` is the project scaffold on GitHub (`mdresch/sidpa-template`); the primary integration branch is `master`.
- Root-level `agent-learning/` is listed in `.gitignore` for optional nested sibling clones and must not be committed as template content.
- Templified agent-learning governance in this repo lives under tracked paths such as `data/agent-learning/store/`, `docs/policy-shapes/`, gate scripts (`scripts/spec_gate.py`, `scripts/pr_gate.py`, etc.), and `.claude/skills/`—not under the gitignored root folder.
- Governance adoption means porting patterns into `.template.md` files, policy shapes, skills, and scripts—not copying filled agent-learning project instances (registers, episodes, amendment JSON, governance CR artifacts).
- The authoritative source for governance amendments to compare against is the standalone `agent-learning` repository (e.g. sibling checkout at `d:\Source\repos\agent-learning`), not the gitignored folder inside this workspace.
- Template integrity is validated with `python -m pytest tests/test_template_integrity.py` (and related governance tests).