# Common Friends Script

## Problem Statement
You are analyzing a social network dataset at Google. Your task is to find mutual friends between two users, Karl and Hans. There is only one user named Karl and one named Hans in the dataset.

The output should contain:
- `user_id`
- `user_name`

### Tables
- **users**:
  - `user_id` (bigint): Unique ID for each user.
  - `user_name` (text): Name of the user.

- **friends**:
  - `friend_id` (bigint): ID of the user's friend.
  - `user_id` (bigint): ID of the user.

---

## Original SQL Solution

```sql
WITH cte AS (
    SELECT 
        friend_id
    FROM friends
    WHERE user_id = (SELECT user_id FROM users WHERE user_name = 'Karl')
), cte1 AS (
    SELECT 
        friend_id
    FROM friends
    WHERE user_id = (SELECT user_id FROM users WHERE user_name = 'Hans')
)
SELECT 
    users.user_id, 
    users.user_name
FROM 
    cte
JOIN 
    cte1 ON cte1.friend_id = cte.friend_id
JOIN 
    users ON users.user_id = cte.friend_id;
```

---

## Optimized SQL Solution

```sql
WITH mutual_friends AS (
    SELECT 
        f1.friend_id
    FROM 
        friends f1
    JOIN 
        friends f2 ON f1.friend_id = f2.friend_id
    WHERE 
        f1.user_id = (SELECT user_id FROM users WHERE user_name = 'Karl')
        AND f2.user_id = (SELECT user_id FROM users WHERE user_name = 'Hans')
)
SELECT 
    u.user_id, 
    u.user_name
FROM 
    mutual_friends mf
JOIN 
    users u ON u.user_id = mf.friend_id;
```

---

## Explanation

### Original Query
1. **Retrieve Friends of Karl**:
   - A CTE retrieves the `friend_id` values for all friends of Karl by finding his `user_id` in the `users` table.

2. **Retrieve Friends of Hans**:
   - A second CTE retrieves the `friend_id` values for all friends of Hans by finding his `user_id` in the `users` table.

3. **Find Mutual Friends**:
   - The `JOIN` between `cte` and `cte1` identifies mutual friends by matching their `friend_id`.
   - The final `JOIN` with the `users` table retrieves the `user_id` and `user_name` of the mutual friends.

### Optimized Query
1. **Single CTE**:
   - Combines the logic for Karl's and Hans' friends by joining the `friends` table on `friend_id`.
   - Reduces redundancy by avoiding two separate CTEs.

2. **Identify Mutual Friends**:
   - Finds the intersection of Karl's and Hans' friends directly in the `mutual_friends` CTE.

3. **Fetch User Details**:
   - Joins with the `users` table to retrieve `user_id` and `user_name` for the mutual friends.

---

## Example Input and Output

### Input Data
#### Table: users
| user_id | user_name |
|---------|-----------|
| 1       | Karl      |
| 2       | Hans      |
| 3       | Alice     |
| 4       | Bob       |
| 5       | Charlie   |

#### Table: friends
| user_id | friend_id |
|---------|-----------|
| 1       | 3         |
| 1       | 4         |
| 2       | 4         |
| 2       | 5         |

### Output Data
| user_id | user_name |
|---------|-----------|
| 4       | Bob       |

---

## Conclusion
Both queries correctly identify mutual friends between Karl and Hans. The optimized query is preferred for its simplicity, performance, and reduced redundancy while maintaining the same functionality.
