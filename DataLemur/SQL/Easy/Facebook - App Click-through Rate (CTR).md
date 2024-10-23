# Click-Through Rate (CTR)

## Problem Statement
Facebook is analyzing its user engagement. Calculate the click-through rate (CTR) for each app in 2022. Round the results to 2 decimal places.

Definition:
CTR = Number of clicks / Number of impressions * 100.0

## Table Structure
**events** table:
| Column Name | Type      |
|-------------|-----------|
| app_id      | integer   |
| event_type  | string    |
| timestamp   | datetime  |

## Expected Output
| app_id | ctr    |
|--------|--------|
| 123    | 10.40  |
| 234    | 3.10   |

## Solution

```sql
SELECT 
  app_id,
  ROUND(
    100.0 * SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) / 
    NULLIF(SUM(CASE WHEN event_type = 'impression' THEN 1 ELSE 0 END), 0),
    2
  ) AS ctr
FROM
  events
WHERE 
  timestamp >= '2022-01-01' AND timestamp < '2023-01-01'
GROUP BY  
  app_id
