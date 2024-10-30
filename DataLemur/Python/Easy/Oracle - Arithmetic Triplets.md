# Arithmetic Triplets

## Problem Statement
You are tasked with finding the number of arithmetic triplets in a list of integers. An arithmetic triplet is defined as three indices \(i < j < k\) such that the elements at these indices form an arithmetic sequence with a common difference.

```py
def arithmeticTriplets(nums: list[int], diff: int) -> int:
    numTriplets = 0
    num_set = set(nums)  # Use a set for O(1) lookups

    for num in nums:
        # Check if the two required numbers exist in the set
        if (num + diff) in num_set and (num + 2 * diff) in num_set:
            numTriplets += 1

    return numTriplets

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 4, 6, 7, 11, 12]
    diff = 5
    result = arithmeticTriplets(nums, diff)
    print(f'Total arithmetic triplets: {result}')
```

## Explanation
1. **Using a Set**: The `num_set` variable is created to store the numbers in `nums`, allowing for O(1) average time complexity for lookups.
2. **Looping Through Each Number**: For each number in `nums`, the code checks if both `num + diff` and `num + 2 * diff` exist in the set.
3. **Counting Valid Triplets**: If both conditions are met, it increments the `numTriplets` counter.

> **Note**: The function counts valid triplets based on the arithmetic sequence defined by the common difference.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in `nums`. Each lookup in the set is O(1).
- **Space Complexity**: O(n) for storing the numbers in the set.

## Key Concepts
- Set operations for efficient lookups
- Arithmetic sequences
- Counting valid triplets

## Additional Notes
- This solution efficiently handles large datasets due to its linear time complexity.
- Ensure that the input list contains unique integers for accurate triplet counting.

## Difficulty
Easy

## Related Topics
- Combinatorial problems
- Array manipulation
- Sequence analysis

## Source
[DataLemur](https://datalemur.com/questions/python-arithmetic-triplets)