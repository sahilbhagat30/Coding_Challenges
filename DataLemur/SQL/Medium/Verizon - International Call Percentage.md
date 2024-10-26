# International Call Percentage Problem

## Problem Statement
Given two tables, `phone_calls` and `phone_info`, the task is to calculate the percentage of calls that are international. A call is considered international if the `country_id` of the caller differs from the `country_id` of the receiver. The result should be rounded to one decimal place.

## Table Structure
**phone_calls** table:
| Column Name | Type    |
|-------------|---------|
| caller_id   | integer |
| receiver_id | integer |

**phone_info** table:
| Column Name | Type    |
|-------------|---------|
| caller_id   | integer |
| country_id  | integer |

## Expected Output
| international_call_pct |
|------------------------|
| ...                    |

```sql
SELECT 
  ROUND(
    100.0 * SUM(CASE
      WHEN caller.country_id <> receiver.country_id THEN 1 ELSE NULL END)/COUNT(*) ,1) AS international_call_pct
FROM phone_calls AS calls
LEFT JOIN phone_info AS caller
  ON calls.caller_id = caller.caller_id
LEFT JOIN phone_info AS receiver
  ON calls.receiver_id = receiver.caller_id;
```

```sql
SELECT
  ROUND(100.0*COUNT(*)/(SELECT COUNT(caller_id)
FROM
  phone_calls),1)
FROM
  phone_calls pc
JOIN
  phone_info phi_c
ON phi_c.caller_id = pc.caller_id 
JOIN
  phone_info phi_r
ON phi_r.caller_id = pc.receiver_id 
WHERE phi_c.country_id != phi_r.country_id
```
## Solution Outline

There are two main query approaches to solve this problem:

1. **Query 1**:
   - Uses `JOIN` to link `phone_calls` with `phone_info` for both the caller and receiver country information.
   - Calculates the total call count with a subquery, which is then used to determine the percentage of international calls.

2. **Query 2**:
   - Uses `LEFT JOIN` to ensure all calls are included in the calculation, even if information for either caller or receiver is missing in `phone_info`.
   - Uses a `CASE` statement within a `SUM` function to conditionally count international calls, then divides by the total count in the main query without a subquery.

## Comparison and Recommendation

- **Efficiency**: Query 2 is more efficient because it avoids the use of a subquery, performing only one scan of `phone_calls`.
- **Readability**: Query 2 is more concise and easier to follow, using a single `SELECT` statement with conditional aggregation.
- **Completeness**: Query 2 uses `LEFT JOIN`, ensuring all calls are counted even if there are missing entries in `phone_info`. This makes it more robust in scenarios where `phone_info` might not have complete data.

### Final Recommendation
**Query 2** is the preferred solution due to its efficiency, readability, and robustness.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of rows in `phone_calls`, as it only requires a single scan for the main query.
- **Space Complexity**: O(1), as no additional storage is required beyond the basic aggregates.

## Key Concepts
- **JOIN operations** and **LEFT JOIN** to handle missing data
- **Conditional Aggregation** with `CASE` statements
- **Division and Percentage Calculations** in SQL

## Additional Notes
- This solution assumes that the `phone_calls` table might contain calls without complete information in `phone_info`, so using `LEFT JOIN` ensures the completeness of the result.
- Rounding to one decimal place with `ROUND` ensures a precise output format for the final percentage.

## Difficulty
Medium

## Related Topics
- **Conditional Aggregation**
- **JOINs and Filtering**
- **Percentage Calculations in SQL**

## Source
[DataLemur](https://datalemur.com/questions/international-call-percentage)
