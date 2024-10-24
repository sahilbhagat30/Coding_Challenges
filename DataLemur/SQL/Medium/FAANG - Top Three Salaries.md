# Top Three Salaries

## Problem Statement
You are tasked with retrieving the top three salaries from each department in a company. If there are ties in salaries, include all employees with the same salary. The output should include the department name, employee name, and salary.

## Table Structure
**employee** table:
| Column Name   | Type      |
|---------------|-----------|
| employee_id   | integer   |
| name          | string    |
| salary        | decimal    |
| department_id | integer    |

**department** table:
| Column Name   | Type      |
|---------------|-----------|
| department_id | integer   |
| department_name | string  |

## Expected Output
| department_name | name       | salary  |
|------------------|------------|---------|
| Sales            | John Doe  | 90000.00|
| Sales            | Jane Smith | 90000.00|
| Sales            | Alice Brown| 85000.00|
| Engineering      | Bob White  | 95000.00|
| Engineering      | Charlie Black| 90000.00|

## Solution

```sql
WITH CTE AS (
  SELECT 
    D.department_name,
    E.name,
    E.salary,
    DENSE_RANK() OVER (
      PARTITION BY E.department_id
      ORDER BY E.salary DESC
    ) AS emp_rank
  FROM 
    employee E
  JOIN
    department D ON E.department_id = D.department_id
)
SELECT
  department_name,
  name,
  salary
FROM
  CTE
WHERE emp_rank <= 3
ORDER BY 
  department_name ASC, 
  salary DESC, 
  name ASC;

