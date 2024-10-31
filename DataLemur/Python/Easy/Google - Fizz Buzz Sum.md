# Fizz Buzz Sum

## Problem Statement
Write a function to find the sum of all multiples of 3 or 5 below a target value. For example, if the target value is 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9. The function should return the sum of these multiples.

## Example
- **Input**: `target = 10`
- **Output**: `23` (because 3 + 5 + 6 + 9 = 23)

## Function Definition
```py
def fizz_buzz_sum(target):
    if target <= 0:
        return 0  # Handle non-positive targets
    total_sum = 0
    for n in range(1, target):  # Loop from 1 to target (exclusive)
        if n % 3 == 0 or n % 5 == 0:
            total_sum += n
    return total_sum

if __name__ == "__main__":
    target = 10
    result = fizz_buzz_sum(target)
    print(f"The sum of all numbers up to {target} that are divisible by 3 or 5 is: {result}")
```

## Explanation
1. **Iterate Through Numbers**: The function iterates through every number below the target.
2. **Check Divisibility**: For each number, it checks if it is divisible by 3 or 5.
3. **Sum the Multiples**: If a number is divisible by 3 or 5, it adds it to a running total.

> **Note**: The runtime complexity of this algorithm is O(n) because it iterates through every number below the target.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the target value. The function checks each number below the target.
- **Space Complexity**: O(1), as no additional space is used that scales with input size.

## Key Concepts
- Iteration and condition checking
- Summation of multiples
- Efficient algorithm design

## Additional Notes
- This problem is often posed in coding interviews to assess problem-solving skills.
- An interesting follow-up question is whether you can find a solution that runs in constant time without iterating through every number below the target.

## Difficulty
Easy

## Related Topics
- Mathematical functions
- Combinatorial problems
- Interview preparation

## Source
[DataLemur](https://datalemur.com/questions/python-fizz-buzz-sum)
