# Business Objective

## Objective

Identify active subscription customers who are at elevated risk of
churning within the next 30 days.

The predictions will be used by the customer-success team to prioritize
retention outreach.

## Intended decision

For each active customer, decide whether the customer should be placed
in a retention-outreach queue.

## Business value

A useful model should help the company:

- retain customers who might otherwise leave
- focus outreach on customers most likely to benefit
- avoid unnecessary or intrusive outreach
- understand the behaviors associated with churn

## Prediction unit

One prediction is produced for one customer at one scoring date.

## Prediction horizon

The model predicts whether a customer will churn within 30 days after
the scoring date.

## Operational constraints

The customer-success team can contact no more than 10 percent of active
customers during each scoring cycle.

The model must therefore support ranking customers by risk rather than
only producing a yes-or-no classification.

## Success criteria

The project should report:

- precision among the highest-risk 10 percent of customers
- recall among the highest-risk 10 percent of customers
- area under the precision-recall curve
- churn rate by risk group
- performance by customer segment

## Non-goals

The first version will not:

- estimate the causal effect of retention outreach
- recommend a specific retention offer
- optimize the financial value of each intervention
- use real customer data
- deploy a production service

## Authoritative status

This document is the authoritative statement of the project's business
objective.

Changes to this artifact may affect the churn definition, evaluation
metrics, intervention policy, reports, and project wiki.
