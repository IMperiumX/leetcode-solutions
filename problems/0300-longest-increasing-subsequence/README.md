# 300. Longest Increasing Subsequence, Difficulty: Medium

## Problem Description

Given an integer array nums, return the length of the longest strictly increasing subsequence.

> A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

Example 2:

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

Example 3:

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

Constraints:

- 1 <= nums.length <= 2500
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

## Approach(es)

### Dynamic Programming (O(n^2))

Algorithm:

1. **Initialization:** Create a `dp` array of the same length as `nums`, initialized with all elements set to 1.  `dp[i]` represents the length of the longest increasing subsequence *ending* at index `i`.  Since a single element itself forms an increasing subsequence of length 1, we initialize all `dp[i]` to 1.
2. **Iteration:** Iterate through the `nums` array from left to right (outer loop with index `i`).
    - For each element `nums[i]`, iterate through all *previous* elements (inner loop with index `j` from 0 to `i-1`).
    - If `nums[i] > nums[j]` (meaning we can extend a previous increasing subsequence), update `dp[i]` to be the maximum of its current value and `dp[j] + 1`.  This step is crucial: we're checking if adding `nums[i]` to the subsequence ending at `nums[j]` creates a longer increasing subsequence.
3. **Result:** After iterating through all elements, the maximum value in the `dp` array is the length of the longest increasing subsequence in the entire `nums` array.

Data Structures:

- `dp` array (list) of length n.

Time Complexity:

- O(n^2) - Due to the nested loops.

Space Complexity:

- O(n) - For the `dp` array.

Trade-offs:

- This approach is relatively easy to understand and implement.
- The O(n^2) time complexity is not optimal for large input sizes.

### Patience Sorting with Binary Search (O(n log n))

Algorithm:

This approach is based on the idea of "patience sorting." Imagine dealing cards one by one.  We maintain several piles of cards, where each pile is sorted in increasing order from top to bottom.  When we deal a new card:

1. If the card is greater than the top card of all existing piles, we start a new pile to the right.
2. Otherwise, we find the *leftmost* pile where the top card is greater than or equal to the current card, and we place the current card on top of that pile (replacing the previous top card).

The number of piles at the end represents the length of the longest increasing subsequence.

To implement this efficiently, we don't need to store the entire piles. We only need to store the top card of each pile.  We use a list called `tails` where `tails[i]` is the smallest tail of all increasing subsequences of length `i+1`.

1. **Initialization:** Create an empty list called `tails`.
2. **Iteration**: Iterate through each number `num` in `nums`.
   - **Binary Search:** Use `bisect_left(tails, num)` to find the index `i` where `num` should be inserted into `tails` to maintain its sorted order.
     - If `i == len(tails)`, this means `num` is greater than all elements in `tails`, so we append `num` to `tails` (extending the longest increasing subsequence).
     - Otherwise, we replace `tails[i]` with `num`. This is because `num` is smaller than the previous tail of a subsequence of the same length.
3. **Result:** Return the length of tails, which is the length of the LIS.

Data Structures:

- `tails` list.

Time Complexity:

- O(n log n) -  The outer loop iterates n times.  Inside the loop, `bisect_left` takes O(log n) time.

Space Complexity:

- O(n) - In the worst case, the `tails` list can have a size of n (e.g., if the input array is strictly increasing).  On average, it will be smaller.

Trade-offs:

- This approach is more efficient than the DP approach (O(n log n) vs. O(n^2)).
- It's slightly more complex to understand the intuition behind patience sorting and why it works. The use of binary search is key to the improved time complexity.

## Code

[Dynamic Programming (O(n^2))](./solution_dp.py)

[Patience Sorting with Binary Search (O(n log n))](./solution_patience.py)

## Notes

The key topics related to the question:

- Array
- Dynamic Programming
- Binary Search
