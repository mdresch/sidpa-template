"""
Initialize a new project from sidpa-template.

Usage:
    # Initialize in-place (inside a cloned sidpa-template repo):
    python scripts/init_project.py --name my-project

    # Initialize / scaffold into an existing repository or target directory:
    python scripts/init_project.py --name enterprise-work-hierarchy --target-dir /path/to/existing-repo

Actions performed:
1. When --target-dir is provided, copies pmbok/, scripts/, docs/, .claude/skills/, and
   data/agent-learning/ from sidpa-template into the target repository without clobbering
   existing project files.
2. Renames active-policies/template-governance/ -> <name>-governance/
3. Renames policies/template-governance/ -> <name>-governance/
4. Updates agent_id: "template-governance" to "<name>-governance" in all policy JSONs.
5. Leaves agent-learning-governance unchanged (shared global namespace).
6. Copies *.template.md files to active *.md documents if they do not already exist.
7. Cleans up redundant *.template.md files to eliminate clutter (pass --keep-templates to preserve).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

source_repo_root = Path(__file__).resolve().parent.parent

def copy_tree_merge(src: Path, dst: Path, overwrite: bool = False):
    """Recursively copy directory tree merging into destination."""
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            copy_tree_merge(item, target, overwrite=overwrite)
        else:
            if not target.exists() or overwrite:
                shutil.copy2(item, target)

def init_project(
    project_name: str,
    target_dir: Path | None = None,
    create_docs: bool = True,
    force: bool = False,
    cleanup_templates: bool = True
):
    # Sanitize project name
    clean_name = re.sub(r"[^a-zA-Z0-9_\-]", "-", project_name).lower().strip("-")
    new_agent_id = f"{clean_name}-governance"
    old_agent_id = "template-governance"

    dest_root = target_dir.resolve() if target_dir else source_repo_root

    print(f"\n=======================================================")
    print(f"  SIDPA Project Initializer")
    print(f"  Project Name: {clean_name}")
    print(f"  Governance Agent ID: {new_agent_id}")
    print(f"  Source Root: {source_repo_root}")
    print(f"  Target Root: {dest_root}")
    print(f"=======================================================\n")

    # Step A: If target_dir is different from template root, scaffold files
    if dest_root != source_repo_root:
        print("  [STEP 1/4] Scaffolding governance structure into target repository...")
        
        # 1. PMBOK engine
        copy_tree_merge(source_repo_root / "pmbok", dest_root / "pmbok", overwrite=force)
        print("    [+] Scaffolding pmbok/ planning engine")

        # 2. Scripts
        (dest_root / "scripts").mkdir(parents=True, exist_ok=True)
        for s in (source_repo_root / "scripts").glob("*.py"):
            target_script = dest_root / "scripts" / s.name
            if not target_script.exists() or force:
                shutil.copy2(s, target_script)
        print("    [+] Scaffolding scripts/ (init_project.py, orchestrate_pmbok.py)")

        # 3. Docs & templates
        copy_tree_merge(source_repo_root / "docs", dest_root / "docs", overwrite=force)
        print("    [+] Scaffolding docs/ (governance chain, templates, policy-shapes)")

        # 4. Agent Learning policies
        copy_tree_merge(
            source_repo_root / "data" / "agent-learning",
            dest_root / "data" / "agent-learning",
            overwrite=force
        )
        print("    [+] Scaffolding data/agent-learning/store/ (policy definitions)")

        # 5. Claude Skills (merging into existing .claude/skills)
        if (source_repo_root / ".claude" / "skills").exists():
            copy_tree_merge(
                source_repo_root / ".claude" / "skills",
                dest_root / ".claude" / "skills",
                overwrite=force
            )
            print("    [+] Merging .claude/skills/ (governance, pmbok-planning, intent-refinement)")

    else:
        print("  [STEP 1/4] Operating in-place on template repository.")

    # Step B: Rename policy folders to project governance agent ID
    print("\n  [STEP 2/4] Configuring project-specific Bayesian policy store...")
    store_dir = dest_root / "data" / "agent-learning" / "store"
    active_dir = store_dir / "active-policies"
    policies_dir = store_dir / "policies"

    old_active = active_dir / old_agent_id
    new_active = active_dir / new_agent_id
    if old_active.exists():
        if new_active.exists() and new_active != old_active:
            shutil.rmtree(new_active)
        old_active.rename(new_active)
        print(f"    [OK] Renamed active policies directory: {new_active.relative_to(dest_root)}")
    elif new_active.exists():
        print(f"    [OK] Active policies directory already configured: {new_active.relative_to(dest_root)}")

    old_policies = policies_dir / old_agent_id
    new_policies = policies_dir / new_agent_id
    if old_policies.exists():
        if new_policies.exists() and new_policies != old_policies:
            shutil.rmtree(new_policies)
        old_policies.rename(new_policies)
        print(f"    [OK] Renamed policy definitions directory: {new_policies.relative_to(dest_root)}")
    elif new_policies.exists():
        print(f"    [OK] Policy definitions directory already configured: {new_policies.relative_to(dest_root)}")

    # Step C: Update agent_id in JSON policy files
    print("\n  [STEP 3/4] Updating agent_id references in policy declarations...")
    updated_files = 0
    for target_dir in [new_active, new_policies]:
        if not target_dir.exists():
            continue
        for json_file in target_dir.glob("*.json"):
            try:
                content = json_file.read_text(encoding="utf-8")
                if old_agent_id in content:
                    updated = content.replace(f'"{old_agent_id}"', f'"{new_agent_id}"')
                    json_file.write_text(updated, encoding="utf-8")
                    updated_files += 1
            except Exception as e:
                print(f"    [WARN] Failed updating {json_file.name}: {e}")

    print(f"    [OK] Updated agent_id in {updated_files} policy file(s).")

    # Step D: Copy template documents to active .md documents if requested
    print("\n  [STEP 4/4] Instantiating project governance documents from templates...")
    if create_docs:
        docs_created = 0
        for template_file in dest_root.glob("docs/**/*.template.md"):
            dest_name = template_file.name.replace(".template.md", ".md")
            dest_file = template_file.parent / dest_name
            if not dest_file.exists():
                shutil.copy2(template_file, dest_file)
                docs_created += 1
                print(f"    [OK] Created document: {dest_file.relative_to(dest_root)}")
            else:
                print(f"    [SKIP] Document already exists: {dest_file.relative_to(dest_root)}")

        print(f"    [OK] Generated {docs_created} initial project document(s) from templates.")

        # Step E: Cleanup redundant .template.md files
        if cleanup_templates:
            cleaned = 0
            for template_file in dest_root.glob("docs/**/*.template.md"):
                try:
                    template_file.unlink()
                    cleaned += 1
                except Exception as e:
                    print(f"    [WARN] Could not remove {template_file.name}: {e}")
            if cleaned > 0:
                print(f"    [OK] Cleaned up {cleaned} redundant .template.md file(s) to eliminate clutter.")

    print(f"\n=======================================================")
    print(f"  SIDPA Project Initialization Complete!")
    print(f"  Target: {dest_root}")
    print(f"  Governance Agent ID: '{new_agent_id}'")
    print(f"  Next Step: Author Spark-Capture.md and Ideation-Document.md")
    print(f"=======================================================\n")

def main():
    parser = argparse.ArgumentParser(description="Initialize or scaffold a project with SIDPA governance")
    parser.add_argument("--name", required=True, help="Project name (e.g. 'enterprise-work-hierarchy')")
    parser.add_argument("--target-dir", default=None, help="Target repository directory (default: current template repo)")
    parser.add_argument("--skip-docs", action="store_true", help="Skip copying .template.md files to active .md files")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files in target directory")
    parser.add_argument("--keep-templates", action="store_true", help="Keep redundant .template.md files after creating active .md files")
    args = parser.parse_args()

    target = Path(args.target_dir) if args.target_dir else None
    init_project(
        args.name,
        target_dir=target,
        create_docs=not args.skip_docs,
        force=args.force,
        cleanup_templates=not args.keep_templates
    )

if __name__ == "__main__":
    main()
