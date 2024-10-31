# Palindrome Checker

## Problem Statement
Write a function to determine if a given phrase is a palindrome. A palindrome is a string that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. For example, "A man, a plan, a canal, Panama!" is a palindrome.

## Example
- **Input**: 
  - `phrase = "A man, a plan, a canal, Panama!"`
- **Output**: 
  - `True` (because the phrase is a palindrome)

## Function Definition
```py
def isPalindrome(phrase):

  # Clean the input string
  cleaned_string = ''.join(char for char in phrase if char.isalnum()).lower()
    
  left = 0
  right = len(cleaned_string) - 1
    
  while left < right:  # Compare until the two pointers meet
      if cleaned_string[left] != cleaned_string[right]:
          return False  # Mismatch found, not a palindrome
      left += 1
      right -= 1
    
  return True  # No mismatches found, it is a palindrome
```

## Explanation
1. **Cleaning the Input**: The function first cleans the input string by removing non-alphanumeric characters and converting it to lowercase.
2. **Two-Pointer Technique**: It uses two pointers, `left` and `right`, to compare characters from the beginning and end of the cleaned string.
3. **Checking for Mismatches**: If any characters do not match, the function returns `False`. If all characters match, it returns `True`.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the cleaned string. The function iterates through the string once.
- **Space Complexity**: O(n) for storing the cleaned string.

## Key Concepts
- String manipulation
- Two-pointer technique
- Palindrome checking

## Additional Notes
- This function effectively handles phrases with spaces and punctuation.
- Ensure that the input is a string to avoid unexpected behavior.

## Difficulty
Easy

## Related Topics
- String algorithms
- Data structures
- Interview preparation

## Source
[DataLemur](https://datalemur.com/questions/python-palindrome)
