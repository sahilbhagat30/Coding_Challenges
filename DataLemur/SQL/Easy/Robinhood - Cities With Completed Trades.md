# Cities With Completed Trades

## Problem Statement
Assume you're given the tables containing completed trade orders and user details in a Robinhood trading system. Write a query to retrieve the top three cities that have the highest number of completed trade orders listed in descending order. Output the city name and the corresponding number of completed trade orders.

## Table Structure
**trades** table:
| Column Name | Type                              |
|-------------|-----------------------------------|
| order_id    | integer                           |
| user_id     | integer                           |
| quantity    | integer                           |
| status      | string ('Completed', 'Cancelled') |
| date        | timestamp                         |
| price       | decimal (5, 2)                    |

**users** table:
| Column Name  | Type     |
|--------------|----------|
| user_id      | integer  |
| city         | string   |
| email        | string   |
| signup_date  | datetime |

## Expected Output
| city          | total_orders |
|---------------|--------------|
| San Francisco | 3            |
| Boston        | 2            |
| Denver        | 1            |

## Solution

```sql
SELECT 
  u.city city,
  count(t.order_id) total_orders
FROM users u
JOIN trades t on u.user_id = t.user_id and t.status = 'Completed'
GROUP BY
  u.city
ORDER BY
  total_orders DESC
LIMIT 3
````

## Explanation
1. We JOIN the users and trades tables on user_id.
2. We filter for only 'Completed' trades in the JOIN condition.
3. We GROUP BY city to get the count for each city.
4. We ORDER BY the count in descending order to get the highest counts first.
5. We LIMIT to 3 to get only the top three cities.

## Most Efficient Solution

```sql
SELECT 
  u.city,
  COUNT(*) AS total_orders
FROM 
  users u
INNER JOIN 
  trades t ON u.user_id = t.user_id
WHERE 
  t.status = 'Completed'
GROUP BY 
  u.city
ORDER BY 
  total_orders DESC
LIMIT 3
````

## Explanation of Efficient Solution
1. We use INNER JOIN instead of JOIN for clarity.
2. We move the status filter to a WHERE clause, which can be more efficient in some databases.
3. We use COUNT(*) instead of COUNT(t.order_id) as it's slightly more efficient.
4. The rest of the query remains the same.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the number of completed trades. This is due to the sorting operation (ORDER BY).
- Space Complexity: O(m), where m is the number of unique cities with completed trades.

## Key Concepts
- JOIN operations
- Aggregation with COUNT
- Filtering with WHERE
- Sorting with ORDER BY
- Limiting results with LIMIT

## Additional Notes
- This solution assumes that each user belongs to only one city.
- The query will automatically handle cases where a user has multiple completed trades.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- JOIN Operations
- Result Limiting

## Source
[DataLemur](https://datalemur.com/questions/completed-trades)

