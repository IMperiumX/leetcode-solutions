# Prefix and Suffix Products Approach

"""
Prefix Products: In the first pass, it calculates the product of all elements
before the current index. result[i] stores the product of nums[0] to nums[i-1].

Suffix Products: In the second pass, it iterates backward and calculates the
product of all elements after the current index. It multiplies this suffix product
with the already calculated prefix product in result[i].

The final result[i] holds the product of all elements in nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Calculates the product of all elements of the array except for the element at each index.

        This approach uses prefix and suffix products to achieve the desired result in O(n) time.
        """
        n = len(nums)
        result = [1] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result
