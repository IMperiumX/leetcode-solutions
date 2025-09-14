# 0209. Minimum Size Subarray Sum
# Approach: Prefix Sum + Binary Search (O(n log n) Time, O(n) Space)

import bisect
import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray whose sum is >= target.
        This solution first computes a prefix sum array. Then, for each starting
        point 'i', it uses binary search to find the smallest endpoint 'j' such that
        the sum from i to j is >= target.

        - prefix_sums[j] - prefix_sums[i] represents the sum of nums[i...j-1].
        - We search for a prefix_sums[j] >= prefix_sums[i] + target.

        Time Complexity: O(n log n) due to iterating through the array (O(n)) and performing a binary search (O(log n)) for each element.
        Space Complexity: O(n) to store the prefix sums.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Create prefix sum array. prefix_sums[i] = sum(nums[0...i-1])
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        min_length = math.inf

        # For each possible start of a subarray (represented by prefix_sums[i])
        for i in range(n + 1):
            # We need to find the smallest j > i such that:
            # prefix_sums[j] - prefix_sums[i] >= target
            # which means prefix_sums[j] >= prefix_sums[i] + target

            # The value we are looking for in the rest of the prefix_sums array
            target_sum = prefix_sums[i] + target

            # Use binary search (bisect_left) to find the insertion point for target_sum
            # in the subarray prefix_sums[i+1:]. This is the first index 'j' where
            # the condition is met.
            # The `lo=i+1` argument ensures we only search in the valid range for endpoints.
            j = bisect.bisect_left(prefix_sums, target_sum, lo=i + 1)

            # If a valid index 'j' is found within the bounds of the array
            if j != len(prefix_sums):
                min_length = min(min_length, j - i)

        return min_length if min_length != math.inf else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(4, [1, 4, 4]))
    print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
