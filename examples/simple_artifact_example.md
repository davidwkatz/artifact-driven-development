# Simple Artifact Example (Conceptual Version)

This example shows the basic idea of artifact-driven development using a small chain of named data objects.

It is intentionally **conceptual rather than executable**. The goal is to show how the structure of the workflow becomes clearer when important intermediate objects are treated as artifacts.

## Two kinds of artifacts

This example uses **two related kinds of artifacts**:

1. **Operational artifacts** are part of the working system itself.  
   Examples:
   - `observations`
   - `v_observations_clean`
   - `v_feature_counts`

2. **Descriptive artifacts** are structured descriptions of the system.  
   Example:
   - a future `artifacts.yaml` file describing artifact names, types, purposes, and dependencies

A descriptive artifact can be viewed as structured documentation, but it can also serve as a usable abstraction layer for AI and tooling.

These work together. The operational artifacts make the system more explicit, which makes structured description possible. The descriptive artifacts then make the operational artifacts easier for humans and AI to understand and use.

A concise way to say this is:

> Operational artifacts make the system legible; descriptive artifacts make that legibility usable.

## Artifact chain and dependency graph

For this small example, the data flow can be shown as a simple artifact chain:

```text
source CSV -> observations -> v_observations_clean -> v_feature_counts
```

This chain is a readable view of the workflow, not a separate source of truth.

The underlying structure is the set of dependency relationships. If the source CSV is treated as an external input rather than an artifact, the operational artifact dependencies are:

```text
v_observations_clean depends on observations
v_feature_counts depends on v_observations_clean
```

Conceptually, the full data flow is still:

```text
source CSV -> observations -> v_observations_clean -> v_feature_counts
```

In a larger system, the structure may no longer be a single chain. It may become a graph, with several artifacts depending on the same upstream artifact:

```text
source CSV -> observations -> v_observations_clean
                                    -> v_feature_counts
                                    -> v_feature_counts_by_entity
```

So the general idea is:

```text
dependencies = the underlying structure
artifact chain = a readable path through that structure
artifact graph = the broader dependency structure when the system branches
```

In this example, the chain is simple enough to show directly. In a fuller system, the chain or graph would usually be constructed from metadata such as the `depends_on` fields in `artifacts.yaml`.

## What the objects mean

- `source CSV` is the original input data.
- `observations` is the base loaded table.
- `v_observations_clean` is a cleaned semantic layer derived from `observations`.
- `v_feature_counts` is a summary derived from the cleaned layer.

Each object has a distinct purpose and can be inspected on its own.

## Objects in this example

| Object | Type | Role |
|---|---|---|
| `source CSV` | external input | original input data |
| `observations` | operational artifact / table | base loaded table |
| `v_observations_clean` | operational artifact / view | cleaned semantic layer |
| `v_feature_counts` | operational artifact / view | downstream summary |
| `artifacts.yaml` | descriptive artifact / metadata file | structured description of artifact names, types, purposes, and dependencies |

The main idea is that the working system contains operational artifacts, while a structured metadata file can describe those artifacts in a compact machine-readable form.

## Example SQL

A simple artifact-oriented version might look like this:

```sql
create or replace table observations as
select *
from read_csv_auto('data/test/observations_test_v1.csv');

create or replace view v_observations_clean as
select *
from observations
where qa_flag is null or qa_flag <> 'bad';

create or replace view v_feature_counts as
select
    feature,
    count(*) as n
from v_observations_clean
group by feature
order by feature;
```

In this version, the intermediate cleanup step is explicit and named.

## The same idea without artifacts

A non-artifact version could compute the summary directly from the base table:

```sql
select
    feature,
    count(*) as n
from observations
where qa_flag is null or qa_flag <> 'bad'
group by feature
order by feature;
```

This may produce the same final result, but the cleanup logic is implicit inside the summary query. There is no named intermediate object like `v_observations_clean` that can be inspected, reused, or referenced by downstream work.

## Why the artifact version is useful

The artifact-oriented version makes the workflow easier to understand:

- the base layer is explicit
- the cleanup layer is explicit
- the summary layer is explicit
- downstream dependencies are easier to see

This is similar in spirit to single responsibility in code: each derived artifact should represent one coherent transformation or semantic layer.

## Why this helps AI

The point is not only that these derived objects exist, but that they form a compact abstraction of part of the system.

An AI assistant does not need to reconstruct everything from scattered Python, SQL, and notes. It can begin from a small artifact graph:

- `observations` is the base table
- `v_observations_clean` is the cleaned semantic layer
- `v_feature_counts` is a summary derived from the cleaned layer

This makes it easier for AI to reason about dependencies, propose changes, assess downstream impact, and identify where new derived objects should fit.

In that sense, the operational artifacts are not just outputs. They are part of the system's explicit structure. A descriptive artifact such as `artifacts.yaml` can then provide a compact machine-readable abstraction of that structure.

## Minimal descriptive artifact

The following YAML illustrates what a future `artifacts.yaml` file might look like:

```yaml
artifacts:
  - name: observations
    artifact_type: operational
    kind: table
    depends_on: []
    purpose: Base loaded observation records

  - name: v_observations_clean
    artifact_type: operational
    kind: view
    depends_on: [observations]
    purpose: Cleaned semantic layer for downstream analysis

  - name: v_feature_counts
    artifact_type: operational
    kind: view
    depends_on: [v_observations_clean]
    purpose: Summary counts by feature

descriptive_artifacts:
  - name: artifacts.yaml
    artifact_type: descriptive
    purpose: Structured description of operational artifacts and their dependencies
```

The `depends_on` fields are the source of the dependency structure. Human-readable chains and graphs can be constructed from those relationships.

This YAML is not the working data system itself. It is a structured description of that system. Its value depends on the operational artifacts being explicit enough to describe cleanly.

## Evaluating alternative design choices

The descriptive artifact does not just document the current design. It also helps compare possible changes to the system.

For example, suppose we want to add a new derived artifact called `v_feature_counts_by_entity`.

There are several plausible design choices:

- derive it directly from `observations`
- derive it from `v_observations_clean`
- add some other intermediate artifact first, then derive it there

Without an explicit artifact structure, this choice can become an implementation detail hidden inside code. With operational and descriptive artifacts, the alternatives can be compared more clearly:

- Should the new summary use raw data or cleaned data?
- Does it belong as a direct downstream consumer of the clean layer?
- Would a new intermediate semantic layer make the design clearer?
- What existing artifacts are actually relevant to this change?

A likely design is:

```text
source CSV -> observations -> v_observations_clean
                                    -> v_feature_counts
                                    -> v_feature_counts_by_entity
```

In that design, both summaries depend on the same cleaned semantic layer. That keeps the raw layer separate from the analysis-ready layer and makes the dependency structure easier to understand.

A descriptive artifact could represent the new design like this:

```yaml
artifacts:
  - name: observations
    artifact_type: operational
    kind: table
    depends_on: []
    purpose: Base loaded observation records

  - name: v_observations_clean
    artifact_type: operational
    kind: view
    depends_on: [observations]
    purpose: Cleaned semantic layer for downstream analysis

  - name: v_feature_counts
    artifact_type: operational
    kind: view
    depends_on: [v_observations_clean]
    purpose: Summary counts by feature

  - name: v_feature_counts_by_entity
    artifact_type: operational
    kind: view
    depends_on: [v_observations_clean]
    purpose: Summary counts by feature and entity
```

In this way, the descriptive artifact helps turn a coding question into a design question.

## Why this matters more in larger systems

In a larger system, the value becomes even clearer. An AI assistant does not need to load the whole repository into context. It can focus on a small relevant subgraph of artifacts.

For the task of adding `v_feature_counts_by_entity`, the most relevant artifacts may be only:

- `v_feature_counts_by_entity`
- `v_observations_clean`
- `observations`

The AI can reason productively about this local neighborhood without needing unrelated parts of the system. That makes the artifact graph a useful abstraction for selective attention: it helps humans and AI focus on the few artifacts most relevant to the task at hand.
