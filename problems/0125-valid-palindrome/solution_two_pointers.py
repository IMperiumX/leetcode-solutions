
def isPalindrome(s):
    """
    Checks if a given string is a palindrome using the two-pointer approach.

    Args:
      s: The string to check.

    Returns:
      True if the string is a palindrome, False otherwise.
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
