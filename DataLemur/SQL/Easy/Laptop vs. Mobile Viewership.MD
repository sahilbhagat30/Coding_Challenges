# Laptop vs. Mobile Viewership

## Problem Statement
Assume you're given a table on user viewership categorized by device type where the three types are laptop, tablet, and phone. Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as "laptop_views" and the total viewership for mobile devices as "mobile_views".

## Table Structure
**viewership** table:
| Column Name  | Type                                 |
|--------------|--------------------------------------|
| user_id      | integer                              |
| device_type  | string ('laptop', 'tablet', 'phone') |
| view_time    | timestamp                            |

## Sample Data
**viewership** table:
| user_id | device_type | view_time           |
|---------|-------------|---------------------|
| 123     | tablet      | 01/02/2022 00:00:00 |
| 125     | laptop      | 01/07/2022 00:00:00 |
| 128     | laptop      | 02/09/2022 00:00:00 |
| 129     | phone       | 02/09/2022 00:00:00 |
| 145     | tablet      | 02/24/2022 00:00:00 |

## Expected Output
| laptop_views | mobile_views |
|--------------|--------------|
| 2            | 3            |

## Solution

```sql
SELECT 
  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
  SUM(CASE WHEN device_type = 'phone' OR device_type = 'tablet' THEN 1 ELSE 0 END) AS mobile_views
FROM viewership
```

## Explanation

This SQL query effectively solves the problem by using CASE statements to count the number of laptop and mobile views.

## Complexity Analysis
[To be added after seeing your solution]

## Alternative Approaches
There are multiple ways to solve this problem:
1. Using COUNT() with CASE statements
2. Using SUM() with CASE statements
3. Using subqueries

Each approach has its own merits and can be more or less efficient depending on the specific database system and data distribution.

[Source](https://datalemur.com/questions/laptop-mobile-viewership)
