# 1639. Number of Ways to Form a Target String Given a Dictionary, Difficulty: Hard

## Problem Description

You are given a list of strings of the same length `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

* `target` should be formed from left to right.
* To form the `i`th character (0-indexed) of `target`, you can choose the `k`th character of the `j`th string in `words` if `target[i] == words[j][k]`.
* Once you use the `k`th character of the `j`th string of `words`, you can no longer use the `x`th character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusable for every string.
* Repeat the process until you form the string `target`.

Notice that you can use multiple characters from the same string in `words` provided the conditions above are met.

Return the *number of ways to form `target` from `words`*. Since the answer may be too large, return it *modulo* `10^9 + 7`.

**Example 1:**

**Input:** words = \["acca","bbbb","caca"], target = "aba"
**Output:** 6
**Explanation:** There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

**Example 2:**

**Input:** words = \["abba","baab"], target = "bab"
**Output:** 4
**Explanation:** There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

**Constraints:**

* `1 <= words.length <= 1000`
* `1 <= words[i].length <= 1000`
* All strings in `words` have the same length.
* `1 <= target.length <= 1000`
* `words[i]` and `target` contain only lowercase English letters.

## Approach: Dynamic Programming

* **Algorithm:**
    1. **Preprocessing:**
        * Create a 2D array `count` of size `m x 26` (where `m` is the length of each word in `words`), to store the frequency of each character at each index across all words. `count[k][c]` will store the number of times character `c` appears at index `k` in all the words.
    2. **Dynamic Programming:**
        * Create a 2D DP table `dp` of size `(n+1) x (m+1)` (where `n` is the length of `target`).
        * `dp[i][k]` will represent the number of ways to form the prefix of `target` of length `i` (i.e., `target[:i]`) using characters up to index `k` in the words.
        * **Base Case:** `dp[0][0] = 1`. There is one way to form an empty string using no characters.
        * **Iteration:** Iterate through `dp` from left to right, top to bottom:
            * **Option 1 (Don't use character at index `k`):** The number of ways to form `target[:i]` using characters up to index `k` is at least the number of ways to form `target[:i]` using characters up to index `k-1`. So, `dp[i][k+1] = (dp[i][k+1] + dp[i][k]) % mod`.
            * **Option 2 (Use character at index `k`):** If the current character `target[i-1]` appears at index `k` in some of the words (check `count[k][target[i-1] - 'a']`), then we can extend the number of ways to form `target[:i-1]` using characters up to index `k-1`. So, `dp[i][k+1] = (dp[i][k+1] + dp[i-1][k] * count[k][target[i-1] - 'a']) % mod`.
    3. **Result:** The final answer is stored in `dp[n][m]`, which represents the number of ways to form the entire `target` string using characters up to index `m` (the end of the words).

* **Data Structures:**
  * `count`: 2D array to store character frequencies.
  * `dp`: 2D array for dynamic programming table.

* **Time Complexity:**
  * O(n\*m), where n is the length of the target and m is the length of the words. We iterate through the `dp` table once. The preprocessing step also takes O(w\*m) where w is the number of words, but since w <= 1000, it is dominated by n\*m
* **Space Complexity:**
  * O(n\*m) to store the `dp` table.

* **Trade-offs:**
  * Dynamic programming provides an efficient solution to this problem, avoiding redundant calculations by storing and reusing the results of subproblems.
  * The space complexity can be optimized to O(m) using space optimization techniques.

## Code

[solution.py](solution.py)

## Notes

This problem is a good example of how dynamic programming can be used to solve combinatorial problems involving string manipulation and constraints.

The modulo operation is essential to prevent integer overflow.

The solution can be optimized for space by using only two rows of the dp table at a time, reducing the space complexity to O(m).
