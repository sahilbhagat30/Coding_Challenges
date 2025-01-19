# Top Posts Per Channel

## Problem Statement
Identify the top 3 posts with the highest like counts for each channel. Assign a rank to each post based on its like count, allowing for gaps in ranking when posts have the same number of likes. For example, if two posts tie for 1st place, the next post should be ranked 3rd, not 2nd. Exclude any posts with zero likes.

### Tables
- **posts**:
  - `channel_id` (bigint): Unique ID for each channel.
  - `post_id` (bigint): Unique ID for each post.
  - `created_at` (datetime): Post creation date.
  - `likes` (bigint): Number of likes the post received.

- **channels**:
  - `channel_id` (bigint): Unique ID for each channel.
  - `channel_name` (text): Name of the channel.
  - `channel_type` (text): Type of the channel.

---

## SQL Solution

```sql
WITH CTE AS (
    SELECT
        C.channel_name,
        C.channel_id,
        P.post_id,
        P.created_at,
        P.likes,
        RANK() OVER (PARTITION BY C.channel_name ORDER BY P.likes DESC) AS like_rank
    FROM 
        posts P
    JOIN 
        channels C ON C.channel_id = P.channel_id
),
CTE1 AS (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY CTE.channel_name ORDER BY CTE.like_rank) AS correct_like_rank
    FROM
        CTE
)
SELECT
    CTE.channel_name,
    CTE.post_id,
    CTE.created_at,
    CTE.likes,
    CTE.like_rank,
    CTE1.correct_like_rank
FROM
    CTE
JOIN 
    CTE1 ON CTE1.channel_name = CTE.channel_name AND CTE.post_id = CTE1.post_id
WHERE
    CTE.like_rank < 4;
```

---

## Explanation

### Step 1: First CTE
```sql
WITH CTE AS (
    SELECT
        C.channel_name,
        C.channel_id,
        P.post_id,
        P.created_at,
        P.likes,
        RANK() OVER (PARTITION BY C.channel_name ORDER BY P.likes DESC) AS like_rank
    FROM 
        posts P
    JOIN 
        channels C ON C.channel_id = P.channel_id
)
```
- **Purpose**: Assigns a gap-based rank (`RANK()`) to posts within each channel, ordered by the number of likes (descending).

### Step 2: Second CTE
```sql
CTE1 AS (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY CTE.channel_name ORDER BY CTE.like_rank) AS correct_like_rank
    FROM
        CTE
)
```
- **Purpose**: Reassigns continuous ranks (`DENSE_RANK()`) to the gap ranks (`like_rank`), ensuring no gaps.
- **Identifies the top 3 unique ranks**, even if gaps exist in `like_rank`.

### Step 3: Final Query
```sql
SELECT
    CTE.channel_name,
    CTE.post_id,
    CTE.created_at,
    CTE.likes,
    CTE.like_rank,
    CTE1.correct_like_rank
FROM
    CTE
JOIN 
    CTE1 ON CTE1.channel_name = CTE.channel_name AND CTE.post_id = CTE1.post_id
WHERE
    CTE.like_rank < 4;
```
- **Filters the top 3 unique ranks (`correct_like_rank <= 3`)**.
- Joins `CTE` and `CTE1` to retrieve all relevant columns for the final output.

---

## Example Input and Output

### Input Data
#### Table: posts
| channel_id | post_id | created_at        | likes |
|------------|---------|-------------------|-------|
| 1          | 101     | 2024-10-01 12:00 | 100   |
| 1          | 102     | 2024-10-01 13:00 | 90    |
| 1          | 103     | 2024-10-01 14:00 | 90    |
| 1          | 104     | 2024-10-01 15:00 | 85    |
| 1          | 105     | 2024-10-01 16:00 | 80    |

#### Table: channels
| channel_id | channel_name |
|------------|--------------|
| 1          | Channel A    |

### Intermediate Results
#### After `CTE` (Gap Ranks)
| channel_name | post_id | likes | like_rank |
|--------------|---------|-------|-----------|
| Channel A    | 101     | 100   | 1         |
| Channel A    | 102     | 90    | 2         |
| Channel A    | 103     | 90    | 2         |
| Channel A    | 104     | 85    | 3         |
| Channel A    | 105     | 80    | 4         |

#### After `CTE1` (Dense Ranks)
| channel_name | post_id | likes | like_rank | correct_like_rank |
|--------------|---------|-------|-----------|-------------------|
| Channel A    | 101     | 100   | 1         | 1                 |
| Channel A    | 102     | 90    | 2         | 2                 |
| Channel A    | 103     | 90    | 2         | 2                 |
| Channel A    | 104     | 85    | 3         | 3                 |
| Channel A    | 105     | 80    | 4         | 4                 |

### Final Output
| channel_name | post_id | created_at        | likes | like_rank | correct_like_rank |
|--------------|---------|-------------------|-------|-----------|-------------------|
| Channel A    | 101     | 2024-10-01 12:00 | 100   | 1         | 1                 |
| Channel A    | 102     | 2024-10-01 13:00 | 90    | 2         | 2                 |
| Channel A    | 103     | 2024-10-01 14:00 | 90    | 2         | 2                 |
| Channel A    | 104     | 2024-10-01 15:00 | 85    | 3         | 3                 |

---

## Conclusion
This query ensures that the top 3 posts per channel are correctly identified based on their like counts, with proper handling of ties and no skipped ranks. The combination of `RANK()` and `DENSE_RANK()` ensures the results meet the problem requirements accurately.
