# Context Selection Example

This example shows how artifact-driven development helps determine what context
to send to an LLM.

The goal is not to send the entire pipeline. The goal is to select the artifacts
needed to reason about a specific question.

## Question

Why does this pipeline perform duplicate removal before feature extraction?

## Task anchor

The task concerns the placement of duplicate removal relative to feature
extraction.

This points to the transition between raw input records, deduplicated records,
cleaned records, and downstream feature generation.

## Relevant artifact chain

The pipeline defines the following sequence of artifacts:

```text
raw_events
  -> deduplicated_events
  -> normalized_events
  -> feature_table
  -> summary_table
```
