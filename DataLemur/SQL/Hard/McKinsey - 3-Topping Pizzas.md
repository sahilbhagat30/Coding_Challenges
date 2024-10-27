# 3-Topping Combination Problem

## Problem Statement
Given three toppings—`Chicken`, `Pepperoni`, and `Sausage`—the task is to determine all unique 3-topping combinations that can be created from this set and calculate the total ingredient cost for each combination.

## Input Table
**pizza_toppings** table:
| topping_name | ingredient_cost |
|--------------|-----------------|
| Chicken      | 0.55            |
| Pepperoni    | 0.50            |
| Sausage      | 0.70            |

## Expected Output
Since there are only three toppings in the input, there is only one unique 3-topping combination possible:

| pizza                     | total_cost |
|---------------------------|------------|
| Chicken, Pepperoni, Sausage | 1.75      |

```sql
SELECT DISTINCT
  CONCAT(p1.topping_name, ',', p2.topping_name, ',', p3.topping_name) AS pizza,
  p1.ingredient_cost + p2.ingredient_cost + p3.ingredient_cost AS total_cost
FROM 
  pizza_toppings AS p1
CROSS JOIN 
  pizza_toppings AS p2
CROSS JOIN 
  pizza_toppings AS p3
WHERE 
  p1.topping_name < p2.topping_name
  AND p2.topping_name < p3.topping_name
ORDER BY 
  total_cost DESC;
```

### Explanation
- The only 3-topping combination possible from this set is `Chicken, Pepperoni, Sausage`.
- The total cost for this combination is calculated by summing the individual ingredient costs:
  - `0.55 (Chicken) + 0.50 (Pepperoni) + 0.70 (Sausage) = 1.75`

## Solution Outline

1. **Generate Unique Combinations**:
   - Since the input set has exactly three toppings, there is only one possible 3-topping combination: `Chicken, Pepperoni, Sausage`.

2. **Calculate Total Cost**:
   - Sum the `ingredient_cost` for `Chicken`, `Pepperoni`, and `Sausage` to get the total cost for the combination.

3. **Output**:
   - Display the single unique 3-topping combination along with its total cost.

## Key Concepts
- **Combination Generation**: For a set of three unique toppings, only one unique 3-topping combination exists.
- **Summation of Costs**: The total cost is computed by summing the individual ingredient costs.

## Additional Notes
- For any distinct set of three toppings, the total combinations of exactly three toppings will always result in one unique combination.
- This approach can be generalized to larger sets where more unique combinations would be possible if subsets of fewer items are included.

## Difficulty
Easy

## Related Topics
- **Combinatorics**
- **Cost Calculation**

## Source
Custom Problem Scenario
