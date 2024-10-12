# Histogram of Tweets

## Problem Statement
Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count as the bucket and the number of Twitter users who fall into that bucket.

## Table Structure
**tweets** table:
| Column Name | Type     |
|-------------|----------|
| tweet_id    | integer  |
| user_id     | integer  |
| tweet_date  | datetime |

## Expected Output
| tweet_bucket | users_num |
|--------------|-----------|
| 1            | 2         |
| 2            | 1         |
| 3            | 2         |

## Solution

```sql

WITH tweet_count AS (
    SELECT 
        user_id,
        COUNT(*) AS tweet_count_per_user
    FROM tweets
    WHERE EXTRACT(YEAR FROM tweet_date) = 2022
    GROUP BY user_id
)

SELECT 
    tweet_count_per_user AS tweet_bucket,
    COUNT(*) AS user_num
FROM tweet_count
GROUP BY tweet_bucket
ORDER BY tweet_bucket;

```

## Explanation

1. We start by creating a Common Table Expression (CTE) named `tweet_counts`:
   - This CTE counts the number of tweets per user for the year 2022.
   - We use `EXTRACT(YEAR FROM tweet_date) = 2022` to filter for tweets from 2022.
   - The `GROUP BY user_id` ensures we get a count for each user.

2. In the main query, we use the `tweet_counts` CTE:
   - We select `tweet_count_per_user` as our `tweet_bucket`.
   - We count the number of users for each `tweet_bucket` using `COUNT(*)`.
   - We group by `tweet_count_per_user` to create the histogram.
   - Finally, we order the results by `tweet_bucket` for a clear presentation.

This solution efficiently creates a histogram of tweet counts, showing how many users (users_num) fall into each tweet count bucket (tweet_bucket).

## Complexity Analysis
- Time Complexity: O(n), where n is the number of rows in the tweets table. We scan the table once to count tweets per user, and then aggregate these counts.
- Space Complexity: O(m), where m is the number of unique users. In the worst case, we need to store a count for each user in the CTE.

## Alternative Approaches
An alternative approach could use a subquery instead of a CTE, but the CTE makes the query more readable and potentially more efficient in some database systems.
