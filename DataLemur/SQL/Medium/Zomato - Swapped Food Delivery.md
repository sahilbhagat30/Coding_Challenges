# Swapped Food Delivery Problem

## Problem Statement
Given a list of food delivery orders, each with a unique `order_id` and an associated `item`, the task is to swap each odd `order_id` with the next even `order_id`. If the last `order_id` is odd and does not have a subsequent even `order_id`, it should remain as is. The solution needs to output the modified `order_id`s in sorted order, reflecting these swaps.

## Table Structure
**orders** table:
| Column Name | Type    |
|-------------|---------|
| order_id    | integer |
| item        | string  |

## Expected Output
| corrected_order_id | item       |
|--------------------|------------|
| ...                | ...        |

```sql
with cte as(
SELECT
  COUNT(*) AS total_orders 
FROM orders
)
select
  CASE
  WHEN order_id % 2 != 0 AND order_id != total_orders THEN order_id + 1 -- Line 1
  WHEN order_id % 2 != 0 AND order_id = total_orders THEN order_id -- Line 1
  ELSE order_id - 1 -- Line 3
  END AS corrected_order_id,
  item
from orders
cross JOIN cte
ORDER BY
  corrected_order_id
```

## Solution Outline

1. **Common Table Expression (CTE)**:
   - The CTE (`with cte as (SELECT COUNT(*) AS total_orders FROM orders)`) calculates the total number of orders, stored as `total_orders`. This count is used to check if an `order_id` is the last one in the list, allowing us to avoid swapping it if it’s an odd number without a partner.

2. **CASE Statement Logic**:
   - The main query uses a `CASE` statement to conditionally modify `order_id`s based on whether they are odd or even:
     - **Line 1**: `WHEN order_id % 2 != 0 AND order_id != total_orders THEN order_id + 1`
       - If `order_id` is odd and is not the last order, increment it by 1 to swap it with the following even order.
     - **Line 2**: `WHEN order_id % 2 != 0 AND order_id = total_orders THEN order_id`
       - If `order_id` is odd and also the last order, it remains unchanged to handle cases with an odd number of total orders.
     - **Line 3**: `ELSE order_id - 1`
       - For even `order_id`s, decrement it by 1 to swap it with the previous odd order.

3. **Cross Join with CTE**:
   - The `CROSS JOIN` allows each row in `orders` to access `total_orders` for conditional logic within the `CASE` statement.

4. **Ordering Results**:
   - The query’s final output is sorted by `corrected_order_id` to display the results in the intended order after swapping.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of rows in `orders`, since we’re iterating through each row once and applying conditional logic.
- **Space Complexity**: O(1), as we only use additional space for the `total_orders` count in the CTE.

## Edge Case Considerations
- **Sequential Order IDs**: This approach assumes `order_id`s are sequential and without gaps. If there are missing IDs, the logic may not work as intended, as it relies on sequential `order_id`s.
- **Alternative Approach**: An alternative approach could use `ROW_NUMBER()` to ensure sequential row numbering even with gaps, improving robustness for datasets with missing IDs.

## Key Concepts
- **Common Table Expressions (CTE)**
- **Conditional Logic with CASE Statements**
- **JOIN Operations and Aggregation**

## Additional Notes
- This solution ensures that any final odd order remains in place if it does not have a subsequent even order to swap with.
- Using `CROSS JOIN` with a CTE allows us to easily reference `total_orders` within each row in the main query.

## Difficulty
Medium

## Related Topics
- **Conditional Aggregation**
- **Modulo Operation**
- **JOINs and Filtering**

## Source
[DataLemur](https://datalemur.com/questions/swapped-food-delivery)
