# 1422. Maximum Score After Splitting a String - One-Pass Approach


def maxScore(s):
    """
    Calculates the maximum score after splitting a string into two non-empty substrings.

    Args:
        s: The string consisting of '0' and '1'.

    Returns:
        The maximum score.
    """
    zeros = 0
    ones = 0
    max_score = float("-inf")

    for i in range(len(s) - 1):
        if s[i] == "0":
            zeros += 1
        else:
            ones -= 1

        max_score = max(max_score, zeros + ones)

    if s[-1] == "1":
        ones += 1
    max_score += ones

    return max_score
