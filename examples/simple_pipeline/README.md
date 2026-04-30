# Simple Pipeline Example

This example makes a small artifact pipeline concrete.

Pipeline:

- `raw_events.csv`
- `deduplicated_events.csv`
- `normalized_events.csv`
- `feature_table.csv`
- `summary_table.csv`

The example is intentionally tiny. Its purpose is not to model a production workflow, but to show how a sequence of explicit artifacts can make intermediate structure visible and reusable.

## Artifact roles

- `raw_events.csv`  
  Base loaded data, including duplicates and inconsistent formatting.

- `deduplicated_events.csv`  
  Exact duplicate rows removed.

- `normalized_events.csv`  
  Cleaned version with standardized categorical values.

- `feature_table.csv`  
  Per-entity derived features.

- `summary_table.csv`  
  A downstream summary built from the normalized data.

## Why this example is useful

This small pipeline helps clarify what artifact-driven development means in practice:

- intermediate products are explicit
- each artifact has a distinct role
- decisions such as where deduplication belongs can be discussed against concrete artifacts
- small context packets can be assembled from named files instead of vague descriptions
