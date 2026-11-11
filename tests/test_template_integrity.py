"""Integrity checks for the SIDPA template itself.

The template stores only template values. These tests keep it that way:
the plan skeletons follow the ADR-012 content contract, their dependency
graph is a DAG rooted at Scope, no project-specific artifacts are stored,
and scripts/init_project.py scaffolds a working project.
"""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / "docs" / "project-docs" / "management-plans"
DOMAINS = {"Governance", "Scope", "Schedule", "Finance", "Stakeholders", "Resources", "Risk"}
REQUIRED_KEYS = [
    "plan_id", "plan_name", "pmbok_edition", "pmbok_focus_area", "primary_pmbok_domain",
    "secondary_pmbok_domains", "legacy_process", "route", "generator", "version", "baseline_id",
    "cycle_id", "owner_role", "depends_on", "inputs", "outputs", "governance_policy",
]
HEADINGS = [
    r"^##\s+1\.\s+Intent,\s+Alignment\s+&\s+Boundaries",
    r"^##\s+2\.\s+Domain\s+Mechanics\s+&\s+Standards",
    r"^##\s+3\.\s+Governance,\s+Control\s+&\s+Decision\s+Rights",
]
WORD = re.compile(r"\b[^\W_]+(?:['’][^\W_]+)?\b")


def split_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """Parse the flat-key, string-list frontmatter subset without PyYAML."""
    text = text.replace("\r\n", "\n").lstrip("﻿")
    assert text.startswith("---\n"), "missing opening frontmatter delimiter"
    head, _, body = text[4:].partition("\n---\n")
    data: dict[str, object] = {}
    key = None
    for raw in head.split("\n"):
        line = re.sub(r"\s+#.*$", "", raw) if not raw.lstrip().startswith("-") else re.sub(r'(?<=")\s+#.*$', "", raw)
        if not line.strip():
            continue
        if line.startswith("  - "):
            assert key is not None
            assert isinstance(data[key], list)
            data[key].append(line[4:].strip().strip('"'))
            continue
        name, _, value = line.partition(":")
        key = name.strip()
        assert re.fullmatch(r"[a-z_]+", key), f"bad key {key!r}"
        assert key not in data, f"duplicate key {key}"
        value = value.strip()
        data[key] = [] if value in ("", "[]") else value.strip('"')
    return data, body


def plan_templates() -> list[Path]:
    return sorted(PLANS.glob("*.template.md"))


def test_there_are_nine_plan_skeletons() -> None:
    assert len(plan_templates()) == 9


@pytest.mark.parametrize("path", plan_templates(), ids=lambda p: p.stem)
def test_plan_skeleton_follows_the_content_contract(path: Path) -> None:
    data, body = split_frontmatter(path.read_text(encoding="utf-8"))
    for key in REQUIRED_KEYS:
        assert key in data, f"{path.name} lacks {key}"
    assert data["primary_pmbok_domain"] in DOMAINS
    assert set(data["secondary_pmbok_domains"]) <= DOMAINS
    assert data["route"] in {"full_plan", "pmp_section", "not_applicable"}
    assert data["generator"] in {"llm", "human", "stub", "mock"}
    assert data["generator"] not in {"stub", "mock"}, "a skeleton must not be marked stub or mock"
    assert re.fullmatch(r"CYC-\d{3,}", str(data["cycle_id"]))
    for pattern in HEADINGS:
        assert re.search(pattern, body, re.M), f"{path.name} lacks heading {pattern}"
    assert not re.search(r"\[(TBD|TODO|Insert here)\]", path.read_text(encoding="utf-8"), re.I)
    assert "Stub content for Artifact" not in body


def test_dependencies_form_a_dag_rooted_at_scope() -> None:
    graph = {}
    for path in plan_templates():
        data, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        graph[str(data["plan_id"])] = list(data["depends_on"])
    assert graph["scope-management"] == []
    assert set(pid for pid, deps in graph.items() if not deps) == {"scope-management"}
    for pid, deps in graph.items():
        assert set(deps) <= set(graph), f"{pid} depends on an unknown plan"
    visiting: set[str] = set()
    done: set[str] = set()

    def visit(node: str) -> None:
        assert node not in visiting, f"cycle through {node}"
        if node in done:
            return
        visiting.add(node)
        for dep in graph[node]:
            visit(dep)
        visiting.discard(node)
        done.add(node)

    for pid in graph:
        visit(pid)


def test_tier_one_plans_have_the_stricter_floors() -> None:
    def floor_line(plan: str) -> str:
        return next(
            (
                line for line in (PLANS / f"{plan}.template.md").read_text(encoding="utf-8").split("\n")
                if line.startswith("Word count")
            ),
            "",
        )

    for plan in ("Scope-Management-Plan", "Schedule-Management-Plan", "Cost-Management-Plan"):
        assert "pmp_section 180 to 750" in floor_line(plan)
        assert "full_plan 700 to 4500" in floor_line(plan)


def test_template_stores_no_project_specific_artifacts() -> None:
    assert not (ROOT / "pmbok").exists()
    assert not (ROOT / "scripts" / "orchestrate_pmbok.py").exists()
    assert not (ROOT / "docs" / "project-docs" / "Project-Management-Plan.md").exists()
    assert all(p.name.endswith(".template.md") for p in PLANS.glob("*.md"))
    frames = ROOT / "docs" / "policy-shapes" / "decision-frames"
    assert sorted(p.name for p in frames.iterdir()) == ["README.md", "approve-adr.frame.template.json"]
    assert not (ROOT / "docs" / "policy-shapes" / "episodes").exists()


def test_policy_shapes_and_frame_template_are_valid_json() -> None:
    for path in (ROOT / "docs" / "policy-shapes").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    frame = json.loads((ROOT / "docs/policy-shapes/decision-frames/approve-adr.frame.template.json").read_text(encoding="utf-8"))
    assert {o["action_id"] for o in frame["options"]} == {"approve_adr", "reject_adr", "request_revision_before_decision"}
    assert len(frame["criteria"]) == 4


def test_governed_templates_carry_baseline_and_cycle_ids() -> None:
    for rel in (
        "docs/07-architecture/ADR-TEMPLATE.md",
        "docs/project-docs/Business-Requirements/BRD-TEMPLATE.md",
        "docs/project-docs/Functional-Design/FDD-TEMPLATE.md",
        "docs/user-stories/EPIC-TEMPLATE.md",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert 'baseline_id: "<target-baseline-id>"' in text, rel
        assert 'cycle_id: "CYC-001"' in text, rel
        assert "pmp_baseline" not in text, rel


@pytest.fixture()
def scratch_copy(tmp_path: Path) -> Path:
    dest = tmp_path / "project"
    shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(".git", ".hypothesis", ".pytest_cache", "__pycache__"))
    return dest


def load_init(project: Path):
    spec = importlib.util.spec_from_file_location("init_project_under_test", project / "scripts" / "init_project.py")
    assert spec is not None and spec.loader is not None, f"Could not create import spec for {project / 'scripts' / 'init_project.py'}"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_init_start_stage_scaffolds_documents_and_opens_the_first_cycle(scratch_copy: Path) -> None:
    init = load_init(scratch_copy)
    init.init_project("My Demo App", stage="start")
    register = (scratch_copy / "docs/registers/Cycle-Register.md").read_text(encoding="utf-8")
    assert "CYC-001 | OPEN" in register
    assert "<date the project starts>" not in register
    assert "My Demo App" in register
    assert (scratch_copy / "docs/project-docs/Project-Charter.md").exists()
    assert (scratch_copy / "docs/registers/Methodology-Best-Practice-Ledger.md").exists()
    assert not (scratch_copy / "docs/project-docs/management-plans/Scope-Management-Plan.md").exists()
    ideation = (scratch_copy / "docs/project-docs/Ideation-Document.md").read_text(encoding="utf-8")
    assert "HYP-my-demo-app-001" in ideation
    store = scratch_copy / "data/agent-learning/store/policies"
    assert (store / "my-demo-app-governance").exists()
    assert not (store / "template-governance").exists()
    assert (store / "agent-learning-governance").exists()


def test_init_plans_stage_creates_the_nine_plans_and_never_overwrites(scratch_copy: Path) -> None:
    init = load_init(scratch_copy)
    init.init_project("demo", stage="plans")
    plans = sorted((scratch_copy / "docs/project-docs/management-plans").glob("*-Plan.md"))
    assert len(plans) == 9
    scope = scratch_copy / "docs/project-docs/management-plans/Scope-Management-Plan.md"
    scope.write_text("edited by a human", encoding="utf-8")
    init.init_project("demo", stage="plans")
    assert scope.read_text(encoding="utf-8") == "edited by a human"


def test_init_rejects_an_empty_project_name(scratch_copy: Path) -> None:
    init = load_init(scratch_copy)
    with pytest.raises(SystemExit):
        init.init_project("---", stage="start")


# --- learning methodologies: catalog, tailoring matrix, ledger template -------------------------------

METHODOLOGIES = ROOT / "docs" / "methodologies"
CLASSES = {"runnable", "proof_of_concept", "documented"}
RUNNABLE_STATES = {"implemented", "example_only", "partial", "practiced"}


def test_methodology_catalog_has_32_entries_with_consistent_classes() -> None:
    catalog = json.loads((METHODOLOGIES / "catalog.json").read_text(encoding="utf-8"))
    assert sorted(entry["id"] for entry in catalog) == list(range(1, 33))
    for entry in catalog:
        label = f"#{entry['id']}"
        assert entry["example_class"] in CLASSES, label
        if entry["state"] in RUNNABLE_STATES:
            assert entry["example_class"] == "runnable", label
        elif entry["state"] == "candidate" and entry.get("adr"):
            assert entry["example_class"] == "proof_of_concept", label
        else:
            assert entry["example_class"] == "documented", label
        if entry["example_class"] == "documented":
            assert entry.get("reason", "").strip() and entry.get("reopening_condition", "").strip(), label
            assert entry.get("path") is None, label
        else:
            assert str(entry.get("path", "")).startswith("examples/methodologies/"), label


def test_tailoring_matrix_rows_are_all_hypotheses_over_existing_catalog_ids() -> None:
    ids = {entry["id"] for entry in json.loads((METHODOLOGIES / "catalog.json").read_text(encoding="utf-8"))}
    rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in (METHODOLOGIES / "Tailoring-Matrix.md").read_text(encoding="utf-8").splitlines()
        if line.startswith("| ") and not line.startswith("| Need") and not line.startswith("|---")
    ]
    assert len(rows) == 6
    for row in rows:
        assert len(row) == 7, row
        assert row[1] in {"store", "lessons-learned"}, row
        assert {int(n) for n in re.findall(r"#(\d+)", row[2])} <= ids, row
        assert row[4], row
        assert row[6] == "hypothesis", row


def test_ledger_template_ships_no_entries_and_no_adopted_practice() -> None:
    text = (ROOT / "docs" / "registers" / "Methodology-Best-Practice-Ledger.template.md").read_text(encoding="utf-8")
    assert not re.search(r"^## BP-\d{3}", text, re.MULTILINE)
    assert "status: adopted" not in text
    assert "real-episodes" in text
