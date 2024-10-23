# Second Day Confirmation

## Problem Statement
TikTok is analyzing its user signup process. Write a query to find the user IDs of those who did not confirm their sign-up on the first day, but confirmed on the second day.

## Table Structure
**emails** table:
| Column Name | Type      |
|-------------|-----------|
| email_id    | integer   |
| user_id     | integer   |
| signup_date | timestamp |

**texts** table:
| Column Name   | Type      |
|---------------|-----------|
| text_id       | integer   |
| email_id      | integer   |
| signup_action | varchar   |
| action_date   | timestamp |

## Expected Output
| user_id |
|---------|
| 123     |
| 456     |

## Solution

```sql
SELECT
  user_id
FROM
  emails e
JOIN texts t ON t.email_id = e.email_id
WHERE t.action_date = e.signup_date + INTERVAL '1 day' AND t.signup_action = 'Confirmed'
````


## Explanation
1. We join the `emails` and `texts` tables on `email_id`.
2. We filter for users who confirmed their signup exactly one day after their signup date using `t.action_date = e.signup_date + INTERVAL '1 day'`.
3. We ensure only 'Confirmed' actions are considered with `t.signup_action = 'Confirmed'`.
4. We select the `user_id` of users meeting these criteria.

## Most Efficient Solution

```sql
SELECT DISTINCT e.user_id
FROM emails e
JOIN texts t ON e.email_id = t.email_id
WHERE t.signup_action = 'Confirmed'
  AND t.action_date = e.signup_date + INTERVAL '1 day'
  AND NOT EXISTS (
    SELECT 1
    FROM texts t2
    WHERE t2.email_id = e.email_id
      AND t2.signup_action = 'Confirmed'
      AND t2.action_date = e.signup_date
  )
````


## Explanation of Efficient Solution
1. We join `emails` and `texts` tables as before.
2. We filter for confirmations on the second day.
3. We use a NOT EXISTS subquery to ensure there was no confirmation on the first day.
4. We use DISTINCT to handle potential duplicate entries.

This solution is more efficient because it explicitly checks for the absence of a first-day confirmation, which is part of the problem statement but was implicit in the original solution.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of rows in the larger of the two tables. This is due to the JOIN operation.
- Space Complexity: O(m), where m is the number of users who confirmed on the second day.

## Key Concepts
- JOIN operations
- Date arithmetic in SQL
- Filtering data based on multiple conditions
- Subqueries and NOT EXISTS clause

## Additional Notes
- The query assumes that the `action_date` in the `texts` table and the `signup_date` in the `emails` table are of compatible types for date arithmetic.
- This solution will work in PostgreSQL and other SQL dialects that support the `INTERVAL` keyword for date arithmetic.
- The most efficient solution handles edge cases better, such as users who might have multiple confirmation attempts.

## Difficulty
Easy

## Related Topics
- Data Manipulation
- Date and Time Operations
- JOIN Operations
- Subqueries

## Source
[DataLemur](https://datalemur.com/questions/second-day-confirmation)

