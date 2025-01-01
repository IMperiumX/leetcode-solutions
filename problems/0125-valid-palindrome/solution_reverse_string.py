def isPalindrome(s):
    """
    Checks if a given string is a palindrome using string reversal.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    processed_s = ''.join(ch for ch in s.lower() if ch.isalnum())
    return processed_s == processed_s[::-1]
