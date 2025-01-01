# 1422. Maximum Score After Splitting a String, Difficulty: Easy

## Problem Description

Given a string `s` of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

**Example 1:**

**Input:** s = "011101"
**Output:** 5
**Explanation:**
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

**Example 2:**

**Input:** s = "00111"
**Output:** 5
**Explanation:** When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

**Example 3:**

**Input:** s = "1111"
**Output:** 3

**Constraints:**

* 2 <= s.length <= 500
* The string s consists of characters '0' and '1' only.

## Approach(es)

### One-Pass Approach

* Algorithm:
    1. Initialize `zeros` and `ones` to 0. `ones` will be used to store the negative of the actual count of ones on the left substring as we are trying to find the maximum of `zeros` + `ones` in the end.
    2. Initialize `max_score` to negative infinity.
    3. Iterate through the string `s` from left to right up to the second to last character:
        * If the current character is '0', increment `zeros`.
        * If the current character is '1', decrement `ones`.
        * Update `max_score` with the maximum of `max_score` and `zeros + ones`.
    4. Finally, increment `ones` if the last character is '1' to account for the ones in the rightmost substring.
    5. Add the final `ones` count to `max_score` to get the final score.
    6. Return `max_score`.
* Data Structures:
  * No extra data structures are used.
* Time Complexity:
  * O(N), where N is the length of the string. We iterate through the string once.
* Space Complexity:
  * O(1), constant extra space is used.
* Trade-offs:
  * This approach is very efficient as it iterates through the string only once and uses constant extra space.

### Prefix Sum Approach

* Algorithm:
    1. Calculate the total number of ones in the string.
    2. Initialize `max_score` to 0.
    3. Initialize `left_zeros` to 0.
    4. Iterate through the string `s` from left to right up to the second to last character:
        * If the current character is '0', increment `left_zeros`.
        * Calculate the number of ones in the right substring: `right_ones = total_ones - (i + 1 - left_zeros)`. Here, `(i + 1 - left_zeros)` calculates the number of ones in the left substring up to index `i`.
        * Update `max_score` with the maximum of `max_score` and `left_zeros + right_ones`.
    5. Return `max_score`.
* Data Structures:
  * No extra data structures are used.
* Time Complexity:
  * O(N), where N is the length of the string. We iterate through the string once.
* Space Complexity:
  * O(1), constant extra space is used.
* Trade-offs:
  * This approach might be slightly less intuitive than the one-pass approach but it still provides a linear time solution with constant space.

## Code

[[One-Pass Approach]](./solution_one_pass.py)
[[Prefix Sum Approach]](./solution_prefix_sum.py))
