-- Simple Pipeline Derivation Example
--
-- This SQL file derives the downstream artifacts from raw_events.csv.
-- The materialized CSV files in this directory are snapshots of the same
-- artifacts, useful for direct inspection and expected-output comparison.

create or replace view raw_events as
select
  event_id,
  entity_id,
  event_time,
  event_type,
  location,
  value_num
from read_csv_auto('raw_events.csv');

create or replace view deduplicated_events as
select distinct
  event_id,
  entity_id,
  event_time,
  event_type,
  location,
  value_num
from raw_events;

create or replace view normalized_events as
select
  event_id,
  entity_id,
  cast(event_time as timestamptz) as event_time,
  lower(trim(event_type)) as event_type,
  case lower(trim(location))
    when 'north marsh' then 'North Marsh'
    when 'south marsh' then 'South Marsh'
    else trim(location)
  end as location,
  cast(value_num as integer) as value_num
from deduplicated_events;

create or replace view feature_table as
select
  entity_id,
  count(*) as event_count,
  sum(value_num) as total_value_num,
  min(event_time) as first_event_time,
  max(event_time) as last_event_time,
  max(case when event_type = 'sighting' then 1 else 0 end) as has_sighting,
  max(case when event_type = 'feeding' then 1 else 0 end) as has_feeding,
  max(case when event_type = 'call' then 1 else 0 end) as has_call
from normalized_events
group by entity_id;

create or replace view summary_table as
select
  event_type,
  count(*) as event_count,
  sum(value_num) as total_value_num,
  count(distinct entity_id) as distinct_entities
from normalized_events
group by event_type;

-- Basic check of the derived artifact sizes.

select 'raw_events' as artifact, count(*) as n_rows from raw_events
union all
select 'deduplicated_events' as artifact, count(*) as n_rows from deduplicated_events
union all
select 'normalized_events' as artifact, count(*) as n_rows from normalized_events
union all
select 'feature_table' as artifact, count(*) as n_rows from feature_table
union all
select 'summary_table' as artifact, count(*) as n_rows from summary_table;
