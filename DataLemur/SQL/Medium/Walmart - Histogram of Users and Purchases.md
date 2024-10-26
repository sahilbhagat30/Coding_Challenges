# Latest Transactions Problem

## Problem Statement
Given a table of user transactions, we need to retrieve the most recent transactions for each user. For each user, the result should include the transaction date, `user_id`, and the count of products purchased on that date. We need to use window functions to rank transactions by date per user, filter only the most recent transactions, and group by each user and transaction date.

## Table Structure
**user_transactions** table:
| Column Name      | Type      |
|------------------|-----------|
| transaction_date | date      |
| user_id          | integer   |
| product_id       | integer   |

## Expected Output
| transaction_date | user_id | purchase_count |
|------------------|---------|----------------|
| ...              | ...     | ...            |

```sql
WITH latest_transactions_cte AS (
SELECT 
 transaction_date, 
 user_id, 
 product_id, 
 RANK() OVER (
   PARTITION BY user_id 
   ORDER BY transaction_date DESC) AS ranking 
FROM user_transactions
)
SELECT 
  transaction_date, 
  user_id,
  COUNT(product_id) AS purchase_count 
FROM latest_transactions_cte 
WHERE ranking = 1
GROUP BY transaction_date, user_id
ORDER BY transaction_date;
```

## Solution Outline

1. **Common Table Expression (CTE)**:
   - We create a CTE named `latest_transactions_cte` to rank each transaction for a user by transaction date in descending order.
   - Using the `RANK()` window function with `PARTITION BY user_id ORDER BY transaction_date DESC`, we assign a rank to each transaction, where the most recent transaction for each user has `days_rank = 1`.

2. **Filtering for Most Recent Transactions**:
   - In the main query, we filter for `days_rank = 1` to select only the most recent transaction for each user.

3. **Grouping and Counting**:
   - We use `GROUP BY transaction_date, user_id` to group the result by each user and transaction date.
   - The `COUNT(product_id)` function calculates the total number of products purchased by each user on their most recent transaction date.

4. **Ordering Results**:
   - Finally, we order the results by `user_id` to display each user’s latest transactions in a clear order.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of rows in `user_transactions`. Sorting within the `RANK()` function takes O(n log n), and grouping afterward takes O(n).
- **Space Complexity**: O(n), as the CTE temporarily holds ranking information for each user transaction.

## Key Concepts
- **Window Functions** (`RANK()` with `PARTITION BY`)
- **Conditional Filtering** in the main query with `WHERE` clause
- **Grouping and Aggregation** with `COUNT`

## Additional Notes
- Ensure that the table `user_transactions` has indexes on `user_id` and `transaction_date` if the dataset is large, as this will improve the performance of ranking and filtering.
- Using `RANK()` instead of `ROW_NUMBER()` handles cases where users may have multiple transactions on the same date by keeping them all in the output if necessary.

## Difficulty
Medium

## Related Topics
- **Window Functions**
- **Data Aggregation**
- **Grouping and Filtering**

## Source
[DataLemur](https://datalemur.com/questions/latest-transactions)
