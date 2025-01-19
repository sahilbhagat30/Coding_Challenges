# Population Density Analysis

## Problem Statement
You are working on a data analysis project at Deloitte where you need to analyze a dataset containing information about various cities. Your task is to calculate the population density of these cities, rounded to the nearest integer, and identify the cities with the minimum and maximum densities.

The population density should be calculated as (Population / Area).

### Output Requirements
The output should contain the following columns:
- `city`: Name of the city.
- `country`: Country of the city.
- `density`: Population density of the city, rounded to the nearest integer.

### Tables
- **cities_population**:
  - `city` (text): Name of the city.
  - `country` (text): Country of the city.
  - `population` (bigint): Population of the city.
  - `area` (decimal): Area of the city in square kilometers.

---

## SQL Solution

```sql
WITH population_density AS (
    SELECT 
        city, 
        country,
        ROUND((population / area), 0) AS density
    FROM
        cities_population
),
min_max_density AS (
    SELECT 
        MIN(density) AS min_density,
        MAX(density) AS max_density
    FROM 
        population_density
)
SELECT 
    city, 
    country,
    density
FROM 
    population_density
WHERE 
    density = (SELECT min_density FROM min_max_density)
    OR density = (SELECT max_density FROM min_max_density);
```

---

## Explanation

### Step 1: Calculate Population Density
```sql
WITH population_density AS (
    SELECT 
        city, 
        country,
        ROUND((population / area), 0) AS density
    FROM
        cities_population
)
```
- This step calculates the population density for each city as `population / area` and rounds the result to the nearest integer using `ROUND(..., 0)`.

### Step 2: Identify Cities with Minimum and Maximum Density
```sql
min_max_density AS (
    SELECT 
        MIN(density) AS min_density,
        MAX(density) AS max_density
    FROM 
        population_density
)
```
- This step computes the minimum and maximum population densities across all cities in one pass.

### Step 3: Retrieve Cities with Min/Max Density
```sql
SELECT 
    city, 
    country,
    density
FROM 
    population_density
WHERE 
    density = (SELECT min_density FROM min_max_density)
    OR density = (SELECT max_density FROM min_max_density);
```
- The final query retrieves cities with densities equal to the `min_density` or `max_density` values calculated in the previous step.
- The `OR` condition ensures that both minimum and maximum density cities are included in the result.

---

## Example Input and Output

### Input Data
#### Table: cities_population
| city       | country      | population | area  |
|------------|--------------|------------|-------|
| City A     | Country X    | 1,000,000  | 500.0 |
| City B     | Country Y    | 2,000,000  | 300.0 |
| City C     | Country Z    | 500,000    | 1000.0|

### Intermediate Results
#### After `population_density` CTE
| city       | country      | density |
|------------|--------------|---------|
| City A     | Country X    | 2000    |
| City B     | Country Y    | 6667    |
| City C     | Country Z    | 500     |

#### After `min_max_density` CTE
| min_density | max_density |
|-------------|-------------|
| 500         | 6667        |

### Final Output
| city       | country      | density |
|------------|--------------|---------|
| City C     | Country Z    | 500     |  -- Minimum Density
| City B     | Country Y    | 6667    |  -- Maximum Density

---

## Conclusion
This query calculates the population density for each city and accurately identifies the cities with the minimum and maximum densities. By leveraging a `WITH` clause and computing `MIN` and `MAX` in one step, the query is both efficient and easy to understand. The final result includes only the cities with the lowest and highest population densities.
