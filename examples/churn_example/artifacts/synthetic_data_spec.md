# Synthetic Data Specification

## Purpose

This artifact defines how synthetic customer, subscription, activity,
support, and payment data should be generated for the churn example.

The generator must produce data that conforms to
`artifacts/source_data_contract.md`.

## Dataset size

Generate 5,000 customers.

The data should cover approximately 18 months of customer history.

## Customer segments

Use these segment proportions:

* `small`: 60 percent
* `mid_market`: 30 percent
* `enterprise`: 10 percent

## Regions

Assign customers to one of these regions:

* `north_america`
* `europe`
* `asia_pacific`
* `latin_america`

## Industries

Use a small fixed set of industries:

* software
* professional_services
* retail
* healthcare
* manufacturing
* education

## Subscription plans

Use these plans:

* `basic`
* `professional`
* `enterprise`

Monthly price should vary by plan and customer segment.

## Churn behavior

The generated data should include both:

* explicit cancellation churn
* inactivity-based churn

The overall churn rate should be high enough to support meaningful model
evaluation.

Target an overall churn rate between 15 and 25 percent.

## Segment effects

Churn probability should differ by segment:

* small customers should churn most often
* mid-market customers should churn less often
* enterprise customers should churn least often

## Behavioral signals

The generated data should contain useful but imperfect churn signals.

Customers at elevated churn risk should be more likely to exhibit:

* declining meaningful activity
* longer gaps between activity events
* failed payments
* low support satisfaction
* high-priority support tickets
* recent support activity
* shorter subscription tenure

No single feature should perfectly determine churn.

## Activity behavior

Meaningful activity should include:

* login
* project_created
* project_edited
* report_run
* data_exported
* user_invited

Non-meaningful activity may include:

* marketing_email_opened
* invoice_received
* documentation_viewed

Active customers should generally have more meaningful events than
customers approaching churn.

## Support behavior

Most customers should have few or no support tickets.

Customers at higher churn risk should be somewhat more likely to have:

* more support tickets
* high-priority tickets
* lower satisfaction scores

Some satisfaction scores should be missing.

## Payment behavior

Most payments should succeed.

A minority of customers should have:

* failed payments
* refunded payments

Failed payments should increase churn probability, but should not
guarantee churn.

## Cancellation behavior

Explicit cancellation dates must occur after subscription start dates.

Customers who churn through inactivity may retain an active subscription
status in the raw subscription table.

This distinction is intentional and supports the business churn
definition.

## Reproducibility

The generator must accept a random seed.

Running the generator with the same seed and configuration should produce
the same outputs.

## Output files

The generator must create:

* `data/raw/customers.csv`
* `data/raw/subscriptions.csv`
* `data/raw/activity_events.csv`
* `data/raw/support_tickets.csv`
* `data/raw/payments.csv`

## Validation expectations

After generation, the process should report:

* row counts for each file
* total customer count
* explicit cancellation rate
# Synthetic Data Specification

## Purpose

This artifact defines how synthetic customer, subscription, activity,
support, and payment data should be generated for the churn example.

The generator must produce data that conforms to
`artifacts/source_data_contract.md`.

## Dataset size

Generate 5,000 customers.

The data should cover approximately 18 months of customer history.

## Customer segments

Use these segment proportions:

* `small`: 60 percent
* `mid_market`: 30 percent
* `enterprise`: 10 percent

## Regions

Assign customers to one of these regions:

* `north_america`
* `europe`
* `asia_pacific`
* `latin_america`

## Industries

Use a small fixed set of industries:

* software
* professional_services
* retail
* healthcare
* manufacturing
* education

## Subscription plans

Use these plans:

* `basic`
* `professional`
* `enterprise`

Monthly price should vary by plan and customer segment.

## Churn behavior

The generated data should include both:

* explicit cancellation churn
* inactivity-based churn

The overall churn rate should be high enough to support meaningful model
evaluation.

Target an overall churn rate between 15 and 25 percent.

## Segment effects

Churn probability should differ by segment:

* small customers should churn most often
* mid-market customers should churn less often
* enterprise customers should churn least often

## Behavioral signals

The generated data should contain useful but imperfect churn signals.

Customers at elevated churn risk should be more likely to exhibit:

* declining meaningful activity
* longer gaps between activity events
* failed payments
* low support satisfaction
* high-priority support tickets
* recent support activity
* shorter subscription tenure

No single feature should perfectly determine churn.

## Activity behavior

Meaningful activity should include:

* login
* project_created
* project_edited
* report_run
* data_exported
* user_invited

Non-meaningful activity may include:

* marketing_email_opened
* invoice_received
* documentation_viewed

Active customers should generally have more meaningful events than
customers approaching churn.

## Support behavior

Most customers should have few or no support tickets.

Customers at higher churn risk should be somewhat more likely to have:

* more support tickets
* high-priority tickets
* lower satisfaction scores

Some satisfaction scores should be missing.

## Payment behavior

Most payments should succeed.

A minority of customers should have:

* failed payments
* refunded payments

Failed payments should increase churn probability, but should not
guarantee churn.

## Cancellation behavior

Explicit cancellation dates must occur after subscription start dates.

Customers who churn through inactivity may retain an active subscription
status in the raw subscription table.

This distinction is intentional and supports the business churn
definition.

## Reproducibility

The generator must accept a random seed.

Running the generator with the same seed and configuration should produce
the same outputs.

## Output files

The generator must create:

* `data/raw/customers.csv`
* `data/raw/subscriptions.csv`
* `data/raw/activity_events.csv`
* `data/raw/support_tickets.csv`
* `data/raw/payments.csv`

## Validation expectations

After generation, the process should report:

* row counts for each file
* total customer count
* explicit cancellation rate
* inactivity churn rate
* total churn rate
* churn rate by segment
* failed-payment rate
* average meaningful events per customer

## Current limitations

The first version will not simulate:

* multiple subscriptions per customer
* subscription upgrades or downgrades
* customer mergers
* late-arriving events
* delayed payment reconciliation
* causal effects of retention outreach
* inactivity churn rate
* total churn rate
* churn rate by segment
* failed-payment rate
* average meaningful events per customer

## Current limitations

The first version will not simulate:

* multiple subscriptions per customer
* subscription upgrades or downgrades
* customer mergers
* late-arriving events
* delayed payment reconciliation
* causal effects of retention outreach
