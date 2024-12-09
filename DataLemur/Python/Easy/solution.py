import math

def is_prime(n):
    # Handle edge cases for numbers less than or equal to 1
    if n <= 1:
        return False
    # Handle small primes directly
    if n <= 3:
        return True
    # Exclude even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Only check divisibility for numbers of the form 6k ± 1 up to the square root of n
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def test_prime():
    prime_count = 0
    prime_list = []
    nums = [326, 303, 313, 351]
    for i in nums:
        if is_prime(i):
            prime_count += 1
            prime_list.append(i)
    return prime_count, prime_list

# Example usage
if __name__ == "__main__":
    print(test_prime())
