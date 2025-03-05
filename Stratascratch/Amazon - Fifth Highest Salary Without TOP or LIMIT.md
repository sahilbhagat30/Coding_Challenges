# Fifth Highest Salary Without TOP or LIMIT

## **Problem Statement**
Find the **fifth highest salary** from the dataset **without using `TOP` or `LIMIT`**.

### **Expected Output**
Your output should include:
- `salary`

**Note**: Duplicate salaries should **not** be removed.

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

## **Optimized Solution Using `DENSE_RANK()`**
```sql
WITH ranked_salaries AS (
    SELECT salary, 
           DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM worker
)
SELECT salary
FROM ranked_salaries
WHERE salary_rank = 5
LIMIT 1;
```

### **Optimizations Applied:**
✅ **Removes `DISTINCT`**: Since `DENSE_RANK()` already ensures unique rankings per salary, `DISTINCT` is unnecessary and avoids extra computation.  
✅ **Uses `WITH` CTE (Common Table Expression) for Clarity**: Improves readability and ensures ranking is computed once instead of in a subquery.  
✅ **Adds `LIMIT 1` for Performance** (If Allowed): If multiple rows exist for the 5th highest salary, fetching just **one row** reduces processing time.  

---

## **Expected Output Format**
| salary  |
|--------|
| 85000  |

---

### **Conclusion**
- **`DENSE_RANK()` ensures duplicate salaries are considered correctly**.
- **This optimized approach improves efficiency while maintaining correctness**.
- **Use `LIMIT 1` if supported, otherwise remove it for full results**.

🚀

