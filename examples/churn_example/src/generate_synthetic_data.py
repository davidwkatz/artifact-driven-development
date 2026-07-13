#!/usr/bin/env python3

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print(
        "PyYAML is not installed. Install it with:\n"
        "python3 -m pip install pyyaml",
        file=sys.stderr,
    )
    raise SystemExit(1)

from pprint import pprint


def main() -> int:
    project_dir = Path(__file__).resolve().parent.parent
    config_path = project_dir / "config" / "synthetic_data.yaml"

    try:
        with config_path.open("r", encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Configuration file not found: {config_path}", file=sys.stderr)
        return 1
    except yaml.YAMLError as exc:
        print(f"Invalid YAML in {config_path}:\n{exc}", file=sys.stderr)
        return 1

    print("Synthetic data configuration:")
    pprint(config)
    print(yaml.safe_dump(config, sort_keys=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
