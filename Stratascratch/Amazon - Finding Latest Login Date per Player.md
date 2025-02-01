# Finding Latest Login Date per Player

## Problem Statement
Write a query to find the latest date when each video game player logged in.

## Given Table: `players_logins`
| player_id | login_date |
|-----------|------------|
| 101       | 2021-12-14 |
| 101       | 2021-12-18 |
| 101       | 2021-12-15 |
| 101       | 2021-12-19 |
| 102       | 2021-12-31 |
| 102       | 2022-01-01 |
| 102       | 2022-01-15 |
| 102       | 2022-01-15 |
| 103       | 2020-12-22 |
| 103       | 2021-12-23 |
| 103       | 2021-12-15 |
| 104       | 2022-01-14 |
| 105       | 2022-01-08 |
| 105       | 2022-01-06 |
| 105       | 2022-01-10 |
| 106       | 2022-01-24 |
| 106       | 2022-01-25 |
| 106       | 2022-01-24 |
| 106       | 2022-01-25 |
| 106       | 2022-01-26 |
| 106       | 2022-01-26 |

## Best Optimized Solution
```sql
SELECT 
    player_id, 
    MAX(login_date) AS latest_date  
FROM players_logins 
GROUP BY player_id;
```

## **Why This is the Best Solution?**
✅ **Uses `MAX(login_date)` to efficiently get the latest login per player**  
✅ **`GROUP BY player_id` groups logins correctly by player**  
✅ **Simple and highly performant for retrieving the latest login date**  

## **Expected Output**
| player_id | latest_date |
|-----------|------------|
| 101       | 2021-12-19 |
| 102       | 2022-01-15 |
| 103       | 2021-12-23 |
| 104       | 2022-01-14 |
| 105       | 2022-01-10 |
| 106       | 2022-01-26 |

## **Alternative Approach Using `ROW_NUMBER()` (For More Flexibility)**
If additional details are required or multiple logins exist on the latest date, we can use `ROW_NUMBER()`:
```sql
WITH latest_logins AS (
    SELECT 
        player_id, 
        login_date, 
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY login_date DESC) AS rn
    FROM players_logins
)
SELECT player_id, login_date AS latest_date
FROM latest_logins
WHERE rn = 1;
```
✅ **Ensures tie-breaking with `ORDER BY login_date DESC`**  
✅ **Allows retrieval of additional details if needed**  

🚀 **Use `MAX()` for best performance, or `ROW_NUMBER()` for more flexibility!** Let me know if you need further refinements! 🎯
