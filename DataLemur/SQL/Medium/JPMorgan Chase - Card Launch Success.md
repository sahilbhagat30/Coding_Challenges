# Card Launch Success Problem

## Problem Statement
Given a table `monthly_cards_issued` that contains information about the monthly issuance of various card types (including the year, month, and issuance count), the task is to retrieve the issuance count of each card type in its initial month of issuance. The query should return the `card_name` and `issued_amount` for each card's first issuance month, sorted by issuance count in descending order.

## Table Structure
**monthly_cards_issued** table:
| Column Name   | Type    |
|---------------|---------|
| card_name     | string  |
| issued_amount | integer |
| issue_year    | integer |
| issue_month   | integer |

## Expected Output
| card_name   | issued_amount |
|-------------|---------------|
| ...         | ...           |

```sql
with cte AS(
SELECT 
  card_name,
  issued_amount,
  MAKE_DATE(issue_year, issue_month, 1) issued_date_ym,
  MIN(MAKE_DATE(issue_year, issue_month, 1)) OVER(PARTITION BY card_name) min_issued_amount
FROM
  monthly_cards_issued
)
SELECT
  card_name,
  issued_amount
FROM
  cte
WHERE 
  issued_date_ym = min_issued_amount
ORDER BY
  issued_amount DESC
```

## Solution Outline

1. **Common Table Expression (CTE)**:
   - We create a CTE that includes:
     - `issued_date_ym`, a date created from `issue_year` and `issue_month`, representing each issuance month as the first day of that month.
     - `min_issued_amount`, the earliest issuance date for each `card_name`, calculated using `MIN(MAKE_DATE(issue_year, issue_month, 1)) OVER(PARTITION BY card_name)`.
   - This CTE allows us to identify the earliest issuance date per card in a single pass.

2. **Filtering for First Issuance Month**:
   - In the main query, we filter for rows where `issued_date_ym` matches `min_issued_amount`, which ensures we select only the first issuance record for each `card_name`.

3. **Sorting Results**:
   - We order the results by `issued_amount` in descending order, so the cards with the highest issuance counts in their first month are displayed at the top.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of rows in `monthly_cards_issued`, primarily due to the window function (`MIN OVER(PARTITION BY ...)`) and sorting.
- **Space Complexity**: O(n), as we store each row's `issued_date_ym` and `min_issued_amount` in the CTE.

## Key Concepts
- **Common Table Expressions (CTE)**
- **Window Functions** (`MIN OVER(PARTITION BY ...)`)
- **Filtering by Calculated Values**

## Additional Notes
- Using `MAKE_DATE(issue_year, issue_month, 1)` standardizes each issuance date to the first day of its respective month, allowing for accurate comparisons.
- This solution captures only the first issuance record for each card, regardless of subsequent issuance amounts or months.

## Difficulty
Medium

## Related Topics
- **Window Functions and Partitioning**
- **Aggregate Functions**
- **Date Functions in SQL**

## Source
[DataLemur](https://datalemur.com/questions/card-launch-success)
