# Who Made Quota?

## Problem Statement
As a data analyst on the Oracle Sales Operations team, you are given a list of salespeople's deals and their annual quotas. Write a query that outputs each employee id and whether they hit the quota or not ('yes' or 'no'). Order the results by employee id in ascending order.

## Table Structure
**deals** table:
| Column Name | Type    |
|-------------|---------|
| employee_id | integer |
| deal_size   | integer |

**sales_quotas** table:
| Column Name | Type    |
|-------------|---------|
| employee_id | integer |
| quota       | integer |

## Expected Output
| employee_id | made_quota |
|-------------|------------|
| 101         | yes        |
| 201         | yes        |
| 301         | no         |

## Solution

```sql
WITH TOTAL_DEALS AS(
  SELECT 
    employee_id,
    SUM(deal_size) total
  FROM
    deals
  GROUP BY 
    employee_id
)
SELECT  
  sq.employee_id,
  CASE WHEN sq.quota > TOTAL_DEALS.total THEN 'no' ELSE 'yes' END made_quota
FROM  
  sales_quotas sq
JOIN TOTAL_DEALS ON TOTAL_DEALS.employee_id = sq.employee_id
ORDER BY sq.employee_id

```
## Explanation

1. We create a CTE named TOTAL_DEALS to sum up the deal sizes for each employee.
2. In the main query, we join the sales_quotas table with the TOTAL_DEALS CTE.
3. We use a CASE statement to compare the quota with the total deal size and output 'yes' or 'no'.
4. The results are ordered by employee_id.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of employees. This is due to the sorting operation and the join.
- Space Complexity: O(n), where n is the number of employees, to store the CTE and the result set.

## Alternative Approaches
A more efficient approach could use a LEFT JOIN and perform the aggregation in the main query:

```sql
SELECT 
  sq.employee_id,
  CASE WHEN sq.quota <= COALESCE(SUM(d.deal_size), 0) THEN 'yes' ELSE 'no' END AS made_quota
FROM 
  sales_quotas sq
LEFT JOIN 
  deals d ON sq.employee_id = d.employee_id
GROUP BY 
  sq.employee_id, sq.quota
ORDER BY 
  sq.employee_id
````

This approach ensures all employees are included, even those without deals, and may be more efficient for larger datasets.

## Key Concepts
- Aggregation (SUM)
- JOINs
- CASE statements
- GROUP BY clause
- Common Table Expressions (CTE)

## Additional Notes
- The solution assumes that all employees in the sales_quotas table have corresponding entries in the deals table. If this is not the case, a LEFT JOIN should be used instead.
- The alternative approach uses COALESCE to handle NULL values for employees without deals.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- Conditional Logic
- Joins

## Source
[DataLemur](https://datalemur.com/questions/oracle-sales-quota)
