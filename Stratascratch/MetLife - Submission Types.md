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
