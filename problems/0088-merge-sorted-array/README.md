# 88. Merge Sorted Array, Difficulty: Easy

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

**Example 1:**

```

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

```

**Example 2:**

```

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

```

**Example 3:**

```

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].

```

## Approach(es)

The key to solving this in-place with O(1) extra space is to merge from the *end* of the `nums1` array. This avoids overwriting elements that we still need to compare.

### Two Pointers (Merge from End)

**Algorithm:**

1. **Initialize Pointers:**
    - `p1`: Points to the last valid element of `nums1` (`m - 1`).
    - `p2`: Points to the last element of `nums2` (`n - 1`).
    - `p_merge`: Points to the last available position in `nums1` (`m + n - 1`).
2. **Merge:**
    - While `p2` is not out of bounds (i.e., `p2 >= 0`):
        - Compare the elements at `nums1[p1]` and `nums2[p2]`.
        - If `p1` is in bounds and `nums1[p1]` is greater than `nums2[p2]`:
            - Place the element from `nums1` at `nums1[p_merge]`.
            - Decrement `p1`.
        - Otherwise (if `nums2[p2]` is greater or equal, or if `p1` is out of bounds):
            - Place the element from `nums2` at `nums1[p_merge]`.
            - Decrement `p2`.
        - Decrement `p_merge`.
3. **Completion:** The loop continues until all elements from `nums2` have been merged. If any elements from `nums1` remain at the beginning of the array, they are already in their correct sorted position.

**Data Structures:**

- Arrays
- Pointers (integer indices)

**Time Complexity:**

- O(m + n), as we iterate through both arrays once.

**Space Complexity:**

- O(1), as we are modifying the array in-place and using only a few extra variables for pointers.

**Trade-offs:**

- Highly efficient in terms of both time and space.
- The key insight is to merge from the end to avoid overwriting elements that need to be considered later.

## Code

[Two Pointers Solution](./solution.py)

## Notes

- This is a classic two-pointer problem.
- The "merge from end" technique is a clever way to solve the in-place requirement without needing extra space.
- It's important to handle the edge case where one of the pointers goes out of bounds (e.g., when `p1` becomes negative, we should always take elements from `nums2`).
- A simpler but less efficient solution would be to copy `nums2` to the end of `nums1` and then sort the entire `nums1` array. This would have a time complexity of O((m+n)log(m+n)).
