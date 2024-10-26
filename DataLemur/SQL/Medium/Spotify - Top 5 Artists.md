# Top Fans Rank

## Problem Statement
You are tasked with finding the top 5 artists whose songs appear most frequently in the Top 10 of the global song rank. Display the top 5 artist names in ascending order, along with their song appearance ranking. If two or more artists have the same number of song appearances, they should be assigned the same ranking, and the rank numbers should be continuous.

## Table Structure
**artists** table:
| Column Name   | Type      |
|---------------|-----------|
| artist_id     | integer   |
| artist_name   | varchar   |
| label_owner    | varchar   |

**songs** table:
| Column Name   | Type      |
|---------------|-----------|
| song_id       | integer   |
| artist_id     | integer   |
| name          | varchar   |

**global_song_rank** table:
| Column Name   | Type              |
|---------------|-------------------|
| day           | integer (1-52)    |
| song_id       | integer           |
| rank          | integer (1-1,000,000) |

## Expected Output
| artist_name   | artist_rank |
|---------------|-------------|
| Ed Sheeran    | 1           |
| Drake         | 2           |
| Bad Bunny     | 3           |
| Lady Gaga     | 4           |
| Adele         | 5           |

## Solution

```sql
WITH CTE AS (
  SELECT
    A.artist_name,
    DENSE_RANK() OVER(ORDER BY COUNT(G.song_id) DESC) AS artist_rank
  FROM
    artists A
  JOIN
    songs S ON S.artist_id = A.artist_id
  JOIN
    global_song_rank G ON G.song_id = S.song_id AND G.rank < 11
  GROUP BY 
    A.artist_name
)
SELECT
  artist_name,
  artist_rank
FROM 
  CTE
WHERE
  artist_rank <= 5  -- Use <= to include ties in the top 5
ORDER BY 
  artist_rank;  -- Order by rank for clarity

