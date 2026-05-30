# Artifact-Driven Development

*A practical introduction to making project structure more explicit for humans and AI.*

Software projects contain more than source code. They also contain intermediate products, decisions, workflow state, dependencies, derived data, and operational constraints. Much of this structure is often left implicit: buried in scripts, conventions, chat history, or in one person’s head.

Artifact-driven development is a simple response: treat important intermediate products as explicit artifacts.

An artifact might be a derived table, a semantic view, a workflow state, a dependency summary, a design decision, a task definition, or a compact record of how one output depends on others. The point is not just to save outputs. The point is to make project structure more visible, inspectable, and reusable.

## What this repo is for

This repo explores artifact-driven development as a practical pattern for AI-assisted software and analytical systems.

The emphasis is on simple, concrete examples rather than heavy formalism.

Topics may include:

- operational and descriptive artifacts
- explicit dependencies between artifacts
- semantic views and derived structures
- design decisions as first-class objects
- project organization for human and AI collaboration
- implications for autonomous agents and governance

## Where to start

Start with the simplest examples and concepts first.

Suggested reading order:

1. this README
2. [`examples/simple_pipeline/README.md`](examples/simple_pipeline/README.md) for a concrete, inspectable data example
3. [`examples/simple_artifact_example.md`](examples/simple_artifact_example.md) for the conceptual version of the same idea
4. [`examples/simple_pipeline/artifacts.yaml`](examples/simple_pipeline/artifacts.yaml) for an explicit artifact catalog showing artifact names, types, purposes, and dependencies
5. longer essays or experiments in the repo

## The core idea

Traditional development often leaves important context outside the working system. Humans reconstruct it from memory, code, and notes. AI systems try to reconstruct it from prompts, files, and chat history.

Both do better when the important intermediate products are made explicit.

Artifact-driven development can be understood as an explicit abstraction layer over a project. Instead of asking humans or AI systems to infer structure from scattered files, scripts, notes, and conversations, it gives the project a layer of named artifacts with purposes, dependencies, and relationships.

Artifact-driven development treats these intermediate products as first-class objects; that is:

- they are named
- they can be inspected
- they can be reused
- they can be connected by dependencies
- they can help explain what exists and why

Together, these artifacts make the system easier to understand, explain, and change. Instead of treating the project as a mass of code, data, and notes, they give both humans and AI systems concrete objects to inspect, discuss, reuse, and modify.

## Minimal vocabulary

This repo uses a small practical vocabulary.

- **Operational artifacts** are things the system actively uses while running or producing outputs. Examples: tables, views, task records, workflow states, checkpoints, budgets, approvals.
- **Descriptive artifacts** are things that help explain or organize the system. Examples: design decisions, dependency summaries, semantic definitions, structured documentation.
- **Dependencies** describe how one artifact relies on another.
- **Artifact-driven development** means making important project structure explicit through artifacts rather than leaving it implicit in code, prompts, or convention.
- **Semantic views** are named ways of interpreting lower-level artifacts as a higher-level project concept. For example, a table or SQL view called `valid_observations` might not just be a derived dataset; it might encode the project’s current definition of which observations are usable for analysis.

These categories are not rigid. A useful artifact can be partly operational and partly descriptive.

## A small example

Suppose a data pipeline computes features from raw event data.

A conventional implementation might have this logic hidden in code:

- clean duplicates
- normalize timestamps
- extract features
- build summary tables

A more artifact-driven version might make several intermediate products explicit:

- `raw_events`
- `deduplicated_events`
- `normalized_events`
- `feature_table`
- `summary_table`
- `decision: duplicate cleaning happens before feature extraction`

That last item is important. A design choice that would otherwise be hidden in code or chat becomes an explicit artifact.

The result is not just better documentation. It is a system whose structure is easier to inspect and reason about.

A human can see what exists and how outputs are formed.  
An AI system can focus on the relevant artifacts instead of reconstructing everything from scratch.

## Why this helps with AI-assisted development

AI is increasingly capable at coding, analysis, and system design. But it still works best when the project exposes clear structure.

Without explicit artifacts, important context is often scattered across:

- source files
- shell scripts
- naming conventions
- issue threads
- chat history
- unwritten assumptions

With explicit artifacts, more of that context becomes available in reusable form.

That helps AI systems:

- understand the current state of a project
- work from stable intermediate products
- trace dependencies
- compare alternative designs
- make smaller, better-scoped changes

In a larger system, this also helps an AI focus on a few relevant artifacts instead of a mass of loosely connected files and conversation.

## Using artifacts as AI context

One practical benefit of making artifacts explicit is that they help with context selection.

Context selection means choosing the subset of project material that is relevant to the current question or task. When working with an AI system, it is often unclear which files, notes, examples, schemas, decisions, or intermediate outputs should be included in the prompt.

Artifact-driven development makes this easier by giving the project named objects with purposes and dependencies. Instead of sending “the whole project,” you can select the artifacts most relevant to the task. This both saves context space and often produces better results.

For example, if the question is why duplicate removal happens before feature extraction, the relevant context might include the raw input artifact, the deduplicated artifact, the normalized artifact, and the artifact catalog describing their dependencies.

## Beyond documentation

Artifact-driven development is not just “write better docs.”

It changes what the project treats as part of the working system.

Instead of leaving important context outside the system, it brings more of that context into the project’s explicit structure. Decisions, dependencies, workflow state, and operational constraints can all become explicit artifacts.

This matters because explicit artifacts are easier to inspect, revise, test, govern, and reuse than hidden conventions.

## Why this matters for autonomous agents

This idea also matters for AI governance.

As AI systems become more autonomous, good behavior depends not only on model capability but on system structure. Goals, budgets, tasks, approvals, permissions, and audit trails should not live only in prompts or operator intuition. They should be explicit artifacts inside the system.

When those structures are explicit, autonomous behavior becomes easier to constrain, inspect, interrupt, and review.

In that sense, artifact-driven development is relevant not only to productivity, but also to alignment and governance.

## Relation to LLM-maintained knowledge systems

A related pattern is the idea of an LLM-maintained wiki or knowledge layer, such as Andrej Karpathy’s [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Artifact-driven development generalizes that idea. Instead of treating maintained context only as wiki pages, it treats decisions, dependencies, summaries, indexes, validation records, and workflow state as first-class artifacts too.

That broader framing preserves the compounding benefits of maintained context while making more room for provenance, human review, role-specific context, and stronger structures such as typed relationships or graphs when a simple markdown layer is no longer enough.

## Limitations: opaque components

Artifact-driven development does not make every part of a system transparent. Some components remain internally opaque even when the surrounding project structure is explicit. Examples include learned models, embedding systems, ranking systems, external APIs, complex heuristics, hidden platform state, and human judgment.

In those cases, the method is still useful, but in a different way. The opaque component can be treated as a bounded artifact, while the surrounding evidence is made explicit: inputs, outputs, training or source data, evaluation results, behavioral tests, counterexamples, monitoring outputs, interpretability attempts, assumptions, and decision records.

This does not turn the opaque component’s internal behavior into a human-readable DAG. It does, however, make the system’s knowledge about that component more visible, inspectable, and revisable.

## A simple claim

Artifact-driven development does not require a new programming language or a fully automated system.

It starts with a smaller and more practical move:

Make important project structure explicit.

That helps humans work with more clarity, and it gives AI systems a better chance of being useful, reliable, and governable.


Feedback is welcome via GitHub Discussions or Issues.
