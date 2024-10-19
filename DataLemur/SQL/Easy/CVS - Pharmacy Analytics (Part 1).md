# Top Profitable Drugs

## Problem Statement
CVS Health is analyzing its pharmacy sales data. Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Display the result from the highest to the lowest total profit.

## Table Structure
**pharmacy_sales** table:
| Column Name | Type    |
|-------------|---------|
| product_id  | integer |
| units_sold  | integer |
| total_sales | decimal |
| cogs        | decimal |
| drug        | varchar |
| date        | date    |

## Expected Output
| drug      | total_profit |
|-----------|--------------|
| HUMIRA    | 24000000     |
| LANTUS    | 22000000     |
| ADVAIR    | 21000000     |

## Solution (Your Code)

```sql
SELECT  
  drug,
  SUM(total_sales - cogs) AS total_profit
FROM 
  pharmacy_sales
GROUP BY drug
ORDER BY total_profit DESC
LIMIT 3
````


## Explanation (Your Code)

1. We select the drug name and calculate the total profit by subtracting COGS from total sales.
2. We group the results by drug name to get the total profit for each drug.
3. We order the results by total profit in descending order to get the most profitable drugs first.
4. We limit the output to the top 3 results.

## Most Efficient Solution

```sql
SELECT 
  drug,
  SUM(total_sales - cogs) AS total_profit
FROM 
  pharmacy_sales
GROUP BY 
  drug
ORDER BY 
  total_profit DESC
LIMIT 3
````


## Explanation (Efficient Solution)

The most efficient solution is actually very similar to your corrected code. It follows the same steps:

1. Select the drug name and calculate the total profit.
2. Group the results by drug name.
3. Order by total profit in descending order.
4. Limit the output to 3 rows.

This approach is efficient because it performs the calculation and aggregation in a single pass over the data, then sorts and limits the results.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of rows in the pharmacy_sales table. This is due to the sorting operation (ORDER BY).
- Space Complexity: O(m), where m is the number of unique drugs. In the worst case, this could be equal to n if every drug is unique.

## Key Concepts
- Aggregation (SUM)
- GROUP BY clause
- ORDER BY clause
- LIMIT clause

## Additional Notes
- This solution assumes that the profit can be calculated by subtracting COGS from total sales.
- The LIMIT clause is used to restrict the output to the top 3 results efficiently.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- Sorting
- Top-N queries

## Source
[DataLemur](https://datalemur.com/questions/top-profitable-drugs)
