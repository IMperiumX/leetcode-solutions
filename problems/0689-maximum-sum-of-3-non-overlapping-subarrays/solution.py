# Dynamic Programming Approach, Difficulty: Hard
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        sums = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        sums[0] = curr_sum
        for i in range(1, n - k + 1):
            curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
            sums[i] = curr_sum

        left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        ans = []
        max_sum = 0
        for j in range(k, len(sums) - k):
            i, l = left[j - k], right[j + k]
            total = sums[i] + sums[j] + sums[l]
            if not ans or total > max_sum:
                max_sum = total
                ans = [i, j, l]
        return ans
