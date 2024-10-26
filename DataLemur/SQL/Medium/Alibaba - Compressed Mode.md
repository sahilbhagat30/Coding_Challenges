# Alibaba Compressed Mode Problem

## Problem Statement
Given a table `items_per_order` that stores the number of times each order size appears (where order size is the number of items in an order), the task is to identify the most frequently occurring order size(s). Specifically, we need to find the `item_count` for orders with the highest occurrence.

## Table Structure
**items_per_order** table:
| Column Name       | Type    |
|-------------------|---------|
| item_count        | integer |
| order_occurrences | integer |

## Expected Output
| item_count |
|------------|
| ...        |

```sql
with cte AS(
SELECT MAX(order_occurrences) max_order_occurrences
FROM items_per_order
)
select item_count
from items_per_order
cross join cte
where order_occurrences = max_order_occurrences
```

## Solution Outline

1. **Common Table Expression (CTE)**:
   - We create a CTE to calculate the maximum `order_occurrences` across all entries in `items_per_order`. This is stored as `max_order_occurrences` and represents the highest frequency of order sizes in the table.

2. **Cross Join with CTE**:
   - In the main query, we use a `CROSS JOIN` with the CTE to access the `max_order_occurrences` for filtering.
   - `CROSS JOIN` allows each row in `items_per_order` to reference the `max_order_occurrences` value in the CTE.

3. **Filtering for Maximum Occurrences**:
   - We filter the main query by `WHERE order_occurrences = max_order_occurrences`, so only rows where the order occurrence matches the maximum frequency are selected.

4. **Selecting `item_count`**:
   - The final result displays only the `item_count` of the most frequently occurring order sizes.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of rows in `items_per_order`, as we perform a single scan to determine the maximum `order_occurrences`.
- **Space Complexity**: O(1), since only the `max_order_occurrences` value is stored in the CTE.

## Key Concepts
- **Common Table Expressions (CTE)**
- **Cross Join**
- **Filtering with Aggregate Values**

## Additional Notes
- This solution assumes that multiple `item_count` values may have the same maximum `order_occurrences`, and it will return all such values.
- The use of a `CROSS JOIN` with a CTE ensures we can reference the maximum occurrence value in each row for filtering purposes.

## Difficulty
Easy to Medium

## Related Topics
- **Aggregate Functions**
- **Common Table Expressions**
- **Filtering Based on Calculated Values**

## Source
[DataLemur](https://datalemur.com/questions/alibaba-compressed-mode)
