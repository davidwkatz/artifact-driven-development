# Simple Pipeline Example

This example shows how a small workflow can be represented using explicit artifacts.

The goal is not complexity, but clarity.

---

## Overview

The pipeline consists of a small dependency graph:

```text
raw_events
  -> deduplicated_events
    -> normalized_events
      -> feature_table
      -> summary_table
```

Each step produces a named artifact derived from previous ones. The last two
artifacts both depend on `normalized_events`: `feature_table` summarizes by
entity, while `summary_table` summarizes by event type.

The dependencies between these artifacts are defined in:

* `artifacts.yaml`

---

## Artifacts

### raw_events

Original input data.

### deduplicated_events

Removes duplicate records from raw input.

### normalized_events

Applies normalization to fields or values.

### feature_table

Derives per-entity features from normalized data.

### summary_table

Produces a summary grouped by `event_type`.

---

g
## Files in this example

This example uses the same artifact names in two related ways.

`pipeline.sql` derives the artifact sequence as DuckDB views, starting from
`raw_events.csv`. The downstream CSV files (`deduplicated_events.csv`,
`normalized_events.csv`, `feature_table.csv`, and `summary_table.csv`) are
materialized snapshots of those same artifacts. They are included so the
intermediate outputs can be inspected directly without running the pipeline.

* `raw_events.csv` is the source input for the example pipeline.
* `pipeline.sql` derives the downstream artifacts as DuckDB views.
* `deduplicated_events.csv`, `normalized_events.csv`, `feature_table.csv`, and
  `summary_table.csv` are materialized snapshots / expected outputs.
* `artifacts.yaml` catalogs the artifact names, purposes, concrete CSV paths,
  and dependencies.
---

## Running the example

Run the SQL using DuckDB from this directory:

```bash
cd examples/simple_pipeline
duckdb :memory: < pipeline.sql
```

The SQL uses relative paths, so it must be run from this directory.

Expected row counts:

| artifact | n_rows |
| --- | ---: |
| `raw_events` | 8 |
| `deduplicated_events` | 6 |
| `normalized_events` | 6 |
| `feature_table` | 3 |
| `summary_table` | 3 |

---

## How to read this example

1. Inspect the CSV files to understand the data at each step.
2. Review `artifacts.yaml` to see how artifacts depend on each other.
3. Read `pipeline.sql` to see how the downstream artifacts are derived from `raw_events.csv`.

In this example the artifacts are DuckDB views for simplicity. In a larger pipeline,
expensive or frequently reused artifacts could be materialized as tables or files.
---

## Why this example matters

This example demonstrates:

* how intermediate results can be made explicit
* how dependencies can be represented clearly
* how documentation and data can align

This is the core idea behind artifact-driven development.
