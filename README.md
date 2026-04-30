# Artifact-Driven Development

*A practical introduction to making project structure more explicit for humans and AI.*

Software projects contain more than source code. They also contain intermediate products, decisions, workflow state, dependencies, derived data, and operational constraints. Much of this structure is often left implicit: buried in scripts, conventions, chat history, or in one person’s head.

Artifact-driven development is a simple response: treat important intermediate products as explicit artifacts.

An artifact might be a derived table, a semantic view, a workflow state, a dependency summary, a design decision, a task definition, or a compact record of how one output depends on others. The point is not just to save outputs. The point is to make project structure more visible, inspectable, and reusable.

## The core idea

Traditional development often leaves important context outside the working system. Humans reconstruct it from memory, code, and notes. AI systems try to reconstruct it from prompts, files, and chat history.

Both do better when the important intermediate products are made explicit.

Artifact-driven development treats these intermediate products as first-class objects:

- they are named
- they can be inspected
- they can be reused
- they can be connected by dependencies
- they can help explain what exists and why

This gives both humans and AI systems a better control surface for working on a project.

## Minimal vocabulary

This repo uses a small practical vocabulary.

- **Operational artifacts** are things the system actively uses while running or producing outputs. Examples: tables, views, task records, workflow states, checkpoints, budgets, approvals.
- **Descriptive artifacts** are things that help explain or organize the system. Examples: design decisions, dependency summaries, semantic definitions, structured documentation.
- **Dependencies** describe how one artifact relies on another.
- **Artifact-driven development** means making important project structure explicit through artifacts rather than leaving it implicit in code, prompts, or convention.

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

## Beyond documentation

Artifact-driven development is not just “write better docs.”

It broadens the effective system boundary.

Instead of treating important context as something outside the system, it brings more of that context inside the working structure of the project. Decisions, dependencies, workflow state, and operational constraints can all become explicit artifacts.

This matters because explicit artifacts are easier to inspect, revise, test, govern, and reuse than hidden conventions.

## Why this matters for autonomous agents

This idea also matters for AI governance.

As AI systems become more autonomous, good behavior depends not only on model capability but on system structure. Goals, budgets, tasks, approvals, permissions, and audit trails should not live only in prompts or operator intuition. They should be explicit artifacts inside the system.

When those structures are explicit, autonomous behavior becomes easier to constrain, inspect, interrupt, and review.

In that sense, artifact-driven development is relevant not only to productivity, but also to alignment and governance.

## Relation to LLM-maintained knowledge systems

A related recent pattern is the idea of an LLM-maintained wiki or knowledge layer, such as Andrej Karpathy’s [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

The most important idea behind “LLM wiki” is not “let the model write a wiki.” It is “let context accumulate into explicit artifacts.” Raw sources remain the source of truth, while maintained intermediate artifacts capture synthesis, cross-references, logs, and operating conventions. Artifact-driven development generalizes this idea beyond wikis. It treats decisions, dependencies, summaries, indexes, validation records, and workflow state as first-class artifacts too. That broader framing is useful because it preserves the compounding benefits of maintained context while making more room for provenance, human review, role-specific context, and stronger structures such as typed relationships or graphs when a simple markdown layer is no longer enough.

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
2. `examples/simple_pipeline/README.md` for a concrete, inspectable data example
3. `examples/simple_artifact_example.md` for the conceptual version of the same idea
4. `examples/simple_pipeline/artifacts.yaml` for an explicit artifact catalog showing artifact names, types, purposes, and dependencies
5. longer essays or experiments in the repo

## A simple claim

Artifact-driven development does not require a new programming language or a fully automated system.

It starts with a smaller and more practical move:

make important project structure explicit.

That helps humans work with more clarity, and it gives AI systems a better chance of being useful, reliable, and governable.
