# The Company Problem

## Problem Statement
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:

Write a query to print the `company_code`, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending `company_code`.

### Notes:
1. The tables may contain duplicate records.
2. The `company_code` is a string, so sorting should not be numeric. For example, if the company codes are `C_1`, `C_2`, and `C_10`, then the ascending order is `C_1`, `C_10`, `C_2`.

## Input Tables
**COMPANY** table:
| Column Name    | Data Type |
|----------------|-----------|
| COMPANY_CODE   | VARCHAR   |
| FOUNDER        | VARCHAR   |

**LEAD_MANAGER** table:
| Column Name         | Data Type |
|---------------------|-----------|
| LEAD_MANAGER_CODE   | VARCHAR   |
| COMPANY_CODE        | VARCHAR   |

**SENIOR_MANAGER** table:
| Column Name         | Data Type |
|---------------------|-----------|
| SENIOR_MANAGER_CODE | VARCHAR   |
| LEAD_MANAGER_CODE   | VARCHAR   |
| COMPANY_CODE        | VARCHAR   |

**MANAGER** table:
| Column Name         | Data Type |
|---------------------|-----------|
| MANAGER_CODE        | VARCHAR   |
| SENIOR_MANAGER_CODE | VARCHAR   |
| LEAD_MANAGER_CODE   | VARCHAR   |
| COMPANY_CODE        | VARCHAR   |

**EMPLOYEE** table:
| Column Name         | Data Type |
|---------------------|-----------|
| EMPLOYEE_CODE       | VARCHAR   |
| MANAGER_CODE        | VARCHAR   |
| SENIOR_MANAGER_CODE | VARCHAR   |
| LEAD_MANAGER_CODE   | VARCHAR   |
| COMPANY_CODE        | VARCHAR   |

## Expected Output
| COMPANY_CODE | FOUNDER  | LEAD_MANAGER_COUNT | SENIOR_MANAGER_COUNT | MANAGER_COUNT | EMPLOYEE_COUNT |
|--------------|----------|--------------------|-----------------------|---------------|----------------|
| C1           | Monika   | 1                  | 2                     | 1             | 2              |
| C2           | Samantha | 1                  | 1                     | 2             | 2              |

## Optimized Solution
```sql
WITH DistinctCounts AS (
    SELECT 
        E.COMPANY_CODE,
        COUNT(DISTINCT LM.LEAD_MANAGER_CODE) AS LeadManagerCount,
        COUNT(DISTINCT SM.SENIOR_MANAGER_CODE) AS SeniorManagerCount,
        COUNT(DISTINCT M.MANAGER_CODE) AS ManagerCount,
        COUNT(DISTINCT E.EMPLOYEE_CODE) AS EmployeeCount
    FROM 
        EMPLOYEE E
    LEFT JOIN LEAD_MANAGER LM ON E.LEAD_MANAGER_CODE = LM.LEAD_MANAGER_CODE
    LEFT JOIN SENIOR_MANAGER SM ON E.SENIOR_MANAGER_CODE = SM.SENIOR_MANAGER_CODE
    LEFT JOIN MANAGER M ON E.MANAGER_CODE = M.MANAGER_CODE
    GROUP BY 
        E.COMPANY_CODE
)
SELECT 
    C.COMPANY_CODE,
    C.FOUNDER,
    DC.LeadManagerCount,
    DC.SeniorManagerCount,
    DC.ManagerCount,
    DC.EmployeeCount
FROM 
    COMPANY C
LEFT JOIN 
    DistinctCounts DC ON C.COMPANY_CODE = DC.COMPANY_CODE
ORDER BY 
    C.COMPANY_CODE;
```

### Explanation
- The `WITH` clause aggregates distinct counts for lead managers, senior managers, managers, and employees by joining their respective tables.
- A `LEFT JOIN` ensures all companies are included in the final result.
- The final `SELECT` retrieves founder information and the calculated counts, sorted by `COMPANY_CODE`.

## Key Concepts
- **JOIN Operations**: Combining data from multiple tables based on relationships.
- **Aggregation Functions**: Using `COUNT(DISTINCT column_name)` to count unique values.
- **Common Table Expressions (CTEs)**: Simplifying complex queries by precomputing results.

## Difficulty
Medium

## Related Topics
- **SQL Joins**
- **Aggregation**
- **CTEs**

---
