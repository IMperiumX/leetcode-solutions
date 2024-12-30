# 2466. Count Ways To Build Good Strings, Defficulty: Medium

## Problem Description

Given the integers `zero`, `one`, `low`, and `high`, we can construct a string by starting with an empty string, and then at each step perform either of the following:

* Append the character '0' `zero` times.
* Append the character '1' `one` times.

This can be performed any number of times.

A **good string** is a string constructed by the above process having a length between `low` and `high` (inclusive).

Return the *number of different good strings that can be constructed satisfying these properties*. Since the answer can be large, return it *modulo* `10^9 + 7`.

**Example 1:**

**Input:** low = 3, high = 3, zero = 1, one = 1
**Output:** 8
**Explanation:**
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011".
All binary strings from "000" to "111" are good strings in this example.

**Example 2:**

**Input:** low = 2, high = 3, zero = 1, one = 2
**Output:** 5
**Explanation:** The good strings are "00", "11", "000", "110", and "011".

**Constraints:**

* `1 <= low <= high <= 10^5`
* `1 <= zero, one <= low`

## Approach: Dynamic Programming

* **Algorithm:**
    1. Create a DP array `dp` of size `high + 1`, where `dp[i]` represents the number of good strings of length `i`.
    2. Initialize `dp[0] = 1` (base case: there's one way to form an empty string).
    3. Iterate from `i = 1` to `high`:
        * If `i - zero >= 0`, it means we can append `zero` '0's to a good string of length `i - zero` to form a good string of length `i`. Add `dp[i - zero]` to `dp[i]`.
        * If `i - one >= 0`, it means we can append `one` '1's to a good string of length `i - one` to form a good string of length `i`. Add `dp[i - one]` to `dp[i]`.
        * Take the modulo `10^9 + 7` of `dp[i]` in each step.
    4. Sum up `dp[i]` for `i` from `low` to `high` to get the total number of good strings within the desired length range. Take the modulo `10^9 + 7` of the sum.

* **Data Structures:**
  * `dp`: 1D array (or list in Python) to store the number of good strings of each length.

* **Time Complexity:**
  * O(high), as we iterate from 1 to `high`.

* **Space Complexity:**
  * O(high) to store the `dp` array.

* **Trade-offs:**
  * Dynamic programming is an efficient approach for this problem as it avoids redundant calculations by storing the number of good strings for each length.
  * The space complexity can be considered relatively high for very large values of `high`. However, given the constraint `high <= 10^5`, it's generally acceptable.

## Code

[solution.py](./solution.py)
