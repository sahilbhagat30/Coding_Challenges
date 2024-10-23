# Compressed Mean

## Problem Statement
You're trying to find the mean number of items per order on Alibaba, rounded to 1 decimal place using tables which includes information on the count of items in each order (items_per_order table) and the corresponding number of orders for each item count (order_occurrences table).

## Table Structure
**items_per_order** table:
| Column Name        | Type    |
|---------------------|---------|
| item_count          | integer |
| order_occurrences   | integer |

## Expected Output
| mean |
|------|
| 2.7  |

## Solution (Your Answer)

```sql
SELECT
  ROUND(CAST((SUM(item_count * order_occurrences) * 1.0 / SUM(order_occurrences)) AS numeric), 1) AS mean
FROM
  items_per_order
```

## Explanation (Your Answer)

1. We calculate the weighted sum of items by multiplying `item_count` and `order_occurrences` and summing the results.
2. We divide this by the total number of orders (sum of `order_occurrences`).
3. We multiply by 1.0 to ensure floating-point division.
4. We cast the result to numeric type and round to 1 decimal place using ROUND function.

## Most Efficient Solution

```sql
SELECT
  ROUND(SUM(item_count * order_occurrences)::numeric / SUM(order_occurrences), 1) AS mean
FROM
  items_per_order
```

## Explanation (Efficient Solution)

1. We calculate the weighted sum of items by multiplying `item_count` and `order_occurrences` and summing the results.
2. We divide this by the total number of orders (sum of `order_occurrences`).
3. We cast the result to numeric type using the `::` operator, which is more concise in PostgreSQL.
4. We round to 1 decimal place using ROUND function.

## Complexity Analysis
- Time Complexity: O(n), where n is the number of rows in the items_per_order table. We need to scan through all rows once.
- Space Complexity: O(1), as we're only storing a single aggregated value.

## Key Concepts
- Weighted average calculation
- Aggregation (SUM)
- Type casting in PostgreSQL
- Rounding numbers

## Additional Notes
- The `::` operator is PostgreSQL-specific syntax for type casting. In other SQL dialects, you might need to use CAST() instead.
- Multiplying by 1.0 (as in your solution) is a common technique to force floating-point division, but PostgreSQL can handle this implicitly when casting to numeric.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- Mathematical Operations in SQL
- Type Casting

## Source
[DataLemur](https://datalemur.com/questions/alibaba-compressed-mean)

