## Second Highest Salary

### Problem Statement
Identify the second-highest salary in each department. The output should include:

1. **Department**
2. **Second-highest salary**
3. **Employee ID(s)**

The following conditions apply:
- Do not remove duplicate salaries when ordering.
- Apply rankings without gaps in the rank. For example, if multiple employees share the same highest salary, the second-highest salary is the next unique salary below the highest.

#### Table: `employee_data`
| Column       | Type    | Description                       |
|--------------|---------|-----------------------------------|
| department   | text    | Name of the department.           |
| employee_id  | bigint  | Unique ID of the employee.        |
| hire_date    | datetime| Date the employee was hired.      |
| rank         | double  | Rank of the employee.             |
| salary       | bigint  | Salary of the employee.           |

---

### Query Solution

The following SQL query correctly identifies the second-highest salary in each department:

```sql
WITH cte AS (
    SELECT 
        department,
        employee_id,
        salary,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_salary
    FROM 
        employee_data
)
SELECT 
    department,
    employee_id,
    salary
FROM 
    cte
WHERE 
    rank_salary = 2;
```

### Explanation

1. **Common Table Expression (CTE)**:
   - The `cte` calculates a rank for each employee's salary within their department using the `DENSE_RANK()` window function.
     - `PARTITION BY department`: Ensures ranking is done separately for each department.
     - `ORDER BY salary DESC`: Ranks salaries from highest to lowest.
     - Employees with the same salary receive the same rank.

2. **Filtering for Rank 2**:
   - The `WHERE rank_salary = 2` condition selects employees with the second-highest salary in their department.

3. **Output Columns**:
   - `department`: Name of the department.
   - `employee_id`: Employee(s) with the second-highest salary.
   - `salary`: The second-highest salary.

---

### Example Dataset

#### Input Data: `employee_data`
| department   | employee_id | salary  |
|--------------|-------------|---------|
| HR           | 101         | 90000   |
| HR           | 102         | 85000   |
| HR           | 103         | 85000   |
| IT           | 201         | 120000  |
| IT           | 202         | 100000  |
| IT           | 203         | 95000   |
| IT           | 204         | 95000   |

#### Output:
| department   | employee_id | salary  |
|--------------|-------------|---------|
| HR           | 102         | 85000   |
| HR           | 103         | 85000   |
| IT           | 202         | 100000  |

---

### Key Points
1. **Handling Ties**:
   - `DENSE_RANK()` ensures that employees with the same salary are assigned the same rank.
   - All employees with the second-highest salary are included in the result.

2. **No Gaps in Ranking**:
   - If there are multiple employees with the highest salary, the next unique salary receives a rank of `2`.

3. **Indexes for Optimization**:
   - Indexing `department` and `salary` can improve performance for large datasets.

---

### Learning Outcomes
- Proper use of `DENSE_RANK()` for ranking scenarios with ties.
- Filtering specific ranks using a CTE for cleaner and more modular SQL queries.
- Handling multiple qualifying results when duplicate values exist in a dataset.
