# Talk to Your Project

Artifact-driven development makes it possible to talk to a project as a structured system, not just as a pile of files.

In a conventional workflow, a developer often has to decide what context to paste into an LLM prompt: a README, a few source files, an error message, maybe some notes about intent. That can work for small tasks, but it does not scale well. Important context is easy to omit, and large context windows encourage dumping too much material into the prompt.

ADD takes a different approach: make the project itself queryable.

## The core idea

A project should be able to answer questions such as:

- What artifacts exist?
- What does each artifact mean?
- Which artifacts depend on which others?
- Which artifacts are operational, and which are descriptive?
- Which artifacts are relevant to this question?
- What higher-level concept does this lower-level file, table, or view represent?

The goal is not merely to store more documentation. The goal is to create enough explicit structure that an agent, tool, or human can retrieve the right context for the task at hand.

## From files to artifacts

Most repositories already contain useful files: source code, tests, README files, configuration files, data examples, design notes, and scripts.

ADD treats selected files, tables, views, records, or generated outputs as **artifacts** with explicit meaning.

An artifact can describe:

- its purpose
- its path or location
- what it depends on
- what depends on it
- whether it is operational or descriptive
- what project concept it represents
- why it might be relevant to particular questions

This turns the repository into something closer to a small knowledge system.

## Why this matters for agents

LLMs are sensitive to context. They can produce better answers when they receive the right information, but they do not automatically know which parts of a project matter.

Without explicit artifacts, an agent may have to guess.

With artifacts, the workflow can become more deliberate:

1. A user asks a project question.
2. The system searches artifact metadata, dependencies, semantic views, and relevant full text.
3. A compact context packet is assembled.
4. The agent answers using the selected project context.

This is different from simply pasting the entire repository into a prompt. ADD is about **context selection**, not just context accumulation.

## Full text still matters

Structured metadata is useful, but it should not replace the underlying project text.

A good ADD workflow can combine:

- artifact metadata
- dependency relationships
- semantic views
- summaries
- selected full text

The metadata helps decide what to retrieve. The full text provides the detailed evidence needed to answer accurately.

In other words, the project should be queryable at two levels:

1. **Structure**: what exists, how it relates, and why it matters.
2. **Content**: the actual text, code, data definitions, examples, or records.

## Query the project, not just the prompt

The practical promise of ADD is that a developer should be able to ask:

> Why does this pipeline remove duplicates before feature extraction?

or:

> Which artifacts would be affected if we changed the definition of a valid observation?

or:

> What context should an agent read before modifying this module?

and get an answer grounded in the project’s explicit artifacts.

This shifts the interaction model from:

> “Here are some files I pasted. Please reason from them.”

to:

> “Here is a question. Use the project’s artifact structure to find the right context.”

That is the sense in which ADD lets you **talk to your project**.

## What this enables

A queryable project structure can support:

- leaner prompts for smaller or cheaper models
- better context selection for coding agents
- clearer onboarding for humans
- impact analysis before changes
- comparison between intended design and actual implementation
- explicit project memory that lives in the repository
- more reliable agent collaboration across multiple tasks

The key point is that the project’s knowledge is not hidden only in code, convention, or chat history. It is represented through artifacts that can be inspected, searched, updated, and used.

## Relation to documentation

ADD does not replace documentation. It gives documentation a more operational role.

A normal documentation file explains the project to a human reader. An ADD artifact can also explain the project to a tool or agent that needs to select context, trace dependencies, or answer a focused question.

This makes documentation less like a static essay and more like part of the project’s working structure.

## How this differs from ordinary documentation

ADD builds on ordinary documentation, but it asks documentation to do a more specific job.

Traditional project documentation can include README files, design notes, architecture diagrams, flowcharts, data dictionaries, comments, and onboarding guides. These are valuable, but they are often written mainly for human reading. They may explain how something works without making the project structure directly queryable.

For example, a flowchart may show the stages of a pipeline, but it may not identify each stage as an artifact with a path, purpose, dependencies, downstream consumers, and relevance to common questions.

ADD tries to preserve the explanatory value of documentation while adding more explicit structure.

A flowchart might show:

> raw data → duplicate removal → normalization → feature extraction → model input

An ADD artifact graph would also ask:

- What artifact represents each stage?
- Where does it live?
- What does it depend on?
- What depends on it?
- What project concept does it encode?
- What questions should retrieve it as context?
- What full text or source files provide the evidence behind it?

This does not make flowcharts obsolete. A flowchart can be one useful descriptive artifact. But ADD treats diagrams, markdown files, tables, code files, and generated outputs as parts of a larger queryable project structure.

The difference is that ADD is not only trying to explain the project. It is trying to make the project easier to interrogate, navigate, and modify.

## Working definition

In this repository, “talking to your project” means:

> Asking questions against the project’s artifacts, dependencies, semantic views, and selected full text, so that answers are grounded in the structure of the project rather than in whatever context happened to be pasted into a prompt.

That is one of the central motivations for artifact-driven development.
