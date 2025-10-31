# 22. Generate Parentheses, Difficulty: Medium

## Problem Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1:**

- Input: n = 3
- Output: ["((()))","(()())","(())()","()(())","()()()"]

**Example 2:**

- Input: n = 1
- Output: ["()"]

**Constraints:**

- 1 <= n <= 8

## Approach(es)

### Backtracking Approach

Algorithm:

1. **Base Case:** If the current string has length `2 * n`, it's a complete combination, so add it to the result list and return.
2. **Recursive Steps:**
    - **Add Open Parenthesis:** If the number of open parentheses is less than `n`, we can add an open parenthesis "(" to the current string and recursively call the function with an incremented `open_count`.
    - **Add Close Parenthesis:** If the number of close parentheses is less than the number of open parentheses, we can add a close parenthesis ")" to the current string and recursively call the function with an incremented `close_count`.  This ensures we only add closing parentheses when there's a corresponding open parenthesis.
3. Start the backtracking process with an empty string and `open_count` and `close_count` both initialized to 0.

Data Structures:

- String: We build the parenthesis combinations as strings.
- List: We store the results in a list.

Time Complexity:

- O(4<sup>n</sup> / sqrt(n)).  This is related to the Catalan numbers, which describe the number of well-formed parenthesis combinations. The complexity is exponential, but tighter bounds exist.

Space Complexity:

- O(4<sup>n</sup> / sqrt(n)) for the result list in the worst case, and O(n) for the recursion call stack (depth of recursion).

Trade-offs:

- Backtracking systematically explores all valid combinations, guaranteeing correctness.
- The exponential time complexity is unavoidable for this problem since we must generate all possible valid combinations.

## Code

[Backtracking Approach](./solution_backtracking.py)

## Notes (Optional)

- This problem is a classic example of backtracking, where we make choices and explore different paths, undoing choices (backtracking) when necessary.
- The key constraint for well-formed parentheses is that at any point, the number of closing parentheses must not exceed the number of open parentheses.
