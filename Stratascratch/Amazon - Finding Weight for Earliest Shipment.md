# Finding Weight for Earliest Shipment

## Problem Statement
Write a query to find the weight for each shipment's earliest shipment date. Output the shipment id along with the weight.

## Given Table: `amazon_shipment`
| shipment_id | sub_id | weight | shipment_date |
|------------|--------|--------|---------------|
| 101        | 1      | 10     | 2021-08-30    |
| 101        | 2      | 20     | 2021-09-01    |
| 101        | 3      | 10     | 2021-09-05    |
| 102        | 1      | 50     | 2021-09-02    |
| 103        | 1      | 25     | 2021-09-01    |
| 103        | 2      | 30     | 2021-09-02    |
| 104        | 1      | 30     | 2021-08-25    |
| 104        | 2      | 10     | 2021-08-26    |
| 105        | 1      | 20     | 2021-09-02    |

## User's Initial Query (With Issues)
```sql
WITH CTE AS(SELECT 
    shipment_id,
    weight,
    RANK() OVER(PARTITION BY shipment_date) EARLIEST_DATE
FROM 
    amazon_shipment)
SELECT 
    shipment_id,
    weight
FROM 
    CTE
WHERE 
    EARLIEST_DATE = 1;
```

### Issues in the Initial Query
1. **Incorrect `RANK()` usage**: Missing `ORDER BY shipment_date` inside `RANK()`.
2. **Incorrect Partitioning**: `PARTITION BY shipment_date` should be `PARTITION BY shipment_id`.
3. **Better Performance Option Available**: `MIN()` is faster than `RANK()` in this case.

## Best Optimized Solution

### **Using `MIN()` (Best Performance and Readability)**
```sql
SELECT 
    a.shipment_id,
    a.weight
FROM amazon_shipment a
JOIN (
    SELECT shipment_id, MIN(shipment_date) AS earliest_date
    FROM amazon_shipment
    GROUP BY shipment_id
) b 
ON a.shipment_id = b.shipment_id AND a.shipment_date = b.earliest_date;
```

### **Alternative Using `RANK()` (If Explicit Ranking is Required)**
```sql
WITH CTE AS (
    SELECT 
        shipment_id,
        weight,
        shipment_date,
        RANK() OVER (PARTITION BY shipment_id ORDER BY shipment_date ASC) AS earliest_rank
    FROM amazon_shipment
)
SELECT 
    shipment_id,
    weight
FROM CTE
WHERE earliest_rank = 1;
```

## **Why is `MIN() + JOIN` the Best Approach?**
✅ **Better Performance**: `MIN()` is computationally cheaper than `RANK()`.
✅ **Simpler Query Structure**: More readable without requiring window functions.
✅ **Handles Duplicates Well**: Returns all shipments if multiple have the same earliest date.

## **Expected Output**
| shipment_id | weight |
|------------|--------|
| 101        | 10     |
| 102        | 50     |
| 103        | 25     |
| 104        | 30     |
| 105        | 20     |

🚀 Use `MIN() + JOIN` for best performance and simplicity! If ranking is needed, use `RANK()`. Let me know if you have further questions! 🎯
