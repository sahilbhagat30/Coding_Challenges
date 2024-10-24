# User's Third Transaction

## Problem Statement
Assume you are given the table below on Uber transactions made by users. Write a query to obtain the third transaction of every user. Output the user id, spend and transaction date.

## Table Structure
**transactions** table:
| Column Name      | Type      |
|------------------|-----------|
| user_id          | integer   |
| spend            | decimal   |
| transaction_date | timestamp |

## Sample Data
**transactions** table:
| user_id | spend  | transaction_date    |
|---------|--------|---------------------|
| 111     | 100.50 | 01/08/2022 12:00:00 |
| 111     | 55.00  | 01/10/2022 12:00:00 |
| 121     | 36.00  | 01/18/2022 12:00:00 |
| 145     | 24.99  | 01/26/2022 12:00:00 |
| 111     | 89.60  | 02/05/2022 12:00:00 |

## Expected Output
| user_id | spend | transaction_date    |
|---------|-------|---------------------|
| 111     | 89.60 | 02/05/2022 12:00:00 |

## Solution

```sql
WITH ranked_transactions AS (
  SELECT 
    user_id,
    spend,
    transaction_date,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) AS transaction_rank
  FROM transactions
)
SELECT 
  user_id,
  spend,
  transaction_date
FROM ranked_transactions
WHERE transaction_rank = 3;
```
## Explanation

1. We use a Common Table Expression (CTE) named `ranked_transactions` to create a ranked list of transactions for each user.
2. Inside the CTE, we use the `ROW_NUMBER()` window function to assign a rank to each transaction within each user's set of transactions, ordered by `transaction_date`.
3. In the main query, we select from this ranked list, filtering for only the transactions with `transaction_rank = 3`.

This approach efficiently finds the 3rd transaction for every user who has at least 3 transactions. Users with fewer than 3 transactions will not appear in the output.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of transactions. This is due to the sorting operation implicit in the `ROW_NUMBER()` function.