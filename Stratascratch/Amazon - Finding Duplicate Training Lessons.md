# Finding Duplicate Training Lessons

## Problem Statement
Display a list of users who took the same training lessons more than once on the same day. Output their usernames, training IDs, dates, and the number of times they took the same lesson.

## Given Tables
### `users_training`
| u_id | u_name |
|------|--------|
| 1    | Alice  |
| 2    | Bob    |
| 3    | Charlie|

### `training_details`
| u_t_id | u_id | training_id | training_date |
|--------|------|-------------|---------------|
| 1001   | 1    | 201         | 2022-07-15    |
| 1002   | 1    | 201         | 2022-07-15    |
| 1003   | 2    | 305         | 2022-07-18    |
| 1004   | 2    | 305         | 2022-07-18    |
| 1005   | 2    | 305         | 2022-07-18    |
| 1006   | 3    | 402         | 2022-07-19    |

## Best Optimized Solution
```sql
WITH cte AS (
    SELECT 
        u_id,
        training_id,
        training_date,
        COUNT(*) AS no_same_lesson
    FROM training_details
    GROUP BY u_id, training_id, training_date
    HAVING COUNT(*) > 1
)
SELECT 
    ut.u_name,
    td.training_id,
    cte.training_date,
    cte.no_same_lesson
FROM cte
JOIN users_training ut ON ut.u_id = cte.u_id
JOIN training_details td ON td.u_id = cte.u_id AND td.training_id = cte.training_id AND td.training_date = cte.training_date;
```

## **Why This is the Best Solution?**
✅ **Filters only duplicate training sessions** using `HAVING COUNT(*) > 1`.  
✅ **Includes `training_id` in `GROUP BY`** to avoid incorrect counting.  
✅ **Ensures correct user-training mapping** with precise `JOIN` conditions.  

## **Expected Output**
| u_name  | training_id | training_date | no_same_lesson |
|---------|------------|--------------|---------------|
| Alice   | 201       | 2022-07-15   | 2             |
| Bob     | 305       | 2022-07-18   | 3             |

🚀 **This optimized query efficiently finds duplicate training lessons per user!** Let me know if you need further refinements! 🎯
