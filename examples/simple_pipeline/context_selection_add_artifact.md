# Context Selection Example — Adding an Artifact

This example shows how artifact-driven development supports proposing a change
to a pipeline.

The goal is to determine where a new artifact should be introduced, and what
context an LLM needs to make that decision.

This is a hypothetical pre-change example: assume the current pipeline does not
yet include `deduplicated_events`.

## Question

Where should a `deduplicated_events` artifact be inserted in this pipeline?

## Task anchor

The task concerns introducing duplicate removal into an existing pipeline.

This requires identifying where duplicates originate and how they affect
downstream artifacts.

## Relevant artifact chain

The current pipeline defines the following sequence:

```text
raw_events
  -> normalized_events
  -> feature_table
  -> summary_table
```

There is no explicit deduplication step.

## Candidate artifacts

| Artifact | Why it may matter |
|---|---|
| `raw_events` | Source records where duplicate events may originate. |
| `normalized_events` | Cleaned semantic layer that currently assumes input quality. |
| `feature_table` | Feature extraction may be distorted by duplicate records. |
| `summary_table` | Downstream summary affected by earlier aggregation choices. |

## Selected context

Selected artifacts:

- `raw_events`
- `normalized_events`
- `feature_table`
- `summary_table`

## Selection reasoning

Duplicate events originate in the source artifact `raw_events`.

If duplicate removal is delayed until after feature extraction, the computed
features may reflect duplicate counts or repeated patterns, leading to
distorted results.

Therefore, the LLM must consider:

- the source artifact where duplicates appear
- the first downstream artifact (`normalized_events`)
- downstream artifacts (`feature_table`, `summary_table`) affected by the choice

This requires selecting both upstream and downstream artifacts around the
proposed insertion point.

## Proposed insertion

A new artifact should be introduced between `raw_events` and `normalized_events`:

```text
raw_events
  -> deduplicated_events
  -> normalized_events
  -> feature_table
  -> summary_table
```

## Context packet sketch

```text
Question:
Where should a deduplicated_events artifact be inserted in this pipeline?

Selected artifacts:
- raw_events
- normalized_events
- feature_table
- summary_table

Proposed artifact:
- deduplicated_events

Reason:
Duplicates originate in raw_events and would distort downstream features if not
removed early. Introducing deduplicated_events before normalized_events ensures
that all downstream artifacts operate on clean input.
```

## Demo

The companion script `context_selection_add_artifact_demo.py` simulates a
pre-change pipeline (without `deduplicated_events`) and prints a context packet.

Run:

```bash
cd examples/simple_pipeline
python3 context_selection_add_artifact_demo.py
```

The script prints a small context packet. To test the selection, give that packet
to an LLM along with the question and ask it to answer using only the packet.

For example:

```text
Use only the context packet below. Do not use prior conversation context or
assumptions about files not shown.

[PASTE CONTEXT PACKET HERE]

Answer the question using only this packet. If the packet is insufficient, say
what is missing.
```

## General lesson

Artifact-driven development supports not only understanding existing pipelines,
but also proposing changes to them.

A good context selection for this type of question should:

- include the source artifact where the issue originates
- include downstream artifacts affected by the decision
- include enough structure to identify a valid insertion point

The goal is not just to retrieve existing artifacts, but to support reasoning
about new artifacts and their placement in the workflow.
