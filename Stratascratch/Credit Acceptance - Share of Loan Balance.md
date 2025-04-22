# Share of Loan Balance – SQL Solutions

## Problem
Write a query that returns each loan’s `rate_type`, `loan_id`, `balance`, and the percentage that this balance contributes to the **total balance of loans with the same `rate_type`**.

Table **`submissions`**
| column | type |
| --- | --- |
| `id` | bigint |
| `loan_id` | bigint |
| `rate_type` | text |
| `interest_rate` | double precision |
| `balance` | double precision |

---

## 1. Solution with a Common Table Expression (CTE)
```sql
WITH total_balance_by_rate_type AS (
    SELECT  rate_type,
            SUM(balance) AS total_balance
    FROM    submissions
    GROUP BY rate_type
)
SELECT  s.rate_type,
        s.loan_id,
        s.balance,
        ROUND(s.balance / tb.total_balance, 2) AS percentage_balance
FROM    submissions AS s
JOIN    total_balance_by_rate_type AS tb
       ON tb.rate_type = s.rate_type
ORDER BY s.rate_type, percentage_balance DESC;
```
**Explanation**
1. The CTE aggregates each `rate_type`’s total loan balance.
2. The main query joins every loan row to its rate‑type total and divides the two balances to get the percentage.
3. `ROUND()` is optional—remove it if you need full precision.

---

## 2. Concise Solution with a Window Function
```sql
SELECT  rate_type,
        loan_id,
        balance,
        ROUND(balance / SUM(balance) OVER (PARTITION BY rate_type), 2) AS percentage_balance
FROM    submissions
ORDER BY rate_type, percentage_balance DESC;
```
**Why use a window?** The analytic function `SUM(balance) OVER (PARTITION BY rate_type)` computes the same total as the CTE **without** an explicit join, often making the query shorter and faster.

---

## Performance Notes
* PostgreSQL’s planner optimises both approaches well; the window‑function version typically needs only one pass over the data.
* If either `balance` or the total were integers, cast them to `numeric` to avoid integer division.

---

## Expected Output (sample)
| rate_type | loan_id | balance | percentage_balance |
|-----------|---------|---------|--------------------|
| fixed     | 4       | 12 727.52 | 0.46 |
| fixed     | 9       | 14 996.58 | 0.54 |
| variable  | 2       | 5 229.12 | 0.11 |
| variable  | 7       | 21 149   | 0.45 |
| variable  | 5       | 14 379   | 0.31 |
| variable  | 11      | 6 221.12 | 0.13 |

Use either query in StrataScratch’s editor—both will produce the correct percentages.
