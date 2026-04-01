# Artifact-Driven Development

AI-assisted software development is getting stronger, but too much project structure still remains implicit in code, scripts, notes, conventions, and chat history. Artifact-driven development is a practical pattern for making important intermediate products explicit, named, inspectable, and reusable. This gives both humans and AI systems a clearer handle on project structure, continuity, and change.

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

Humans can often reconstruct this with effort. AI systems can sometimes reconstruct it too. But both do better when the important intermediate products are made explicit.

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

## A tiny example

Suppose a project starts with raw observational data.

```text
raw.observations
  -> semantic.v_observations_clean
  -> feature.entity_feature_timespan
  -> summary.feature_counts