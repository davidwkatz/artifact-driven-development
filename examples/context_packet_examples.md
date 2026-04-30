# Context Packet Examples

This file shows how artifact-driven development can support context construction for AI-assisted work.

These examples assume an existing project with code, data artifacts, and workflow structure already in place. The goal is usually not to reason from scratch, but to identify the smallest set of existing artifacts needed to support a specific question or change. That small set of artifacts is then provided to the LLM as context for the task.

Each example below identifies a task, a likely focal area, a small context packet, and why that packet is useful.

## Example 1. Decide where duplicate removal belongs

**Task**  
Decide whether duplicate removal should happen before or after feature extraction.

**Likely focal area**  
The transition between the base loaded layer and the cleaned semantic layer, for example between `observations`, `v_observations_clean`, and the downstream feature extraction step.

**Context packet**
- `observations`
- `v_observations_clean`
- the downstream feature extraction artifact
- any existing decision artifact about cleaning order
- a small validation or test artifact showing duplicate cases

**Why this packet**  
This task is about pipeline ordering. The AI needs the current insertion point, the nearby semantic layer, the downstream consumer, and any artifact that explains the intended order of operations.

## 2. Debug incorrect feature counts

**Task**  
Debug incorrect feature counts.

**Likely focal area**  
The summary artifact and its upstream dependencies.

**Context packet**
- `v_feature_counts`
- `v_observations_clean`
- `observations`
- any test or validation artifact for count correctness
- any schema or semantic note defining what counts should mean

**Why this packet**  
This task starts from a downstream summary and works upward. The AI needs the summary definition, its immediate upstream layer, the base source, and any artifact that states the intended meaning of the count.

## 3. Assess impact of changing the clean layer schema

**Task**  
Assess the impact of changing the clean layer schema.

**Likely focal area**  
The clean semantic layer and its downstream dependents.

**Context packet**
- `v_observations_clean`
- its schema description
- downstream artifacts such as `v_feature_counts`
- any dependency summary
- any decision artifact explaining why the clean layer has its current structure

**Why this packet**  
This task is about change impact. The AI needs the artifact being changed, its schema definition, the artifacts that depend on it, and any explanation of why the current schema exists.

Different context packets may support different kinds of responses, such as decision support, implementation guidance, debugging help, or change-impact analysis.

## What these examples show

These examples illustrate a simple pattern:

1. identify the focal artifact or focal layer
2. include the closest structural neighbors
3. include nearby descriptive artifacts
4. keep the final packet small

The goal is not to retrieve everything. The goal is to retrieve the smallest set of artifacts that supports productive reasoning.

