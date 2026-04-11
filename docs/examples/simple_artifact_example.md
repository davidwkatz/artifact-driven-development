# A Small Concrete Example

This is a minimal example of artifact-driven development.

Suppose a data workflow starts with raw observational data and produces a summary.

## Conventional version

In a conventional implementation, the important structure may be mostly implicit:

- a script cleans duplicates
- another step normalizes timestamps
- feature extraction happens next
- a summary table is produced
- the reason for the ordering lives only in code or chat history

A reader may be able to reconstruct the workflow, but only with effort.

## More artifact-driven version

Instead, make the important intermediate structure explicit.

Artifacts:

- `raw.observations`
- `semantic.v_observations_clean`
- `feature.entity_feature_timespan`
- `summary.feature_counts`

One simple dependency chain:

    raw.observations
      -> semantic.v_observations_clean
      -> feature.entity_feature_timespan
      -> summary.feature_counts

Now add one decision artifact:

- `decision.cleaning_before_feature_extraction`

That artifact records that duplicate cleaning happens before feature extraction, and why.

## Why this helps

This is not just better documentation.

It makes important project structure easier to inspect and reuse.

A human can see what exists and how outputs are formed.  
An AI system can focus on a few relevant artifacts instead of reconstructing everything from a mass of files and history.

## Minimal vocabulary in this example

- **Operational artifacts**: `raw.observations`, `semantic.v_observations_clean`, `feature.entity_feature_timespan`, `summary.feature_counts`
- **Decision artifact**: `decision.cleaning_before_feature_extraction`
- **Dependency structure**: each artifact depends on the one before it

This is a small example, but it already shows the basic move:

make important project structure explicit.
