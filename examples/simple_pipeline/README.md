# Simple Pipeline Example

This example shows how a small workflow can be represented using explicit artifacts.

The goal is not complexity, but clarity.

---

## Overview

The pipeline consists of a sequence of transformations:

* `raw_events`
* `deduplicated_events`
* `normalized_events`
* `feature_table`
* `summary_table`

Each step produces a new artifact derived from previous ones.

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

Derives features from normalized data.

### summary_table

Produces a summary grouped by `event_type`.

---

## Files

* `artifacts.yaml` describes the artifacts and their dependencies.
* `pipeline.sql` shows one simple way to derive the artifacts from the CSV files.
* The CSV files are small example artifacts that can be inspected directly.

---

## Running the example

Run the SQL using DuckDB from this directory:

```bash
cd examples/simple_pipeline
duckdb :memory: < pipeline.sql
```

The SQL uses relative paths, so it must be run from this directory.

---

## How to read this example

1. Inspect the CSV files to understand the data at each step.
2. Review `artifacts.yaml` to see how artifacts depend on each other.
3. Read `pipeline.sql` to see one possible implementation of those transformations.

---

## Why this example matters

This example demonstrates:

* how intermediate results can be made explicit
* how dependencies can be represented clearly
* how documentation and data can align

This is the core idea behind artifact-driven development.


