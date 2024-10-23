# Pharmacy Analytics (Part 3)

## Problem Statement
CVS Health wants to gain a clearer understanding of its pharmacy sales and the performance of various products. Write a query to calculate the total drug sales for each manufacturer. Round the answer to the nearest million and report your results in descending order of total sales. In case of any duplicates, sort them alphabetically by the manufacturer name. Format the results as "$36 million".

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
| manufacturer | sale        |
|--------------|-------------|
| Biogen       | $4 million  |
| Eli Lilly    | $3 million  |

## Solution

```sql
SELECT
  manufacturer,
  CONCAT('$', ROUND(SUM(total_sales)/1000000, 0), ' million') AS sale
FROM
  pharmacy_sales
GROUP BY 
  manufacturer
ORDER BY
  SUM(total_sales) DESC, manufacturer
```

## Explanation

1. We start by selecting from the `pharmacy_sales` table.
2. We group the results by `manufacturer` to get total sales for each manufacturer.
3. We calculate the total sales using `SUM(total_sales)`.
4. We divide the total sales by 1,000,000 to convert to millions, then round to the nearest whole number using `ROUND(..., 0)`.
5. We use `CONCAT()` to format the result as "$X million".
6. We order the results first by total sales in descending order, then by manufacturer name alphabetically.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of rows in the pharmacy_sales table. This is due to the sorting operation (ORDER BY).
- Space Complexity: O(m), where m is the number of unique manufacturers.

## Alternative Approaches
An alternative approach could use the TO_CHAR function (in some SQL dialects) for formatting instead of CONCAT and ROUND:

```sql
SELECT
  manufacturer,
  TO_CHAR(ROUND(SUM(total_sales)/1000000, 0), '$FM999G999" million"') AS sale
FROM
  pharmacy_sales
GROUP BY 
  manufacturer
ORDER BY
  SUM(total_sales) DESC, manufacturer
```

This approach might be more concise in some SQL dialects, but may not be as widely supported.

## Key Concepts
- Aggregation (SUM)
- GROUP BY clause
- String manipulation (CONCAT)
- Rounding and formatting numbers
- Multi-level sorting

## Additional Notes
- The ROUND function is used to round to the nearest million.
- The ORDER BY clause sorts first by total sales (descending) and then by manufacturer name (ascending) to handle any ties.
- Different SQL dialects might have slightly different functions for string formatting and number rounding.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- String Formatting
- Sorting

## Source
[DataLemur](https://datalemur.com/questions/total-drugs-sales)
