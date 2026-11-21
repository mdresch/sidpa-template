"""Export a thin, non-duplicating 5-field Portfolio Rollup from Project-Status-Register.md.

Designed for graduated Track B SIDPA repositories reporting macro progress back to an
upstream portfolio funnel (for example, an opportunities register) without duplicating
ADRs, stories, subsidiary plans, gate JSONs, or execution queues.

Usage:
    python scripts/export_portfolio_rollup.py
    python scripts/export_portfolio_rollup.py --format json
    python scripts/export_portfolio_rollup.py --repo /path/to/repo --opportunity-id OP-ITG-017
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date
from pathlib import Path


def _git(repo: Path, *args: str) -> str:
    try:
        res = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            check=True,
        )
        return res.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def _parse_kv_table(section_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in section_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].startswith("---") or cells[0].lower() == "field":
            continue
        key = re.sub(r"\*+", "", cells[0]).strip()
        key = re.sub(r"\s*\(.*?\)\s*$", "", key).strip()
        out[key.lower()] = cells[1].strip()
    return out


def _extract_section(text: str, heading_prefix: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading_prefix)}\s+.*$", re.M)
    m = pattern.search(text)
    if not m:
        return ""
    rest = text[m.end() :]
    nxt = re.search(r"^##\s+\d+\.", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def _parse_epic_progress(section_text: str) -> tuple[int, int, int, int]:
    """Return (epics_complete, epics_total, stories_done, stories_total) from Section 3."""
    epics_complete = 0
    epics_total = 0
    stories_done = 0
    stories_total = 0
    for line in section_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0].startswith("---") or cells[0].lower() == "epic":
            continue
        if cells[0].startswith("*("):
            continue
        epics_total += 1
        if "complete" in cells[3].lower():
            epics_complete += 1
        m = re.search(r"(\d+)\s*/\s*(\d+)", cells[4])
        if m:
            stories_done += int(m.group(1))
            stories_total += int(m.group(2))
    return epics_complete, epics_total, stories_done, stories_total


def build_rollup(
    repo: Path,
    status_file: Path,
    opportunity_id: str | None = None,
    portfolio_repo: str | None = None,
    commercial_status: str | None = None,
    git_ref: str | None = None,
) -> dict[str, object]:
    if git_ref:
        rel = status_file.relative_to(repo).as_posix()
        text = _git(repo, "show", f"{git_ref}:{rel}")
        if not text:
            raise FileNotFoundError(f"Could not read {rel} from git ref {git_ref} in {repo}")
        branch = git_ref
        commit = _git(repo, "rev-parse", "--short", git_ref)
    else:
        if not status_file.is_file():
            raise FileNotFoundError(f"Project status register not found: {status_file}")
        text = status_file.read_text(encoding="utf-8")
        branch = _git(repo, "rev-parse", "--abbrev-ref", "HEAD")
        commit = _git(repo, "rev-parse", "--short", "HEAD")

    remote_url = _git(repo, "remote", "get-url", "origin")
    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]

    sec1 = _parse_kv_table(_extract_section(text, "1."))
    sec3 = _extract_section(text, "3.")
    sec5 = _parse_kv_table(_extract_section(text, "5."))

    epics_done, epics_total, stories_done, stories_total = _parse_epic_progress(sec3)

    macro_stage = sec1.get("current macro stage", "Unknown")
    baseline = sec1.get("current pmp baseline", "Unbaselined")
    phase = sec1.get("current phase", "")
    next_unit = sec1.get("next epic/unit of work to implement", "")

    op_id = opportunity_id or sec5.get("opportunity id", "<opportunity-id>")
    up_repo = portfolio_repo or sec5.get("upstream portfolio repo", "<portfolio-repo>")
    comm_status = commercial_status or sec5.get(
        "commercial / pilot status",
        "Track B technical build active; commercial pilot status governed in upstream portfolio",
    )
    sync_trigger = sec5.get(
        "next rollup sync trigger",
        "Macro gate crossing only (Stage 8 auth, Phase/Epic completion / Stage 11 Audit, Stage 12/18 close)",
    )

    progress_parts: list[str] = []
    if epics_total:
        progress_parts.append(f"{epics_done}/{epics_total} Epics")
    if stories_total:
        progress_parts.append(f"{stories_done}/{stories_total} stories")
    coarse_progress = " · ".join(progress_parts) if progress_parts else "No epics tracked yet"

    return {
        "as_of": date.today().isoformat(),
        "opportunity_id": op_id,
        "upstream_portfolio_repo": up_repo,
        "graduated_repo_url": remote_url or str(repo),
        "ssot_register": "docs/registers/Project-Status-Register.md",
        "branch": branch,
        "commit": commit,
        "phase": phase,
        "pmp_baseline": baseline,
        "macro_stage": macro_stage,
        "coarse_delivery_progress": coarse_progress,
        "next_unit": next_unit,
        "commercial_pilot_status": comm_status,
        "next_sync_trigger": sync_trigger,
    }


def format_markdown(rollup: dict[str, object]) -> str:
    repo_ref = f"`{rollup['graduated_repo_url']}` (`{rollup['branch']}` @ `{rollup['commit']}`)"
    return "\n".join(
        [
            "| Opportunity ID | Graduated Track B Repo (SSOT) | Macro Stage & Baseline | Coarse Delivery Progress | Commercial / Pilot Status | As Of |",
            "| --- | --- | --- | --- | --- | --- |",
            (
                f"| `{rollup['opportunity_id']}` | {repo_ref} → `{rollup['ssot_register']}` | "
                f"{rollup['macro_stage']} ({rollup['pmp_baseline']}) | "
                f"{rollup['coarse_delivery_progress']} | {rollup['commercial_pilot_status']} | {rollup['as_of']} |"
            ),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export a thin, non-duplicating 5-field Portfolio Rollup from Project-Status-Register.md."
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Path to the SIDPA repository root (defaults to this repository).",
    )
    parser.add_argument(
        "--status-file",
        type=Path,
        default=None,
        help="Path to Project-Status-Register.md (defaults to <repo>/docs/registers/Project-Status-Register.md).",
    )
    parser.add_argument("--ref", default=None, help="Optional git ref (e.g. origin/feat/hyperv-v2-rebased) to read from.")
    parser.add_argument("--opportunity-id", default=None, help="Override Opportunity ID (e.g. OP-ITG-017).")
    parser.add_argument("--portfolio-repo", default=None, help="Override upstream portfolio repository slug.")
    parser.add_argument("--commercial-status", default=None, help="Override commercial / pilot status note.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    args = parser.parse_args()

    repo = args.repo.expanduser().resolve()
    status_file = (
        args.status_file.expanduser().resolve()
        if args.status_file
        else repo / "docs" / "registers" / "Project-Status-Register.md"
    )
    rollup = build_rollup(
        repo=repo,
        status_file=status_file,
        opportunity_id=args.opportunity_id,
        portfolio_repo=args.portfolio_repo,
        commercial_status=args.commercial_status,
        git_ref=args.ref,
    )
    if args.format == "json":
        print(json.dumps(rollup, indent=2))
    else:
        print(format_markdown(rollup))


if __name__ == "__main__":
    main()
