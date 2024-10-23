# Teams Power Users

## Problem Statement
Microsoft Teams is analyzing its user activity to identify power users. Write a query to find the top 2 users who sent the most messages in August 2022. Output the sender_id and the corresponding message count.

## Table Structure
**messages** table:
| Column Name | Type      |
|-------------|-----------|
| message_id  | integer   |
| sender_id   | integer   |
| sent_date   | timestamp |

## Expected Output
| sender_id | message_count |
|-----------|---------------|
| 101       | 150           |
| 202       | 140           |

## Solution

```sql
SELECT
  sender_id,
  COUNT(sender_id) AS message_count
FROM
  messages
WHERE
  EXTRACT(MONTH FROM sent_date) = 8 AND
  EXTRACT(YEAR FROM sent_date) = 2022
GROUP BY
  sender_id
ORDER BY
  message_count DESC
LIMIT 2;
````

## Explanation
1. **EXTRACT(MONTH FROM sent_date) = 8**: Filters for messages sent in August.
2. **EXTRACT(YEAR FROM sent_date) = 2022**: Ensures the messages are from the year 2022.
3. **GROUP BY sender_id**: Groups the results by sender to count messages per sender.
4. **ORDER BY message_count DESC**: Orders the results by the number of messages in descending order.
5. **LIMIT 2**: Limits the results to the top 2 senders.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of messages in August 2022. This is due to the sorting operation (ORDER BY).
- **Space Complexity**: O(m), where m is the number of unique sender_ids.

## Key Concepts
- Date extraction and filtering
- Aggregation with COUNT
- Sorting and limiting results

## Additional Notes
- This solution assumes that the `sent_date` column is of a timestamp type that supports the EXTRACT function.
- The query efficiently handles large datasets by filtering and aggregating before sorting.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- Date and Time Functions
- Sorting and Limiting

## Source
[DataLemur](https://datalemur.com/questions/teams-power-users)

