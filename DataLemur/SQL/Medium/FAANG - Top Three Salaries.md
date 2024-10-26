# Top Three Salaries

## Problem Statement
You are tasked with retrieving the top three salaries from each department in a company. If there are ties in salaries, include all employees with the same salary. The output should include the department name, employee name, and salary.

## Table Structure
**employee** table:
| Column Name   | Type      |
|---------------|-----------|
| employee_id   | integer   |
| name          | string    |
| salary        | decimal   |
| department_id | integer   |

**department** table:
| Column Name      | Type    |
|------------------|---------|
| department_id    | integer |
| department_name  | string  |

## Expected Output
| department_name | name         | salary   |
|-----------------|--------------|----------|
| Sales           | John Doe     | 90000.00 |
| Sales           | Jane Smith   | 90000.00 |
| Sales           | Alice Brown  | 85000.00 |
| Engineering     | Bob White    | 95000.00 |
| Engineering     | Charlie Black| 90000.00 |

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
```
## Solution Outline

1. **Common Table Expression (CTE)**:
   - We use a CTE to rank each employee within their department based on their salary.
   - The `DENSE_RANK()` function, partitioned by `department_id` and ordered by salary in descending order, assigns a ranking to each employee’s salary within their department.
   - Using `DENSE_RANK()` ensures that employees with the same salary receive the same rank, allowing ties in the top three salaries to be included.

2. **Filtering for Top Three Salaries**:
   - In the main query, we filter the CTE to include only rows where the rank (`emp_rank`) is 3 or less, capturing the top three salaries in each department.
   - If a tie occurs within the top three salaries, all employees with that salary are included in the result.

3. **Ordering Results**:
   - The final result is ordered by `department_name` (alphabetically), `salary` (highest to lowest), and `name` (alphabetically within the same salary) for a clear and structured output.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of rows in the `employee` table, primarily due to the `DENSE_RANK()` window function, which sorts salaries within each department.
- **Space Complexity**: O(n), as the CTE stores ranking information for each employee in the table.

## Key Concepts
- **Window Functions** (`DENSE_RANK()`)
- **Filtering with Ranking**
- **JOIN Operations**

## Additional Notes
- This solution includes all employees with the same salary if it falls within the top three, ensuring fair representation in case of ties.
- The query assumes each employee is associated with only one department, simplifying the ranking process within each department.

## Difficulty
Medium

## Related Topics
- **Ranking Functions in SQL**
- **Partitioning with Window Functions**
- **Data Aggregation and Filtering**

## Source
[DataLemur](https://datalemur.com/questions/top-three-salaries)
