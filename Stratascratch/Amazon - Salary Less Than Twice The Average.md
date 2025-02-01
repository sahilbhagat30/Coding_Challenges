# Salary Less Than Twice The Average

## Interview Question Date: April 2022

### Companies:
- Amazon
- Walmart
- Best Buy
- Medium

### Roles:
- Data Engineer
- Data Scientist
- BI Analyst
- Data Analyst
- ML Engineer

## Problem Statement
Write a SQL query to get the list of managers whose salary is **less than twice the average salary of employees reporting to them**. The query should output:
- `manager_empl_id`: The manager's employee ID
- `manager_salary`: The salary of the manager
- `avg_emp_salary`: The average salary of employees reporting to the manager

### Tables Used:
#### `map_employee_hierarchy`
| Column Name      | Data Type |
|-----------------|-----------|
| empl_id         | text      |
| manager_empl_id | text      |

#### `dim_employee`
| Column Name  | Data Type |
|-------------|-----------|
| empl_city   | text      |
| empl_dob    | datetime  |
| empl_id     | text      |
| empl_name   | text      |
| empl_pin    | bigint    |
| salary      | bigint    |

---

## Best SQL Query Solution
```sql
WITH EmployeeAvgSalary AS (
    SELECT 
        meh.manager_empl_id,
        AVG(de.salary) AS avg_emp_salary
    FROM 
        map_employee_hierarchy meh
    JOIN 
        dim_employee de 
        ON de.empl_id = meh.empl_id
    GROUP BY 
        meh.manager_empl_id
)
SELECT 
    de.empl_id AS manager_empl_id,
    de.salary AS manager_salary,
    eavg.avg_emp_salary
FROM 
    dim_employee de
JOIN 
    EmployeeAvgSalary eavg 
    ON de.empl_id = eavg.manager_empl_id
WHERE 
    de.salary < 2 * eavg.avg_emp_salary;
```

---

## Explanation
1. **Compute the average salary of employees reporting to each manager**
   - We use a **Common Table Expression (CTE)** named `EmployeeAvgSalary` to calculate the average salary (`avg_emp_salary`) for each `manager_empl_id` by grouping data in `map_employee_hierarchy` and joining with `dim_employee`.
2. **Retrieve manager details efficiently**
   - Instead of using an additional join with `map_employee_hierarchy`, we directly join `dim_employee` with `EmployeeAvgSalary` to fetch the manager's salary.
3. **Filter the results**
   - The `WHERE` clause ensures we only select managers whose salary is **less than twice** the average salary of their employees.

---

## Expected Output Format
| manager_empl_id | manager_salary | avg_emp_salary |
|-----------------|---------------|---------------|
| 1001           | 120000        | 65000         |
| 1005           | 95000         | 48000         |

---

## Key Takeaways
- Optimized the SQL query by reducing unnecessary joins.
- Used a **Common Table Expression (CTE)** to efficiently precompute average salaries.
- Applied filtering using `WHERE` for accurate selection of managers.
- Ensured performance optimization by minimizing unnecessary computations.

This optimized query efficiently retrieves the required manager details while ensuring high performance through structured SQL best practices.
