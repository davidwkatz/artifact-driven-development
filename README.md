# Artifact-Driven Development

*A practical pattern for making project structure more explicit for humans and AI.*

Artifact-driven development is a practical pattern for making important intermediate products explicit, named, inspectable, and reusable.

Software and analytical projects contain more than source code. They also contain intermediate products, workflow state, dependencies, design decisions, and operational constraints. Much of this structure is often left implicit in code, scripts, conventions, and chat history.

This repository explores a simple response:

treat important project structure as explicit artifacts.

## Repo status

This is an early concept-and-examples repository.  
The emphasis is on clear ideas, small examples, and practical vocabulary rather than a heavy framework.

## Why this matters

Humans can often reconstruct missing project structure from memory, habit, and scattered notes.

AI systems can sometimes reconstruct it too.

But both do better when important intermediate products are made explicit.

That helps make a project easier to inspect, reuse, revise, and govern.

## A tiny example

Suppose a project starts with raw observational data.

    raw.observations
      -> semantic.v_observations_clean
      -> feature.entity_feature_timespan
      -> summary.feature_counts

Now add one decision artifact:

    decision.cleaning_before_feature_extraction

That decision might record that duplicate cleaning happens before feature extraction, and why.

Without an explicit artifact, that choice may exist only in code, comments, or chat history.  
With it, the structure of the system becomes easier to inspect and explain.

## What is in this repo

- [Introduction](docs/introduction.md)
- [A small concrete example](docs/examples/simple_artifact_example.md)
- [Artifact-Driven Development for Semi-Autonomous Agents](docs/semi_autonomous_agents.md)

## Suggested reading order

1. this README
2. [Introduction](docs/introduction.md)
3. [A small concrete example](docs/examples/simple_artifact_example.md)
4. [Artifact-Driven Development for Semi-Autonomous Agents](docs/semi_autonomous_agents.md)

## A simple claim

Artifact-driven development does not require a new programming language or a fully automated system.

It starts with a smaller and more practical move:

make important project structure explicit.

That helps humans work with more clarity, and it gives AI systems a better chance of being useful, reliable, and governable.
