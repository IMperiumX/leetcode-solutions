# 1422. Maximum Score After Splitting a String - Prefix Sum Approach


def maxScore(s):
    """
    Calculates the maximum score after splitting a string into two non-empty substrings
    using prefix sums.

    Args:
        s: The string consisting of '0' and '1'.

    Returns:
        The maximum score.
    """

    n = len(s)

    # Calculate total number of ones in the string
    total_ones = s.count("1")

    max_score = 0
    left_zeros = 0

    for i in range(n - 1):
        if s[i] == "0":
            left_zeros += 1

        # Calculate ones in the right substring
        right_ones = total_ones - (i + 1 - left_zeros)

        max_score = max(max_score, left_zeros + right_ones)

    return max_score
