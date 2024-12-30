# 2466. Count Ways To Build Good Strings - Dynamic Programming


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Counts the number of good strings that can be constructed within the given length range.

        Args:
          low: The minimum length of a good string.
          high: The maximum length of a good string.
          zero: The number of '0' characters to append in one step.
          one: The number of '1' characters to append in one step.

        Returns:
          The number of good strings modulo 10^9 + 7.
        """
        dp = [0] * (high + 1)  # dp[i] stores the number of good strings of length i
        dp[0] = 1  # Base case: 1 way to form an empty string
        mod = 10**9 + 7

        for i in range(1, high + 1):
            # If we can append '0's to reach length i
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            # If we can append '1's to reach length i
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % mod

        # Sum up the number of good strings within the range [low, high]
        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % mod

        return ans
