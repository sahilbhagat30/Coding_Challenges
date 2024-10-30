# Factorial Function

## Problem Statement
You are tasked with implementing a function to calculate the factorial of a non-negative integer \( n \). The factorial of \( n \) (denoted as \( n! \)) is the product of all positive integers less than or equal to \( n \). The factorial of 0 is defined to be 1.

## Function Definition
```py
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        factorial = n
        while n > 1:
            factorial *= (n - 1)
            n -= 1
        return factorial
```
## Test Function
```py
def test_factorial():
    test_cases = [
        (0, 1),  # 0! = 1
        (1, 1),  # 1! = 1
        (2, 2),  # 2! = 2
        (3, 6),  # 3! = 6
        (4, 24), # 4! = 24
        (5, 120),# 5! = 120
        (6, 720) # 6! = 720
    ]
    
    for n, expected in test_cases:
        result = factorial(n)
        assert result == expected, f"Test failed for n={n}: expected {expected}, got {result}"
    
    print("All tests passed!")

# Example usage
if __name__ == "__main__":
    test_factorial()
```
## Explanation
1. **Factorial Calculation**: The function calculates the factorial of a given non-negative integer \( n \) using an iterative approach.
2. **Test Cases**: The test function defines a list of test cases, where each case is a tuple containing an input number and the expected factorial result.
3. **Assertions**: The function iterates through each test case, calling the factorial function and checking if the result matches the expected value. If it doesn't, it raises an assertion error with a message.
4. **Success Message**: If all tests pass, it prints "All tests passed!"

## Complexity Analysis
- **Time Complexity**: O(n), where \( n \) is the input number. The function iterates through all integers from \( n \) down to 1.
- **Space Complexity**: O(1), as no additional space is used that scales with input size.

## Key Concepts
- Iterative approach for calculating factorial
- Test-driven development with assertions
- Handling of edge cases (e.g., factorial of 0)

## Additional Notes
- This solution efficiently handles non-negative integers.
- Ensure that the input is a non-negative integer to avoid unexpected behavior.

## Difficulty
Easy

## Related Topics
- Recursion vs. Iteration
- Combinatorial problems
- Mathematical functions

## Source
[DataLemur](https://datalemur.com/questions/python-factorial-formula)
