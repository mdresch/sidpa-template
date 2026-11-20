"""One-shot sync: agent-learning Stage-*-Methodology.md → sidpa-template docs/methodology/*.template.md."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

DEFAULT_SOURCE = (
    Path(os.environ["AGENT_LEARNING_METHODOLOGY_DIR"]).expanduser()
    if os.environ.get("AGENT_LEARNING_METHODOLOGY_DIR")
    else Path(__file__).resolve().parents[2] / "agent-learning" / "docs" / "project-docs" / "Methodology"
)
SOURCE = DEFAULT_SOURCE
TARGET = Path(__file__).resolve().parents[1] / "docs" / "methodology"

SLUGS: dict[int, str] = {
    1: "Intent",
    2: "Hypothesis",
    3: "Benefit",
    4: "Objective",
    5: "Pillars-and-Architecture",
    6: "Requirement",
    7: "Project-PMP-and-Baselines",
    8: "Implementation-Readiness",
    9: "Deliverable",
    10: "Verification-Evidence",
    11: "Audit-Record",
    12: "Actual-Outcome",
    13: "Observation",
    14: "Insight",
    15: "Lesson-Learned",
    16: "Governance-Change",
    17: "Adaptation-Plan",
    18: "Intent-Refinement",
}

SOURCE_NAMES: dict[int, str] = {
    15: "Stage-15-Lesson-Learned-Methodology.md",
    18: "Stage-18-Intent-Refinement-Methodology.md",
}

IPO_BLURBS: dict[int, str] = {
    1: "Inputs: Trigger event / strategic driver. Process: Validate intent. Output: Approved Ideation.",
    2: "Inputs: Design assumptions & test logs. Process: Evaluate empirical evidence. Output: Validated / testing status.",
    3: "Inputs: Hypotheses & ROI premise. Process: Validate economics. Output: Benefits artifacts (Charter inputs).",
    4: "Inputs: Business Case & Benefits. Process: Authorize project & assign sponsor. Output: Project Charter.",
    5: "Inputs: Charter & initiating artifacts. Process: Decompose into pillars; draft ADRs. Output: Approved pillars & ADRs.",
    6: "Inputs: Approved Pillars & Architecture. Process: BRD, FDD, and user stories. Output: Approved technical requirements.",
    7: "Inputs: Stage 6 requirements and foundation packs. Process: Integrate subsidiary plans. Output: Approved PMP baseline.",
    8: "Inputs: Approved stories & PMP. Process: Reconcile traceability before build. Output: Implementation authorization.",
    9: "Inputs: Approved stories & ACs. Process: TDD / contract-first build. Output: Executable deliverable.",
    10: "Inputs: Code deliverable & contract tests. Process: Execute test suite. Output: Verification evidence.",
    11: "Inputs: Deliverables & verification logs. Process: Audit architectural conformance. Output: Audit register entries.",
    12: "Inputs: Telemetry & Benefits Statement. Process: Compare realized vs expected. Output: Impact deltas.",
    13: "Inputs: Runtime telemetry & findings. Process: Record raw facts. Output: Observation log (§3.2).",
    14: "Inputs: Observation logs. Process: Synthesize causal significance. Output: Resolved insight node (§3.2).",
    15: "Inputs: Verified insights. Process: Crystallize actionable knowledge. Output: Lessons Learned register (§3.2).",
    16: "Inputs: Lessons & proposed diffs. Process: Classify & escalate. Output: Governed baseline update.",
    17: "Inputs: Validated Stage 16 change & outcomes. Process: Tailor PMP via impact matrix. Output: Impacted plan list.",
    18: "Inputs: Stage 17 adaptations & phase review. Process: Strategic review of intent. Output: Catalyst for Phase N+1 Spark.",
}

REPLACEMENTS = [
    (r"intent-to-outcome-chain-coverage\.md", "chain-coverage.md"),
    (r"Menno Drescher", "<project maintainer>"),
    (r"`scripts/stage16_amend\.py`", "`(stage16_amend tooling when IMP-062 lands)`"),
    (r"uv run python scripts/stage16_amend\.py", "(stage16_amend propose/accept when available)"),
    (r"scripts/orchestrate_pmbok\.py", "(project phase-close / seed tooling — not shipped in sidpa-template)"),
    (r"from pmbok\.models", "(legacy pmbok models — not in template)"),
    (r"tests/pmbok/", "tests/ (project-specific) "),
    (r"../../intent-to-outcome-chain-coverage.md", "../../chain-coverage.md"),
    (r"../intent-to-outcome-chain-coverage.md", "../chain-coverage.md"),
    (r"\../../chain-coverage\.md", "../chain-coverage.md"),
    (r"Authority in this repository:", "Authority in the project:"),
    (r"\*\*This repository has", "**This project has"),
    (r"this repository's", "the project's"),
    (r"In this repository", "In the project"),
]

KEEP_THROUGH_SECTION_2 = {15, 16, 17, 18}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return "", text
    return m.group(1), text[m.end() :]


def normalize_frontmatter(raw: str, stage: int, body: str) -> str:
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip().strip('"')
    stage_name = fields.get("stage_name") or SLUGS[stage].replace("-", " ")
    if stage == 15 and "stage_name" not in fields:
        stage_name = "Lesson Learned"
    gov = fields.get("governance_policy", "")
    if stage == 15 and not gov:
        gov = "resolve-kb-conflict (reference shape; human_review until initialized)"
    if stage == 14 and not gov:
        gov = "resolve-kb-conflict (reference shape; see chain-coverage §3.2)"
    lines = [
        "---",
        'artifact_type: "methodology_guide"',
        f'stage: "{stage}"',
        f'stage_name: "{stage_name}"',
        f'pmbok_process: "{fields.get("pmbok_process", "")}"',
        'version: "1.0"',
        'date: ""',
        'owner: "<project maintainer>"',
    ]
    if gov:
        lines.append(f'governance_policy: "{gov}"')
    lines.append("---")
    return "\n".join(lines)


def remove_current_instance(body: str) -> str:
    patterns = [
        r"\n## 3\. Current Instance.*?(?=\n## [45]\.|\Z)",
        r"\n## 3\. Current Instance.*?(?=\n## Change Log|\Z)",
    ]
    for pat in patterns:
        body = re.sub(pat, "\n", body, flags=re.S)
    return body


def remove_change_log(body: str) -> str:
    body = re.sub(r"\n## Change Log.*", "", body, flags=re.S)
    body = re.sub(r"\n## 📝 Appendix:.*", "", body, flags=re.S)
    return body


def strip_phase1_examples_stage15(body: str) -> str:
    body = re.sub(
        r"\*\*Input Requirements \(Phase 1.*?(?=\n---\n\n### Step 2:)",
        "",
        body,
        flags=re.S,
    )
    body = re.sub(
        r"\*\*Example \(LL-044\):\*\*.*?```\n",
        "",
        body,
        flags=re.S,
    )
    body = body.replace("## 📚 Overview", "## 1. Overview")
    body = body.replace("## 🎯 Step-by-Step Stage 15 Process", "## 2. Process")
    body = re.sub(r"## [📊🎓🔗📝🎯🔄📚].*", "", body, flags=re.S)
    return body


def _find_heading_outside_fences(text: str, heading_pattern: str) -> int | None:
    """Return char index of the first line matching heading_pattern outside fenced code blocks."""
    compiled = re.compile(heading_pattern)
    in_fence = False
    fence_char = ""
    fence_len = 0
    offset = 0
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        fence_match = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len and stripped[len(marker) :].strip() == "":
                in_fence = False
        elif not in_fence and compiled.match(line):
            return offset
        offset += len(line)
    return None


def truncate_after_section_2(body: str, stage: int) -> str:
    start = _find_heading_outside_fences(body, r"^## 2\. ")
    if start is None:
        start = _find_heading_outside_fences(body, r"^## 2\. Process")
    if start is None:
        return body
    rest = body[start:]
    cut = _find_heading_outside_fences(rest, r"^## 3\. ")
    if cut is not None:
        rest = rest[:cut]
    pitfall = _find_heading_outside_fences(body, r"^## [58]\. Common Pitfalls")
    refs = _find_heading_outside_fences(body, r"^## [69]\. References")
    suffix = ""
    if pitfall is not None and refs is not None:
        next_sec = _find_heading_outside_fences(body[refs:], r"^## 1[01]\.")
        chunk_end = refs + next_sec if next_sec is not None else len(body)
        chunk = body[pitfall:chunk_end]
        chunk = re.sub(r"## 8\. Common Pitfalls", "## 5. Common Pitfalls", chunk)
        chunk = re.sub(r"## 9\. References", "## 6. References", chunk)
        chunk = re.sub(r"### 9\.", "###", chunk)
        chunk = re.sub(r"### 8\.", "###", chunk)
        suffix = "\n\n---\n\n" + chunk.strip() + "\n"
    elif stage == 16:
        suffix = (
            "\n\n---\n\n## 5. Common Pitfalls\n\n"
            "See `.claude/skills/governance/SKILL.md` and `docs/chain-coverage.md` §3.1–§3.2.\n\n"
            "## 6. References\n\n"
            "- [Chain coverage](../chain-coverage.md)\n"
            "- [Sequence and lessons](../sequence-and-lessons.md)\n"
            "- [Governance skill](../../.claude/skills/governance/SKILL.md)\n"
        )
    return body[:start] + rest.rstrip() + suffix


def shrink_large_fences(text: str, max_lines: int = 45) -> str:
    def repl(m: re.Match[str]) -> str:
        block = m.group(0)
        if block.count("\n") <= max_lines:
            return block
        lang = m.group(1) or ""
        return f"```{lang}\n# (Extended template omitted — port detail from agent-learning when instantiating.)\n```"

    return re.sub(r"```(\w*)\n.*?```", repl, text, flags=re.S)


def ensure_ipo_blockquote(body: str, stage: int) -> str:
    blurb = IPO_BLURBS.get(stage, "")
    if not blurb or "> **Lifecycle IPO:**" in body:
        return body
    title_m = re.search(r"^# .+$", body, re.M)
    if not title_m:
        return body
    insert = f"\n> **Lifecycle IPO (template):** {blurb}\n"
    after = body.find("\n>", title_m.end())
    if after == -1:
        return body[: title_m.end()] + insert + body[title_m.end() :]
    return body[:after] + insert + body[after:]


def fix_title(body: str, stage: int) -> str:
    name = SLUGS[stage].replace("-", " ")
    if stage == 5:
        name = "Pillars & Architecture"
    elif stage == 15:
        name = "Lesson Learned"
    elif stage == 18:
        name = "Intent Refinement"
    elif stage == 16:
        if body.startswith("# Stage 16: Governance Change Methodology"):
            body = body.replace(
                "# Stage 16: Governance Change Methodology",
                "# Stage 16: Governance Change — Methodology Guide",
                1,
            )
            return body
    elif stage == 17:
        body = body.replace(
            "# Stage 17: Adaptation Plan Methodology",
            "# Stage 17: Adaptation Plan — Methodology Guide",
            1,
        )
        return body
    body = re.sub(
        rf"^# Stage {stage}:.*$",
        f"# Stage {stage}: {name} — Methodology Guide",
        body,
        count=1,
        flags=re.M,
    )
    if stage == 15:
        body = body.replace(
            "# Stage 15: Lesson Learned - Complete Methodology Guide",
            "# Stage 15: Lesson Learned — Methodology Guide",
            1,
        )
    return body


def cross_link_stage_refs(body: str) -> str:
    for n, slug in SLUGS.items():
        body = re.sub(
            rf"\(\./Stage-{n}-[A-Za-z0-9-]+\.md\)",
            f"(Stage-{n:02d}-{slug}-Methodology.template.md)",
            body,
        )
    return body


def templify_stage(stage: int) -> str:
    if stage in SOURCE_NAMES:
        path = SOURCE / SOURCE_NAMES[stage]
    else:
        candidates = sorted(SOURCE.glob(f"Stage-{stage}-*.md"))
        if not candidates:
            raise FileNotFoundError(f"No source for stage {stage}")
        path = candidates[0]
    text = path.read_text(encoding="utf-8")
    raw_fm, body = split_frontmatter(text)
    fm = normalize_frontmatter(raw_fm, stage, body)
    body = remove_current_instance(body)
    body = remove_change_log(body)
    if stage == 15:
        body = strip_phase1_examples_stage15(body)
    for old, new in REPLACEMENTS:
        body = re.sub(old, new, body)
    if stage in KEEP_THROUGH_SECTION_2:
        body = truncate_after_section_2(body, stage)
    if stage == 16:
        body = re.sub(
            r"\*\*BRP Template:\*\*.*?(?=\n### Step 7:)",
            "**BRP Template:** use your project's BRP artifact pattern; full example lives in agent-learning.\n\n---\n\n",
            body,
            flags=re.S,
        )
        body = re.sub(
            r"\*\*SPA Template:\*\*.*?(?=\n---\n\n### Step 7:|\n### Step 7:)",
            "**SPA Template:** use subsidiary-plan amendment pattern from Stage 17.\n\n---\n\n",
            body,
            flags=re.S,
        )
    if stage == 17:
        body = re.sub(
            r"\*\*Inventory for Current Stage:\*\*.*?(?=\n---\n\n### Step 3:)",
            "",
            body,
            flags=re.S,
        )
    body = shrink_large_fences(body, max_lines=40)
    body = ensure_ipo_blockquote(body, stage)
    body = fix_title(body, stage)
    body = cross_link_stage_refs(body)
    body = body.strip() + "\n"
    return fm + "\n\n" + body


def main() -> None:
    global SOURCE
    parser = argparse.ArgumentParser(
        description="Sync Stage-*-Methodology.md from agent-learning into docs/methodology/*.template.md."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="Path to agent-learning Methodology directory (or set AGENT_LEARNING_METHODOLOGY_DIR).",
    )
    args = parser.parse_args()
    SOURCE = args.source.expanduser().resolve()
    if not SOURCE.is_dir():
        raise FileNotFoundError(
            f"Methodology source directory not found: {SOURCE}. "
            "Pass --source <path> or set AGENT_LEARNING_METHODOLOGY_DIR."
        )
    obsolete = [
        "Stage-14-Reflection-Methodology.template.md",
        "Stage-15-Learning-Object-Methodology.template.md",
        "Stage-18-Phase-Close-Methodology.template.md",
    ]
    for name in obsolete:
        p = TARGET / name
        if p.exists():
            p.unlink()
    for stage, slug in SLUGS.items():
        out = TARGET / f"Stage-{stage:02d}-{slug}-Methodology.template.md"
        out.write_text(templify_stage(stage), encoding="utf-8")
        print("wrote", out.name, "lines", len(out.read_text(encoding="utf-8").splitlines()))


if __name__ == "__main__":
    main()