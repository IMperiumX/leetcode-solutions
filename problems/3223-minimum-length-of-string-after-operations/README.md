# 3223. Minimum Length of String After Operations, Difficulty: Medium

## Problem Description

You are given a string `s`.

You can perform the following process on `s` any number of times:

- Choose an index `i` in the string such that there is at least one character to the left of index `i` that is equal to `s[i]`, and at least one character to the right that is also equal to `s[i]`.
- Delete the closest character to the left of index `i` that is equal to `s[i]`.
- Delete the closest character to the right of index `i` that is equal to `s[i]`.

Return the minimum length of the final string `s` that you can achieve.

**Example 1:**

```
Input: s = "abaacbcbb"
Output: 5
Explanation:
We do the following operations:
- Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
- Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
```

**Example 2:**

```
Input: s = "aa"
Output: 2
Explanation:
We cannot perform any operations, so we return the length of the original string.
```

**Constraints:**

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of lowercase English letters.

## Approach(es)

### Stack-based Approach

**Algorithm:**

1. Initialize a `deleted` array of the same size as the input string `s`, filled with `False`. This array will track which characters are deleted.
2. Initialize an empty stack `stack` to store indices of characters.
3. Iterate through the string `s` from left to right:
    - If the `stack` is not empty and the current character `s[i]` is equal to the character at the top of the stack (`s[stack[-1]]`), it means we have a potential operation.
        - Find the nearest left index `left` such that `s[left]` is equal to `s[i]` and `deleted[left]` is `False`.
        - Find the nearest right index `right` such that `s[right]` is equal to `s[i]` and `deleted[right]` is `False`.
        - If both `left` and `right` are found:
            - Mark `deleted[left]` and `deleted[right]` as `True`.
            - Pop the top element from the `stack` (as it's no longer needed).
            - Continue to the next iteration.
    - Otherwise, push the current index `i` onto the `stack`.
4. After iterating through the entire string, count the number of characters that are not marked as deleted (i.e., `deleted[i]` is `False`).
5. Return the count.

**Data Structures:**

- `deleted` array (list of booleans)
- `stack` (list of integers)

**Time Complexity:**

- O(n^2) in the worst case, where n is the length of the string. This is because finding the nearest left and right indices can take O(n) time in the worst case for each potential operation.

**Space Complexity:**

- O(n) to store the `deleted` array and the `stack`.

**Trade-offs:**

- This approach correctly handles the deletion operations and ensures that we find a valid minimum length.
- The time complexity is not optimal, especially for very long strings. There might be more efficient solutions using dynamic programming or other advanced techniques.

## Code

[Stack-based Approach](./solution.py)

## Notes

- This problem highlights the importance of carefully choosing the order of operations to achieve the minimum length. A greedy approach might not always work.
- The stack-based approach provides a way to track potential operations and efficiently mark characters for deletion.
- For very large inputs, exploring more advanced techniques like dynamic programming could lead to a more optimized solution.
- This problem relates to the concept of string manipulation and finding optimal subsequences.
