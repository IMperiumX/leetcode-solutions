# 300. Longest Increasing Subsequence - Patience Sorting with Binary Search (O(n log n))
import bisect


def lengthOfLIS(nums):
    """
    Finds the length of the longest increasing subsequence using patience sorting and binary search.

    Args:
        nums: The input list of numbers.

    Returns:
        The length of the longest increasing subsequence.
    """
    if not nums:
        return 0

    tails = []  # tails[i] is the smallest tail of all increasing subsequences of length i+1.

    for num in nums:
        # If we find a number in `tails` that is greater than or equal to the current number (using binary search)
        # we replace that number with the current number. This maintains the property that `tails` is always sorted.
        # bisect_left returns the insertion point to maintain sorted order.
        i = bisect.bisect_left(tails, num)

        if i == len(tails):
            # If the current number is greater than all numbers in `tails`, it extends the longest increasing subsequence.
            tails.append(num)
        else:
            # Otherwise, replace the element at the insertion point.
            tails[i] = num
    return len(tails)
