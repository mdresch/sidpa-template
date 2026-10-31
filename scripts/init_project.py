"""
Initialize a new project from sidpa-template.

Usage:
    python scripts/init_project.py --name my-project

Actions performed:
1. Resolves the real agent-learning store root the same way the `agent-learn`
   CLI does (AGENT_LEARNING_LOCAL_STORE_DIR env var, falling back to this
   repo's local data/agent-learning/store/) -- NOT always this repo's own
   data/ folder. A machine can have that env var pointing at a different,
   shared store (e.g. another project's data/agent-learning/store/), and the
   CLI only ever reads/writes there.
2. If a `template-governance` agent already exists in that store, renames it
   to `<name>-governance` (local, first-time-only path).
3. Otherwise (the common case once the store is shared across projects),
   initializes a brand-new `<name>-governance` policy directly in that store
   via `agent-learn task-policy-init`, one call per policy shape under
   docs/policy-shapes/*.actions.json -- so the learners are live and
   decidable the moment this script finishes, not just the moment someone
   remembers to run a second setup step.
4. Leaves agent-learning-governance unchanged (shared global namespace).
5. Copies *.template.md files to active *.md documents if they do not already exist.
6. Initializes the four management-plan foundation packs without overwriting existing files.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent


def resolve_store_dir() -> Path:
    """Resolve the agent-learning store root the same way the `agent-learn`
    CLI does, so policies land where the CLI will actually find them."""
    env_dir = os.environ.get("AGENT_LEARNING_LOCAL_STORE_DIR")
    if env_dir:
        return Path(env_dir)
    return repo_root / "data" / "agent-learning" / "store"


def init_policy_via_cli(agent_id: str, task_id: str, actions_file: Path) -> bool:
    """Create a fresh task policy directly through the agent-learn CLI so it
    is initialized wherever the CLI's own store resolution actually points."""
    try:
        with actions_file.open(encoding="utf-8") as f:
            actions = json.load(f)
        decision_context = (
            actions[0]["description"] if actions and "description" in actions[0]
            else f"Governs the {task_id} decision."
        )
        result = subprocess.run(
            [
                "agent-learn", "task-policy-init",
                "--agent-id", agent_id,
                "--task-id", task_id,
                "--decision-context", decision_context,
                "--actions", str(actions_file),
            ],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"  [WARN] task-policy-init failed for {task_id}: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"  [WARN] task-policy-init raised for {task_id}: {e}")
        return False


def init_project(project_name: str, create_docs: bool = True):
    # Sanitize project name
    clean_name = re.sub(r"[^a-zA-Z0-9_\-]", "-", project_name).lower().strip("-")
    new_agent_id = f"{clean_name}-governance"
    old_agent_id = "template-governance"

    print(f"\n=======================================================")
    print(f"  SIDPA Project Initializer")
    print(f"  Project Name: {clean_name}")
    print(f"  New Governance Agent ID: {new_agent_id}")
    print(f"=======================================================\n")

    store_dir = resolve_store_dir()
    print(f"  Resolved agent-learning store: {store_dir}")
    active_dir = store_dir / "active-policies"
    policies_dir = store_dir / "policies"

    old_active = active_dir / old_agent_id
    new_active = active_dir / new_agent_id
    old_policies = policies_dir / old_agent_id
    new_policies = policies_dir / new_agent_id

    if old_active.exists() or old_policies.exists():
        # First-time path: a pristine template-governance identity exists in
        # this store -- rename it in place.
        if old_active.exists():
            if new_active.exists():
                shutil.rmtree(new_active)
            old_active.rename(new_active)
            print(f"  [OK] Renamed active policies directory: {new_active}")

        if old_policies.exists():
            if new_policies.exists():
                shutil.rmtree(new_policies)
            old_policies.rename(new_policies)
            print(f"  [OK] Renamed policy definitions directory: {new_policies}")

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
                    print(f"  [WARN] Failed updating {json_file.name}: {e}")

        print(f"  [OK] Updated agent_id in {updated_files} policy file(s).")
    else:
        # Common path once the store is shared/external: there is no local
        # template-governance to rename. Initialize each policy fresh,
        # directly through the CLI, so the learners can be run immediately.
        print(f"  No 'template-governance' identity found in this store -- "
              f"initializing '{new_agent_id}' policies directly via agent-learn.")
        shape_files = sorted(repo_root.glob("docs/policy-shapes/*.actions.json"))
        initialized, skipped = 0, 0
        for shape_file in shape_files:
            task_id = shape_file.name.split(".")[0]
            if ".ALTERNATE-NOT-INITIALIZED." in shape_file.name:
                skipped += 1
                continue
            if init_policy_via_cli(new_agent_id, task_id, shape_file):
                print(f"  [OK] Initialized policy: {task_id}")
                initialized += 1
            else:
                skipped += 1
        print(f"  [OK] Initialized {initialized} policy/policies via agent-learn "
              f"({skipped} skipped).")

    # Copy template documents to active .md documents if requested
    if create_docs:
        docs_created = 0
        for template_file in repo_root.glob("docs/**/*.template.md"):
            # Target path replaces .template.md with .md
            dest_name = template_file.name.replace(".template.md", ".md")
            dest_file = template_file.parent / dest_name
            if not dest_file.exists():
                shutil.copy2(template_file, dest_file)
                docs_created += 1
                print(f"  [OK] Created document: {dest_file.relative_to(repo_root)}")
            else:
                print(f"  [SKIP] Document already exists: {dest_file.relative_to(repo_root)}")

        print(f"  [OK] Generated {docs_created} initial project document(s) from templates.")

        subprocess.run(
            [
                sys.executable,
                str(repo_root / "scripts" / "init_management_plan_foundations.py"),
                "--target-root",
                str(repo_root),
                "--project-name",
                clean_name,
            ],
            check=True,
        )

    print(f"\nProject initialization complete! You can now start with Step 2 (Spark & Ideation).")
    print(f"To run governance decisions, use agent-id: '{new_agent_id}'\n")

def main():
    parser = argparse.ArgumentParser(description="Initialize a new project from sidpa-template")
    parser.add_argument("--name", required=True, help="New project name (e.g. 'my-awesome-app')")
    parser.add_argument(
        "--skip-docs",
        action="store_true",
        help="Skip instantiating document and management-plan foundation templates",
    )
    args = parser.parse_args()

    init_project(args.name, create_docs=not args.skip_docs)

if __name__ == "__main__":
    main()
