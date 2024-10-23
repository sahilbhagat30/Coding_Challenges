# Duplicate Job Listings

## Problem Statement
Assume you're given a table containing job postings from various companies on the LinkedIn platform. Write a query to retrieve the count of companies that have posted duplicate job listings.

Definition:
- Duplicate job listings are defined as two jobs at the same company with identical job titles and descriptions.

## Table Structure
**job_listings** table:
| Column Name | Type    |
|-------------|---------|
| job_id      | integer |
| company_id  | integer |
| title       | string  |
| description | string  |

## Expected Output
| duplicate_companies |
|---------------------|
| 1                   |

## Solution using INNER JOIN

```sql
SELECT COUNT(DISTINCT j1.company_id) AS duplicate_companies
FROM job_listings j1
INNER JOIN job_listings j2 ON 
  j1.company_id = j2.company_id AND
  j1.title = j2.title AND
  j1.description = j2.description AND
  j1.job_id < j2.job_id
````

## Explanation of INNER JOIN Solution
1. We use a self-join on the job_listings table.
2. The join conditions match company_id, title, and description.
3. We add `j1.job_id < j2.job_id` to avoid matching a job with itself and to avoid counting the same pair twice.
4. We count distinct company_ids to get the number of companies with duplicates.

## Complexity Analysis
- Time Complexity: O(n^2) in the worst case, where n is the number of job listings. This is due to the self-join operation.
- Space Complexity: O(1), as we're only storing a single count.

## Key Concepts
- Self-join
- INNER JOIN
- COUNT and DISTINCT operations

## Additional Notes
- This solution might be less efficient than the GROUP BY approach for large datasets due to the self-join.
- It correctly handles multiple duplicates within the same company.

## Alternative Solution (Using GROUP BY)

```sql
SELECT COUNT(DISTINCT company_id) AS duplicate_companies
FROM (
  SELECT 
    company_id, 
    title, 
    description, 
    COUNT(*) AS job_count
  FROM 
    job_listings
  GROUP BY 
    company_id, title, description
  HAVING 
    COUNT(*) > 1
) AS duplicates;
````

## Explanation of GROUP BY Solution
1. We use a subquery to group job listings by company_id, title, and description.
2. The HAVING clause filters for groups with more than one job listing (duplicates).
3. In the outer query, we count the distinct company_ids from this result.

## Difficulty
Easy

## Related Topics
- Data Aggregation
- INNER JOIN
- Self-join
- Duplicate Detection

## Source
[DataLemur](https://datalemur.com/questions/duplicate-job-listings)

