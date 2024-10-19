# Pharmacy Analytics (Part 3)

## Problem Statement
CVS Health wants to gain a clearer understanding of its pharmacy sales and the performance of various products. Write a query to calculate the total drug sales for each manufacturer. Round the answer to the nearest million and report your results in descending order of total sales. In case of any duplicates, sort them alphabetically by the manufacturer name. Format the results as "$36 million".

## Table Structure
**pharmacy_sales** table:
| Column Name  | Type    |
|--------------|---------|
| product_id   | integer |
| units_sold   | integer |
| total_sales  | decimal |
| cogs         | decimal |
| manufacturer | varchar |
| drug         | varchar |

## Expected Output
| manufacturer | sale        |
|--------------|-------------|
| Biogen       | $4 million  |
| Eli Lilly    | $3 million  |

## Solution


