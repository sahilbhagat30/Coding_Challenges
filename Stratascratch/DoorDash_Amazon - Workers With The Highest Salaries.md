### Query: Workers with the Highest Salaries

#### Objective:
The goal of this query is to identify the job titles of workers with the highest salary from the `worker` and `title` tables.

#### Dataset Details:
- **Table 1**: `worker`
  - `department` (text)
  - `first_name` (text)
  - `joining_date` (datetime)
  - `last_name` (text)
  - `salary` (bigint)
  - `worker_id` (bigint)

- **Table 2**: `title`
  - `affected_from` (datetime)
  - `worker_ref_id` (bigint)
  - `worker_title` (text)

#### SQL Query:
```sql
SELECT
    worker_title
FROM
    (
        SELECT 
            t.worker_title,
            w.salary,
            MAX(w.salary) OVER() max_salary
        FROM
            title t
        JOIN 
            worker w ON t.worker_ref_id = w.worker_id
    ) AS t
WHERE max_salary = salary;
```

#### Explanation:
1. **Inner Query**:
   - Join the `title` table with the `worker` table on `worker_ref_id` and `worker_id` respectively.
   - Select `worker_title` and `salary` from the joined tables.
   - Use the `MAX()` window function to compute the maximum salary across all workers and assign it to `max_salary`.

2. **Outer Query**:
   - Filter the results to include only rows where the `salary` equals `max_salary`.
   - Select the `worker_title` of the workers who earn the highest salary.

#### Output Columns:
- `worker_title`: The job title(s) of the worker(s) with the highest salary.

#### Use Case:
This query is useful for identifying the roles or job titles associated with the highest-paid employees in an organization, providing insights into salary distribution and top-paying positions.
