# Workers With The Highest And Lowest Salaries

## **Problem Statement**
You have been asked to find the employees with the highest and lowest salaries across the whole dataset.

Your output should include:
- The employee's **ID** (`worker_id`)
- Their **salary**
- The employee's **department**
- A column **salary_type** that categorizes the output by:
  - **'Highest Salary'** representing the highest salary
  - **'Lowest Salary'** representing the lowest salary

### **Database Schema**
#### **worker Table**
| Column Name   | Data Type |
|--------------|-----------|
| worker_id    | bigint    |
| first_name   | text      |
| last_name    | text      |
| salary       | bigint    |
| joining_date | datetime  |
| department   | text      |

#### **title Table**
| Column Name    | Data Type |
|---------------|-----------|
| worker_ref_id | bigint    |
| worker_title  | text      |
| affected_from | datetime  |

---

## **Solution 1: Using Window Functions**
```sql
WITH cte AS (
    SELECT
        worker_id,
        salary,
        department,
        MAX(salary) OVER() AS highest_salary,
        MIN(salary) OVER() AS lowest_salary
    FROM worker
),
cte1 AS (
    SELECT
        worker_id,
        salary,
        department,
        CASE
            WHEN salary = highest_salary THEN 'Highest Salary'
            WHEN salary = lowest_salary THEN 'Lowest Salary'
        END AS salary_type
    FROM cte
)
SELECT
    worker_id,
    salary,
    department,
    salary_type
FROM cte1
WHERE salary_type IS NOT NULL;
```

### **Explanation:**
1. **CTE (`cte`)**: Computes the highest and lowest salaries using window functions (`MAX() OVER()` and `MIN() OVER()`).
2. **CTE (`cte1`)**: Assigns a `salary_type` label based on the computed salary extremes.
3. **Final Query**: Filters out employees that do not match the highest or lowest salary.

---

## **Solution 2: Optimized Approach with CTE and JOIN**
```sql
WITH salary_extremes AS (
    SELECT
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
    FROM worker
)
SELECT
    w.worker_id,
    w.salary,
    w.department,
    CASE
        WHEN w.salary = s.highest_salary THEN 'Highest Salary'
        WHEN w.salary = s.lowest_salary THEN 'Lowest Salary'
    END AS salary_type
FROM worker w
JOIN salary_extremes s
ON w.salary = s.highest_salary OR w.salary = s.lowest_salary;
```

### **Why is this the Best Approach?**
✅ **Performance Optimization**: Computes `MAX()` and `MIN()` **only once**, reducing redundant calculations.  
✅ **Better Readability**: A clear separation between computing salary extremes and filtering employees.  
✅ **Faster Execution**: Uses a **JOIN** instead of repeated window function calculations.  

---

## **Expected Output Format**
| worker_id | salary  | department | salary_type     |
|-----------|--------|------------|----------------|
| 1001      | 150000 | IT         | Highest Salary |
| 1002      | 30000  | HR         | Lowest Salary  |

---

### **Conclusion**
Both queries provide correct results, but Solution 2 is **more efficient** in large datasets due to reduced computation overhead. 🚀

