# Supercloud Customer Problem

## Problem Statement
Given two tables, `customer_contracts` and `products`, we want to identify customers who have purchased at least one product from every product category available in the `products` table. The objective is to write a SQL query that returns the `customer_id` of these customers.

## Table Structure
**customer_contracts** table:
| Column Name | Type    |
|-------------|---------|
| customer_id | integer |
| product_id  | integer |

**products** table:
| Column Name      | Type    |
|------------------|---------|
| product_id       | integer |
| product_category | string  |

## Expected Output
| customer_id |
|-------------|
| ...         |

```sql
SELECT 
   C.customer_id
FROM
   customer_contracts C
JOIN
   products P ON P.product_id = C.product_id
GROUP BY
   C.customer_id
HAVING COUNT(DISTINCT P.product_category) = (SELECT COUNT(DISTINCT product_category) FROM products)
```

## Explanation

1. **JOIN Operation**: We join the `customer_contracts` table with the `products` table using `product_id`. This allows us to link each customer's contract to the respective product and its category.

2. **Grouping and Aggregation**:
   - We group by `customer_id` so that each row in the result set corresponds to a unique customer.
   - For each customer, we count the distinct product categories they have purchased.

3. **HAVING Clause**:
   - The `HAVING` clause filters customers who have purchased from all available categories.
   - We achieve this by comparing each customer’s count of distinct product categories to the total number of categories available in the `products` table.

## Complexity Analysis
- **Time Complexity**: O(n * m), where n is the number of contracts in `customer_contracts` and m is the number of unique product categories in `products`. This is due to the grouping and counting operations.
- **Space Complexity**: O(k), where k is the number of unique customers in `customer_contracts` who match the criteria.

## Key Concepts
- **JOIN operations**
- **Aggregate functions** (`COUNT`, `DISTINCT`)
- **Filtering in the HAVING clause**

## Additional Notes
- This solution assumes that `product_id` exists in both `customer_contracts` and `products` and that each product belongs to a single category.
- Indexing `product_category` in `products` and `product_id` in `customer_contracts` can improve performance.

## Difficulty
Medium

## Related Topics
- **Data Aggregation**
- **JOINs and Filtering**
- **Grouping and HAVING clause**

## Source
[DataLemur](https://datalemur.com/questions/supercloud-customer)
