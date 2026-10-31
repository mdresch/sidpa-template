from pathlib import Path

import pytest

from scripts.init_management_plan_foundations import initialize_foundation_packs


TEMPLATE_ROOT = (
    Path(__file__).resolve().parents[1]
    / "templates"
    / "management-plans"
)


def _project_root(tmp_path: Path) -> Path:
    (tmp_path / "docs").mkdir()
    return tmp_path


def test_initializes_all_packs_and_renders_project_tokens(tmp_path: Path) -> None:
    target_root = _project_root(tmp_path)

    created, skipped = initialize_foundation_packs(
        target_root,
        "Example Project",
        template_root=TEMPLATE_ROOT,
    )

    generated = list(
        (target_root / "docs" / "project-docs" / "management-plans").rglob("*.md")
    )
    assert (created, skipped) == (31, 0)
    assert len(generated) == 31
    assert all("{{" not in path.read_text(encoding="utf-8") for path in generated)
    assert all(".template.md" not in path.read_text(encoding="utf-8") for path in generated)
    manifest = (
        target_root
        / "docs"
        / "project-docs"
        / "management-plans"
        / "scope-baseline"
        / "Scope-Foundation-Pack-Manifest.md"
    )
    assert manifest.is_file()
    assert "Project: **Example Project**" in manifest.read_text(encoding="utf-8")
    assert "(foundation/Scope-Pillar-Overview-and-Trace.md)" in manifest.read_text(
        encoding="utf-8"
    )


def test_preserves_existing_artifacts_and_is_idempotent(tmp_path: Path) -> None:
    target_root = _project_root(tmp_path)
    initialize_foundation_packs(target_root, "mxc", template_root=TEMPLATE_ROOT)
    manifest = (
        target_root
        / "docs"
        / "project-docs"
        / "management-plans"
        / "scope-baseline"
        / "Scope-Foundation-Pack-Manifest.md"
    )
    manifest.write_text("project-authored content\n", encoding="utf-8")

    created, skipped = initialize_foundation_packs(
        target_root,
        "mxc",
        template_root=TEMPLATE_ROOT,
    )

    assert (created, skipped) == (0, 31)
    assert manifest.read_text(encoding="utf-8") == "project-authored content\n"


def test_initializes_only_selected_pack(tmp_path: Path) -> None:
    target_root = _project_root(tmp_path)

    created, skipped = initialize_foundation_packs(
        target_root,
        "mxc",
        packs=("scope",),
        template_root=TEMPLATE_ROOT,
    )

    assert (created, skipped) == (7, 0)
    assert len(
        list(
            (
                target_root
                / "docs"
                / "project-docs"
                / "management-plans"
                / "scope-baseline"
            ).rglob("*.md")
        )
    ) == 7


def test_rejects_missing_docs_directory(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="no docs directory"):
        initialize_foundation_packs(tmp_path, "mxc", template_root=TEMPLATE_ROOT)


def test_rejects_unknown_pack(tmp_path: Path) -> None:
    target_root = _project_root(tmp_path)

    with pytest.raises(ValueError, match="Unknown management-plan pack"):
        initialize_foundation_packs(
            target_root,
            "mxc",
            packs=("risk",),
            template_root=TEMPLATE_ROOT,
        )
