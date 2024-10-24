# Rolling Average Tweets

## Problem Statement
Twitter is analyzing user activity to understand tweeting behavior. Write a query to calculate the 3-day rolling average of tweets for each user. Output the user_id, tweet_date, and the rolling average of tweet_count, rounded to two decimal places.

## Table Structure
**tweets** table:
| Column Name | Type      |
|-------------|-----------|
| tweet_id    | integer   |
| user_id     | integer   |
| tweet_date  | date      |
| tweet_count | integer   |

## Expected Output
| user_id | tweet_date | rolling_avg |
|---------|------------|-------------|
| 101     | 2023-01-01 | 5.00        |
| 101     | 2023-01-02 | 4.50        |
| 101     | 2023-01-03 | 4.67        |

## Solution

```sql
SELECT 
  user_id,
  tweet_date,
  ROUND(AVG(tweet_count)
  OVER(
    PARTITION BY user_id
    ORDER BY tweet_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ), 2) AS rolling_avg
FROM tweets;
````

## Explanation
1. **PARTITION BY user_id**: Ensures that the rolling average is calculated separately for each user.
2. **ORDER BY tweet_date**: Orders the tweets by date to calculate the rolling average over time.
3. **ROWS BETWEEN 2 PRECEDING AND CURRENT ROW**: Specifies a window frame that includes the current row and the two preceding rows, effectively calculating a 3-day rolling average.
4. **ROUND(..., 2)**: Rounds the rolling average to two decimal places.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of tweets. This is due to the ordering operation (ORDER BY).
- **Space Complexity**: O(m), where m is the number of unique user_ids.

## Key Concepts
- Window functions
- Rolling averages
- Date ordering

## Additional Notes
- This solution assumes that the `tweet_date` column is of a date type that supports ordering.
- The query efficiently handles large datasets by using window functions.

## Difficulty
Medium

## Related Topics
- Window Functions
- Data Aggregation
- Rolling Calculations

## Source
[DataLemur](https://datalemur.com/questions/rolling-average-tweets)

