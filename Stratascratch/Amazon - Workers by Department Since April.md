# 🧑‍💻 Workers by Department Since April

**Last Updated:** March 2025  
**Company:** Amazon  
**ID:** 9847  
**Level:** Easy  
**Roles:** Data Engineer, Data Scientist, BI Analyst, Data Analyst, ML Engineer

---

## ❓ Problem Statement

Find the number of workers by department who joined on or after **April 1, 2014**.

**Output:**  
- `department`  
- `count` of workers

**Order by** the count of workers **in descending order**.

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
  COUNT(worker_id) AS count
FROM
  worker
WHERE
  joining_date >= '2014-04-01'
GROUP BY
  department
ORDER BY
  count DESC;
```

---

## 💡 Explanation

- `WHERE joining_date >= '2014-04-01'`: Filters only those who joined on or after April 1, 2014.
- `GROUP BY department`: Groups the data by department.
- `COUNT(worker_id)`: Counts the number of workers in each department.
- `ORDER BY count DESC`: Sorts the result with the most workers first.

---

## 📟 Sample Output

| department | count |
|------------|-------|
| Admin      | 4     |
| Account    | 1     |
| HR         | 1     |

---

Let me know if you'd like to build a chart or export this!

