# 🌟 Best Selling Item

**Last Updated:** February 2025  
**Companies:** Ebay, Best Buy, Amazon  
**ID:** 10172  
**Level:** Hard  
**Roles:** Data Engineer, Data Scientist, BI Analyst, Data Analyst, ML Engineer, Software Engineer

---

## ❓ Problem Statement

Find the **best-selling item** for each month (no need to separate by year).  
The best-selling item is determined by the **highest total sales amount** per month, where:

```sql
total_paid = unitprice * quantity
```

**Output columns:**
- `month`
- `description` (of the item)
- `total_amount_paid`

---

## 🗃️ Table Used

### `online_retail`
| Column       | Type            |
|--------------|-----------------|
| country      | text            |
| customerid   | double precision|
| description  | text            |
| invoicedate  | date            |
| invoiceno    | text            |
| quantity     | bigint          |
| stockcode    | text            |
| unitprice    | double precision|

---

## ✅ Solution A: Include All Ties (Multiple Items per Month)

```sql
WITH total_by_item AS (
    SELECT 
        *,
        EXTRACT(MONTH FROM invoicedate) AS month,
        unitprice * quantity AS total_paid
    FROM online_retail
),
max_by_month AS (
    SELECT 
        month,
        MAX(total_paid) AS total_amount_paid
    FROM total_by_item
    GROUP BY month
)
SELECT 
    m.month,
    t.description,
    m.total_amount_paid
FROM 
    total_by_item t
JOIN 
    max_by_month m 
    ON t.month = m.month AND t.total_paid = m.total_amount_paid
ORDER BY m.month;
```

### 💡 Explanation (A)
- Includes **all best-selling items** that tie for the max `total_paid` per month.
- May return **multiple rows per month** if there are ties.

---

## ✅ Solution B: One Best-Seller Per Month Only

```sql
WITH total_by_item AS (
    SELECT 
        EXTRACT(MONTH FROM invoicedate) AS month,
        description,
        unitprice * quantity AS total_paid
    FROM online_retail
),
ranked_items AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY month ORDER BY total_paid DESC) AS rn
    FROM total_by_item
)
SELECT 
    month, 
    description, 
    total_paid AS total_amount_paid
FROM 
    ranked_items
WHERE 
    rn = 1
ORDER BY 
    month;
```

### 💡 Explanation (B)
- Uses `ROW_NUMBER()` to **rank items by total_paid per month**.
- Picks the **top-ranked item** per month.
- Ensures **only one row per month** even if there are ties.

---

## 📟 Sample Output

| month | description                     | total_amount_paid |
|-------|----------------------------------|--------------------|
| 1     | PAPER BUNTING WHITE LACE        | 66                 |
| 2     | RED DRAWER KNOB ACRYLIC EDWARDIAN| 38.25              |
| ...   | ...                              | ...                |

---

Let me know if you want to visualize these results or filter for a specific year!

