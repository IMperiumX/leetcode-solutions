def count_palindromic_subsequence(s: str) -> int:
    """
    Counts the number of unique length-3 palindromic subsequences in a string.

    Args:
        s: The input string.

    Returns:
        The number of unique length-3 palindromic subsequences.
    """
    result = 0
    unique_chars = set(s)

    for char in unique_chars:
        first_occurrence = s.find(char)
        last_occurrence = s.rfind(char)

        if (
            first_occurrence != -1
            and last_occurrence != -1
            and first_occurrence < last_occurrence
        ):
            middle_chars = set(s[first_occurrence + 1 : last_occurrence])
            result += len(middle_chars)

    return result

count_palindromic_subsequence("aabca")  # Expected output: 3
