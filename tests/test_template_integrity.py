"""
Template integrity and lifecycle sequence tests for SIDPA template.

Enforces:
1. Stage 6: Requirements (ADRs, BRDs, FDDs, User Stories)
2. Stage 7: Integrated PMP & 9 Subsidiary Management Plans (PMP-BL-v1.0.0, Foundation Packs 7.A-7.D)
3. Stage 8: Implementation Readiness Gate & Implementation Authorization Notice
4. Valid JSON structure across all policy declarations and decision frames
"""

from __future__ import annotations

import json
import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

NINE_PLANS = [
    "Scope-Management-Plan.md",
    "Schedule-Management-Plan.md",
    "Cost-Management-Plan.md",
    "Resource-Management-Plan.md",
    "Quality-Management-Plan.md",
    "Communications-Management-Plan.md",
    "Risk-Management-Plan.md",
    "Procurement-Management-Plan.md",
    "Stakeholder-Engagement-Plan.md",
]


def test_there_are_nine_subsidiary_plans() -> None:
    plans_dir = REPO_ROOT / "docs" / "project-docs" / "management-plans"
    assert plans_dir.is_dir()
    for plan_name in NINE_PLANS:
        plan_path = plans_dir / plan_name
        assert plan_path.is_file(), f"Missing subsidiary plan: {plan_name}"
        content = plan_path.read_text(encoding="utf-8")
        assert 'lifecycle_stage: "Stage 7 (Planning: Integrated PMP & Baselines)"' in content, (
            f"{plan_name} does not reflect Stage 7 lifecycle stage"
        )


def test_project_management_plan_has_stage_7_frontmatter() -> None:
    for filename in ["Project-Management-Plan.template.md", "Project-Management-Plan.md"]:
        path = REPO_ROOT / "docs" / "project-docs" / filename
        assert path.is_file(), f"Missing {filename}"
        content = path.read_text(encoding="utf-8")
        assert 'lifecycle_stage: "Stage 7 (Planning: Integrated PMP & Baselines)"' in content, (
            f"{filename} does not reflect Stage 7 lifecycle stage"
        )
        assert 'pmbok_process: "4.2 Develop Project Management Plan"' in content


def test_requirements_templates_have_stage_6_frontmatter() -> None:
    req_templates = [
        (REPO_ROOT / "docs" / "07-architecture" / "ADR-TEMPLATE.md", "Stage 6 (Requirement: Architecture)"),
        (REPO_ROOT / "docs" / "project-docs" / "Business-Requirements" / "BRD-TEMPLATE.md", "Stage 6 (Requirement: Business)"),
        (REPO_ROOT / "docs" / "project-docs" / "Functional-Design" / "FDD-TEMPLATE.md", "Stage 6 (Requirement: Solution)"),
        (REPO_ROOT / "docs" / "user-stories" / "EPIC-TEMPLATE.md", "Stage 6 (Requirement: Story)"),
    ]
    for path, expected_stage in req_templates:
        assert path.is_file(), f"Missing {path}"
        content = path.read_text(encoding="utf-8")
        assert f'lifecycle_stage: "{expected_stage}"' in content, (
            f"{path.name} does not declare {expected_stage}"
        )


def test_stage_8_authorization_notice_templates_exist() -> None:
    reports_dir = REPO_ROOT / "docs" / "project-docs" / "Status-Reports"
    assert reports_dir.is_dir()

    template_notice = reports_dir / "Stage-8-Implementation-Authorization-Notice.template.md"
    active_notice = reports_dir / "Stage-8-Implementation-Authorization-Notice.md"

    assert template_notice.is_file(), "Missing Stage 8 notice template"
    assert active_notice.is_file(), "Missing Stage 8 active notice document"

    for path in [template_notice, active_notice]:
        content = path.read_text(encoding="utf-8")
        assert 'artifact_type: "execution_authorization_notice"' in content
        assert "Stage 8 (Implementation Readiness Gate" in content
        assert "AUTHORIZED_TO_EXECUTE" in content


def test_foundation_packs_have_stage_7_manifests() -> None:
    pack_checks = [
        ("scope-baseline", "Scope-Foundation-Pack-Manifest.template.md", "Stage 7.A"),
        ("schedule-baseline", "Schedule-Foundation-Pack-Manifest.template.md", "Stage 7.B"),
        ("resource-baseline", "Resource-Foundation-Pack-Manifest.template.md", "Stage 7.C"),
        ("cost-baseline", "Cost-Foundation-Pack-Manifest.template.md", "Stage 7.D"),
    ]
    for pack_dir, manifest_name, expected_stage in pack_checks:
        path = REPO_ROOT / "templates" / "management-plans" / pack_dir / manifest_name
        assert path.is_file(), f"Missing {path}"
        content = path.read_text(encoding="utf-8")
        assert f"## {expected_stage} process" in content, (
            f"{manifest_name} does not reference {expected_stage}"
        )


def test_policy_shapes_and_frames_are_valid_json() -> None:
    policy_dir = REPO_ROOT / "docs" / "policy-shapes"
    assert policy_dir.is_dir()
    json_files = list(policy_dir.rglob("*.json"))
    assert len(json_files) >= 10, "Found fewer policy JSON files than expected"
    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
            assert isinstance(data, (dict, list)), f"{jf.name} did not load as dict or list"
        except Exception as e:
            pytest.fail(f"Invalid JSON in {jf}: {e}")
