## Interaction Summary

### Problem Statement
Calculate the total number of interactions and the total number of content items created for each customer. Include all interaction types and content types in your calculations.

The output should include:
1. **Customer ID**
2. **Total number of interactions**
3. **Total number of content items**

#### Tables:

**customer_interactions**:
| Column          | Type     | Description                       |
|-----------------|----------|-----------------------------------|
| customer_id     | bigint   | Unique ID of the customer.        |
| interaction_id  | bigint   | Unique ID of the interaction.     |
| interaction_date| datetime | Date of the interaction.          |
| interaction_type| text     | Type of interaction.              |

**user_content**:
| Column          | Type     | Description                       |
|-----------------|----------|-----------------------------------|
| content_id      | bigint   | Unique ID of the content.         |
| content_text    | text     | Text of the content.              |
| content_type    | text     | Type of the content.              |
| customer_id     | bigint   | ID of the customer who created it.|

---

### SQL Solution

The query below calculates the total interactions and total content items for each customer, including customers with data only in one of the two tables:

```sql
WITH CTE1 AS (
    SELECT 
        customer_id,
        COUNT(interaction_id) AS total_interactions
    FROM 
        customer_interactions
    GROUP BY 
        customer_id
),
CTE2 AS (
    SELECT 
        customer_id,
        COUNT(content_id) AS total_content
    FROM 
        user_content
    GROUP BY 
        customer_id
)
SELECT 
    COALESCE(A.customer_id, B.customer_id) AS customer_id,
    COALESCE(A.total_interactions, 0) AS total_interactions,
    COALESCE(B.total_content, 0) AS total_content
FROM (
    SELECT * FROM CTE1
) A
LEFT JOIN (
    SELECT * FROM CTE2
) B ON A.customer_id = B.customer_id

UNION

SELECT 
    COALESCE(A.customer_id, B.customer_id) AS customer_id,
    COALESCE(A.total_interactions, 0) AS total_interactions,
    COALESCE(B.total_content, 0) AS total_content
FROM (
    SELECT * FROM CTE1
) A
RIGHT JOIN (
    SELECT * FROM CTE2
) B ON A.customer_id = B.customer_id;
```

---

### Explanation

1. **Common Table Expressions (CTEs)**:
   - `CTE1`: Counts the total interactions for each customer from `customer_interactions`.
   - `CTE2`: Counts the total content items for each customer from `user_content`.

2. **Handling Missing Data**:
   - Use a `LEFT JOIN` to include customers with only interactions.
   - Use a `RIGHT JOIN` to include customers with only content.
   - Combine results with a `UNION` to simulate a `FULL OUTER JOIN`.

3. **COALESCE**:
   - Handles `NULL` values resulting from the joins:
     - `COALESCE(A.customer_id, B.customer_id)`: Ensures the `customer_id` is included from either table.
     - `COALESCE(..., 0)`: Replaces `NULL` interaction or content counts with `0`.

---

### Example Output
Given the following input:

#### customer_interactions
| customer_id | interaction_id | interaction_type | interaction_date |
|-------------|----------------|------------------|------------------|
| 1           | 101            | like             | 2024-10-01       |
| 1           | 102            | comment          | 2024-10-02       |
| 2           | 103            | like             | 2024-10-03       |

#### user_content
| customer_id | content_id | content_type | content_text |
|-------------|------------|--------------|--------------|
| 1           | 201        | post         | "Hello"    |
| 3           | 202        | post         | "Hi"       |

#### Output:
| customer_id | total_interactions | total_content |
|-------------|--------------------|---------------|
| 1           | 2                  | 1             |
| 2           | 1                  | 0             |
| 3           | 0                  | 1             |

---

### Key Points
- This query ensures that all customers are included, even if they appear in only one table.
- It handles `NULL` values effectively using `COALESCE`.
- The `UNION` of `LEFT JOIN` and `RIGHT JOIN` simulates a `FULL OUTER JOIN` since MySQL does not natively support it.

---

### Optimization Tips
1. **Indexing**:
   - Add indexes on `customer_id` in both tables to optimize the joins.

2. **Data Volume**:
   - For large datasets, consider testing performance and optimizing further based on execution plans.

---

### Learnings
- MySQL does not support `FULL OUTER JOIN`, but it can be simulated using `LEFT JOIN`, `RIGHT JOIN`, and `UNION`.
- `COALESCE` is essential for handling `NULL` values when merging datasets.
