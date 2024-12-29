# 53. Maximum Subarray - Kadane's Algorithm


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

        Args:
          nums: The input array of numbers.

        Returns:
          The maximum sum of a contiguous subarray.
        """
        max_current = nums[0]  # Initialize current maximum to the first element
        max_global = nums[0]  # Initialize global maximum to the first element

        for i in range(1, len(nums)):
            # Decide whether to extend the current subarray or start a new one
            max_current = max(nums[i], max_current + nums[i])
            # Update the global maximum
            max_global = max(max_global, max_current)

        return max_global
