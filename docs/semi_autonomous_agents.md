# Artifact-Driven Development for Semi-Autonomous Agents

*A practical extension of artifact-driven development for longer-running agent workflows.*

Artifact-driven development is about making important project structure explicit.

That matters for ordinary software and analytical work. It matters even more when the project includes semi-autonomous agents.

A human can often recover missing context from memory, habit, and informal judgment. An agent usually cannot. It may perform well on a local task and still lose track of what has already been tried, why a decision was made, which constraints matter, or what part of the project state should shape the next step.

This is one reason semi-autonomous agents often look stronger in short bursts than in longer-running projects. The problem is not always model capability. Often the surrounding project structure is too implicit.

Important context may exist, but in forms that are easy to miss:

- chat history
- scattered notes
- half-maintained logs
- scripts that embed decisions without naming them
- outputs with unclear status
- conventions that live mostly in one person’s head

Humans can often work around this. Agents tend to drift, repeat work, or reopen questions that were already settled.

Artifact-driven development helps because it gives the agent a more explicit working environment.

## Not just documentation

It is tempting to describe this as a documentation problem. That is only partly right.

Documentation is often written for later human reference. Semi-autonomous agents need something closer to an external working structure: explicit artifacts that preserve project state, prior decisions, intermediate results, and relevant constraints in forms that can be repeatedly consulted and updated.

In that setting, artifacts are not only records of the work. They become part of the environment in which the work happens.

That is the key shift.

For semi-autonomous agents, notes, state summaries, run records, decision logs, task definitions, and source indexes are not merely helpful extras. They often function as external working memory.

## Why agents need explicit structure

A semi-autonomous agent commonly runs into three problems.

The first is drift. It keeps doing plausible local work while slowly moving away from the actual project objective.

The second is repetition. It retries earlier experiments, revisits known dead ends, or reconstructs conclusions that already exist somewhere in the project.

The third is context collapse. A relevant constraint, document, or prior result exists, but not in a stable reusable form, so it stops influencing behavior.

These are not mysterious failures. They are what we should expect when important structure remains implicit.

If the state of a project lives mostly in conversation, operator memory, and loosely connected files, then the agent has to reconstruct continuity from fragments. Sometimes it will do that well. Often it will not.

Artifact-driven development improves this by making more of that continuity explicit, inspectable, and reusable.

## Operational, descriptive, and decision artifacts

The distinctions used elsewhere in this repo still matter here.

Operational artifacts are the things the system directly uses or produces: datasets, transformed tables, feature sets, models, configs, reports, workflow states, task records, checkpoints.

Descriptive artifacts are structured descriptions of the system and its state: artifact indexes, dependency summaries, run summaries, source maps, structured notes, checklists, state files.

Decision artifacts record important design choices and rationale: why a cleaning step happens before feature extraction, why one metric is treated as primary, why a search path was abandoned, why a workflow requires approval before certain actions.

For semi-autonomous agents, all three matter.

Operational artifacts carry the work itself.  
Descriptive artifacts preserve orientation.  
Decision artifacts preserve rationale and constraints.

Without decision artifacts in particular, agents often end up rediscovering choices that were already made, or undoing them without realizing it.

## A small example

Consider a semi-automated machine learning experimenter.

Such an agent may be able to launch runs, inspect metrics, compare outputs, and propose follow-up experiments. But without explicit structure around that work, it may still become unreliable over time.

It may not know:

- which hypothesis a run was meant to test
- which dataset or code version was used
- whether a metric change was expected
- why a line of investigation was abandoned
- which notes contain important caveats
- what the next useful step should be

A more artifact-driven setup can make this much clearer.

An experiment registry can record, for each run:

- a stable run identifier
- the hypothesis
- dataset and code versions
- parameters
- outputs and metrics
- status
- conclusion
- next action

A compact project state artifact can summarize:

- what is currently believed
- what remains uncertain
- what has already been tried
- which paths are known dead ends
- what the next few candidate actions are

A decision log can record why certain evaluation criteria, feature choices, stopping rules, or constraints were adopted.

A source index can record which documents matter, what each contains, and which claims are currently being relied on.

None of these artifacts is glamorous. Their value comes from keeping project continuity from dissolving into scattered traces.

## Procedure matters as much as artifacts

Artifacts alone are not enough.

A project can accumulate many files and still remain incoherent. The point is not simply to save more material. The point is to create a disciplined loop in which the agent is required to consult and update the right artifacts at the right times.

That means procedure matters as much as artifact type.

A useful pattern is simple.

Before acting, the agent should:

- read the current project state
- inspect recent run summaries
- check relevant decision artifacts
- identify the source documents that matter for the task
- state its intended action explicitly

After acting, it should:

- save outputs in stable locations
- update the run or task record
- record what changed
- summarize what was learned
- leave a clear next-step artifact for later reuse

This is still a lightweight pattern. It does not require a heavy orchestration framework. But it changes the character of the project. The system no longer depends so heavily on reconstructing state from a shifting mass of code, prompts, and chat history.

## Artifact-driven development as context engineering

This also clarifies the connection between artifact-driven development and context engineering.

Context engineering is often described as a prompt problem: what to include, what to retrieve, how to fit the right information into the model’s context window.

That is part of the picture, but not the whole of it.

In longer-running agent workflows, context is not only what gets passed into the model at one moment. It is also the maintained artifact environment from which usable context can be assembled again and again.

Seen this way, artifact-driven development is one practical form of context engineering.

It reduces dependence on fragile prompt reconstruction by moving continuity into explicit project objects. It makes context less transient. Instead of rebuilding working memory from scratch each time, the system can rely more on maintained artifacts that preserve state, decisions, dependencies, and constraints across runs.

## Why this also matters for governance

This is not only about productivity. It is also about governability.

As agents become more capable, good behavior depends not only on model capability but also on system structure. Budgets, permissions, approvals, task boundaries, escalation rules, and audit trails are easier to constrain and inspect when they are explicit artifacts rather than vague operator expectations.

This is one reason artifact-driven development matters for semi-autonomous agents in particular. It moves important control surfaces out of hidden convention and into explicit system structure.

That does not solve alignment by itself. But it can make agent behavior easier to constrain, interrupt, inspect, and improve.

In that sense, alignment is not just a property of the model. It is also a property of the surrounding artifact system.

## Limits

This approach has limits.

Artifacts can become stale. Logs can become noisy. State files can drift into vague narrative. Source indexes can turn into clutter. Too many artifacts can be almost as unhelpful as too few.

The answer is not maximal documentation. It is selective explicitness.

A good artifact-driven setup makes the most important structure visible without burying the project in ceremony. It uses lightweight schemas, stable names, and procedures that are simple enough to follow repeatedly.

## A practical test

A useful test is this:

Could a fresh agent instance enter the project, read a small set of maintained artifacts, and continue the work without repeating known failures or losing the thread?

If the answer is no, then some important part of the project’s working structure is probably still implicit.

That does not mean every detail must be formalized. It means the parts that carry continuity, rationale, and constraints should be explicit enough to survive across time, tools, and agent runs.

## A simple claim

Semi-autonomous agents do not just need goals.

They need a maintained external working structure.

Artifact-driven development helps provide that structure by turning project state, decisions, intermediate products, and constraints into explicit reusable artifacts. For human teams, that improves clarity and continuity. For semi-autonomous agents, it can make the difference between impressive local behavior and sustained, recoverable progress.