# Pharmacy Analytics (Part 2)

## Problem Statement
CVS Health is analyzing its pharmacy sales data to identify manufacturers associated with drugs that resulted in losses. Write a query to find the manufacturers, the number of drugs associated with losses, and the total amount of losses incurred. Display the results sorted in descending order with the highest losses at the top.

## Table Structure
**pharmacy_sales** table:
| Column Name  | Type    |
|--------------|---------|
| product_id   | integer |
| units_sold   | integer |
| total_sales  | decimal |
| cogs         | decimal |
| manufacturer | varchar |
| drug         | varchar |

## Expected Output
| manufacturer | drug_count | total_loss |
|--------------|------------|------------|
| Biogen       | 1          | 297324.73  |
| AbbVie       | 1          | 221429.36  |
| Eli Lilly    | 1          | 221422.17  |

## Solution

```sql
SELECT 
  manufacturer,
  SUM(CASE WHEN (total_sales - cogs)<=0 THEN 1 ELSE 0 END) drug_count,
  SUM(total_sales - cogs)*(-1) AS total_profit
FROM 
  pharmacy_sales
WHERE
  (total_sales - cogs)<=0
GROUP BY 
  manufacturer
ORDER BY 
  total_profit DESC
```

## Explanation

This solution does the following:
1. Selects manufacturers with drugs that resulted in losses.
2. Counts the number of drugs with losses for each manufacturer.
3. Calculates the total loss for each manufacturer.
4. Orders the results by total loss in descending order.

However, there are two small adjustments needed:
1. The column name should be `total_loss` instead of `total_profit`.
2. Using ABS() function would be more explicit than multiplying by -1 for the loss calculation.

## Optimized Solution

```sql
SELECT 
  manufacturer,
  COUNT(*) AS drug_count,
  ABS(SUM(total_sales - cogs)) AS total_loss
FROM 
  pharmacy_sales
WHERE
  total_sales - cogs <= 0
GROUP BY 
  manufacturer
ORDER BY 
  total_loss DESC
```

This optimized version simplifies the query and addresses the mentioned adjustments.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of rows in the pharmacy_sales table. This is due to the sorting operation (ORDER BY).
- Space Complexity: O(m), where m is the number of manufacturers with drugs that resulted in losses.

## Key Concepts
- Aggregation (SUM, COUNT)
- GROUP BY clause
- WHERE clause for filtering
- ORDER BY clause for sorting
- Use of ABS() function for absolute value

## Additional Notes
- The ABS() function ensures we get positive values for the losses, which is more explicit than multiplying by -1.
- Using COUNT(*) instead of a CASE statement for drug_count simplifies the query, as we're already filtering for loss-making drugs in the WHERE clause.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- Filtering
- Sorting

## Source
[DataLemur](https://datalemur.com/questions/non-profitable-drugs)

