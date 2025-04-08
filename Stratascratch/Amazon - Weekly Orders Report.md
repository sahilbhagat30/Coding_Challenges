# 📊 Weekly Orders Report

**Last Updated:** March 2025  
**Company:** Amazon  
**ID:** 10363  
**Level:** Easy  
**Roles:** Data Scientist, BI Analyst, Data Analyst, ML Engineer

---

## ❓ Problem Statement

For each week (starting on **Sunday**), calculate the total quantity across all orders for that week.

Only include orders from the **first quarter of 2023**.

The output should contain:
- `week` (starting Sunday)
- `quantity` (sum of all orders for that week)

Include a **row number** to index the weekly summary.

---

## 🗃️ Table Used

### `orders_analysis`
| Column          | Type    |
|------------------|---------|
| stage_of_order   | text    |
| week             | date    |
| quantity         | integer |

---

## ✅ SQL Query

```sql
SELECT
  ROW_NUMBER() OVER (ORDER BY DATE_TRUNC('week', week)) AS row_num,
  DATE_TRUNC('week', week)::date AS week_starting_sunday,
  SUM(quantity) AS total_quantity
FROM
  orders_analysis
WHERE
  week >= '2023-01-01' AND week < '2023-04-01'
GROUP BY
  DATE_TRUNC('week', week)
ORDER BY
  week_starting_sunday;
```

---

## 💡 Explanation

- `DATE_TRUNC('week', week)`: Rounds the `week` date down to the previous Sunday.
- `WHERE week >= '2023-01-01' AND week < '2023-04-01'`: Restricts data to Q1 2023.
- `SUM(quantity)`: Totals quantity for each week.
- `ROW_NUMBER() OVER (...)`: Adds a sequential row number per week.
- `GROUP BY`: Groups data by truncated week.

---

## 📟 Sample Output

| row_num | week_starting_sunday | total_quantity |
|---------|----------------------|----------------|
| 1       | 2023-01-01           | 303            |
| 2       | 2023-01-08           | 312            |
| ...     | ...                  | ...            |

---

Let me know if you want to visualize this in a line chart or export it as a report!

