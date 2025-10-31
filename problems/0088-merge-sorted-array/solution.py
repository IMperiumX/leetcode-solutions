"""
88. Merge Sorted Array - Two Pointers (Merge from End) Solution
"""

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merges nums2 into nums1 in-place.
    Do not return anything, modify nums1 in-place instead.

    Args:
      nums1: The first sorted array with space at the end.
      m: The number of elements in nums1.
      nums2: The second sorted array.
      n: The number of elements in nums2.
    """
    # Pointers for the last element of nums1, nums2, and the merged array
    p1 = m - 1
    p2 = n - 1
    p_merge = m + n - 1

    # Merge from the end
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p_merge] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merge] = nums2[p2]
            p2 -= 1
        p_merge -= 1
