## Responsible for Most Customers

### **Objective**
Each employee is assigned one territory and is responsible for the customers from this territory. There may be multiple employees assigned to the same territory. The goal is to find the employees who are responsible for the highest number of customers.

### **Tables:**

#### **map_employee_territory**
| Column        | Data Type |
|--------------|----------|
| empl_id      | text     |
| territory_id | text     |

#### **map_customer_territory**
| Column        | Data Type |
|--------------|----------|
| cust_id      | text     |
| territory_id | text     |

---

### **Initial Solution (Suboptimal)**
```sql
WITH cte AS(
    SELECT 
        et.empl_id,
        ct.cust_id,
        COUNT(*) OVER(PARTITION BY et.empl_id) AS customer_count
    FROM map_employee_territory et
    JOIN map_customer_territory ct
        ON ct.territory_id = et.territory_id
)   
SELECT 
    empl_id, customer_count
FROM 
    cte
WHERE 
    customer_count = (SELECT MAX(customer_count) FROM cte);
```

### **Issues with the Initial Solution**
1. **Redundant Window Function:**
   - `COUNT(*) OVER(PARTITION BY et.empl_id)` recalculates for every row unnecessarily.
2. **Use of Subquery for MAX():**
   - The subquery for `MAX(customer_count)` forces an additional scan over `cte`, making it inefficient.

---

### **Optimized Solution (Best Approach)**
```sql
WITH CustomerCounts AS (
    SELECT 
        et.empl_id,
        COUNT(ct.cust_id) AS customer_count
    FROM map_employee_territory et
    JOIN map_customer_territory ct
        ON et.territory_id = ct.territory_id
    GROUP BY et.empl_id
),
RankedEmployees AS (
    SELECT 
        empl_id,
        customer_count,
        RANK() OVER (ORDER BY customer_count DESC) AS rank_order
    FROM CustomerCounts
)
SELECT empl_id, customer_count
FROM RankedEmployees
WHERE rank_order = 1;
```

### **Why This Solution is Better**
✅ **Avoids Redundant Window Functions:**
   - Uses `COUNT(ct.cust_id)` with `GROUP BY` instead of `COUNT(*) OVER()`.
✅ **Uses `RANK()` Instead of MAX() Subquery:**
   - Efficiently retrieves employees with the highest customer count.
✅ **Handles Ties Gracefully:**
   - If multiple employees have the highest customer count, it returns all of them.

---

### **Expected Output Example**
| empl_id | customer_count |
|---------|---------------|
| E849    | 4             |
| E850    | 4             |

---

### **Conclusion**
This optimized query significantly improves efficiency by:
1. **Precomputing aggregations** to minimize recalculations.
2. **Using ranking functions** to remove unnecessary subqueries.
3. **Ensuring scalability** for larger datasets with more employees and customers.

This solution effectively retrieves employees managing the highest number of customers with minimal computation overhead. 🚀
