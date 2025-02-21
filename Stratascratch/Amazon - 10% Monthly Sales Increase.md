# 10% Monthly Sales Increase

## Problem Statement
You have been asked to compare sales of the current month, May, to those of the previous month, April.

The company requested that you only display products whose sales (**UNITS SOLD * PRICE**) have increased by more than **10%** from the previous month to the current month.

Your output should include the **product_id** and the **percentage growth in sales**.

## Given Table
### `online_orders`
| product_id | promotion_id | cost_in_dollars | customer_id | date_sold | units_sold |
|------------|--------------|----------------|-------------|-----------|------------|
| 101        | 5001         | 20             | 300         | 2024-04-15 | 10         |
| 101        | 5002         | 20             | 301         | 2024-05-12 | 15         |
| 102        | 5003         | 50             | 302         | 2024-04-20 | 5          |
| 102        | 5004         | 50             | 303         | 2024-05-18 | 7          |
| 103        | 5005         | 30             | 304         | 2024-05-22 | 12         |

## **Original Solution**
```sql
WITH MAY_SALES AS (
    SELECT 
        product_id,
        (units_sold * cost_in_dollars) AS SALES
    FROM online_orders
    WHERE EXTRACT(MONTH FROM date_sold) = 5
), 
APRIL_SALES AS (
    SELECT 
        product_id,
        (units_sold * cost_in_dollars) AS SALES
    FROM online_orders
    WHERE EXTRACT(MONTH FROM date_sold) = 4
), 
MAY_FOR_EACH_SALES AS (
    SELECT product_id, SUM(SALES) AS sales 
    FROM MAY_SALES 
    GROUP BY product_id
), 
APRIL_FOR_EACH_SALES AS (
    SELECT product_id, SUM(SALES) AS sales 
    FROM APRIL_SALES 
    GROUP BY product_id
), 
PERCENTAGE_CHANGE AS (
    SELECT 
        m.product_id,
        ROUND(((m.sales - a.sales) / NULLIF(a.sales, 0)) * 100.0, 2) AS percentage_change 
    FROM MAY_FOR_EACH_SALES m
    JOIN APRIL_FOR_EACH_SALES a ON m.product_id = a.product_id
)
SELECT 
    product_id,
    percentage_change
FROM PERCENTAGE_CHANGE
WHERE percentage_change > 10;
```

## **Optimized Solution**
```sql
WITH SALES_BY_MONTH AS (
    SELECT 
        product_id,
        SUM(CASE WHEN EXTRACT(MONTH FROM date_sold) = 4 THEN units_sold * cost_in_dollars ELSE 0 END) AS april_sales,
        SUM(CASE WHEN EXTRACT(MONTH FROM date_sold) = 5 THEN units_sold * cost_in_dollars ELSE 0 END) AS may_sales
    FROM online_orders
    WHERE EXTRACT(MONTH FROM date_sold) IN (4, 5)  -- Filters only relevant data
    GROUP BY product_id
)
SELECT 
    product_id,
    ROUND(((may_sales - NULLIF(april_sales, 0)) / NULLIF(april_sales, 0)) * 100.0, 2) AS percentage_change
FROM SALES_BY_MONTH
WHERE may_sales > april_sales * 1.1; -- Filters only products with >10% increase
```

## **Why This is the Best Solution?**
✅ **Reduces Table Scans:** Instead of scanning `online_orders` **twice**, we filter both months in **one scan**.
✅ **Eliminates Extra CTEs:** Merges April and May sales into a **single CTE** instead of separate ones.
✅ **Uses Conditional Aggregation:** Instead of filtering in `WHERE`, we use `SUM(CASE WHEN...)` to compute sales efficiently.
✅ **Avoids Division by Zero:** Uses `NULLIF(a.sales, 0)` to prevent errors.
✅ **Better Index Utilization:** Works better with an index on `date_sold` for improved performance.

## **Indexing for Performance Optimization**
To further improve query performance, consider adding indexes:
```sql
CREATE INDEX idx_date_sold ON online_orders (date_sold);
CREATE INDEX idx_product_sales ON online_orders (product_id, date_sold, units_sold, cost_in_dollars);
```
### **Why Indexing Helps?**
✅ **Speeds Up Filtering:** Indexing `date_sold` allows faster access to relevant rows.
✅ **Enhances Aggregation Performance:** Indexing `(product_id, date_sold, units_sold, cost_in_dollars)` optimizes group-by operations.
✅ **Reduces Full Table Scans:** Queries will read only necessary rows, reducing I/O overhead.

## **Expected Output**
| product_id | percentage_change |
|------------|------------------|
| 101        | 50.00            |
| 102        | 40.00            |

🚀 **This optimized query runs faster and is more efficient on large datasets!** Let me know if you need further refinements! 🎯

