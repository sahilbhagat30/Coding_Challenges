# Calculating Shipments Per Month

## Problem Statement
Write a query to calculate the number of shipments per month. A shipment is uniquely identified by a combination of `shipment_id` and `sub_id`. The output should display the year and month in the `YYYY-MM` format along with the count of shipments.

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

## User's Initial Query
```sql
SELECT 
    *,
    extract(month from shipment_date) as month_value,
    CONCAT(shipment_id, sub_id) AS ID
FROM 
    amazon_shipment
)
SELECT 
    DATE_FORMAT(shipment_date, "%Y-%m"),
    COUNT(id)
FROM 
    cte
GROUP BY 
    month_value;
```
### Issues in the Initial Query
1. **Syntax Error**: The `WITH` statement is incorrectly structured. There is an extra closing parenthesis `)`.
2. **CTE Usage**: The second `SELECT` statement should refer to the correct CTE alias.
3. **COUNT(id) Issue**: The column `id` does not exist in the CTE.

## Optimized Query (Best Solution)
### MySQL Version:
```sql
WITH cte AS (
    SELECT 
        shipment_id, 
        sub_id, 
        shipment_date, 
        DATE_FORMAT(shipment_date, '%Y-%m') AS year_month
    FROM amazon_shipment
)
SELECT 
    year_month, 
    COUNT(DISTINCT CONCAT(shipment_id, sub_id)) AS num_shipments
FROM cte
GROUP BY year_month
ORDER BY year_month;
```

### PostgreSQL Version:
```sql
WITH cte AS (
    SELECT 
        shipment_id, 
        sub_id, 
        shipment_date, 
        TO_CHAR(shipment_date, 'YYYY-MM') AS year_month
    FROM amazon_shipment
)
SELECT 
    year_month, 
    COUNT(DISTINCT shipment_id || sub_id) AS num_shipments
FROM cte
GROUP BY year_month
ORDER BY year_month;
```

## Explanation of the Optimized Query
1. **Extracting Year-Month**:
   - MySQL: `DATE_FORMAT(shipment_date, '%Y-%m')`
   - PostgreSQL: `TO_CHAR(shipment_date, 'YYYY-MM')`
   - This ensures the correct `YYYY-MM` format.
2. **Concatenating shipment_id and sub_id**:
   - MySQL: `CONCAT(shipment_id, sub_id)`
   - PostgreSQL: `shipment_id || sub_id`
   - Ensures each shipment is uniquely identified.
3. **COUNT DISTINCT**:
   - Ensures only unique shipments per month are counted.
4. **Using WITH CTE**:
   - Improves readability and maintainability.
5. **Ordering by year_month**:
   - Ensures chronological order of results.

## Expected Output
| year_month | num_shipments |
|------------|--------------|
| 2021-08    | 3            |
| 2021-09    | 6            |

This optimized query is efficient, structured correctly, and ensures accurate results. 🚀
