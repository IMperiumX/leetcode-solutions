# 78. Subsets - Bit Manipulation Approach

def subsets(nums):
    """
    Generates all possible subsets of a given set of numbers using bit manipulation.

    Args:
      nums: A list of unique integers.

    Returns:
      A list of lists, where each inner list represents a subset.
    """
    n = len(nums)
    result = []

    for i in range(2**n):  # Iterate through all possible combinations (2^n)
        subset = []
        for j in range(n):
            if (i >> j) & 1:  # Check if the j-th bit is set in i
                subset.append(nums[j])  # If set, include the j-th number in the subset
        result.append(subset)

    return result
