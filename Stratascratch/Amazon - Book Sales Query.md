## Book Sales Query

### **Objective**
Calculate the total revenue made per book. The output should include the book ID and the total sales per book. If a book has never been sold, it should still be included in the output with a total sales value of 0.

### **Tables:**

#### **amazon_books**
| Column     | Data Type |
|------------|----------|
| book_id    | text     |
| book_title | text     |
| unit_price | bigint   |

#### **amazon_books_order_details**
| Column           | Data Type |
|-----------------|----------|
| book_id         | text     |
| order_details_id | text     |
| order_id        | text     |
| quantity        | bigint   |

---

### **SQL Query**
```sql
SELECT 
    ab.book_id,
    SUM(COALESCE(ab.unit_price * abod.quantity, 0)) AS total_sales_per_book
FROM 
    amazon_books ab
LEFT JOIN 
    amazon_books_order_details abod ON ab.book_id = abod.book_id
GROUP BY 
    ab.book_id;
```

---

### **Explanation:**
1. **Join the `amazon_books` and `amazon_books_order_details` tables** using a LEFT JOIN to ensure all books are included, even if they have no sales.
2. **Multiply `unit_price` by `quantity`** to calculate the revenue per book.
3. **Use `SUM()`** to aggregate total sales per book.
4. **Use `COALESCE()`** to replace `NULL` values with `0` for books that have never been sold.
5. **Group by `book_id`** to get sales totals per book.

---

### **Expected Output Example:**
| book_id | total_sales_per_book |
|---------|----------------------|
| B001    | 450                 |
| B002    | 0                   |
| B003    | 1500                |

---

### **Why This Query is Optimized?**
✅ **Ensures all books are included** even if they haven't been sold.
✅ **Uses `SUM()` instead of calculating per row** for efficiency.
✅ **Replaces NULL values with 0** using `COALESCE()`.
✅ **Scalable for large datasets** with proper indexing on `book_id`.

This solution effectively computes book sales revenue while handling edge cases efficiently! 🚀
