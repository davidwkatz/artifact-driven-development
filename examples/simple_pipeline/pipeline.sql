-- Simple Pipeline Artifact Inspection
--
-- This SQL file shows the concrete artifacts in this example as inspectable
-- DuckDB relations. The dependency structure is described in artifacts.yaml.

create or replace view raw_events as
select *
from read_csv_auto('raw_events.csv');

create or replace view deduplicated_events as
select *
from read_csv_auto('deduplicated_events.csv');

create or replace view normalized_events as
select *
from read_csv_auto('normalized_events.csv');

create or replace view feature_table as
select *
from read_csv_auto('feature_table.csv');

create or replace view summary_table as
select *
from read_csv_auto('summary_table.csv');

-- Basic inspection queries

select 'raw_events' as artifact, count(*) as n_rows from raw_events
union all
select 'deduplicated_events' as artifact, count(*) as n_rows from deduplicated_events
union all
select 'normalized_events' as artifact, count(*) as n_rows from normalized_events
union all
select 'feature_table' as artifact, count(*) as n_rows from feature_table
union all
select 'summary_table' as artifact, count(*) as n_rows from summary_table;
