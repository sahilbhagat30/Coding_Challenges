# Top 10 Salaries

## **Problem Statement**
Find the top ten highest-paid employees from the dataset.

### **Expected Output**
Your output should include:
- `worker_id`
- `salary`
- `department`

The records should be sorted based on salary in **descending order**.

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

## **SQL Query to Find the Top 10 Salaries**
```sql
SELECT
    worker_id,
    salary,
    department
FROM worker
ORDER BY
    salary DESC
LIMIT 10;
```

### **Explanation:**
1. **Sorting Salaries**: The query orders salaries in descending order (`ORDER BY salary DESC`).
2. **Fetching Top 10 Records**: `LIMIT 10` ensures that only the top 10 highest-paid employees are retrieved.

---

## **Expected Output Format**
| worker_id | salary  | department |
|-----------|--------|------------|
| 1001      | 150000 | IT         |
| 1002      | 145000 | Finance    |
| 1003      | 140000 | HR         |
| 1004      | 135000 | Engineering|

---

## **Alternative Approach Using `DENSE_RANK()`**
If there are salary ties and you want to include all employees who share the 10th highest salary:
```sql
WITH salary_rank AS (
    SELECT
        worker_id,
        salary,
        department,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rank_num
    FROM worker
)
SELECT
    worker_id,
    salary,
    department
FROM salary_rank
WHERE rank_num <= 10;
```

### **Why Use `DENSE_RANK()`?**
✅ Ensures employees with the **same salary** are included.  
✅ Useful in cases where multiple employees earn the **same 10th highest salary**.

---

### **Conclusion**
Both approaches work well:
- The first method is **simple and efficient**.  
- The second method ensures **fair inclusion of tied salaries**.

🚀

