def palindrome_number(x: int) -> bool:
    """
    Check if a given integer is a palindrome.

    A palindrome is a number that reads the same backward as forward.

    Args:
        x (int): The integer to check.

    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """
    # Convert the integer to a string
    s = str(x)
    
    # Use two pointers to check if the string is a palindrome
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example usage
result = palindrome_number(-121) 
print(result)