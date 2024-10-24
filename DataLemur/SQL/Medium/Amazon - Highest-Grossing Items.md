# Top Products by Category Spending

## Problem Statement
You are tasked with analyzing product spending data to identify the top two products by spending within each category for the year 2022. Write a query to output the category, product, and total spending for these top products.

## Table Structure
**product_spend** table:
| Column Name       | Type      |
|-------------------|-----------|
| category          | string    |
| product           | string    |
| spend             | decimal   |
| transaction_date  | date      |

## Expected Output
| category | product | total_spend |
|----------|---------|-------------|
| A        | X       | 1000.00     |
| A        | Y       | 800.00      |
| B        | Z       | 1200.00     |

## Solution

```sql
WITH ranked_spending_cte AS (
  SELECT 
    category, 
    product, 
    SUM(spend) AS total_spend,  
    RANK() OVER (
      PARTITION BY category
      ORDER BY SUM(spend) DESC
    ) AS ranking
  FROM 
    product_spend 
  WHERE 
    EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY 
    category, product
)
SELECT 
  category, 
  product, 
  total_spend 
FROM 
  ranked_spending_cte 
WHERE 
  ranking < 3;
```

## Explanation
1. **WITH ranked_spending_cte AS**: Creates a Common Table Expression (CTE) to rank products by spending within each category.
2. **SUM(spend) AS total_spend**: Aggregates the spending for each product within a category.
3. **RANK() OVER (PARTITION BY category ORDER BY SUM(spend) DESC)**: Ranks products within each category based on their total spend in descending order.
4. **WHERE EXTRACT(YEAR FROM transaction_date) = 2022**: Filters the data to include only transactions from the year 2022.
5. **WHERE ranking < 3**: Filters the results to include only the top two products by spending in each category.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of transactions in 2022. This is due to the sorting operation within each category.
- **Space Complexity**: O(m), where m is the number of unique category-product combinations.

## Key Concepts
- Window functions
- Ranking within partitions
- Aggregation with SUM
- Filtering with WHERE

## Additional Notes
- This solution assumes that the `transaction_date` column is of a date type that supports the EXTRACT function.
- The query efficiently handles large datasets by using window functions and CTEs.

## Difficulty
Medium

## Related Topics
- Window Functions
- Data Aggregation
- Ranking and Partitioning

## Source
[DataLemur](https://datalemur.com/questions/top-products-by-category-spending)

