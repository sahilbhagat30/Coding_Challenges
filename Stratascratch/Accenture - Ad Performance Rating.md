# Ad Performance Rating

## Interview Question Details
- **Interview Question Date:** March 2023
- **Company:** Accenture
- **Difficulty Level:** Medium
- **Question ID:** 2155
- **Relevant Roles:**
  - Data Engineer
  - Data Scientist
  - BI Analyst
  - Data Analyst
  - ML Engineer

## Question Description
Following a recent advertising campaign, the marketing department wishes to classify its efforts based on the total number of units sold for each product.

You have been tasked with calculating the total number of units sold for each product and categorizing ad performance based on the following criteria for items sold:

| Items Sold | Performance Category |
|------------|----------------------|
| 30+        | Outstanding          |
| 20 - 29    | Satisfactory         |
| 10 - 19    | Unsatisfactory       |
| 1 - 9      | Poor                 |

Your output should contain:
- `product_id`
- `total_quantity` (total units sold)
- `categorized` (ad performance category)

## Table Schema
### `marketing_campaign`
| Column Name | Data Type |
|-------------|----------|
| `user_id`   | `bigint`  |
| `created_at` | `datetime` |
| `product_id` | `bigint`  |
| `quantity`   | `bigint`  |
| `price`      | `bigint`  |

## SQL Query Solution
```sql
WITH total_quantity_cte AS (
    SELECT
        product_id,
        SUM(quantity) AS total_quantity
    FROM marketing_campaign
    GROUP BY product_id
)
SELECT
    product_id,
    total_quantity,
    CASE
        WHEN total_quantity >= 30 THEN 'Outstanding'
        WHEN total_quantity BETWEEN 20 AND 29 THEN 'Satisfactory'
        WHEN total_quantity BETWEEN 10 AND 19 THEN 'Unsatisfactory'
        WHEN total_quantity BETWEEN 1 AND 9 THEN 'Poor'
    END AS categorized
FROM total_quantity_cte
ORDER BY total_quantity DESC;
```

## Expected Output Example
| product_id | total_quantity | categorized    |
|------------|---------------|---------------|
| 105        | 41            | Outstanding   |
| 102        | 29            | Satisfactory  |
| 118        | 22            | Satisfactory  |
| 114        | 23            | Satisfactory  |
| 101        | 10            | Unsatisfactory |
| 120        | 21            | Satisfactory  |
| 112        | 14            | Unsatisfactory |
| 110        | 12            | Unsatisfactory |
| 113        | 12            | Unsatisfactory |
| 115        | 12            | Unsatisfactory |
| 104        | 11            | Unsatisfactory |
| 119        | 19            | Unsatisfactory |
| 117        | 20            | Satisfactory  |
| 111        | 6             | Poor          |
| 109        | 5             | Poor          |
| 106        | 4             | Poor          |
| 108        | 5             | Poor          |
| 116        | 7             | Poor          |
| 103        | 7             | Poor          |
| 107        | 8             | Poor          |

## Explanation
1. **CTE (`total_quantity_cte`)**:
   - Groups data by `product_id`.
   - Sums up the `quantity` column to get `total_quantity` for each product.

2. **Main Query**:
   - Uses a `CASE` statement to categorize each product's ad performance based on the given criteria.
   - Orders the output in descending order of `total_quantity`.

## Notes
- The query ensures that products with no sales are not included in the final result.
- `COALESCE` is not needed since the grouping will return NULLs only if there is no data, which is not possible in this case.
- The `CASE` statement correctly defines the ranges for categorization.

## Additional Improvements
- If the dataset includes `NULL` or `0` sales values, a `HAVING SUM(quantity) > 0` condition could be added to filter them out.
- The query could be modified to include a `LIMIT` or pagination in case of large datasets.

## Complexity Analysis
- **Aggregation Step (`SUM`)**: O(n) complexity where `n` is the number of rows.
- **Grouping Step (`GROUP BY`)**: O(k log k) where `k` is the number of unique `product_id`s.
- **Sorting Step (`ORDER BY`)**: O(k log k) complexity.
- **Overall Complexity**: O(n + k log k) which is efficient for medium to large datasets.

