### Query: Most Profitable Companies

#### Objective:
The goal of this query is to find the top 3 most profitable companies from the `forbes_global_2010_2014` dataset.

#### Dataset Details:
- **Table Name**: `forbes_global_2010_2014`
- **Columns**:
  - `assets` (double)
  - `company` (text)
  - `continent` (text)
  - `country` (text)
  - `industry` (text)
  - `marketvalue` (double)
  - `profits` (double)
  - `rank` (bigint)
  - `sales` (double)
  - `sector` (text)
  - `forbeswebpage` (text)

#### SQL Query:
```sql
SELECT company, profits
FROM 
(
    SELECT
        company,
        profits,
        DENSE_RANK() OVER(ORDER BY profits DESC) company_rank
    FROM 
        forbes_global_2010_2014
) AS t 
WHERE t.company_rank <= 4;
```

#### Explanation:
1. **Subquery**:
   - Select `company` and `profits` from the table.
   - Use the `DENSE_RANK()` window function to rank companies based on their `profits` in descending order.
   - Assign the rank to a new column `company_rank`.

2. **Outer Query**:
   - Filter the results to include only companies with a rank (`company_rank`) less than 4, i.e., the top 3 most profitable companies.

#### Output Columns:
- `company`: Name of the company.
- `profits`: Profit value of the company.

#### Use Case:
This query is useful for identifying the most profitable companies globally and can help stakeholders make informed business decisions.


-- Query: Most Profitable Companies

-- Objective:
-- The goal of this query is to find the top 3 most profitable companies
-- from the `forbes_global_2010_2014` dataset.

-- Dataset Details:
-- Table Name: `forbes_global_2010_2014`
-- Columns:
--   assets (double)
--   company (text)
--   continent (text)
--   country (text)
--   industry (text)
--   marketvalue (double)
--   profits (double)
--   rank (bigint)
--   sales (double)
--   sector (text)
--   forbeswebpage (text)

-- Optimized SQL Query

SELECT company, profits
FROM (
    SELECT company, profits,
           DENSE_RANK() OVER (ORDER BY profits DESC) AS company_rank
    FROM forbes_global_2010_2014
) ranked_companies
WHERE company_rank <= 3;

-- Explanation:
-- 1. Subquery:
--    - Select `company` and `profits` from the table.
--    - Use the `DENSE_RANK()` window function to rank companies based on their `profits` in descending order.
--    - Assign the rank to a new column `company_rank`.

-- 2. Outer Query:
--    - Filter the results to include only companies with a rank (`company_rank`) less than or equal to 3, i.e., the top 3 most profitable companies.

-- Output Columns:
-- - company: Name of the company.
-- - profits: Profit value of the company.

-- Use Case:
-- This query is useful for identifying the most profitable companies globally and can help stakeholders make informed business decisions.
