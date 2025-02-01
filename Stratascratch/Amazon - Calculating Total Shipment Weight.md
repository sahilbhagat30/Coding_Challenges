# Calculating Total Shipment Weight

## Problem Statement
Write a query to calculate the total weight for each shipment and add it as a new column. The output should include all existing columns along with an additional column that shows the total weight per shipment. Each shipment can have multiple rows.

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

## Solution Using Window Function (Best Approach)
```sql
SELECT 
    *,
    SUM(weight) OVER(PARTITION BY shipment_id) AS total_shipment_weight
FROM amazon_shipment;
```

## **Why This is the Best Solution?**
✅ **Uses `SUM(weight) OVER(PARTITION BY shipment_id)` to Calculate Shipment Weight Efficiently**  
✅ **Maintains Row-Level Data** Instead of Aggregating via `GROUP BY`  
✅ **Best for Reporting and Analysis** Without Losing Original Row Details  

## **Expected Output**
| shipment_id | sub_id | weight | shipment_date | total_shipment_weight |
|------------|--------|--------|---------------|----------------------|
| 101        | 1      | 10     | 2021-08-30    | 40                   |
| 101        | 2      | 20     | 2021-09-01    | 40                   |
| 101        | 3      | 10     | 2021-09-05    | 40                   |
| 102        | 1      | 50     | 2021-09-02    | 50                   |
| 103        | 1      | 25     | 2021-09-01    | 55                   |
| 103        | 2      | 30     | 2021-09-02    | 55                   |
| 104        | 1      | 30     | 2021-08-25    | 40                   |
| 104        | 2      | 10     | 2021-08-26    | 40                   |
| 105        | 1      | 20     | 2021-09-02    | 20                   |

🚀 **This is the most efficient and scalable approach!** Let me know if you need further refinements. 🎯
