# 53. Maximum Subarray, Medium

## Notes

The Maximum Subarray problem is a classic example where dynamic programming (specifically, Kadane's Algorithm) provides an optimal solution.

Understanding both Kadane's Algorithm and the divide and conquer approach is beneficial for developing a strong algorithmic foundation.

Kadane's Algorithm is often preferred for its efficiency, while the divide and conquer approach showcases a different problem-solving paradigm.

## Problem Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

**Input:** nums = \[-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** \[4,-1,2,1] has the largest sum = 6.

**Example 2:**

**Input:** nums = \[1]
**Output:** 1

**Example 3:**

**Input:** nums = \[5,4,-1,7,8]
**Output:** 23

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`

**Follow up:** If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Approach(es)

### Kadane's Algorithm

* **Algorithm:**
  * Initialize two variables: `current_max` and `global_max`, both initially set to the first element of the array.
  * Iterate through the array, starting from the second element.
  * For each element, update `current_max` to be the maximum of either the current element itself or the sum of the current element and the previous `current_max`. This step determines whether to start a new subarray or extend the existing one.
  * Update `global_max` to be the maximum of `global_max` and `current_max`.
  * Return `global_max`.
* **Data Structures:**
  * No extra data structures are needed beyond the two variables `current_max` and `global_max`.
* **Time Complexity:**
  * O(n), where n is the length of the array. We iterate through the array once.
* **Space Complexity:**
  * O(1), as we only use constant extra space.
* **Trade-offs:**
  * Kadane's Algorithm is very efficient in both time and space. It's the optimal solution for this problem in terms of time complexity.

### Divide and Conquer Approach

* **Algorithm:**
    1. **Divide:** Divide the array into two halves.
    2. **Conquer:** Recursively find the maximum subarray sum in the left and right halves.
    3. **Combine:** Find the maximum subarray sum that crosses the midpoint. This involves finding the maximum sum starting from the midpoint and extending to the left, and the maximum sum starting from the midpoint + 1 and extending to the right. The maximum crossing subarray sum is the sum of these two maximums.
    4. **Return:** Return the maximum of the three sums found in steps 2 and 3 (left half, right half, and crossing).
* **Data Structures:**
  * No extra data structures are needed beyond the recursive call stack.
* **Time Complexity:**
  * O(n log n). The recursive calls create a binary tree structure where each level takes O(n) time to process (finding the crossing subarray), and there are log n levels.
* **Space Complexity:**
  * O(log n) due to the recursive call stack.
* **Trade-offs:**
  * The divide and conquer approach is less efficient than Kadane's Algorithm in terms of time complexity. However, it demonstrates a different algorithmic technique that can be useful for other problems. It is also a good exercise in understanding recursion and how to combine solutions from subproblems.

## Code

### Python - Kadane's Algorithm and Divide and Conquer Approach

[kadane algorithm](./solution.py)
[dive and conquer](./divide_and_conquer.py)

see other 5 solutions [post](https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/)
