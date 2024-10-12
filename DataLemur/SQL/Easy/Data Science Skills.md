# Data Science Skills

## Problem Statement
Given a table of candidates and their skills, you're tasked with finding candidates who are proficient in Python, Tableau, and PostgreSQL.

## Table Structure
**candidates** table:
| Column Name  | Type    |
|--------------|---------|
| candidate_id | integer |
| skill        | varchar |

## Expected Output
| candidate_id |
|--------------|
| 123          |

## Solution

```sql
SELECT candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id ASC;
```

## Explanation

1. We start by selecting from the candidates table:
   - We use `WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')` to filter for the required skills.
   - The `GROUP BY candidate_id` groups the results by each candidate.

2. In the HAVING clause:
   - We use `COUNT(skill) = 3` to ensure that each candidate has all three required skills.

3. Finally:
   - We `ORDER BY candidate_id ASC` to sort the results as required.

This solution efficiently identifies candidates with all the required skills without using subqueries or complex joins.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of rows in the candidates table. This is due to the sorting operation.
- Space Complexity: O(m), where m is the number of unique candidates with at least one of the required skills.

## Alternative Approaches
An alternative approach could use a self-join or subqueries, but this solution is more efficient and readable for this specific problem.

## Key Concepts
- Aggregation
- GROUP BY
- HAVING
- Subqueries (potentially)

## Additional Notes
- This problem tests your ability to filter candidates based on multiple criteria.
- Pay attention to how you handle the requirement for all three skills.

## Difficulty
Easy

## Related Topics
- Data Manipulation
- Filtering
- Aggregation

## Source
DataLemur
