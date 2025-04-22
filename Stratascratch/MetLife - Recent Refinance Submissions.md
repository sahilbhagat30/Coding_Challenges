# Users with **Both** Refinance and InSchool Loans – SQL Solutions

## Problem
Write a query that returns the `user_id` of every user who has **at least one** `'Refinance'` loan *and* **at least one** `'InSchool'` loan.

<table>
<tr><th>Table `loans` (schema)</th><th>type</th></tr>
<tr><td>id</td><td>bigint ▪︎ PK</td></tr>
<tr><td>user_id</td><td>bigint ▪︎ FK → users</td></tr>
<tr><td>type</td><td>text <em>(e.g., 'Refinance', 'InSchool')</em></td></tr>
<tr><td>status</td><td>text</td></tr>
<tr><td>created_at</td><td>date</td></tr>
</table>

---

## 1 . Set‑logic solution using `INTERSECT`
```sql
-- Users who submitted at least one Refinance loan
SELECT user_id
FROM   loans
WHERE  type = 'Refinance'

INTERSECT

-- AND at least one InSchool loan
SELECT user_id
FROM   loans
WHERE  type = 'InSchool';
```
*`INTERSECT`* returns the rows common to both sub‑queries, i.e., users present in **both** result sets.

---

## 2 . Single‑scan solution using `GROUP BY … HAVING`
```sql
SELECT  user_id
FROM    loans
WHERE   type IN ('Refinance', 'InSchool')            -- only rows we care about
GROUP BY user_id
HAVING  COUNT(DISTINCT type) = 2;                    -- must see BOTH types
```
* One pass over the table.
* `COUNT(DISTINCT type) = 2` → user contributed at least one row of each type.

---

## Which query should I use?

| Criterion                         | `INTERSECT`                                   | `GROUP BY … HAVING`                       |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Readability / interview clarity** | ✅ Extremely explicit set logic                | Slightly more to parse                    |
| **Scans of the table**            | 2 (one per sub‑query)                         | 1 (covers both types)                     |
| **Index friendliness**            | Uses the index twice                          | Uses the index once, enables stream agg.  |
| **Portability**                   | Not in some engines (e.g., pre‑8 MySQL)       | Works in virtually every SQL engine       |
| **Memory footprint**              | Holds two intermediate hash sets              | Groups on the fly – lower peak memory     |

### Performance tip
If the dataset is large and the query is run often, create a composite index:
```sql
CREATE INDEX idx_loans_type_user ON loans (type, user_id);
```
Both queries then become index‑only reads; the single‑scan `GROUP BY` version typically wins by a small margin.

---

## Sample result
| user_id |
|---------|
| 1045    |
| 2190    |
| 3678    |

All three users above have submitted **both** Refinance and InSchool loans – precisely what the prompt requires.

---

# Total Loan Balance per User from **Most‑Recent** Refinance Submission – SQL Solution

## Problem
For every user, find the **most recent** loan whose `type = 'Refinance'`; then return that user’s **total loan balance** (from the `submissions` table) for that loan.

**Tables**  
`loans(id, user_id, type, created_at, …)`  
`submissions(id, loan_id, balance, interest_rate, …)`  
Join key: `submissions.loan_id → loans.id`.

---

## Window‑function solution (robust)
```sql
WITH latest_refi AS (
    SELECT  id        AS loan_id,
            user_id,
            ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY      created_at DESC,   -- newest first
                              id DESC            -- tie‑breaker
            ) AS rn
    FROM    loans
    WHERE   type = 'Refinance'
)
SELECT  lr.user_id,
        SUM(s.balance) AS total_balance   -- use SUM in case of 1‑to‑many submissions
FROM    latest_refi AS lr
JOIN    submissions AS s
       ON s.loan_id = lr.loan_id
WHERE   lr.rn = 1                         -- keep each user’s latest Refinance loan only
GROUP BY lr.user_id
ORDER BY lr.user_id;
```

### Explanation
1. **`latest_refi` CTE**: ranks each user’s Refinance loans newest→oldest (`ROW_NUMBER`).  
2. **`WHERE lr.rn = 1`**: filters to the single newest loan per user.  
3. **Join to `submissions`**: pulls every balance tied to that loan.  
4. **`SUM`** collapses multiple submission rows (if any) into one figure per user.

> **Schema guarantees one‐row‑per‑loan?** Replace `SUM(s.balance)` with `s.balance` and drop `GROUP BY`; otherwise the query is future‑proof as written.

---

## Alternate (simpler) query when submission is 1‑to‑1 with loan
```sql
WITH latest_refi AS (
    SELECT  id AS loan_id,
            user_id,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC, id DESC) AS rn
    FROM    loans
    WHERE   type = 'Refinance'
)
SELECT  lr.user_id,
        s.balance AS total_balance
FROM    latest_refi AS lr
JOIN    submissions AS s
       ON s.loan_id = lr.loan_id
WHERE   lr.rn = 1
ORDER BY lr.user_id;
```

---

## Sample Output (based on the prompt’s preview data)
| user_id | total_balance |
|---------|---------------|
| 100     |  5 229.12 |
| 101     | 12 727.52 |
| 108     | 14 996.58 |

Each row represents a user, and the balance shown is that user’s total from the **latest** Refinance submission only.
