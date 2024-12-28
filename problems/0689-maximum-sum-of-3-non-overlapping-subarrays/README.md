# 689. Maximum Sum of 3 Non-Overlapping Subarrays, Difficulty: Hard

## Problem Description

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

**Example 1:**

**Input:** nums = [1,2,1,2,6,7,5,1], k = 2
**Output:** [0,3,5]
**Explanation:** Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

**Example 2:**

**Input:** nums = [1,2,1,2,1,2,1,2,1], k = 2
**Output:** [0,2,4]

**Constraints:**

- 1 <= nums.length <= 2 * 104
- 1 <= nums[i] < 216
- 1 <= k <= floor(nums.length / 3)

## Approach

We can use dynamic programming to solve this problem efficiently.

1. **Calculate Subarray Sums:** We first calculate the sum of all possible subarrays of length `k` and store them in a `sums` array.
2. **Left Maximums:** We create a `left` array where `left[i]` stores the index of the maximum sum subarray to the left of `i` (including `i`).
3. **Right Maximums:** We create a `right` array where `right[i]` stores the index of the maximum sum subarray to the right of `i` (including `i`). When two sums are the same, we pick the lexicographically smaller one.
4. **Iterate and Find Maximum:** We iterate through all possible middle subarrays (starting from index `k` to `n - 2k`) and find the corresponding left and right maximum subarrays using the `left` and `right` arrays. We then calculate the total sum of these three subarrays.
5. **Update Result:** We keep track of the maximum sum found so far and update the result array with the indices of the three subarrays that give the maximum sum.

**Time Complexity:** O(n), where n is the length of the input array. We iterate through the array a few times to calculate sums, left maximums, right maximums, and the final result.

**Space Complexity:** O(n), as we use arrays of size n to store subarray sums, left maximums, and right maximums.

## from the [soultion section](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solutions/127574/maximum-sum-of-3-non-overlapping-subarrays/) LC

Approach #1: Ad-Hoc [Accepted]
Intuition

It is natural to consider an array W of each interval's sum,
where each interval is the given length k.
To create W, we can either use prefix sums, or manage the sum of the interval
as a window slides along the array.

From there, we approach the reduced problem: Given some array W and an integer k,
what is the lexicographically smallest tuple of indices (i, j, l) with i + k <= j and
j + k <= l that maximizes W[i] + W[j] + W[l]?

Algorithm

Suppose we fixed j.
We would like to know on the intervals i∈[0,j−k] and
l∈[j+k,len(W)−1],
where the largest value of W[i] (and respectively W[l]) occurs first.
(Here, first means the smaller index.)

We can solve these problems with dynamic programming.
For example, if we know that i is where the largest value of
W[i] occurs first on [0,5], then on [0,6] the first occurrence of the
largest W[i] must be either i or 6.
If say, 6 is better, then we set best = 6.

At the end, left[z] will be the first occurrence of the largest value of W[i]
on the interval i∈[0,z], and right[z] will be the same but on the interval
i∈[z,len(W)−1]. This means that for some choice j,
the candidate answer must be (left[j - k], j, right[j + k]).
We take the candidate that produces the maximum W[i] + W[j] + W[l].

## Code

### Python - Dynamic Programming

[solution](./solution.py)

Notes (Optional)
This problem can also be approached using other techniques, but the dynamic programming approach provides an efficient solution with linear time complexity. It's important to pay attention to the lexicographical order requirement when multiple solutions with the same maximum sum exist.
