
class Solution:
    # 53. Maximum Subarray - Divide and Conquer Approach
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray using the divide and conquer approach.

        Args:
          nums: The input array of numbers.

        Returns:
          The maximum sum of a contiguous subarray.
        """

        def maxCrossingSubArray(arr, low, mid, high):
            """
            Finds the maximum sum of a subarray that crosses the midpoint.
            """
            # Find maximum subarray sum on the left side of mid
            left_sum = float("-inf")
            curr_sum = 0
            for i in range(mid, low - 1, -1):
                curr_sum += arr[i]
                left_sum = max(left_sum, curr_sum)

            # Find maximum subarray sum on the right side of mid
            right_sum = float("-inf")
            curr_sum = 0
            for i in range(mid + 1, high + 1):
                curr_sum += arr[i]
                right_sum = max(right_sum, curr_sum)

            return left_sum + right_sum

        def maxSubArrayRecursive(arr, low, high):
            """
            Recursive function to find the maximum subarray sum.
            """
            if low == high:
                return arr[low]  # Base case: single element

            mid = (low + high) // 2

            # Find maximum subarray sum in the left and right halves
            left_sum = maxSubArrayRecursive(arr, low, mid)
            right_sum = maxSubArrayRecursive(arr, mid + 1, high)

            # Find maximum subarray sum that crosses the midpoint
            cross_sum = maxCrossingSubArray(arr, low, mid, high)

            # Return the maximum of the three
            return max(left_sum, right_sum, cross_sum)

        return maxSubArrayRecursive(nums, 0, len(nums) - 1)
