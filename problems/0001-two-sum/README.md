
# 1. Two Sum, Difficulty: Easy

**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
```

```python
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
```

```python
Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:

`2 <= nums.length <= 104`
`-109 <= nums[i] <= 109`
`-109 <= target <= 109`
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Hint 1
> A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.

Hint 2
> So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?

Hint 3
> The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

## Solution Approach (Prefix and Suffix Products)

The [`solution.py`](./solution.py) file contains a Python solution using hash table (unordered_map in C++). We can iterate through the array once, and for each element, check if the target minus the current element exists in the hash table. If it does, we have found a valid pair of numbers. If not, we add the current element to the hash table.

1. Create an empty hash table to store elements and their indices.
2. Iterate through the array from left to right.
3. For each element nums[i], calculate the complement by subtracting it from the target: complement = target - nums[i].
4. Check if the complement exists in the hash table. If it does, we have found a solution.
5. If the complement does not exist in the hash table, add the current element nums[i] to the hash table with its index as the value.
6. Repeat steps 3-5 until we find a solution or reach the end of the array.
7. If no solution is found, return an empty array or an appropriate indicator.

This approach has a time complexity of O(n) since hash table lookups take constant time on average. It allows us to solve the Two Sum problem efficiently by making just one pass through the array.
