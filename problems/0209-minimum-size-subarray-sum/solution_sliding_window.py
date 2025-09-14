# 0209. Minimum Size Subarray Sum
# Approach: Sliding Window (O(n) Time, O(1) Space)

import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray whose sum is >= target.
        This solution uses a sliding window approach with two pointers, 'left' and 'right'.

        - 'right' pointer expands the window by including new elements.
        - 'left' pointer shrinks the window from the left when the sum condition is met.

        Time Complexity: O(n) because each element is visited at most twice (by left and right pointers).
        Space Complexity: O(1) as we only use a few variables to store the state.
        """

        # Initialize pointers and state variables
        left = 0
        current_sum = 0
        min_length = math.inf

        # Iterate through the array with the 'right' pointer to expand the window
        for right in range(len(nums)):
            current_sum += nums[right]

            # Once the current window sum is >= target, try to shrink the window
            # from the left to find the smallest possible window.
            while current_sum >= target:
                # Update the minimum length found so far
                min_length = min(min_length, right - left + 1)

                # Shrink the window by moving the 'left' pointer forward
                current_sum -= nums[left]
                left += 1

        # If min_length was never updated, it means no valid subarray was found.
        # Otherwise, return the minimal length found.
        return min_length if min_length != math.inf else 0
