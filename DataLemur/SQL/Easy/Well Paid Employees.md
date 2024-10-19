# Well Paid Employees

## Problem Statement
As an HR Analyst, you're asked to identify all employees who earn more than their direct managers. The result should include the employee's ID and name.

## Table Structure
**employee** table:
| Column Name   | Type    |
|---------------|---------|
| employee_id   | integer |
| name          | string  |
| salary        | integer |
| department_id | integer |
| manager_id    | integer |

## Expected Output
| employee_id | employee_name |
|-------------|---------------|
| 3           | Olivia Smith  |

## Solution

```sql
SELECT e.employee_id, e.name AS employee_name
FROM employee e
JOIN employee m ON e.manager_id = m.employee_id
WHERE e.salary > m.salary
ORDER BY e.employee_id;

```

## Explanation

1. We use a self-join on the employee table, joining it with itself.
2. The join condition `e.manager_id = m.employee_id` links each employee to their manager.
3. The WHERE clause `e.salary > m.salary` filters for employees who earn more than their managers.
4. We select only the employee_id and name of the employees who meet this condition.
5. The results are ordered by employee_id for consistency.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of employees. This is due to the join operation and the sorting (ORDER BY).
- Space Complexity: O(m), where m is the number of employees who earn more than their managers.

## Alternative Approaches
An alternative approach could use a subquery instead of a join, but the join method is generally more efficient for this problem.

## Key Concepts
- Self-join
- Comparison operations
- Filtering with WHERE clause

## Additional Notes
- This solution assumes that the manager_id in the employee table corresponds to a valid employee_id of another employee in the same table.
- Employees with NULL as manager_id (likely top-level managers) are automatically excluded from the result.

## Difficulty
Easy

## Related Topics
- Data Manipulation
- Joins
- Filtering

## Source
[DataLemur](https://datalemur.com/questions/sql-well-paid-employees)
