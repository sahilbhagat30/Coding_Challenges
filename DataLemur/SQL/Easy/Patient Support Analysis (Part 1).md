# Patient Support Analysis (Part 1)

## Problem Statement
UnitedHealth Group (UHG) has a program called Advocate4Me, which allows policy holders to call an advocate for support. Write a query to find how many UHG policy holders made three or more calls.

## Table Structure
**callers** table:
| Column Name         | Type      |
|---------------------|-----------|
| policy_holder_id    | integer   |
| case_id             | varchar   |
| call_category       | varchar   |
| call_date           | timestamp |
| call_duration_secs  | integer   |

## Expected Output
| policy_holder_count |
|---------------------|
| 1                   |

## Solution

```sql
WITH holder_count AS
(
SELECT
COUNT(policy_holder_id)	AS policy_holder_count
FROM callers
GROUP BY policy_holder_id
HAVING COUNT(policy_holder_id)>=3
)
SELECT COUNT(policy_holder_count)
FROM holder_count
```

## Explanation

1. We create a Common Table Expression (CTE) named `holder_count`:
   - It groups the callers by `policy_holder_id`
   - It counts the number of calls for each policy holder
   - It filters for policy holders with 3 or more calls using the HAVING clause

2. In the main query, we count the number of rows in the `holder_count` CTE, which gives us the number of policy holders who made 3 or more calls.

## Complexity Analysis
- Time Complexity: O(n), where n is the number of rows in the callers table. We need to scan through all rows once.
- Space Complexity: O(m), where m is the number of policy holders with 3 or more calls. This is the space needed to store the CTE.

## Alternative Approaches
An alternative approach could use a subquery instead of a CTE:

```sql
SELECT COUNT(*) AS policy_holder_count
FROM (
  SELECT policy_holder_id
  FROM callers
  GROUP BY policy_holder_id
  HAVING COUNT(*) >= 3
) AS frequent_callers;
```

This approach achieves the same result without using a CTE.

## Key Concepts
- Common Table Expressions (CTE)
- Aggregation (COUNT)
- GROUP BY and HAVING clauses

## Additional Notes
- The solution assumes that each row in the callers table represents a unique call.
- The HAVING clause is used instead of WHERE because we're filtering on an aggregate function.
- Both the main solution and the alternative approach have similar time and space complexities.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- CTEs
- Subqueries

## Source
[DataLemur](https://datalemur.com/questions/frequent-callers)
