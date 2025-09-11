# 704. Binary Search, Difficulty: Easy

**Link:** [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)

## Problem Description

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

```python
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

Example 2:

```python
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

Constraints:

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

## Solution Approach (Binary Search)

The [`solution.py`](./solution.py) file contains a Python solution using the classic binary search algorithm. Since the array is sorted, we can efficiently search by repeatedly dividing the search space in half.

1. Initialize left and right pointers to the start and end of the array.
2. While left <= right:
   - Calculate the middle index: mid = left + (right - left) // 2
   - If nums[mid] equals target, return mid
   - If nums[mid] < target, search the right half: left = mid + 1
   - If nums[mid] > target, search the left half: right = mid - 1
3. If target is not found, return -1.

**Time Complexity:** O(log n) where n is the length of the array
**Space Complexity:** O(1) - constant space

Key points:
- Use `left + (right - left) // 2` to avoid integer overflow
- The search space shrinks by half with each iteration
- This is the most efficient approach for sorted arrays