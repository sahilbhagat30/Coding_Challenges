# 💰 Total Salary by Department

**Last Updated:** January 2025  
**Companies:** Siemens, Amazon  
**ID:** 9869  
**Level:** Easy  
**Roles:** Data Engineer, Data Scientist, BI Analyst, Data Analyst, ML Engineer

---

## ❓ Problem Statement

Calculate the **total salary** for each department.  
Output the **department name** along with the **total salary**.

---

## 🗃️ Table Used

### `worker`
| Column        | Type    |
|---------------|---------|
| worker_id     | bigint  |
| first_name    | text    |
| last_name     | text    |
| department    | text    |
| salary        | bigint  |
| joining_date  | date    |

---

## ✅ Correct SQL Query

```sql
SELECT
  department,
  SUM(salary) AS total_salary
FROM
  worker
GROUP BY
  department;
```

---

## 💡 Explanation

- `SUM(salary)`: Aggregates salaries for each department.
- `GROUP BY department`: Groups records by department name.
- The alias `total_salary` is optional but improves readability.

---

## 📟 Sample Output

| department | total_salary |
|------------|--------------|
| Admin      | 1260000      |
| Account    | 350000       |
| HR         | 550000       |

---

Let me know if you'd like this exported or visualized!

