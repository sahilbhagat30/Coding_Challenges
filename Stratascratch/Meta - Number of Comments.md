# Meta Challenge – Comments per User (30‑Day Window)

**Challenge ID 2004**  
*Difficulty • Easy*  
*Platform • Meta*

---

## Problem
Return the **total number of comments** each user received in the **30 days before** `2020‑02‑10` (exclusive). Exclude users who received no comments in that period.

**Table**  
`fb_comments_count(user_id bigint, created_at date, number_of_comments bigint)`

Date window: **2020‑01‑11 → 2020‑02‑09** (inclusive of start date, exclusive of anchor date).

---

## SQL Solution
```sql
SELECT  user_id,
        SUM(number_of_comments) AS total_comments
FROM    fb_comments_count
WHERE   created_at >= DATE '2020-02-10' - INTERVAL '30 days'  -- start: 2020‑01‑11
  AND   created_at  < DATE '2020-02-10'                       -- end:   2020‑02‑09
GROUP BY user_id
ORDER BY total_comments DESC;   -- optional
```

### Explanation
1. `DATE '2020-02-10'` casts the literal as a `date` type.
2. Subtracting `INTERVAL '30 days'` yields *2020‑01‑11* (the window’s first day).
3. The `< DATE '2020-02-10'` bound excludes the anchor date itself, giving exactly 30 days.
4. `SUM(number_of_comments)` aggregates per user.
5. Users with no rows in the period naturally vanish, satisfying the “don’t output” rule.

---

## Dynamic Variant (rolling 30‑day window)
```sql
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
  AND created_at  <  CURRENT_DATE
```
Useful if you want the query to stay valid without hard‑coding a date.

---

## Why explicit range beats `EXTRACT(DAYS FROM …)`
Using an `interval`’s `days` field fails across month boundaries (the `days` component resets to 0‑30 inside the interval). The explicit comparison shown above is accurate, index‑friendly, and easier to read.
