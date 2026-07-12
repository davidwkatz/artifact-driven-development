# Open Questions

## Business questions

1. Should explicit cancellation and inactivity churn be modeled
   separately?

2. Is 60 days without meaningful activity the correct inactivity
   threshold?

3. Should customers with failed payments be treated as churned?

4. Should the prediction horizon be 30 days, 60 days, or another period?

5. What intervention capacity should be assumed?

## Data questions

1. How should multiple subscriptions owned by one customer be handled?

2. Are activity timestamps complete and reliable?

3. Can late-arriving cancellation records change historical labels?

4. How much history is required before a customer becomes eligible?

## Modeling questions

1. Should predictions be made weekly or daily?

2. Is probability calibration required?

3. Which customer segments require separate evaluation?

4. How should class imbalance be handled?

## Policy questions

1. What risk threshold should trigger outreach?

2. Should recent support complaints increase or decrease outreach
   priority?

3. Which customers should never receive automated retention outreach?

## Status convention

Each question will eventually receive one of these states:

- open
- under investigation
- decided
- deferred
