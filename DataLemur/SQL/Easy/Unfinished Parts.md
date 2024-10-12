# Unfinished Parts

## Problem Statement
Tesla is investigating production bottlenecks and they need your help to extract the relevant data. Write a query to determine which parts have begun the assembly process but are not yet finished.

Assumptions:
* The table contains all parts currently in production, each at varying stages of the assembly process.
* An unfinished part is one that lacks a finish_date.

## Table Structure
**parts** table:
| Column Name    | Type     |
|----------------|----------|
| part           | string   |
| finish_date    | datetime |
| assembly_step  | integer  |

## Sample Data
**parts** table:
| part    | finish_date        | assembly_step |
|---------|---------------------|---------------|
| battery | 01/22/2022 00:00:00 | 1             |
| battery | 02/22/2022 00:00:00 | 2             |
| battery | 03/22/2022 00:00:00 | 3             |
| bumper  | 01/22/2022 00:00:00 | 1             |
| bumper  | 02/22/2022 00:00:00 | 2             |
| bumper  | NULL                | 3             |
| bumper  | NULL                | 4             |

## Expected Output
| part   | assembly_step |
|--------|---------------|
| bumper | 3             |
| bumper | 4             |

## Solution

```sql
SELECT part, assembly_step 
FROM parts_assembly
WHERE finish_date IS NULL
ORDER BY part ASC, assembly_step ASC;
```

## Explanation

[I'll provide the explanation after you've added your SQL code]

## Complexity Analysis
[To be added after seeing your solution]

## Alternative Approaches
[To be added if there are multiple valid approaches]

[Source](https://datalemur.com/questions/tesla-unfinished-parts)

