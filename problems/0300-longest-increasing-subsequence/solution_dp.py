# 300. Longest Increasing Subsequence - Dynamic Programming (O(n^2))

# YT: https://www.youtube.com/watch?v=CE2b_-XfVDk


def lengthOfLIS_dp(nums):
    """
    Finds the length of the longest increasing subsequence using dynamic programming.

    Args:
        nums: The input list of numbers.

    Returns:
        The length of the longest increasing subsequence.
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] stores the length of the LIS ending at index i.

    for i in range(1, n):
        for j in range(i):
            num_i, num_j = nums[i], nums[j]
            if num_i > num_j:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"LIS is: {lengthOfLIS_dp(nums)}")
