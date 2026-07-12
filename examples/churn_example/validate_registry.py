#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print(
        "PyYAML is not installed.\n"
        "Install it with: python -m pip install pyyaml",
        file=sys.stderr,
    )
    raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and inspect the ADD artifact registry."
    )

    parser.add_argument(
        "--status",
        action="append",
        help=(
            "List artifacts with this status. "
            "May be supplied more than once, for example: "
            "--status planned --status stale"
        ),
    )

    parser.add_argument(
        "--list-statuses",
        action="store_true",
        help="List all statuses currently used in the registry.",
    )

    return parser.parse_args()


def load_registry(registry_path: Path) -> dict[str, Any]:
    with registry_path.open("r", encoding="utf-8") as handle:
        registry = yaml.safe_load(handle)

    if not isinstance(registry, dict):
        raise ValueError("The registry must contain a YAML mapping.")

    if "artifacts" not in registry:
        raise ValueError("The registry has no 'artifacts' section.")

    return registry


def artifact_exists(project_dir: Path, artifact: dict[str, Any]) -> bool:
    artifact_path = artifact.get("path")

    if not artifact_path:
        return False

    return (project_dir / artifact_path).exists()


def list_statuses(artifacts: list[dict[str, Any]]) -> None:
    statuses = sorted(
        {
            str(artifact.get("status", "unspecified"))
            for artifact in artifacts
        }
    )

    print("Statuses used in the registry:")

    for status in statuses:
        count = sum(
            artifact.get("status", "unspecified") == status
            for artifact in artifacts
        )
        print(f"- {status}: {count}")


def list_artifacts(
    artifacts: list[dict[str, Any]],
    selected_statuses: set[str],
    project_dir: Path,
) -> None:
    matches = [
        artifact
        for artifact in artifacts
        if artifact.get("status", "unspecified") in selected_statuses
    ]

    if not matches:
        statuses = ", ".join(sorted(selected_statuses))
        print(f"No artifacts found with status: {statuses}")
        return

    print("Matching artifacts:")

    for artifact in matches:
        artifact_id = artifact.get("id", "<missing id>")
        status = artifact.get("status", "unspecified")
        path = artifact.get("path", "<missing path>")
        exists = artifact_exists(project_dir, artifact)

        existence_label = "exists" if exists else "missing"

        print(
            f"- {artifact_id}: "
            f"status={status}, "
            f"path={path}, "
            f"file={existence_label}"
        )


def validate_registry(
    artifacts: list[dict[str, Any]],
    project_dir: Path,
) -> bool:
    errors: list[str] = []
    artifact_ids: set[str] = set()

    for artifact in artifacts:
        artifact_id = artifact.get("id")
        status = artifact.get("status")
        artifact_path = artifact.get("path")

        if not artifact_id:
            errors.append("An artifact is missing its 'id'.")
            continue

        if artifact_id in artifact_ids:
            errors.append(f"Duplicate artifact id: {artifact_id}")
        else:
            artifact_ids.add(artifact_id)

        if not status:
            errors.append(f"{artifact_id}: missing 'status'.")

        if not artifact_path:
            errors.append(f"{artifact_id}: missing 'path'.")
            continue

        # Planned artifacts are allowed to point to files that do not yet exist.
        if status != "planned" and not artifact_exists(project_dir, artifact):
            errors.append(
                f"{artifact_id}: status is '{status}', but path is missing: "
                f"{artifact_path}"
            )

    for artifact in artifacts:
        artifact_id = artifact.get("id", "<missing id>")

        for dependency in artifact.get("depends_on", []):
            if dependency not in artifact_ids:
                errors.append(
                    f"{artifact_id}: unknown dependency '{dependency}'."
                )

        for consumer in artifact.get("consumed_by", []):
            if consumer not in artifact_ids:
                errors.append(
                    f"{artifact_id}: unknown consumer '{consumer}'."
                )

    if errors:
        print("Registry validation failed:", file=sys.stderr)

        for error in errors:
            print(f"- {error}", file=sys.stderr)

        return False

    print("Registry validation passed.")
    return True


def main() -> int:
    args = parse_args()

    project_dir = Path(__file__).resolve().parent
    registry_path = project_dir / "artifacts.yaml"

    try:
        registry = load_registry(registry_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"Could not load registry: {exc}", file=sys.stderr)
        return 1

    artifacts = registry["artifacts"]

    if not isinstance(artifacts, list):
        print(
            "The 'artifacts' section must be a YAML list.",
            file=sys.stderr,
        )
        return 1

    print("Project:", registry.get("project", {}).get("name", "Unnamed project"))

    if args.list_statuses:
        list_statuses(artifacts)

    if args.status:
        list_artifacts(
            artifacts=artifacts,
            selected_statuses=set(args.status),
            project_dir=project_dir,
        )

    if not args.list_statuses and not args.status:
        return 0 if validate_registry(artifacts, project_dir) else 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
