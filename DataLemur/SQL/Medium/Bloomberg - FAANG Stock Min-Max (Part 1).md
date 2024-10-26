# Bloomberg Stock Min-Max Prices Problem

## Problem Statement
Given a table `stock_prices` containing historical stock prices, we need to find the month and opening price for each stock ticker’s highest and lowest opening prices. The result should display each `ticker` with its highest and lowest opening prices along with the corresponding months, ordered by `ticker`.

## Table Structure
**stock_prices** table:
| Column Name | Type      |
|-------------|-----------|
| ticker      | string    |
| date        | date      |
| open        | decimal   |

## Example Input

Suppose the `stock_prices` table has the following data:

| ticker | date       | open |
|--------|------------|------|
| AAPL   | 2023-01-10 | 150  |
| AAPL   | 2023-02-15 | 155  |
| AAPL   | 2023-03-10 | 145  |
| AAPL   | 2023-04-05 | 160  |
| MSFT   | 2023-01-12 | 300  |
| MSFT   | 2023-02-20 | 310  |
| MSFT   | 2023-03-18 | 295  |
| MSFT   | 2023-04-22 | 305  |
| TSLA   | 2023-01-18 | 180  |
| TSLA   | 2023-02-19 | 175  |
| TSLA   | 2023-03-15 | 190  |
| TSLA   | 2023-04-11 | 185  |

### Explanation of Example Data
In this data:
- `AAPL` has the highest opening price of 160 in April 2023 and the lowest opening price of 145 in March 2023.
- `MSFT` has the highest opening price of 310 in February 2023 and the lowest opening price of 295 in March 2023.
- `TSLA` has the highest opening price of 190 in March 2023 and the lowest opening price of 175 in February 2023.

## Expected Output
| ticker | highest_mth | highest_open | lowest_mth | lowest_open |
|--------|-------------|--------------|------------|-------------|
| AAPL   | Apr-2023    | 160          | Mar-2023   | 145         |
| MSFT   | Feb-2023    | 310          | Mar-2023   | 295         |
| TSLA   | Mar-2023    | 190          | Feb-2023   | 175         |

```sql
WITH ranked_prices AS (
  SELECT 
    ticker,
    TO_CHAR(date, 'Mon-YYYY') AS month,
    open,
    ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open DESC, date) AS high_rank,
    ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open ASC, date) AS low_rank
  FROM stock_prices
)
SELECT
  ticker,
  COALESCE(MAX(CASE WHEN high_rank = 1 THEN month END), 'N/A') AS highest_mth,
  COALESCE(MAX(CASE WHEN high_rank = 1 THEN open END), 0) AS highest_open,
  COALESCE(MAX(CASE WHEN low_rank = 1 THEN month END), 'N/A') AS lowest_mth,
  COALESCE(MAX(CASE WHEN low_rank = 1 THEN open END), 0) AS lowest_open
FROM ranked_prices
GROUP BY ticker
ORDER BY ticker;
```

```sql
WITH highest_prices AS (
    SELECT 
        ticker,
        TO_CHAR(date, 'Mon-YYYY') AS highest_mth,
        MAX(open) AS highest_open,
        ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open DESC) AS row_num
    FROM stock_prices
    GROUP BY ticker, open, date
),
lowest_prices AS (
    SELECT 
        ticker,
        TO_CHAR(date, 'Mon-YYYY') AS lowest_mth,
        MIN(open) AS lowest_open,
        ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open) AS row_num
    FROM stock_prices
    GROUP BY ticker, open, date
)
SELECT
    highest.ticker,
    highest.highest_mth,
    highest.highest_open,
    lowest.lowest_mth,
    lowest.lowest_open
FROM highest_prices AS highest
JOIN lowest_prices AS lowest
    ON lowest.ticker = highest.ticker
    AND highest.row_num = 1  -- Highest open price
    AND lowest.row_num = 1   -- Lowest open price
ORDER BY highest.ticker;
```

## Solution Outline

1. **Common Table Expression (CTE)**:
   - We use a single CTE to calculate the ranks for both the highest and lowest opening prices for each ticker.
   - The `ROW_NUMBER()` function is applied twice to rank prices:
     - `ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open DESC, date)` ranks the highest prices (with ties resolved by date).
     - `ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open ASC, date)` ranks the lowest prices (with ties resolved by date).

2. **Selecting the Highest and Lowest Prices**:
   - The main query uses conditional aggregation to select only the rows where the highest and lowest prices occur (where `high_rank = 1` and `low_rank = 1`).
   - This ensures that only the top-ranked highest and lowest records per ticker are selected without duplicate entries.

3. **Handling Missing Values with `COALESCE`**:
   - We use `COALESCE` to provide default values in cases where there may be no match for the highest or lowest prices, ensuring consistent output.

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the number of rows in `stock_prices`. The use of `ROW_NUMBER()` with `PARTITION BY` and `ORDER BY` has a complexity of O(n log n) due to sorting.
- **Space Complexity**: O(n), as the CTE temporarily stores rankings for each row in `stock_prices`.

## Key Concepts
- **Window Functions** (`ROW_NUMBER() OVER (PARTITION BY ...)`)
- **Conditional Aggregation** with `CASE` statements
- **Handling NULLs with `COALESCE`**

## Additional Notes
- This optimized solution avoids multiple scans of the `stock_prices` table, making it more efficient than approaches with multiple CTEs.
- Ordering `open DESC, date` and `open ASC, date` within `ROW_NUMBER()` ensures consistent results for tied values by selecting the earliest date.

## Difficulty
Medium

## Related Topics
- **Window Functions and Ranking**
- **Aggregate Functions**
- **Date Formatting in SQL**

## Source
[DataLemur](https://datalemur.com/questions/sql-bloomberg-stock-min-max-1)
