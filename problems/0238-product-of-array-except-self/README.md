# 238. Product of Array Except Self, Difficulty: Medium

**Link:** [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)

## Problem Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

**Input:** nums = \[1,2,3,4]
**Output:** \[24,12,8,6]

**Example 2:**

**Input:** nums = \[-1,1,0,-3,3]
**Output:** \[0,0,9,0,0]

**Constraints:**

* `2 <= nums.length <= 105`
* `-30 <= nums[i] <= 30`
* The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## Solution Approach (Prefix and Suffix Products)

The [`solution.py`](./solution.py) file contains a Python solution that utilizes the concept of prefix and suffix products to achieve the desired result in `O(n)` time and without using division.

1. **Initialization:**
    * Create a result array `res` of the same size as the input array `nums`, initialized with all elements set to 1.

2. **Prefix Products:**
    * Iterate through the `nums` array from left to right.
    * Maintain a `prefix` variable to store the product of all elements encountered so far.
    * For each element at index `i`, set `res[i]` to the current `prefix` value.
    * Update `prefix` by multiplying it with the current element `nums[i]`.

3. **Suffix Products:**
    * Iterate through the `nums` array from right to left.
    * Maintain a `postfix` variable to store the product of all elements encountered so far (from the right).
    * For each element at index `i`, multiply `res[i]` by the current `postfix` value. This effectively incorporates the product of elements to the right of `i`.
    * Update `postfix` by multiplying it with the current element `nums[i]`.

4. **Return:**
    * Return the `res` array, which now contains the product of all elements except the element at each index.
