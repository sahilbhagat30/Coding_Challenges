# User Activity Analysis

## Problem Statement
Identify users who have logged at least one activity within 30 days of their registration date. 

The output should include:
- The user's `ID`
- Their `registration date`
- A count of the number of activities logged within that 30-day period.

**Conditions:**
- Exclude users who did not perform any activity within the 30-day period.

**Tables:**
1. **user_profiles**:
   - `user_id`: bigint
   - `signup_date`: datetime
   - `name`: text
   - `email`: text

2. **user_activities**:
   - `user_id`: bigint
   - `activity_date`: datetime
   - `activity_type`: text

---

## SQL Solution

```sql
WITH CTE AS (
    SELECT 
        UA.USER_ID,
        COUNT(*) AS NUMBER_OF_ACTIVITIES
    FROM 
        user_activities UA
    JOIN 
        user_profiles UP 
    ON 
        UA.USER_ID = UP.USER_ID
    WHERE 
        UA.ACTIVITY_DATE BETWEEN UP.signup_date AND DATE_ADD(UP.signup_date, INTERVAL 30 DAY)
    GROUP BY 
        UA.USER_ID
)
SELECT 
    CTE.USER_ID,
    UP.signup_date,
    CTE.NUMBER_OF_ACTIVITIES
FROM 
    CTE
JOIN 
    user_profiles UP 
ON 
    CTE.USER_ID = UP.USER_ID;
```

---

## Explanation
1. **CTE Step:**
   - Filters activities logged within 30 days of `signup_date`.
   - Counts the number of activities (`COUNT(*)`) for each `USER_ID`.
   
2. **Main Query:**
   - Joins the `CTE` back to `user_profiles` to retrieve the `signup_date` and include only those users who meet the criteria.

---

## Output Columns
1. `USER_ID`: Unique identifier of the user.
2. `signup_date`: The date the user signed up.
3. `NUMBER_OF_ACTIVITIES`: Number of activities logged by the user within 30 days of signing up.

---

## Notes
- This query ensures that users without activities in the 30-day window are excluded.
- The `WHERE` clause inside the `CTE` handles filtering of activities to the desired date range.

---

## Use Case
This query can be used to identify user engagement soon after signup, which can provide insights into user behavior and help in improving onboarding processes.
