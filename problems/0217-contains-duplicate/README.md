# 217. Contains Duplicate, Difficulty: Easy

**Link:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

## Problem Description

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

```python
Input: nums = [1,2,3,1]
Output: true
```

Example 2:

```python
Input: nums = [1,2,3,4]
Output: false
```

Example 3:

```python
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution Approach (Hash Set)

The [`solution.py`](./solution.py) file contains a Python solution using a hash set. We can iterate through the array and check if each element has been seen before by storing elements in a set.

1. Create an empty set to store seen elements.
2. Iterate through the array.
3. For each element, check if it exists in the set.
4. If it exists, return true (duplicate found).
5. If it doesn't exist, add it to the set.
6. If we finish iterating without finding duplicates, return false.

**Time Complexity:** O(n) where n is the length of the array
**Space Complexity:** O(n) for the hash set in worst case

Alternative approaches:
- **Sorting:** Sort the array and check adjacent elements - O(n log n) time, O(1) space
- **Brute Force:** Compare each element with every other element - O(n²) time, O(1) space