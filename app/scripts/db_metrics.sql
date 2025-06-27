-- Total Database Size
SELECT pg_size_pretty(pg_database_size(current_database()));

-- Size of All Tables
SELECT
  relname AS table_name,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
  pg_size_pretty(pg_relation_size(relid)) AS table_size,
  pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) AS index_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- Total Size of Tables
SELECT
  pg_size_pretty(SUM(pg_relation_size(relid))) AS total_table_data
FROM pg_catalog.pg_statio_user_tables;