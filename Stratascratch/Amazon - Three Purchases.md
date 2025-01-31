# Three Purchases

## Interview Question Date: February 2022
**Company**: Amazon  
**Difficulty**: Medium  
**ID**: 2095  

## Relevant Roles:
- Data Engineer
- Data Scientist
- BI Analyst
- Data Analyst
- ML Engineer

## Objective:
List the IDs of customers who made at least 3 orders in both 2020 and 2021.

---

## Table: `amazon_orders`
**Columns**:
- `id` (int): Unique identifier for each order
- `user_id` (int): ID of the user who placed the order
- `order_date` (date): Date the order was placed
- `order_total` (double): Total value of the order

---

## SQL Query:

```sql
WITH orders_per_year AS (
    SELECT 
        user_id,
        EXTRACT(YEAR FROM order_date) AS order_year,
        COUNT(id) AS order_count
    FROM amazon_orders
    WHERE EXTRACT(YEAR FROM order_date) IN (2020, 2021)
    GROUP BY user_id, EXTRACT(YEAR FROM order_date)
),
qualified_users AS (
    SELECT 
        user_id
    FROM orders_per_year
    WHERE order_count >= 3
    GROUP BY user_id
    HAVING COUNT(DISTINCT order_year) = 2
)
SELECT DISTINCT user_id
FROM qualified_users;
```

---

## Explanation:
1. **`orders_per_year` CTE**:
    - Filters orders from the years 2020 and 2021.
    - Groups by `user_id` and `order_year` to count the number of orders per user per year.

2. **`qualified_users` CTE**:
    - Selects users who made at least 3 orders in each year (2020 and 2021).
    - Ensures users have data for both years by checking the count of distinct years equals 2.

3. **Final SELECT**:
    - Retrieves the distinct `user_id` of qualified users who meet the criteria.

---

## Output:
This query returns the list of user IDs who made at least 3 orders in both 2020 and 2021.
