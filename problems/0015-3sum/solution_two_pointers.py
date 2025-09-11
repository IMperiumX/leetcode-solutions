# 15. 3Sum - Two Pointers Approach
"""
1. sort to make the two pointer more efficient
2. low is set to i + 1, hi is set to the end of the array
3. while low is less than hi, we check the sum of the three numbers
4. if the sum is less than 0, we increment low
5. if the sum is greater than 0, we decrement hi
6. if the sum is equal to 0, we add the triplet to the result
7. we increment low and decrement hi
8. we skip any duplicate elements at low and hi to avoid duplicate triplets
"""


def threeSum(nums):
    res = []
    nums.sort()  # 1
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSumII(nums, i, res)
    return res


def twoSumII(nums, i, res):
    lo, hi = i + 1, len(nums) - 1  # 2
    while lo < hi:  # 3
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:  # 4
            lo += 1
        elif sum > 0:  # 5
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])  # 6
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:  # 8
                lo += 1
