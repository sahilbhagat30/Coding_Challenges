# Find Duplicate Records in the Dataset

## **Problem Statement**
You need to identify duplicate records in the dataset.

### **Expected Output**
Your output should include:
- `worker_title`
- `affected_from` date
- The number of times each duplicate record appears in the dataset.

### **Database Schema**
#### **title Table**
| Column Name    | Data Type  |
|---------------|------------|
| worker_ref_id | bigint     |
| worker_title  | text       |
| affected_from | datetime   |

---

## **SQL Query to Find Duplicate Records**
```sql
SELECT
    worker_title,
    affected_from,
    COUNT(*) AS duplicate_count
FROM title
GROUP BY worker_title, affected_from
HAVING COUNT(*) > 1;
```

### **Explanation:**
1. **Grouping Data**: The query groups records by `worker_title` and `affected_from`.
2. **Counting Duplicates**: `COUNT(*)` counts the number of occurrences of each record.
3. **Filtering Duplicates**: `HAVING COUNT(*) > 1` ensures that only duplicate records appear in the output.

---

## **Expected Output Format**
| worker_title      | affected_from | duplicate_count |
|-------------------|--------------|----------------|
| Data Engineer    | 2024-05-01    | 2              |
| Data Scientist   | 2024-06-10    | 3              |

---

## **Alternative Query Using `ROW_NUMBER()`**
If you want to retrieve duplicate records with row numbers:
```sql
WITH duplicate_records AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY worker_title, affected_from ORDER BY worker_ref_id) AS row_num
    FROM title
)
SELECT
    worker_title,
    affected_from,
    COUNT(*) AS duplicate_count
FROM duplicate_records
WHERE row_num > 1
GROUP BY worker_title, affected_from;
```

### **Why Use `ROW_NUMBER()`?**
✅ Useful when dealing with large datasets.  
✅ Provides row-level duplicate detection.  
✅ Can help in debugging and deduplication tasks.

---

### **Conclusion**
Both approaches effectively identify duplicate records. The first method is **simple and efficient**, while the second method is **useful for row-level duplicate analysis**. 🚀

