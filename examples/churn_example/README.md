# ADD Churn Example

This project demonstrates Artifact-Driven Development using a customer
churn prediction system.

The example is designed to show how project artifacts such as business
definitions, data contracts, feature specifications, datasets, models,
evaluations, policies, and documentation depend on one another.

## Central scenario

A fictional subscription software company wants to identify customers
at risk of churn so that its customer-success team can intervene.

The initial churn definition is:

> A customer has churned if the customer cancels the subscription or
> records no meaningful product activity for 60 consecutive days.

During the demonstration, this definition will be changed. The project
will then identify which downstream artifacts have become stale and
must be reviewed or rebuilt.

## Main artifact families

The completed example will include:

- business objective
- churn definition
- source-data contract
- label specification
- feature catalog
- training dataset
- model specification
- trained model
- evaluation report
- segment analysis
- retention policy
- project wiki
- context packets
- artifact dependency graph
- change-impact report

## Project stages

1. Define the business problem.
2. Generate synthetic source data.
3. Define labels and data contracts.
4. Build a training dataset.
5. Train baseline models.
6. Evaluate overall and segment-level performance.
7. Register artifact dependencies.
8. Detect stale artifacts after a definition changes.
9. Generate a project wiki.
10. Select context for specific project tasks.
