# Sending vs. Opening Snaps

## Problem Statement
Given tables with information on Snapchat users, including their ages and time spent sending and opening snaps, write a query to obtain a breakdown of the time spent sending vs. opening snaps as a percentage of total time spent on these activities grouped by age group. Round the percentage to 2 decimal places in the output.

## Table Structure
**activities** table:
| Column Name    | Type                            |
|----------------|-------------------------------- |
| activity_id    | integer                         |
| user_id        | integer                         |
| activity_type  | string ('send', 'open', 'chat') |
| time_spent     | float                           |
| activity_date  | datetime                        |

**age_breakdown** table:
| Column Name | Type                               |
|-------------|----------------------------------- |
| user_id     | integer                            |
| age_bucket  | string ('21-25', '26-30', '31-25') |

## Expected Output
| age_bucket | send_perc | open_perc |
|------------|-----------|-----------|
| 26-30      | 65.40     | 34.60     |
| 31-35      | 43.75     | 56.25     |

## Solution

```sql
SELECT ab.age_bucket,
ROUND(SUM(CASE WHEN activity_type = 'send' THEN a.time_spent ELSE 0 END) / 
      SUM(CASE WHEN activity_type IN ('send','open') THEN a.time_spent ELSE 0 END) * 100, 2) AS send_perc,
ROUND(SUM(CASE WHEN activity_type = 'open' THEN a.time_spent ELSE 0 END) / 
      SUM(CASE WHEN activity_type IN ('send','open') THEN a.time_spent ELSE 0 END) * 100, 2) AS open_perc
FROM activities a
JOIN age_breakdown ab ON a.user_id = ab.user_id
GROUP BY ab.age_bucket
```

## Alternative Approaches
A more efficient and readable approach uses a Common Table Expression (CTE) to first calculate the total times and then compute percentages:

```sql
WITH snap_stats AS (
  SELECT 
    ab.age_bucket,
    SUM(CASE WHEN a.activity_type = 'send' THEN a.time_spent ELSE 0 END) AS send_time,
    SUM(CASE WHEN a.activity_type = 'open' THEN a.time_spent ELSE 0 END) AS open_time,
    SUM(CASE WHEN a.activity_type IN ('send', 'open') THEN a.time_spent ELSE 0 END) AS total_time
  FROM activities a
  JOIN age_breakdown ab ON a.user_id = ab.user_id
  WHERE a.activity_type IN ('send', 'open')
  GROUP BY ab.age_bucket
)
SELECT 
  age_bucket,
  ROUND(100.0 * send_time / total_time, 2) AS send_perc,
  ROUND(100.0 * open_time / total_time, 2) AS open_perc
FROM snap_stats
ORDER BY age_bucket;
```