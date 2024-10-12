# Page With No Likes

## Problem Statement
Assume you're given two tables containing data about Facebook Pages and their respective likes. Write a query to return the IDs of the Facebook pages that have zero likes. The output should be sorted in ascending order based on the page IDs.

## Table Structure
**pages** table:
| Column Name | Type    |
|-------------|---------|
| page_id     | integer |
| page_name   | varchar |

**page_likes** table:
| Column Name | Type     |
|-------------|----------|
| user_id     | integer  |
| page_id     | integer  |
| liked_date  | datetime |

## Sample Data
**pages** table:
| page_id | page_name |
|---------|-----------|
| 20001   | SQL Solutions |
| 20045   | Brain Exercises |
| 20701   | Tips for Data Analysts |

**page_likes** table:
| user_id | page_id | liked_date |
|---------|---------|------------|
| 111     | 20001   | 04/08/2022 |
| 121     | 20045   | 03/12/2022 |
| 156     | 20001   | 07/25/2022 |

## Expected Output
| page_id |
|---------|
| 20701   |

## Solution

```sql
SELECT p.page_id
FROM pages p
LEFT OUTER JOIN page_likes pl ON p.page_id = pl.page_id
WHERE pl.page_id IS NULL
ORDER BY p.page_id ASC;
```

## Explanation

This SQL query solves the problem through the following steps:

1. We start with a LEFT OUTER JOIN between the `pages` table (p) and the `page_likes` table (pl) on the `page_id` column.
2. The LEFT OUTER JOIN ensures that all pages are included in the result, even if they don't have any likes.
3. We then use a WHERE clause to filter for pages where `pl.page_id IS NULL`. This condition is true only for pages that don't have any corresponding entries in the `page_likes` table, i.e., pages with zero likes.
4. Finally, we ORDER BY `p.page_id ASC` to sort the results in ascending order of page IDs.

This approach effectively identifies pages that don't have any likes and presents them in the required order.

## Complexity Analysis
- Time Complexity: O(n log n), where n is the total number of rows in both tables combined. This is due to the sorting operation (ORDER BY) which typically uses a comparison-based sorting algorithm.
- Space Complexity: O(m), where m is the number of pages with no likes. In the worst case, this could be equal to the total number of pages.

## Alternative Approaches
1. Using EXCEPT operator:
   ```sql
   SELECT page_id FROM pages
   EXCEPT
   SELECT page_id FROM page_likes
   ORDER BY page_id ASC;
   ```
2. Using NOT IN clause:
   ```sql
   SELECT page_id FROM pages
   WHERE page_id NOT IN (SELECT page_id FROM page_likes)
   ORDER BY page_id ASC;
   ```
3. Using NOT EXISTS clause:
   ```sql
   SELECT p.page_id FROM pages p
   WHERE NOT EXISTS (SELECT 1 FROM page_likes pl WHERE pl.page_id = p.page_id)
   ORDER BY p.page_id ASC;
   ```

Each approach has its own merits and can be more or less efficient depending on the specific database system and data distribution. The LEFT OUTER JOIN approach used in the solution is generally efficient and widely supported across different database systems.

[Source](https://datalemur.com/questions/sql-page-with-no-likes)
