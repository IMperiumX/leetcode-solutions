# 121. Best Time to Buy and Sell Stock, Difficulty: Easy

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1:**

**Input:** prices = [7,1,5,3,6,4]

**Output:** 5

**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

**Input:** prices = [7,6,4,3,1]

**Output:** 0

**Explanation:** In this case, no transactions are done and the max profit = 0.

**Constraints:**

* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`

## Approach(es)

### One Pass Approach

* **Algorithm:**
  * Initialize `min_price` to positive infinity and `max_profit` to 0.
  * Iterate through the `prices` array.
  * For each `price`:
    * Update `min_price` with the minimum value seen so far (including the current `price`).
    * Calculate the potential `profit` by subtracting `min_price` from the current `price`.
    * Update `max_profit` with the maximum value between the current `max_profit` and the calculated `profit`.
  * Return `max_profit`.
* **Data Structures:**
  * We only need to store two variables: `min_price` and `max_profit`.
* **Time Complexity:**
  * O(n), where n is the length of the `prices` array, as we iterate through the array once.
* **Space Complexity:**
  * O(1), as we use only a constant amount of extra space.
* **Trade-offs:**
  * This approach provides an optimal solution with excellent time and space complexity. There are no significant trade-offs. It's the most efficient way to solve this problem.

### Kadane's Algorithm Approach

* **Algorithm:**
  * Transform the `prices` array into a `diffs` array where `diffs[i] = prices[i+1] - prices[i]`.
  * Initialize `current_max` and `global_max` to 0.
  * Iterate through the `diffs` array.
  * For each element in `diffs`:
    * Update `current_max` to be the maximum between 0 and the sum of `current_max` and the current element. This decides whether to extend the current subarray or start a new one.
    * Update `global_max` to be the maximum between `global_max` and `current_max`.
  * Return `global_max`.
* **Data Structures:**
  * `diffs` array (optional - you can calculate the differences on the fly as shown in the code below)
  * `current_max` and `global_max` variables
* **Time Complexity:**
  * O(n), where n is the length of the `prices` array.
* **Space Complexity:**
  * O(1) - We can avoid creating the `diffs` array explicitly by calculating the price differences on the fly.
* **Trade-offs:**
  * This approach might be considered slightly less intuitive than the one-pass approach for this specific problem. However, it demonstrates a powerful technique (Kadane's Algorithm) that is useful for a broader range of problems.

## Code

### Python - One Pass and Kadane's Algorithm

[solution](./solution.py)
