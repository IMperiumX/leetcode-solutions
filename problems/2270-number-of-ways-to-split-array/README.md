
# 2270. Number of Ways to Split Array, Difficulty: Medium

## Problem Description

You are given a 0-indexed integer array `nums` of length `n`.

`nums` contains a valid split at index `i` if the following are true:

* The sum of the first `i + 1` elements is greater than or equal to the sum of the last `n - i - 1` elements.
* There is at least one element to the right of `i`. That is, `0 <= i < n - 1`.

Return the number of valid splits in `nums`.

**Example 1:**

**Input:** `nums = [10,4,-8,7]`

**Output:** `2`

**Explanation:**

There are three ways of splitting `nums` into two non-empty parts:

* Split `nums` at index 0. Then, the first part is `[10]`, and its sum is 10. The second part is `[4,-8,7]`, and its sum is 3. Since `10 >= 3`, `i = 0` is a valid split.
* Split `nums` at index 1. Then, the first part is `[10,4]`, and its sum is 14. The second part is `[-8,7]`, and its sum is -1. Since `14 >= -1`, `i = 1` is a valid split.
* Split `nums` at index 2. Then, the first part is `[10,4,-8]`, and its sum is 6. The second part is `[7]`, and its sum is 7. Since `6 < 7`, `i = 2` is not a valid split.

Thus, the number of valid splits in `nums` is 2.

**Example 2:**

**Input:** `nums = [2,3,1,0]`

**Output:** `2`

**Explanation:**

There are two valid splits in `nums`:

* Split `nums` at index 1. Then, the first part is `[2,3]`, and its sum is 5. The second part is `[1,0]`, and its sum is 1. Since `5 >= 1`, `i = 1` is a valid split.
* Split `nums` at index 2. Then, the first part is `[2,3,1]`, and its sum is 6. The second part is `[0]`, and its sum is 0. Since `6 >= 0`, `i = 2` is a valid split.

**Constraints:**

* `2 <= nums.length <= 10^5`
* `-10^5 <= nums[i] <= 10^5`

## Approach

### Prefix Sum

#### Algorithm

1. Calculate the total sum of the array `nums`.
2. Initialize `left_sum` to 0. This will store the sum of the left part of the array.
3. Iterate through the array from left to right (excluding the last element since we need at least one element on the right).
    * Add the current element to `left_sum`.
    * Calculate `right_sum` as `total_sum - left_sum`.
    * If `left_sum >= right_sum`, increment a `count` (the number of valid splits).
4. Return the `count`.

#### Data Structures

* No extra data structures are needed beyond a few variables to store sums and the count.

#### Time Complexity

* O(n), where n is the length of the array. We iterate through the array once.

#### Space Complexity

* O(1) - We use only a constant amount of extra space.

#### Trade-offs

* **Pros:** Simple, efficient, and easy to understand.
* **Cons:** None in this case. The prefix sum approach is optimal for this problem.

## Code

* [Prefix Sum Approach](./solution.py)

## Notes

* This problem demonstrates a straightforward application of the prefix sum concept, although we don't explicitly create a separate prefix sum array. We calculate the prefix sums on the fly.
* The key insight is to realize that we can calculate the right sum efficiently by subtracting the left sum from the total sum, avoiding the need to iterate through the right part of the array repeatedly.
