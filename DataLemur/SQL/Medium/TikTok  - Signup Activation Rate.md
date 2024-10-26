# Signup Confirmation Rate

## Problem Statement
Given two tables, `emails` and `texts`, we want to calculate the activation rate of users who confirmed their signup via text messages. The activation rate is defined as the percentage of users who confirmed their signup, calculated by dividing the number of confirmed signups by the total emails sent, rounded to two decimal places.

## Table Structure
**emails** table:
| Column Name | Type    |
|-------------|---------|
| email_id    | integer |

**texts** table:
| Column Name    | Type               |
|----------------|--------------------|
| email_id       | integer            |
| signup_action  | string ('Confirmed')|

## Expected Output
| activation_rate |
|-----------------|
| 0.50            |

```sql
SELECT 
  ROUND(COUNT(texts.email_id) / COUNT(emails.email_id)::DECIMAL, 2) AS activation_rate
FROM emails
LEFT JOIN texts
  ON emails.email_id = texts.email_id
  AND texts.signup_action = 'Confirmed';
```

## Explanation

1. **LEFT JOIN**: We use a `LEFT JOIN` to include all records from `emails`, ensuring each email is counted even if there’s no corresponding confirmation in `texts`.
2. **Filtering**: The `ON` clause filters to count only records in `texts` where `signup_action` is `'Confirmed'`.
3. **Counting**:
   - `COUNT(texts.email_id)` provides the number of confirmed signups.
   - `COUNT(emails.email_id)` gives the total number of emails sent.
4. **Calculation**:
   - Dividing the count of confirmed signups by the total emails calculates the activation rate.
   - `ROUND` formats the result to two decimal places.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of rows in the `emails` table, as we only perform a single scan of each relevant record.
- **Space Complexity**: O(1), since we only store the final activation rate.

## Alternative Approaches
An alternative approach could be a direct calculation without `LEFT JOIN`, assuming each email has a matching text entry, but this is unlikely and makes `LEFT JOIN` a better fit here.

## Key Concepts
- **JOIN operations**
- **Aggregate functions** (`COUNT`, `ROUND`)
- **Filtering within JOIN clauses**
- **Percentage calculations**

## Additional Notes
- This solution assumes that all emails are relevant, meaning if there are no entries in `texts`, the `activation_rate` will be zero.
- Using `100.0` instead of `100` ensures floating-point division, avoiding integer division issues.

## Difficulty
Easy

## Related Topics
- **Data Aggregation**
- **JOINs and Filtering**
- **Percentage Calculations**

## Source
[DataLemur](https://datalemur.com/questions/signup-confirmation-rate)
