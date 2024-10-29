# Year-Over-Year Spend Growth Rate

## Problem Statement
Given a table of user transactions, the goal is to calculate the year-over-year (YoY) growth rate in spending for each product. The output should include the year, product ID, current year’s spend, previous year’s spend, and the YoY growth rate as a percentage.


## Table Structure
**user_transactions** table:
| Column Name       | Type     | Description                        |
|-------------------|----------|------------------------------------|
| transaction_date  | date     | Date of the transaction            |
| product_id        | integer  | Unique identifier for each product |
| spend             | decimal  | Amount spent in the transaction    |

## Example Input

| transaction_date | product_id | spend |
|------------------|------------|-------|
| 2021-01-15       | 101        | 200   |
| 2021-03-10       | 101        | 150   |
| 2022-02-20       | 101        | 250   |
| 2021-05-05       | 102        | 300   |
| 2022-06-14       | 102        | 350   |
| 2022-09-21       | 101        | 100   |

### Explanation of Input Data
- For `product_id` 101, there are transactions in 2021 and 2022, with total spends of 350 and 350, respectively.
- For `product_id` 102, there is a transaction in 2021 with a spend of 300, and another in 2022 with a spend of 350.

## Expected Output

| year | product_id | curr_year_spend | prev_year_spend | yoy_rate |
|------|------------|-----------------|-----------------|----------|
| 2022 | 101        | 350             | 350             | 0.00     |
| 2022 | 102        | 350             | 300             | 16.67    |

```sql
WITH cte AS (
    SELECT 
        EXTRACT(YEAR FROM transaction_date) AS year, 
        product_id,
        SUM(spend) AS curr_year_spend
    FROM 
        user_transactions
    GROUP BY 
        year, product_id
    ORDER BY 
        product_id
),
cte1 AS (
    SELECT
        year,
        product_id,
        curr_year_spend,
        LAG(curr_year_spend) OVER (PARTITION BY product_id ORDER BY year) AS prev_year_spend
    FROM 
        cte
)
SELECT 
    year,
    product_id,
    curr_year_spend,
    prev_year_spend,
    ROUND(100.0 * (curr_year_spend - prev_year_spend) / prev_year_spend, 2) AS yoy_rate
FROM 
    cte1;
```

### Explanation of Output Columns
- **year**: The year for the current transaction data.
- **product_id**: Unique identifier for each product.
- **curr_year_spend**: Total spending for the product in the current year.
- **prev_year_spend**: Total spending for the product in the previous year.
- **yoy_rate**: Year-over-year growth rate as a percentage, calculated as `(curr_year_spend - prev_year_spend) / prev_year_spend * 100`.

## Solution Outline

1. **Common Table Expression (CTE)**:
   - The first CTE (`cte`) extracts the year from `transaction_date`, calculates the total spending per product for each year (`curr_year_spend`), and groups the results by year and `product_id`.

2. **Calculate Previous Year’s Spend**:
   - The second CTE (`cte1`) uses the `LAG` window function to retrieve the previous year’s spend (`prev_year_spend`) for each `product_id`.

3. **Final Calculation**:
   - In the main query, the year-over-year growth rate (`yoy_rate`) is calculated by comparing the current and previous year’s spend for each product.
   - The formula used for `yoy_rate` is `100 * (curr_year_spend - prev_year_spend) / prev_year_spend`, rounded to two decimal places.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of rows in `user_transactions`. The grouping and window function add computational overhead.
- **Space Complexity**: O(n), as the intermediate CTEs store yearly transaction summaries for each product.

## Key Concepts
- **Date Functions**: `EXTRACT(YEAR FROM transaction_date)` extracts the year from each transaction.
- **Window Functions**: `LAG()` retrieves the previous year’s spend for each product to compute the YoY growth rate.
- **Conditional Aggregation and Grouping**: Aggregating total spending by `year` and `product_id`.

## Additional Notes
- This solution is applicable for datasets containing yearly transaction data, assuming there are sufficient records for year-over-year comparisons.
- The `ROUND` function ensures that the YoY growth rate is displayed to two decimal places for clarity.

## Difficulty
Medium

## Related Topics
- **Window Functions**
- **Date and Time Functions**
- **Aggregate Functions**

## Source
Custom Problem Scenario
