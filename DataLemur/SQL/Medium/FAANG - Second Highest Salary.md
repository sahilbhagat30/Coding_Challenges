# Second Highest Salary

## Problem Statement
As an HR analyst at a tech company, you're tasked with determining the second highest salary among all employees. In case of duplicate salaries, display the salary only once.

## Table Structure
**employee** table:
| Column Name   | Type    | Description                        |
|---------------|---------|----------------------------------- |
| employee_id   | integer | The unique ID of the employee      |
| name          | string  | The name of the employee           |
| salary        | integer | The salary of the employee         |
| department_id | integer | The department ID of the employee  |
| manager_id    | integer | The manager ID of the employee     |

## Expected Output
| second_highest_salary |
|-----------------------|
| 2230                  |

## Solution
```sql
SELECT MAX(SALARY) FROM employee WHERE SALARY < (SELECT MAX(SALARY) FROM employee);
```

## Explanation

1. The inner subquery `(SELECT MAX(SALARY) FROM employee)` finds the highest salary in the employee table.
2. The outer query then selects the maximum salary from all salaries that are less than this highest salary.
3. This effectively gives us the second highest salary.
4. By using `MAX()` in the outer query, we ensure that if there are multiple employees with the second highest salary, it's only displayed once.

## Complexity Analysis
- Time Complexity: O(n), where n is the number of employees. We need to scan the table twice (once for the subquery and once for the main query).
- Space Complexity: O(1), as we're only storing a single value (the second highest salary).

## Alternative Approaches
1. Using a CTE (Common Table Expression)
2. Using DENSE_RANK() window function
3. Using LIMIT and OFFSET

## Key Concepts
- Subqueries
- Aggregate functions (MAX)
- Comparison operations

## Additional Notes
- This solution assumes that there are at least two distinct salary values in the table.
- If there's only one distinct salary or the table is empty, this query will return NULL.

## Difficulty
Medium

## Related Topics
- Data Manipulation
- Subqueries
- Aggregation

## Source
[DataLemur](https://datalemur.com/questions/sql-second-highest-salary)
