class Solution:
    def twoSum(self, nums, target):
        mapping = {}

        for idx, num in enumerate(nums):
            guess = target - num
            if guess in mapping:
                return [mapping[guess], idx]
            mapping[num] = idx
