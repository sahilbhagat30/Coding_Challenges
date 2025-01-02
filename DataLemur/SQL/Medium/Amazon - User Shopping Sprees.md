-- **SQL Query for Users with Two Future Transactions**

## Problem Statement
Identify users who have at least two future transactions following any given transaction, ordered by the transaction date.

---

## Query

### Correct Query 1:
```sql
SELECT DISTINCT a.user_id
FROM (
    SELECT 
        user_id, 
        transaction_date, 
        LEAD(transaction_date, 1) OVER (PARTITION BY user_id ORDER BY transaction_date) AS oneday,
        LEAD(transaction_date, 2) OVER (PARTITION BY user_id ORDER BY transaction_date) AS twoday
    FROM transactions
) a
WHERE a.oneday IS NOT NULL AND a.twoday IS NOT NULL;
```

#### Explanation:

### Step 1: LEAD Function
- **Purpose**: The `LEAD` function retrieves subsequent rows for the same `user_id`, ordered by the `transaction_date`.
- **How it Works**:
  - `LEAD(transaction_date, 1)`: Fetches the next transaction date.
  - `LEAD(transaction_date, 2)`: Fetches the transaction date two rows ahead.

- Example Output for `LEAD`:
| user_id | transaction_date     | oneday              | twoday              |
|---------|----------------------|---------------------|---------------------|
| 1       | 2022-08-01 00:00:00 | 2022-08-02 00:00:00 | 2022-08-03 00:00:00 |
| 1       | 2022-08-02 00:00:00 | 2022-08-03 00:00:00 | 2022-08-05 00:00:00 |
| 1       | 2022-08-03 00:00:00 | 2022-08-05 00:00:00 | NULL                |
| 1       | 2022-08-05 00:00:00 | NULL                | NULL                |

---

### Step 2: WHERE Clause
- **Condition**:
  - `a.oneday IS NOT NULL`: Ensures there is at least one future transaction.
  - `a.twoday IS NOT NULL`: Ensures there is a second future transaction.

- **Filtered Output**:
| user_id | transaction_date     | oneday              | twoday              |
|---------|----------------------|---------------------|---------------------|
| 1       | 2022-08-01 00:00:00 | 2022-08-02 00:00:00 | 2022-08-03 00:00:00 |
| 1       | 2022-08-02 00:00:00 | 2022-08-03 00:00:00 | 2022-08-05 00:00:00 |

---

### Step 3: DISTINCT and Final Output
- **Purpose**: Use `DISTINCT` to return unique `user_id` values from the filtered rows.

- **Final Output**:
| user_id |
|---------|
| 1       |

---

### Correct Query 2:
```sql
SELECT a.user_id
FROM (
    SELECT 
        user_id, 
        transaction_date, 
        LAG(transaction_date, 1) OVER (PARTITION BY user_id ORDER BY transaction_date) AS oneday,
        LAG(transaction_date, 2) OVER (PARTITION BY user_id ORDER BY transaction_date) AS twoday
    FROM transactions
) a
WHERE a.oneday = transaction_date - INTERVAL '1 day' 
  AND a.twoday = transaction_date - INTERVAL '2 day';
```

#### Explanation:

### Step 1: LAG Function
- **Purpose**: The `LAG` function retrieves rows preceding the current row for the same `user_id`, ordered by `transaction_date`.
  - `LAG(transaction_date, 1)`: Fetches the previous transaction date.
  - `LAG(transaction_date, 2)`: Fetches the transaction date two rows before.

- Example Output for `LAG`:
| user_id | transaction_date     | oneday              | twoday              |
|---------|----------------------|---------------------|---------------------|
| 1       | 2022-08-01 00:00:00 | NULL                | NULL                |
| 1       | 2022-08-02 00:00:00 | 2022-08-01 00:00:00 | NULL                |
| 1       | 2022-08-03 00:00:00 | 2022-08-02 00:00:00 | 2022-08-01 00:00:00 |

---

### Step 2: WHERE Clause
- **Condition**:
  - `a.oneday = transaction_date - INTERVAL '1 day'`: Checks if the previous transaction occurred exactly one day earlier.
  - `a.twoday = transaction_date - INTERVAL '2 day'`: Checks if the transaction two rows earlier occurred exactly two days earlier.

- **Filtered Output**:
| user_id | transaction_date     | oneday              | twoday              |
|---------|----------------------|---------------------|---------------------|
| 1       | 2022-08-03 00:00:00 | 2022-08-02 00:00:00 | 2022-08-01 00:00:00 |

---

### Step 3: Final Output
- **Final Output**:
| user_id |
|---------|
| 1       |

---

### Correct Query 3:
```sql
WITH RankedTransactions AS (
    SELECT
        user_id,
        DATE(transaction_date) AS transaction_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY DATE(transaction_date)) AS row_num
    FROM
        transactions
),
GroupedTransactions AS (
    SELECT
        user_id,
        transaction_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY DATE(transaction_date)) - 
        DATEDIFF(transaction_date, '1970-01-01') AS grp
    FROM
        RankedTransactions
),
ConsecutiveGroups AS (
    SELECT
        user_id,
        COUNT(*) AS consecutive_days
    FROM
        GroupedTransactions
    GROUP BY
        user_id,
        grp
    HAVING
        COUNT(*) >= 3
)
SELECT DISTINCT
    user_id
FROM
    ConsecutiveGroups
ORDER BY
    user_id;
```

#### Explanation:

### Step 1: Assigning Row Numbers
- **ROW_NUMBER()**: Assigns sequential row numbers for each user based on their transaction dates.

### Step 2: Calculating Group Identifiers
- The formula `ROW_NUMBER() - DATEDIFF(transaction_date, '1970-01-01')` ensures consecutive dates receive the same group identifier (`grp`).

### Step 3: Grouping and Counting
- Transactions are grouped by `grp` values, and sequences with three or more consecutive dates are identified using `HAVING COUNT(*) >= 3`.

### Final Output:
| user_id |
|---------|
| 2       |
| 5       |

---

## Performance Considerations
1. **Indexing**:
   - Ensure indexes on `user_id` and `transaction_date` to optimize the partitioning and ordering operations.

2. **Window Function Efficiency**:
   - The `LEAD`, `LAG`, and `ROW_NUMBER` functions perform efficiently for sequential data, avoiding self-joins.

---
