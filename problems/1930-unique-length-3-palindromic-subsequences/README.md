# 1930. Unique Length-3 Palindromic Subsequences, Difficulty: Medium

## Problem Description

Given a string `s`, return the number of unique palindromes of length three that are a subsequence of `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

**Example 1:**

**Input:** `s = "aabca"`

**Output:** `3`

**Explanation:** The 3 palindromic subsequences of length 3 are:

* "aba" (subsequence of "aabca")
* "aaa" (subsequence of "aabca")
* "aca" (subsequence of "aabca")

**Example 2:**

**Input:** `s = "adc"`

**Output:** `0`

**Explanation:** There are no palindromic subsequences of length 3 in "adc".

**Example 3:**

**Input:** `s = "bbcbaba"`

**Output:** `4`

**Explanation:** The 4 palindromic subsequences of length 3 are:

* "bbb" (subsequence of "bbcbaba")
* "bcb" (subsequence of "bbcbaba")
* "bab" (subsequence of "bbcbaba")
* "aba" (subsequence of "bbcbaba")

**Constraints:**

* `3 <= s.length <= 10^5`
* `s` consists of only lowercase English letters.

## Approach

### Two Pointers and Hash Set

#### Algorithm

1. Iterate through the unique characters in the string `s`.
2. For each unique character, find its first and last occurrences in `s`.
3. If a character appears at least twice (first occurrence index is less than the last occurrence index), then:
    * Find all the unique characters that appear between the first and last occurrences of the current character.
    * The number of unique characters in between contributes to the total count of unique palindromic subsequences. We are essentially counting the number of valid "middle" characters for a palindrome of the form `char` + `middle_char` + `char`.

#### Data Structures

* `set()`: To store the unique characters in the string and the unique characters between the first and last occurrences of a character.

#### Time Complexity

* O(N), where N is the length of the string `s`. We iterate through the unique characters (at most 26) and in the worst case, we might scan a significant portion of the string for each character to find the unique characters in between.

#### Space Complexity

* O(1), as the number of unique characters is limited to 26 (lowercase English letters).

#### Trade-offs

* **Pros:** Relatively easy to understand and implement. Efficient for strings with a large number of repeated characters.
* **Cons:** Might not be the most optimal for strings with very few repetitions.

## Code

* [Two Pointers and Hash Set Approach](./solution.py)

## Notes

* The key insight here is to recognize that we only need to find the first and last occurrences of each character and then count the unique characters in between. This avoids unnecessary computations and gives us an efficient solution.
* Alternative approaches might involve using more complex data structures or algorithms, but they are likely to be less efficient for this problem's constraints.
