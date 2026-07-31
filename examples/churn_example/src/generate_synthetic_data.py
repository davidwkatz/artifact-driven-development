#!/usr/bin/env python3
"""Generate a small, reproducible set of raw churn-example tables."""

from __future__ import annotations

import argparse
import csv
import random
import sys
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    raise SystemExit(
        "PyYAML is required. Install it with: python3 -m pip install pyyaml"
    )


INDUSTRIES = [
    "software",
    "professional_services",
    "retail",
    "healthcare",
    "manufacturing",
    "education",
]

MEANINGFUL_EVENTS = [
    "login",
    "project_created",
    "project_edited",
    "report_run",
    "data_exported",
    "user_invited",
]

NON_MEANINGFUL_EVENTS = [
    "marketing_email_opened",
    "invoice_received",
    "documentation_viewed",
]

EMPLOYEE_RANGES = {
    "small": (2, 49),
    "mid_market": (50, 499),
    "enterprise": (500, 5000),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/synthetic_data.yaml")
    parser.add_argument("--output", default="data/raw")
    return parser.parse_args()


def load_config(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    required = {
        "random_seed",
        "num_customers",
        "start_date",
        "end_date",
        "segments",
        "regions",
    }
    missing = required - set(config or {})
    if missing:
        raise ValueError(f"Missing configuration keys: {sorted(missing)}")

    weight = sum(
        float(settings["weight"])
        for settings in config["segments"].values()
    )
    if abs(weight - 1.0) > 0.0001:
        raise ValueError("Segment weights must sum to 1.0")

    return config


def choose(rng: random.Random, values: dict[str, Any]) -> str:
    names = list(values)
    weights = [float(values[name]["weight"]) for name in names]
    return rng.choices(names, weights=weights, k=1)[0]


def random_date(rng: random.Random, start: date, end: date) -> date:
    return start + timedelta(days=rng.randint(0, (end - start).days))


def timestamp(rng: random.Random, day: date) -> str:
    value = datetime.combine(day, time.min, tzinfo=timezone.utc)
    value += timedelta(seconds=rng.randint(0, 86_399))
    return value.isoformat().replace("+00:00", "Z")


def write_csv(
    output_dir: Path,
    filename: str,
    fields: list[str],
    rows: list[dict[str, Any]],
) -> None:
    with (output_dir / filename).open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def generate(config: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    rng = random.Random(int(config["random_seed"]))
    start = date.fromisoformat(str(config["start_date"]))
    end = date.fromisoformat(str(config["end_date"]))

    rows: dict[str, list[dict[str, Any]]] = {
        "customers": [],
        "subscriptions": [],
        "activity_events": [],
        "support_tickets": [],
        "payments": [],
    }
    event_id = ticket_id = payment_id = 0

    for number in range(1, int(config["num_customers"]) + 1):
        customer_id = f"cust_{number:06d}"
        segment = choose(rng, config["segments"])
        settings = config["segments"][segment]

        signup = random_date(rng, start, end - timedelta(days=90))
        churned = rng.random() < float(settings["churn_rate"])
        churn_date = (
            random_date(rng, signup + timedelta(days=90), end)
            if churned
            else None
        )
        explicit_cancellation = churned and rng.random() < 0.5
        active_end = churn_date if explicit_cancellation else end

        employee_min, employee_max = EMPLOYEE_RANGES[segment]
        rows["customers"].append(
            {
                "customer_id": customer_id,
                "signup_date": signup.isoformat(),
                "segment": segment,
                "region": rng.choice(config["regions"]),
                "employee_count": rng.randint(employee_min, employee_max),
                "industry": rng.choice(INDUSTRIES),
            }
        )

        rows["subscriptions"].append(
            {
                "subscription_id": f"sub_{number:06d}",
                "customer_id": customer_id,
                "plan": settings["plan"],
                "monthly_price": f"{float(settings['monthly_price']):.2f}",
                "start_date": signup.isoformat(),
                "status": "cancelled" if explicit_cancellation else "active",
                "cancellation_date": (
                    churn_date.isoformat() if explicit_cancellation else ""
                ),
            }
        )

        # Generate a modest number of activity events. Churned customers
        # become less active near churn, creating a useful but imperfect signal.
        active_days = max((active_end - signup).days, 1)
        event_count = max(1, int(active_days / rng.randint(12, 30)))
        if churned:
            event_count = max(1, event_count // 2)

        for _ in range(event_count):
            event_id += 1
            event_day = random_date(rng, signup, active_end)
            meaningful = rng.random() < (0.70 if churned else 0.90)
            event_types = (
                MEANINGFUL_EVENTS if meaningful else NON_MEANINGFUL_EVENTS
            )
            rows["activity_events"].append(
                {
                    "event_id": f"evt_{event_id:08d}",
                    "customer_id": customer_id,
                    "event_time": timestamp(rng, event_day),
                    "event_type": rng.choice(event_types),
                    "meaningful": str(meaningful).lower(),
                }
            )

        # Most customers have no support ticket; churned customers are likelier
        # to have one and to report lower satisfaction.
        ticket_probability = 0.35 if churned else 0.12
        if rng.random() < ticket_probability:
            ticket_id += 1
            opened = random_date(rng, signup, active_end)
            closed = min(opened + timedelta(days=rng.randint(1, 10)), end)
            rows["support_tickets"].append(
                {
                    "ticket_id": f"ticket_{ticket_id:07d}",
                    "customer_id": customer_id,
                    "opened_at": timestamp(rng, opened),
                    "closed_at": timestamp(rng, closed),
                    "priority": rng.choice(
                        ["medium", "high"] if churned else ["low", "medium"]
                    ),
                    "category": rng.choice(
                        ["billing", "technical", "account", "integration"]
                    ),
                    "satisfaction_score": (
                        ""
                        if rng.random() < 0.2
                        else rng.randint(1, 3)
                        if churned
                        else rng.randint(3, 5)
                    ),
                }
            )

        # One payment approximately every 30 days.
        payment_day = signup
        while payment_day <= active_end:
            payment_id += 1
            failed = rng.random() < (0.08 if churned else 0.02)
            rows["payments"].append(
                {
                    "payment_id": f"pay_{payment_id:08d}",
                    "customer_id": customer_id,
                    "payment_date": payment_day.isoformat(),
                    "amount": f"{float(settings['monthly_price']):.2f}",
                    "status": "failed" if failed else "paid",
                }
            )
            payment_day += timedelta(days=30)

    return rows


def write_outputs(
    output_dir: Path,
    rows: dict[str, list[dict[str, Any]]],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    schemas = {
        "customers": [
            "customer_id",
            "signup_date",
            "segment",
            "region",
            "employee_count",
            "industry",
        ],
        "subscriptions": [
            "subscription_id",
            "customer_id",
            "plan",
            "monthly_price",
            "start_date",
            "status",
            "cancellation_date",
        ],
        "activity_events": [
            "event_id",
            "customer_id",
            "event_time",
            "event_type",
            "meaningful",
        ],
        "support_tickets": [
            "ticket_id",
            "customer_id",
            "opened_at",
            "closed_at",
            "priority",
            "category",
            "satisfaction_score",
        ],
        "payments": [
            "payment_id",
            "customer_id",
            "payment_date",
            "amount",
            "status",
        ],
    }
    for name, fields in schemas.items():
        write_csv(output_dir, f"{name}.csv", fields, rows[name])


def main() -> int:
    args = parse_args()
    project_dir = Path(__file__).resolve().parent.parent
    config_path = Path(args.config)
    output_dir = Path(args.output)
    if not config_path.is_absolute():
        config_path = project_dir / config_path
    if not output_dir.is_absolute():
        output_dir = project_dir / output_dir

    try:
        config = load_config(config_path)
        rows = generate(config)
        write_outputs(output_dir, rows)
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"Generation failed: {error}", file=sys.stderr)
        return 1

    print(f"Wrote synthetic data to {output_dir}")
    for name, values in rows.items():
        print(f"- {name}.csv: {len(values):,} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
