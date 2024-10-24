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
| 21-25      | 35.56     | 64.44     |
| 26-30      | 43.18     | 56.82     |
| 31-35      | 49.15     | 50.85     |

## Solution

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

## Explanation

1. We start by creating a Common Table Expression (CTE) named `snap_stats`:
   - We join the `activities` table with the `age_breakdown` table using the `user_id` field.
   - We use `SUM` and `CASE` statements to calculate the total time spent on sending and opening snaps separately, as well as the total time for both activities.
   - We filter activities to include only 'send' and 'open' types.
   - Results are grouped by age bucket.

2. In the main query, we use the `snap_stats` CTE to calculate percentages:
   - We divide the time spent on each activity by the total time and multiply by 100.0 to get percentages.
   - We use `ROUND` to limit the result to 2 decimal places.

3. Finally, we order the results by age bucket for consistent output.

## Complexity Analysis
- Time Complexity: O(n), where n is the number of rows in the activities table. We need to scan through all relevant activities once.
- Space Complexity: O(m), where m is the number of distinct age buckets. This is the space needed to store the grouped results in the CTE and final output.

## Alternative Approaches
An alternative approach could directly calculate percentages without using a CTE, but it would be less readable and potentially less efficient:

```sql
SELECT ab.age_bucket,
ROUND(SUM(CASE WHEN activity_type = 'send' THEN a.time_spent ELSE 0 END) / 
      SUM(CASE WHEN activity_type IN ('send','open') THEN a.time_spent ELSE 0 END) * 100, 2) AS send_perc,
ROUND(SUM(CASE WHEN activity_type = 'open' THEN a.time_spent ELSE 0 END) / 
      SUM(CASE WHEN activity_type IN ('send','open') THEN a.time_spent ELSE 0 END) * 100, 2) AS open_perc
FROM activities a
JOIN age_breakdown ab ON a.user_id = ab.user_id
GROUP BY ab.age_bucket
ORDER BY ab.age_bucket;
```

## Key Concepts
- Common Table Expressions (CTE)
- JOIN operations
- Aggregate functions (SUM, ROUND)
- CASE statements
- Percentage calculations

## Additional Notes
- This solution assumes that there are activities of type 'send' and 'open' for each age bucket. If an age bucket has no activities, it won't appear in the output.
- Using `100.0` instead of `100` ensures floating-point division, avoiding potential issues with integer division.
- The `ORDER BY` clause ensures consistent output ordering, which is important for presentation and testing.

## Difficulty
Medium

## Related Topics
- Data Manipulation
- Aggregation
- Percentage Calculations
- Grouping
- Common Table Expressions

## Source
[DataLemur](https://datalemur.com/questions/time-spent-snaps)
