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