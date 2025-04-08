# 🧑‍💼 Workers Who Are Also Managers

**Last Updated:** January 2025  
**Companies:** DoorDash, Bosch, Amazon, Medium  
**ID:** 9848  
**Level:** 25  
**Roles Covered:**  
`Data Engineer`, `Data Scientist`, `BI Analyst`, `Data Analyst`, `ML Engineer`, `Software Engineer`

---

## ❓ Problem Statement

Find all employees who **have or had** a job title that **includes** the word _"manager"_.

---

## 🗃️ Tables Used

### `worker`
| Column        | Type    |
|---------------|---------|
| worker_id     | bigint  |
| first_name    | text    |
| last_name     | text    |
| department    | text    |
| salary        | bigint  |
| joining_date  | date    |

### `title`
| Column         | Type    |
|----------------|---------|
| worker_ref_id  | bigint  |
| worker_title   | text    |
| affected_from  | date    |

---

## ✅ Solution

```sql
SELECT
  w.first_name,
  t.worker_title
FROM
  title t
JOIN
  worker w
ON
  w.worker_id = t.worker_ref_id
WHERE
  LOWER(t.worker_title) LIKE '%manager%';
```

---

## 💡 Explanation

- We join the `worker` and `title` tables using `worker_id` and `worker_ref_id`.
- The `WHERE` clause uses `LIKE '%manager%'` (in lowercase) to ensure all variations like:
  - `Manager`
  - `Senior Manager`
  - `Product Manager`
  - etc.
  are included.
- The result returns the employee's `first_name` and the matching `worker_title`.

---

## 📟 Sample Output

| first_name | worker_title     |
|------------|------------------|
| Monika     | Manager          |
| Vivek      | Manager          |

---

Let me know if you'd like this saved as a downloadable `.md` file or pushed to GitHub!

