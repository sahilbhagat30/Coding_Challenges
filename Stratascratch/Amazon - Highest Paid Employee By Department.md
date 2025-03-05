# Highest Paid Employee By Department

## **Problem Statement**
Determine the highest salary and employee ID for each department.

### **Expected Output**
Your output should include:
- `department`
- `worker_id`
- `salary`

If there is a tie (multiple employees with the highest salary in a department), include all of them.

### **Database Schema**
#### **worker Table**
| Column Name   | Data Type  |
|--------------|-----------|
| worker_id    | bigint    |
| first_name   | text      |
| last_name    | text      |
| salary       | bigint    |
| joining_date | datetime  |
| department   | text      |

---

## **Solution 1: Using `MAX()` and `JOIN`**
```sql
WITH cte AS (
    SELECT 
        department, 
        MAX(salary) AS highest_salary 
    FROM worker 
    GROUP BY department
)
SELECT 
    w.department, 
    w.worker_id, 
    w.salary
FROM worker w
JOIN cte 
    ON cte.department = w.department 
    AND cte.highest_salary = w.salary;
```

### **Explanation:**
1. **CTE (`cte`)**: Computes the highest salary per department.
2. **JOIN**: Retrieves employees who have that highest salary, ensuring ties are included.

---

## **Solution 2: Using `DENSE_RANK()`**
If you want a ranking-based approach:
```sql
WITH ranked_salaries AS (
    SELECT 
        department, 
        worker_id, 
        salary, 
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_num
    FROM worker
)
SELECT 
    department, 
    worker_id, 
    salary
FROM ranked_salaries
WHERE rank_num = 1;
```

### **Why Use `DENSE_RANK()`?**
✅ Ensures employees with the **same highest salary** are included.  
✅ More **efficient and scalable** when ranking multiple salary levels.  
✅ Avoids explicit `MAX()` calculation, making it **easier to adapt for further ranking analysis**.

---

## **Expected Output Format**
| department  | worker_id | salary  |
|------------|----------|--------|
| IT         | 1001     | 150000 |
| Finance    | 1005     | 145000 |
| HR         | 1010     | 140000 |

---

### **Conclusion**
Both solutions effectively find the highest-paid employees per department:
- **Solution 1 (`MAX() and JOIN`)** is simple and efficient.
- **Solution 2 (`DENSE_RANK()`)** is more flexible for ranking-based queries.

🚀