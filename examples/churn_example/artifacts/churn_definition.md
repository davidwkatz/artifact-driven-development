# Churn Definition

## Version

Version: 1.0

## Definition

A customer is considered churned when either of the following occurs:

1. The customer explicitly cancels the subscription.
2. The customer records no meaningful product activity for 60
   consecutive days.

## Meaningful product activity

Meaningful product activity includes:

- logging into the application
- creating or editing a project
- running a report
- exporting data
- inviting another user

The following do not count as meaningful activity:

- receiving an automated email
- opening a marketing email
- viewing a public documentation page
- receiving an invoice

## Churn date

For an explicit cancellation, the churn date is the effective
cancellation date.

For inactivity churn, the churn date is the 60th consecutive day without
meaningful activity.

## Prediction label

At a scoring date, the churn label is 1 when the customer churns within
the next 30 days.

Otherwise, the label is 0.

## Eligibility

A customer is eligible for scoring when:

- the subscription is active on the scoring date
- the customer has been subscribed for at least 30 days
- sufficient activity history is available to calculate the features

## Known limitations

This definition combines contractual churn and behavioral inactivity.

A customer may be labeled as churned because of inactivity even when the
subscription remains active.

The 60-day inactivity threshold is a business assumption and has not yet
been validated empirically.

## Authoritative status

This document is the authoritative business definition of churn.

The executable label specification must implement this definition.

Changes to this artifact may affect:

- label specification
- training dataset
- trained models
- evaluation reports
- segment analysis
- retention policy
- monitoring rules
- project wiki
