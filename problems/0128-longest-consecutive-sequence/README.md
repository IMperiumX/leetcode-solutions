# 128. Longest Consecutive Sequence, Difficulty: Medium

**Link:** [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example 1:**

**Input:** nums = \[100,4,200,1,3,2]
**Output:** 4
**Explanation:** The longest consecutive elements sequence is \[1, 2, 3, 4]. Therefore its length is 4.

**Example 2:**

**Input:** nums = \[0,3,7,2,5,8,4,6,0,1]
**Output:** 9

**Constraints:**

* 0 <= nums.length <= 10^5
* -10^9 <= nums\[i] <= 10^9

## Solution Approach (Hash Set)

The `solution.py` file contains a Python solution that uses a hash set to achieve the desired O(n) time complexity.

1. **Create a Set:** Convert the input array `nums` into a set `num_set`. This allows for O(1) average time complexity for checking if an element exists.

2. **Iterate and Find Start of Sequences:** Iterate through each number `num` in the `num_set`. For each number, check if it's the start of a consecutive sequence by verifying if `num - 1` is **not** present in the `num_set`.

3. **Extend Sequence:** If `num` is the start of a sequence:
    * Initialize `current_num` to `num` and `current_streak` to 1.
    * Use a `while` loop to extend the sequence as long as `current_num + 1` exists in the `num_set`.
    * Increment `current_num` and `current_streak` in each iteration of the `while` loop.

4. **Update Longest Streak:** After the `while` loop finishes, update `longest_streak` with the maximum value between `longest_streak` and `current_streak`.

5. **Return:** Return the `longest_streak`, which represents the length of the longest consecutive sequence found.
