# 2559. Count Vowel Strings in Ranges, Difficulty: Medium

## Problem Description

You are given a 0-indexed array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [li, ri]` asks us to find the number of strings present in the range `li` to `ri` (both inclusive) of `words` that start and end with a vowel.

Return an array `ans` of size `queries.length`, where `ans[i]` is the answer to the `i`th query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: `words = ["aba","bcb","ece","aa","e"]`, `queries = [[0,2],[1,4],[1,1]]`
Output: `[2,3,0]`
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query `[0,2]` is 2 (strings "aba" and "ece").
to query `[1,4]` is 3 (strings "ece", "aa", "e").
to query `[1,1]` is 0.
We return `[2,3,0]`.

Example 2:

Input: `words = ["a","e","i"]`, `queries = [[0,2],[0,1],[2,2]]`
Output: `[3,2,1]`
Explanation: Every string satisfies the conditions, so we return `[3,2,1]`.

Constraints:

- `1 <= words.length <= 10^5`
- `1 <= words[i].length <= 40`
- `words[i]` consists only of lowercase English letters.
- `sum(words[i].length) <= 3 * 10^5`
- `1 <= queries.length <= 10^5`
- `0 <= li <= ri < words.length`

## Approach(es)

### Prefix Sum Approach

Algorithm:

1. Create a set of vowels for efficient checking.
2. Create a `prefix_sums` array of size `len(words) + 1` initialized with 0s.
3. Iterate through the `words` array:
    - If a word starts and ends with a vowel, increment the current `prefix_sums` element by 1, otherwise keep the same value as the previous element.
4. Create an `ans` array to store the results.
5. Iterate through the `queries` array:
    - For each query `[l, r]`, calculate the number of vowel strings in the range as `prefix_sums[r + 1] - prefix_sums[l]`.
    - Append the result to the `ans` array.
6. Return the `ans` array.

Data Structures:

- Set for storing vowels.
- List (prefix\_sums) for storing prefix sums.

Time Complexity:

- O(n + q), where n is the length of `words` and q is the length of `queries`.
- Iterating through `words` takes O(n).
- Iterating through `queries` takes O(q).
- Checking if a word starts and ends with a vowel takes O(1) on average (assuming the average word length is constant).

Space Complexity:

- O(n) to store the `prefix_sums` array.

Trade-offs:

- Efficiently handles multiple range queries by precomputing prefix sums.
- Requires extra space to store the prefix sums.

## Code

[Prefix Sum Approach](./solution_prefix_sum.py)

## Notes

- The prefix sum technique is a common and efficient way to handle range queries.
- The time complexity is linear with respect to the number of words and queries.
- The space complexity is linear with respect to the number of words.
- This problem highlights the usefulness of preprocessing to optimize query answering.
