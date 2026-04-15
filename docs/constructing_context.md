Constructing Context

Artifact-driven development makes important parts of a system explicit: operational artifacts, descriptive artifacts, decision artifacts, dependencies, and constraints.

That helps both humans and AI systems. But a second problem remains:

how do we select the right subset of that material for a particular question?

This document is about that step.

Why construct context

We want to ask useful questions about a system and its development without always providing the entire system as input.

In most real projects, the whole system is too large and too noisy for every task. Good answers usually depend on a smaller working set: the specific artifact, dependency chain, decision history, or nearby precedent relevant to the question.

Context construction is the process of selecting that smaller working set. It helps a human or AI reason about the part of the system that matters for the current task, rather than starting from the whole system every time.

The goal is not maximal context. The goal is relevant context.

From query to response

A useful way to think about context construction is as a short pipeline:

query -> anchor -> context packet -> response

The query is the user’s request in natural language, such as:

“add duplicate removal before feature extraction”
“should we add duplicate removal before or after feature extraction”
“debug incorrect feature counts”

The anchor is the resolved focal point of the work. It identifies what the request is really centered on: an implementation change, a design decision, a bug, a file, a view, or a named artifact. The anchor defines relevance.

The context packet is the smallest useful set of surrounding material for that anchor. It may include upstream dependencies, downstream consumers, nearby precedent, and relevant decision artifacts or constraints.

The response is the output shaped for a human or supervisor. It should not merely repeat the context. It should help the reader act, decide, review, or delegate more effectively.

Different kinds of queries can lead to different anchors and different context packets. An implementation request usually calls for local operational context. A decision request usually calls for comparative context, tradeoffs, and prior reasoning.

Step 1: identify the focal artifact or task anchor

Start by identifying the specific object of work.

This is the center of gravity for the context packet. It is the thing being changed, created, evaluated, debugged, or explained.

The anchor does not have to be a formal artifact yet. It just has to be concrete enough to guide relevance.

This may be:

a named artifact
a file path
a view name
a user request such as “add duplicate removal before feature extraction”

Examples:

summary.feature_counts
v_observations_clean
src/bird_migration/query.py
“assess impact of changing the clean layer schema”

A useful question to ask is:

What exactly is this context packet for?

That answer becomes the anchor.

In practice, there are often two layers:

a surface anchor, which is what the user said
a resolved anchor, which is the artifact or small set of artifacts the request is really about

For example:

surface anchor: “add duplicate removal before feature extraction”
resolved anchor: the current feature extraction step, its upstream input, and a possible new deduplication artifact

That translation from request to resolved anchor is often where much of the intelligence lies.

Different request types lead to different context packets

The same system can support several kinds of requests, but it should not treat them all the same.

Common request types include:

implementation
decision
debugging
impact analysis
explanation

These request types shape the context packet differently.

An implementation request usually asks:

where should this change be made
what does it depend on
what nearby precedent exists

A decision request usually asks:

what are the alternatives
what tradeoffs matter
what prior decisions or constraints apply

A debugging request usually asks:

where could the fault lie
what changed recently
what outputs or assumptions are inconsistent

An impact analysis request usually asks:

what depends on this
what downstream artifacts would change
what should be reviewed before changing it

An explanation request usually asks:

what role does this artifact play
how does it fit in the system
why was it designed this way

So the input to context construction is not just “what artifact?” It is also “what kind of work is being requested?”

Step 2: gather the minimal relevant surroundings

Once the anchor is identified, the next step is to gather the smallest useful set of surrounding material.

In an artifact-driven system, that often includes only a few categories:

the focal artifact or proposed artifact
its likely upstream inputs
its immediate downstream consumers
a nearby design or implementation precedent
relevant decision artifacts or constraints

This is where artifact-driven structure helps. If dependencies and decisions are explicit, context construction becomes more targeted and less dependent on broad search.

The key principle is:

include what is needed for the task, but not the whole neighborhood

What a useful context packet might include

A useful context packet might include only:

the focal artifact or proposed change
one likely upstream semantic layer
one base source or operational input
one nearby precedent
one relevant decision artifact, if one exists

For example, for a proposed new summary artifact such as v_feature_counts_by_entity, a useful packet might include only:

v_feature_counts_by_entity as the proposed new artifact
v_observations_clean as the likely upstream semantic layer
observations as the base source
v_feature_counts as a nearby design precedent
a decision artifact, if one exists, about whether summaries should depend on raw or cleaned data

This kind of packet is intentionally small. It is not a dump of all related files. It is a focused working set.

Example: implementation request

Consider this query:

“add duplicate removal before feature extraction”

This is primarily an implementation request. The requested direction is already mostly decided.

A likely anchor is:

implement deduplication before feature extraction

A likely context packet would emphasize:

the current feature extraction artifact or step
the upstream input it currently consumes
a likely insertion point for deduplication
any precedent for cleanup before feature extraction

The purpose of the packet is to support making the change correctly.

Example: decision request

Now consider this query:

“should we add duplicate removal before or after feature extraction”

This is primarily a decision request. The problem is not only how to implement a change, but where that change belongs.

A likely anchor is:

decide where deduplication should occur relative to feature extraction

A likely context packet would emphasize:

the raw data semantics
the feature extraction step
the meaning of duplicates before and after extraction
downstream consequences of each choice
any prior decision about whether summaries should depend on raw or cleaned data

The purpose of the packet is to support comparison and judgment, not just implementation.

Why artifact-driven development helps here

Artifact-driven development helps because it gives context construction more structure.

Instead of searching only across files or chat logs, the system can reason over:

named artifacts
explicit dependencies
semantic layers
decision artifacts
known precedents

That makes it easier to ask:

what is this request about
what does it depend on
what nearby artifacts are relevant
what prior reasoning constrains it

In that sense, artifact-driven development complements context engineering. It makes more of the system visible and inspectable, which makes better context packets possible.

What the response should do

The response should not merely summarize the packet.

It should help a human or supervisor do something useful with it.

Depending on the request type, that may mean:

proposing a likely implementation path
comparing alternatives
identifying risks
showing expected downstream impact
suggesting the next decision or review point

In other words, context construction is not the end of the process. It is the preparation step that makes a better response possible.

A practical summary

A practical context-construction workflow looks like this:

Start with the query.
Resolve it into a task type and anchor.
Gather the smallest useful set of surrounding artifacts, dependencies, precedents, and decisions.
Produce a response that helps a human or supervisor act, decide, review, or delegate.

The central idea is simple:

we want to ask useful questions about a system and its development without starting from the whole system every time.

Context construction is the step that makes that possible.