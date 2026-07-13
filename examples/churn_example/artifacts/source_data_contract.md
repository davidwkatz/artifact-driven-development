# Source Data Contract

## Purpose

This artifact defines the raw source tables used by the churn example.

The synthetic data generator must produce files that conform to this contract.

## General conventions

* Dates use ISO 8601 format: `YYYY-MM-DD`.
* Timestamps use ISO 8601 format with UTC timezone.
* Identifiers are strings.
* Missing values are represented as empty fields in CSV files.
* Monetary values are expressed in U.S. dollars.
* One customer may have only one subscription in the first version of the example.

## `customers.csv`

One row per customer.

| Column           | Type    | Required | Description                                              |
| ---------------- | ------- | -------: | -------------------------------------------------------- |
| `customer_id`    | string  |      yes | Stable customer identifier                               |
| `signup_date`    | date    |      yes | Date the customer first subscribed                       |
| `segment`        | string  |      yes | Customer segment: `small`, `mid_market`, or `enterprise` |
| `region`         | string  |      yes | Geographic region                                        |
| `employee_count` | integer |      yes | Approximate company size                                 |
| `industry`       | string  |      yes | Customer industry                                        |

## `subscriptions.csv`

One row per customer subscription.

| Column              | Type   | Required | Description                        |
| ------------------- | ------ | -------: | ---------------------------------- |
| `subscription_id`   | string |      yes | Stable subscription identifier     |
| `customer_id`       | string |      yes | References `customers.customer_id` |
| `plan`              | string |      yes | Subscription plan                  |
| `monthly_price`     | number |      yes | Monthly subscription price         |
| `start_date`        | date   |      yes | Subscription start date            |
| `status`            | string |      yes | `active` or `cancelled`            |
| `cancellation_date` | date   |       no | Effective cancellation date        |

## `activity_events.csv`

One row per recorded product activity event.

| Column        | Type      | Required | Description                                             |
| ------------- | --------- | -------: | ------------------------------------------------------- |
| `event_id`    | string    |      yes | Stable event identifier                                 |
| `customer_id` | string    |      yes | References `customers.customer_id`                      |
| `event_time`  | timestamp |      yes | Time of the event                                       |
| `event_type`  | string    |      yes | Type of activity                                        |
| `meaningful`  | boolean   |      yes | Whether the event counts as meaningful product activity |

Meaningful activity types include:

* `login`
* `project_created`
* `project_edited`
* `report_run`
* `data_exported`
* `user_invited`

Non-meaningful event types may include:

* `marketing_email_opened`
* `invoice_received`
* `documentation_viewed`

## `support_tickets.csv`

One row per support ticket.

| Column               | Type      | Required | Description                        |
| -------------------- | --------- | -------: | ---------------------------------- |
| `ticket_id`          | string    |      yes | Stable ticket identifier           |
| `customer_id`        | string    |      yes | References `customers.customer_id` |
| `opened_at`          | timestamp |      yes | Time the ticket was opened         |
| `closed_at`          | timestamp |       no | Time the ticket was closed         |
| `priority`           | string    |      yes | `low`, `medium`, or `high`         |
| `category`           | string    |      yes | Ticket category                    |
| `satisfaction_score` | integer   |       no | Integer from 1 to 5                |

## `payments.csv`

One row per payment event.

| Column         | Type   | Required | Description                        |
| -------------- | ------ | -------: | ---------------------------------- |
| `payment_id`   | string |      yes | Stable payment identifier          |
| `customer_id`  | string |      yes | References `customers.customer_id` |
| `payment_date` | date   |      yes | Payment date                       |
| `amount`       | number |      yes | Payment amount                     |
| `status`       | string |      yes | `paid`, `failed`, or `refunded`    |

## Referential integrity

* Every `customer_id` in downstream files must exist in `customers.csv`.
* Every subscription must reference exactly one customer.
* Cancellation dates may only appear for cancelled subscriptions.
* Activity events must occur on or after the customer's signup date.
* Payment dates must occur on or after the subscription start date.

## Synthetic data requirements

The synthetic generator should produce:

* enough active and churned customers to support model evaluation
* different churn rates across segments
* realistic variation in activity frequency
* some explicit cancellations
* some inactivity-based churn
* some failed payments
* some missing support satisfaction scores

## Current limitations

The first version does not include:

* multiple subscriptions per customer
* plan upgrades or downgrades
* merged customer accounts
* delayed event ingestion
* currency conversion
* real personal or company information
