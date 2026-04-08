# Artifact-Driven Development

*A practical introduction and guide to this repository.*

AI-assisted software development is getting stronger, but too much project structure still remains implicit in code, scripts, notes, conventions, and chat history. Artifact-driven development is a practical pattern for making important intermediate products explicit, named, inspectable, and reusable. This gives both humans and AI systems a clearer handle on project structure, continuity, and change.

This repository explores that idea through simple examples, vocabulary, and working notes.

## The problem

In many projects, important structure is real but mostly implicit.

It may exist in:

- derived tables and views
- workflow stages
- dependency relationships
- design decisions
- intermediate outputs
- scripts that only one person fully understands
- chat history that explains *why* something was done

Humans can often reconstruct this with effort. AI systems can sometimes reconstruct it too. But both do better when important intermediate products are made explicit.

## The core idea

Treat important intermediate products as first-class artifacts.

An artifact might be:

- a derived table
- a semantic view
- a cleaned dataset
- a feature summary
- a dependency map
- a workflow state
- a compact representation of system structure

The point is not just to save outputs. The point is to make project structure more explicit and more usable.

## Minimal vocabulary

This repo uses a small, practical vocabulary for describing artifacts and how they relate.

- **Operational artifacts** are things the system uses or produces directly.
- **Descriptive artifacts** are structured descriptions of artifacts, interfaces, or dependencies.
- **Decision artifacts** record important design choices and rationale.

A few simple relationships go a long way:

- `depends_on` — what an artifact is derived from
- `produced_by` — what process, script, or transformation creates it

This is enough to express useful structure without introducing a heavy framework.

## A tiny example

Suppose a project starts with raw observational data.

    raw.observations
      -> semantic.v_observations_clean
      -> feature.entity_feature_timespan
      -> summary.feature_counts

Even this small chain is already useful. It makes intermediate structure visible instead of burying it in code.

Now add one decision artifact:

    decision.cleaning_before_feature_extraction

That decision might record that duplicate cleaning happens before feature extraction, and why. Without an explicit artifact, that choice may exist only in code, comments, or chat history. With it, the structure of the system becomes easier to inspect and explain.

## Why this helps with AI-assisted development

AI systems work better when a project exposes stable intermediate structure.

Without explicit artifacts, important context is often scattered across files, scripts, prompts, naming conventions, and conversation. With explicit artifacts, more of that context becomes available in reusable form.

That helps both humans and AI systems:

- understand what exists
- trace how outputs are formed
- reuse stable intermediate products
- compare alternative designs
- make smaller, better-scoped changes

In larger systems, this also helps an AI focus on a few relevant artifacts instead of reconstructing everything from a mass of loosely connected files and history.

## Beyond documentation

Artifact-driven development is not just “write better docs.”

It broadens the effective system boundary. More of the structure that matters to the project becomes part of the working system rather than remaining outside it as hidden convention.

That can include:

- intermediate data products
- semantic views
- dependency relationships
- workflow state
- design decisions
- operational constraints

This matters because explicit structure is easier to inspect, revise, test, and reuse than implicit structure.

## Why this may matter for autonomous agents

This idea also matters for governance.

As AI systems become more autonomous, good behavior depends not only on model capability but also on system structure. Goals, budgets, tasks, approvals, permissions, and audit trails should not live only in prompts or operator intuition. They can also be treated as artifacts inside the system.

When those structures are explicit, autonomous behavior becomes easier to constrain, inspect, interrupt, and review.

## What this repo is for

This repo is a place to explore artifact-driven development as a practical pattern for software, analytics, and AI-assisted work.

The emphasis is on simple, concrete examples rather than heavy formalism.

Topics may include:

- operational, descriptive, and decision artifacts
- lightweight dependency structure
- semantic views and derived products
- design decisions as first-class objects
- project organization for human and AI collaboration
- implications for autonomous agents and governance

## Where to start

A suggested reading order:

1. this README
2. the introduction document
3. the smallest concrete examples in the repo
4. notes on artifact types and relationships
5. longer essays or experiments, if present


## A simple claim

Artifact-driven development does not require a new programming language or a fully automated system.

It starts with a smaller and more practical move:

make important project structure explicit.

Artifact-driven development matters for autonomous agents because alignment is not just a property of the model. It is also a property of the surrounding system. When goals, limits, approvals, and decision trails are made explicit as artifacts, autonomous behavior becomes more governable.