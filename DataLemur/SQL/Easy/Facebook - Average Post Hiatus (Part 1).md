# Average Post Hiatus (Part 1)

## Problem Statement
Facebook is analyzing user activity to understand posting behavior. Write a query to find the number of days between the first and last post for each user in the year 2021. Only include users who have posted at least twice. Output the user_id and the number of days between their first and last post, ordered by the number of days in descending order.

## Table Structure
**posts** table:
| Column Name | Type      |
|-------------|-----------|
| post_id     | integer   |
| user_id     | integer   |
| post_date   | date      |

## Expected Output
| user_id | days_between |
|---------|--------------|
| 101     | 300          |
| 202     | 250          |

## Solution

```sql
SELECT
  user_id,
  (MAX(post_date) - MIN(post_date))::int AS days_between
FROM  
  posts
WHERE EXTRACT(YEAR FROM post_date) = 2021 
GROUP BY
  user_id
HAVING  
  COUNT(user_id) >= 2
ORDER BY
  days_between DESC;
````

## Explanation
1. **(MAX(post_date) - MIN(post_date))::int**: Calculates the difference between the latest and earliest post dates for each user in 2021 and casts the interval to an integer to get the number of days.
2. **WHERE EXTRACT(YEAR FROM post_date) = 2021**: Filters posts to include only those from the year 2021.
3. **GROUP BY user_id**: Groups the results by user to calculate the difference for each user.
4. **HAVING COUNT(user_id) >= 2**: Ensures that only users who posted at least twice in 2021 are included.
5. **ORDER BY days_between DESC**: Orders the results by the number of days between the first and last post in descending order.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of posts in 2021. This is due to the sorting operation (ORDER BY).
- **Space Complexity**: O(m), where m is the number of unique user_ids.

## Key Concepts
- Date arithmetic
- Aggregation with MAX and MIN
- Filtering with HAVING
- Sorting results

## Additional Notes
- This solution assumes that the `post_date` column is of a date type that supports subtraction to yield an interval.
- The query efficiently handles large datasets by filtering and aggregating before sorting.

## Difficulty
Easy

## Related Topics
- Date and Time Functions
- Data Aggregation
- Filtering and Sorting

## Source
[DataLemur](https://datalemur.com/questions/sql-average-post-hiatus-1)

