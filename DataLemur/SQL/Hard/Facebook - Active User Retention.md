# User Retention - Monthly Active Users (MAU)

## Problem Statement
You are tasked with calculating the number of Monthly Active Users (MAUs) for a given month (e.g., July 2022). An active user is defined as a user who has performed actions (such as 'sign-in', 'like', or 'comment') in both the current month and the previous month. The output should include the month in numerical format and the count of unique active users for that month.

## Table Structure
**user_actions** table:
| Column Name | Type       | Description                           |
|-------------|------------|---------------------------------------|
| user_id     | integer    | Unique identifier for each user       |
| event_id    | integer    | Unique identifier for each event      |
| event_type  | string     | Type of action performed by the user  |
| event_date  | datetime   | Date and time of the user action      |

## Example Input
| user_id | event_id | event_type | event_date           |
|---------|----------|------------|-----------------------|
| 445     | 7765     | sign-in    | 2022-05-31 12:00:00  |
| 742     | 6458     | sign-in    | 2022-06-03 12:00:00  |
| 445     | 3634     | like       | 2022-06-05 12:00:00  |
| 742     | 1374     | comment    | 2022-06-05 12:00:00  |
| 648     | 3124     | like       | 2022-06-18 12:00:00  |

## Expected Output
| month | monthly_active_users |
|-------|-----------------------|
| 6     | 1                    |
| 7     | ...                  |

```sql
SELECT
  EXTRACT(MONTH FROM curr_month.event_date) AS month,
  COUNT(DISTINCT curr_month.user_id) AS monthly_active_users
FROM
  user_actions AS curr_month
WHERE EXISTS (
  SELECT 
    last_month.user_id
  FROM
    user_actions AS last_month
  WHERE 
    last_month.user_id = curr_month.user_id
    AND EXTRACT(MONTH FROM last_month.event_date) = EXTRACT(MONTH FROM curr_month.event_date - INTERVAL '1 month')
    AND EXTRACT(YEAR FROM last_month.event_date) = EXTRACT(YEAR FROM curr_month.event_date)
)
GROUP BY 
  EXTRACT(MONTH FROM curr_month.event_date)
ORDER BY 
  EXTRACT(MONTH FROM curr_month.event_date);
```

### Explanation
In the provided example, for June 2022, only user `445` qualifies as a Monthly Active User (MAU), as they were active in both May and June. The count of monthly active users for June is therefore `1`.

## Solution Outline

1. **Extract and Group Activity by Month**:
   - Extract the month and year from the `event_date` column to determine the user’s activity for each month.
   - Filter activity based on whether users were active in both the current and previous months.

2. **Identify Users Active in Consecutive Months**:
   - Use a subquery or filtering condition to check if each user has activity recorded in both the current and prior month.
   - Ensure that the user is counted as active only if they have actions in both months within the same year.

3. **Count Unique Users**:
   - In the final step, count each unique `user_id` to determine the number of active users for the target month.
   - Ensure each user is counted only once per month, even if they performed multiple actions.

4. **Order the Results by Month**:
   - The output is ordered by month in ascending order for a clear and structured presentation of monthly active user counts.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of rows in the `user_actions` table. The complexity arises from checking each user's activity across months and the sorting operation.
- **Space Complexity**: O(n), as temporary storage is needed to store intermediate results for monthly activity.

## Key Concepts
- **Filtering with EXISTS**: Used to check if a user was active in the previous month.
- **Date Functions**: Extracting the month and year from `event_date` to filter activity by month.
- **Grouping and Counting**: Counting unique users per month for the final output.

## Additional Notes
- This solution identifies monthly active users based on their activity in both the current and previous months, fulfilling the criteria for Monthly Active Users (MAU).
- Using `DISTINCT` for `user_id` counts ensures each user is only counted once per month, avoiding duplicates due to multiple actions.

## Difficulty
Medium

## Related Topics
- **Date Functions and Filtering**
- **Subqueries and EXISTS**
- **Grouping and Aggregation**

## Source
[DataLemur](https://datalemur.com/questions/user-retention)
