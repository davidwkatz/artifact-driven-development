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

## Candidate artifacts

| Artifact | Why it may matter |
|---|---|
| `raw_events` | Source records where duplicate events may appear. |
| `deduplicated_events` | Direct representation of duplicate removal. |
| `normalized_events` | Cleaned semantic layer that depends on deduplication. |
| `feature_table` | Feature extraction depends on the cleaned event records. |
| `summary_table` | Downstream summary that may change if duplicates are handled differently. |

## Selected context

Selected artifacts:

- `deduplicated_events`
- `raw_events`
- `normalized_events`
- `feature_table`
- `summary_table`

## Selection reasoning

The most directly relevant artifact is `deduplicated_events`, because the
question concerns duplicate removal.

However, the question cannot be answered from `deduplicated_events` alone. The
decision affects downstream artifacts, especially `normalized_events` and
`feature_table`.

The upstream artifact `raw_events` is also relevant because duplicates originate
in the raw input.

Therefore, a good context packet should include the focal artifact together with
its nearby upstream and downstream artifacts.

## Context packet sketch

```text
Question:
Why does this pipeline perform duplicate removal before feature extraction?

Selected artifacts:
- raw_events
- deduplicated_events
- normalized_events
- feature_table
- summary_table

Reason:
The question concerns where duplicate removal belongs in the pipeline. The LLM
needs the source artifact, the deduplication artifact, the cleaned layer, and
the downstream feature artifacts in order to reason about the design choice.
```

## Demo

The companion script `context_selection_example_demo.py` reads `artifacts.yaml`,
scores the artifacts for this question, and prints a small context packet.

Run:

```bash
cd examples/simple_pipeline
python3 context_selection_example_demo.py
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

Artifact selection should not rely only on text similarity.

A good selection should:

- include the focal artifact(s)
- include immediate upstream and downstream dependencies
- include artifacts needed to understand the decision
- avoid including the entire pipeline by default

The goal is not merely to retrieve similar artifacts. The goal is to retrieve
the artifacts needed to reason about the question.
