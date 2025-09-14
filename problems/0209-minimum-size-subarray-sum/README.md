# 209\. Minimum Size Subarray Sum, Difficulty: Medium

## Problem Description

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

**Example 1:**
Input: `target = 7`, `nums = [2,3,1,2,4,3]`
Output: `2`
Explanation: The subarray `[4,3]` has the minimal length under the problem constraint.

**Example 2:**
Input: `target = 4`, `nums = [1,4,4]`
Output: `1`

**Example 3:**
Input: `target = 11`, `nums = [1,1,1,1,1,1,1,1]`
Output: `0`

**Constraints:**

* `1 <= target <= 10^9`
* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^4`

-----

## Approach(es)

### Sliding Window Approach

This is the most optimal approach for this problem, offering a linear time complexity. It works by maintaining a "window" (a subarray) that we expand and shrink as we iterate through the main array.

* **Algorithm:**
    1. Initialize two pointers, `left` and `right`, at the beginning of the array (`0`), a `current_sum` to `0`, and `min_length` to infinity.
    2. Expand the window by moving the `right` pointer forward, adding `nums[right]` to `current_sum`.
    3. Once `current_sum` is greater than or equal to the `target`, we've found a valid subarray. We record its length (`right - left + 1`) and update `min_length` if this new length is smaller.
    4. Now, we try to find an even smaller valid subarray by shrinking the window from the left. We subtract `nums[left]` from `current_sum` and increment the `left` pointer.
    5. Repeat step 4 as long as `current_sum` remains greater than or equal to `target`.
    6. Continue expanding the window with the `right` pointer (step 2) until it reaches the end of the array.
    7. The final `min_length` is the answer. If it's still infinity, no such subarray exists, so we return 0.
* **Data Structures:**
  * Standard array for input.
  * Integer variables for pointers and sums. No auxiliary data structures are needed.
* **Time Complexity:** $O(n)$
  * Each element is visited at most twice, once by the `right` pointer and once by the `left` pointer.
* **Space Complexity:** $O(1)$
  * We only use a constant amount of extra space for variables.
* **Trade-offs:** This approach is highly efficient in both time and space, making it the preferred solution. It's specifically well-suited for problems asking for a "subarray" or "substring" that satisfies a condition based on its sum or count of elements.

### Prefix Sum + Binary Search Approach

This approach is a clever way to solve the problem and satisfies the `O(n log n)` follow-up. It transforms the problem from finding a subarray sum to a search problem on a sorted (or sortable) data structure.

* **Algorithm:**
    1. First, create a `prefix_sums` array of size `n+1`. `prefix_sums[i]` will store the sum of the first `i` elements of `nums`. `prefix_sums[0]` is `0`.
    2. The sum of any subarray `nums[i...j]` can now be calculated as `prefix_sums[j+1] - prefix_sums[i]`.
    3. Iterate through the `prefix_sums` array from `i = 0` to `n`. For each `prefix_sums[i]`, we need to find the smallest index `j > i` such that `prefix_sums[j] - prefix_sums[i] >= target`.
    4. This can be rewritten as finding the smallest `j` where `prefix_sums[j] >= target + prefix_sums[i]`.
    5. Since the `prefix_sums` array is monotonically increasing (all `nums` elements are positive), we can use binary search on the subarray `prefix_sums[i+1:]` to find this index `j` efficiently.
    6. For each `i`, if we find such a `j`, the length of the subarray is `j - i`. We update our `min_length` with the minimum length found across all `i`.
* **Data Structures:**
  * An auxiliary array of size `n+1` to store the prefix sums.
* **Time Complexity:** $O(n \\log n)$
  * We iterate through `n` starting points ($O(n)$), and for each one, we perform a binary search on the prefix sum array ($O(\\log n)$).
* **Space Complexity:** $O(n)$
  * We need an extra array to store the `n+1` prefix sums.
* **Trade-offs:** While less optimal than the sliding window, this technique is very powerful. It's a great tool to have when the sliding window condition (e.g., all positive numbers) doesn't hold, or for variations of the problem.

-----

## Code

* [Sliding Window Approach](./solution_sliding_window.py)
* [Prefix Sum + Binary Search Approach](./solution_binary_search.py)

-----

## Notes

* The **Sliding Window** approach is the clear winner for this specific problem due to its superior $O(n)$ time and $O(1)$ space complexity.
* The **Prefix Sum + Binary Search** method is a great example of how to use pre-computation to change the structure of a problem, enabling a different type of algorithm (binary search) to be used.
