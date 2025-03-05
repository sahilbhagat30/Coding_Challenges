# Finding User Purchases

## **Problem Statement**
Identify **returning active users** by finding users who made a **second purchase** within **7 days** of any previous purchase.

### **Expected Output**
Your output should include:
- `user_id`

### **Database Schema**
#### **amazon_transactions Table**
| Column Name  | Data Type  |
|-------------|-----------|
| transaction_id | bigint  |
| user_id     | bigint    |
| product_id  | bigint    |
| created_at  | datetime  |
| amount      | decimal   |

---

## **SQL Query to Identify Returning Active Users**
```sql
SELECT DISTINCT fp.user_id
FROM amazon_transactions fp
JOIN amazon_transactions sp
    ON fp.user_id = sp.user_id
    AND sp.created_at > fp.created_at
WHERE DATEDIFF(sp.created_at, fp.created_at) < 7;
```

### **Explanation:**
1. **Self-Join on `user_id`**: Joins the `amazon_transactions` table to itself to find transactions for the same user.
2. **Filtering Future Purchases**: Ensures `sp.created_at > fp.created_at` to compare only subsequent transactions.
3. **Checking the 7-Day Window**: Uses `DATEDIFF(sp.created_at, fp.created_at) < 7` to find purchases within 7 days.
4. **`DISTINCT` Ensures Unique Users**: Outputs only the unique `user_id` values that meet the condition.

---

## **Expected Output Format**
| user_id  |
|---------|
| 10234   |
| 10567   |
| 11089   |

---

### **Optimized Alternative Using `EXISTS`**
If performance is a concern for large datasets:
```sql
SELECT DISTINCT user_id
FROM amazon_transactions fp
WHERE EXISTS (
    SELECT 1
    FROM amazon_transactions sp
    WHERE fp.user_id = sp.user_id
    AND sp.created_at > fp.created_at
    AND DATEDIFF(sp.created_at, fp.created_at) < 7
);
```

### **Why Use `EXISTS`?**
✅ Improves efficiency by stopping the search **once a match is found**.  
✅ Reduces the number of rows processed in large datasets.

---

### **Conclusion**
- **The JOIN approach** works well for moderate-sized datasets.
- **Using `EXISTS`** is more efficient for large-scale transaction tables.

🚀

