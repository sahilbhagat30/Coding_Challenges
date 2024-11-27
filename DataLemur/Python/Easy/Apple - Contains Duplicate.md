# Contains Duplicate

## Problem Statement
Given a list of integers called `input`, return `True` if any value appears at least twice in the array. Return `False` if every element in the input list is distinct.

For example:
- If the input list is `[1, 3, 5, 7, 1]`, return `True` because the number `1` appears twice.
- If the input list is `[1, 3, 5, 7]`, return `False` because every element of the list is distinct.

## Function Definition
```python
def contains_duplicate(input) -> bool:
    uniqueList = []
    
    for i in input:
        if i not in uniqueList:
            uniqueList.append(i)
        else:
            return True
            
    return False
```

## Example Usage
```python
# Example inputs
input_1 = [1, 3, 5, 7, 1]
input_2 = [1, 3, 5, 7]

# Checking for duplicates
print(contains_duplicate(input_1))  # Output: True
print(contains_duplicate(input_2))  # Output: False
```

**Output**:
```
True
False
```

## Explanation
1. **Duplicate Check**: The function iterates over the input list and checks if each element already exists in the `uniqueList`. If an element already exists, it returns `True`. Otherwise, it adds the element to the `uniqueList`.
2. **Return False**: If no duplicates are found after iterating through the list, it returns `False`.

## Complexity Analysis
- **Time Complexity**: O(n^2) due to the `in` operation on a list being O(n). Each lookup can take O(n) time, and in the worst case, we iterate over the entire list.
- **Space Complexity**: O(n), as a list is used to store unique elements.

## Optimized Version
For better performance, consider using a set to keep track of unique elements.

```python
def contains_duplicate(input) -> bool:
    unique_set = set()
    
    for i in input:
        if i in unique_set:
            return True
        unique_set.add(i)
            
    return False
```

This version has a:
- **Time Complexity**: O(n), as set lookups are on average O(1).
- **Space Complexity**: O(n), as a set is used to store unique elements.

## Related Topics
- Lists
- Set operations
- Complexity analysis

## Difficulty
Easy
