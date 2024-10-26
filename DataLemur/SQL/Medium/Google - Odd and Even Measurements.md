# Odd-Even Measurements Problem

## Problem Statement
Given a table with a list of measurements, the task is to calculate and display separate statistics for odd and even measurements. Specifically, you need to determine how to split the measurements into odd and even based on a unique identifier (e.g., `measurement_id`) and calculate aggregate statistics such as `COUNT`, `SUM`, or `AVG` for each set.

## Table Structure
**measurements** table:
| Column Name      | Type    |
|------------------|---------|
| measurement_id   | integer |
| value            | integer |

## Expected Output
| type  | count | sum   | avg   |
|-------|-------|-------|-------|
| odd   | ...   | ...   | ...   |
| even  | ...   | ...   | ...   |

```sql
WITH CTE AS (
SELECT 
    CAST(measurement_time AS DATE) AS measurement_day, 
    measurement_value,
    ROW_NUMBER() OVER(
    PARTITION BY CAST(measurement_time AS DATE)
    ORDER BY measurement_time) AS measurement_num 
  FROM measurements
)
SELECT
  measurement_day,
  SUM(measurement_value) FILTER (WHERE MOD(measurement_num,2)=1) odd_sum,
  SUM(measurement_value) FILTER (WHERE MOD(measurement_num,2)=0) even_sum
FROM  
  CTE
GROUP BY
  measurement_day
```


## Solution Outline

1. **Identify Odd and Even Measurements**:
   - To distinguish between odd and even measurements, we use the modulo operation on `measurement_id`:
     - A measurement is **even** if `measurement_id % 2 = 0`.
     - A measurement is **odd** if `measurement_id % 2 != 0`.

2. **Aggregate Data Separately for Odd and Even Measurements**:
   - We can use a `CASE` statement inside aggregate functions to calculate statistics separately for odd and even measurements.
   - Aggregate functions like `COUNT`, `SUM`, and `AVG` will be used to get the desired statistics.

3. **Combine Results**:
   - The results for odd and even measurements can be selected in the same query, using conditional aggregation with `CASE` statements.
   - This allows us to have all necessary aggregates in one result set.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of rows in the `measurements` table, as each row needs to be checked and aggregated once.
- **Space Complexity**: O(1), as we are only storing the final aggregates.

## Key Concepts
- **Conditional Aggregation** using `CASE` statements
- **Modulo Operation** for identifying odd/even values
- **Aggregate Functions** (`COUNT`, `SUM`, `AVG`)

## Additional Notes
- If there are no odd or even measurements, the query should handle this gracefully, typically returning `NULL` or zero for the aggregate values.
- Ensure that the table is indexed on `measurement_id` if the table is large, to speed up the filtering by odd and even values.

## Difficulty
Medium

## Related Topics
- **Conditional Aggregation**
- **Mathematical Operators (Modulo)**
- **Aggregate Functions in SQL**

## Source
[DataLemur](https://datalemur.com/questions/odd-even-measurements)
