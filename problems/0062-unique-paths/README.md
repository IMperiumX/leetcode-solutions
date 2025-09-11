Okay, let's generate the LeetCode solution repository for "Unique Paths" (Problem 62).

**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem from the following input: `62. Unique Paths ... [problem description]`."
*   **Output:** "Problem Number: 62, Problem Name: Unique Paths, Difficulty: Medium"

**Step 2: Problem File Creation**

*   Create a directory named `0062-unique-paths`.

**Step 3: Solution File Generation**

We'll generate three solutions: one using dynamic programming (bottom-up), one using recursion with memoization (top-down), and one using a combinatorial approach (math).

*   **Prompt 3.2:** "Generate solutions in Python for the LeetCode problem: `Unique Paths` (Number: `62`). ... Create files named `solution_dp.py`, `solution_recursive.py`, and `solution_combinatorial.py`."

*   Create `solution_dp.py`:

```python
# 62. Unique Paths - Dynamic Programming (Bottom-Up)

def uniquePaths_dp(m, n):
    """
    Calculates the number of unique paths in an m x n grid using dynamic programming.

    Args:
        m: The number of rows.
        n: The number of columns.

    Returns:
        The number of unique paths.
    """
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and first column to 1 (only one way to reach any cell in the first row or column).
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the DP table.  The number of paths to reach cell (i, j) is the sum of paths
    # from the cell above (i-1, j) and the cell to the left (i, j-1).
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]
```

*   Create `solution_recursive.py`:

```python
# 62. Unique Paths - Recursion with Memoization (Top-Down)

def uniquePaths_recursive(m, n, memo=None):
    """
    Calculates the number of unique paths in an m x n grid using recursion with memoization.

    Args:
        m: The number of rows.
        n: The number of columns.
        memo: A dictionary to store intermediate results (for memoization).

    Returns:
        The number of unique paths.
    """
    if memo is None:
        memo = {}

    if (m, n) in memo:
        return memo[(m, n)]

    # Base cases:
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:  # Handle edge cases if m or n is invalid.
        return 0

    # Recursive calls with memoization:
    memo[(m, n)] = uniquePaths_recursive(m - 1, n, memo) + uniquePaths_recursive(m, n - 1, memo)
    return memo[(m, n)]
```

*   Create `solution_combinatorial.py`:

```python
# 62. Unique Paths - Combinatorial Approach (Math)
import math

def uniquePaths_combinatorial(m, n):
    """
    Calculates the number of unique paths in an m x n grid using a combinatorial formula.

    Args:
        m: The number of rows.
        n: The number of columns.

    Returns:
        The number of unique paths.
    """
    # We need to take a total of (m-1) + (n-1) steps.
    # Out of these, (m-1) steps are down, and (n-1) steps are right.
    # The number of unique paths is the number of ways to choose (m-1) down steps
    # from a total of (m-1 + n-1) steps, which is given by the binomial coefficient:
    # (m+n-2) choose (m-1)  or  (m+n-2) choose (n-1)

    total_steps = m + n - 2
    down_steps = m - 1

    # Using the formula for combinations: nCr = n! / (r! * (n-r)!)
    return math.comb(total_steps, down_steps)

```

**Step 4: Problem README Generation**

*   **Prompt 4:** "Generate a `README.md` file for the problem: `Unique Paths` (Number: `62`, Difficulty: `Medium`)."

```markdown
# 62. Unique Paths, Difficulty: Medium

## Problem Description

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid\[0]\[0]). The robot tries to move to the bottom-right corner (i.e., grid\[m - 1]\[n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10<sup>9</sup>.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3

Constraints:

1 <= m, n <= 100

## Approach(es)

### Dynamic Programming (Bottom-Up)

Algorithm:

1.  **Create DP Table:** Create a 2D array `dp` of size m x n, where `dp[i][j]` stores the number of unique paths to reach cell (i, j).
2.  **Initialize Base Cases:**
    *   Set `dp[i][0] = 1` for all `i` (only one way to reach any cell in the first column - by moving down).
    *   Set `dp[0][j] = 1` for all `j` (only one way to reach any cell in the first row - by moving right).
3.  **Fill DP Table:** Iterate through the remaining cells of the `dp` array (from `i = 1` to `m-1` and `j = 1` to `n-1`):
    *   `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (The number of paths to reach (i, j) is the sum of paths from the cell above and the cell to the left).
4.  **Return Result:** Return `dp[m-1][n-1]` (the number of paths to reach the bottom-right corner).

Data Structures:

*   A 2D array `dp` of size m x n.

Time Complexity:

*   O(m * n) - We fill each cell of the `dp` array once.

Space Complexity:

*   O(m * n) - We use a 2D array of size m x n. This can be optimized to O(min(m, n)) by using only one row/column at a time, since we only need the previous row/column to calculate the current one.

Trade-offs:

*   This approach is efficient and easy to understand.  It uses extra space for the `dp` array.

### Recursion with Memoization (Top-Down)

Algorithm:

1.  **Base Cases:**
    *   If `m == 1` or `n == 1`, return 1 (only one path).
    *   If `m == 0` or `n == 0`, return 0 (invalid path).
2.  **Memoization:** Use a dictionary `memo` to store the results of already computed subproblems (to avoid redundant calculations).
3.  **Recursive Calls:**
    *   If the result for `(m, n)` is already in `memo`, return it.
    *   Otherwise, recursively calculate the number of paths by summing the results of:
        *   `uniquePaths(m-1, n, memo)` (moving down)
        *   `uniquePaths(m, n-1, memo)` (moving right)
    *   Store the result in `memo` before returning it.

Data Structures:

*   A dictionary `memo` to store intermediate results.

Time Complexity:

*   O(m * n) - Each subproblem (m, n) is solved only once due to memoization.

Space Complexity:

*   O(m * n) -  The `memo` dictionary can store up to m * n entries in the worst case. The recursion depth can also be O(m + n) in the worst case.

Trade-offs:

*   This approach is more intuitive than the bottom-up DP approach for some people. It uses memoization to avoid redundant calculations, making it as efficient as the DP approach. It can have larger overhead than the DP because of function call stack.

### Combinatorial Approach (Math)

Algorithm:

1.  **Total Steps:**  To reach the bottom-right corner from the top-left corner, the robot must take a total of `(m - 1) + (n - 1)` steps.
2.  **Down Steps:** Out of these total steps, `(m - 1)` steps must be "down" movements, and the remaining `(n - 1)` steps must be "right" movements.
3.  **Combinations:** The number of unique paths is equivalent to the number of ways to choose `(m - 1)` "down" steps (or `(n - 1)` "right" steps) from the total `(m + n - 2)` steps. This can be calculated using the binomial coefficient:
    *   <sup>(m+n-2)</sup>C<sub>(m-1)</sub> = (m + n - 2)! / ((m - 1)! * (n - 1)!)
    * We use the `math.comb` function for efficient computation.

Data Structures:
* No extra data structures used.

Time Complexity:

*   O(min(m, n)). The time complexity is related to calculating nCr using the comb function (from Python 3.8). The implementation details of math.comb are efficient, typically relying on multiplicative methods that avoid large intermediate factorials.

Space Complexity:

*   O(1) - Constant extra space is used.

Trade-offs:

*   This is the most efficient approach in terms of both time and space complexity.  It requires understanding the underlying combinatorial principle. It's the most mathematically elegant solution.

## Code

[Dynamic Programming (Bottom-Up)](./solution_dp.py)

[Recursion with Memoization (Top-Down)](./solution_recursive.py)

[Combinatorial Approach (Math)](./solution_combinatorial.py)

## Notes
Key Topics related to question:
* Dynamic Programming
* Recursion
* Math
* Arrays
```
**Step 5: Related Topics**
* We created the `Math.md`, `Arrays.md` in the previous steps.

* Create `Dynamic Programming.md` and `Recursion.md`
```
# Dynamic Programming

Dynamic Programming (DP) is an algorithmic technique for solving optimization problems by breaking them down into smaller overlapping subproblems, solving each subproblem only once, and storing their solutions to avoid redundant computations.

## Key Concepts

*   **Overlapping Subproblems:** The problem can be broken down into smaller subproblems, and these subproblems are often solved repeatedly.
*   **Optimal Substructure:** The optimal solution to the problem can be constructed from optimal solutions to its subproblems.
*   **Memoization (Top-Down):**  Storing the results of expensive function calls and reusing them for the same inputs later.  This is typically implemented using recursion.
*   **Tabulation (Bottom-Up):** Building a table (usually an array) to store the solutions to subproblems in a bottom-up manner, starting with the smallest subproblems and working up to the main problem.

## Common Approaches

1.  **Memoization (Top-Down):**
    *   Start with the original problem and recursively break it down into subproblems.
    *   Use a data structure (usually a dictionary or hash map) to store the solutions to subproblems as they are computed.
    *   Before making a recursive call, check if the solution for that subproblem is already in the memo. If it is, return the stored value; otherwise, compute it, store it, and then return it.

2.  **Tabulation (Bottom-Up):**
    *   Identify the smallest subproblems (base cases).
    *   Create a table (usually a 1D or 2D array) to store the solutions to subproblems.
    *   Iteratively fill the table, starting with the base cases and building up to the solution for the original problem. The order of filling the table is crucial; you must solve smaller subproblems before larger ones that depend on them.

## Examples

*   **Fibonacci Sequence:** Calculate the nth Fibonacci number (using memoization or tabulation).
*   **Longest Common Subsequence (LCS):** Find the length of the longest subsequence common to two sequences.
*   **Shortest Path Problems:**  Find the shortest path in a graph (e.g., Dijkstra's algorithm, Floyd-Warshall algorithm).
*   **Knapsack Problem:** Determine the most valuable items to include in a knapsack with a limited weight capacity.
*   **Coin Change:** Find the minimum number of coins needed to make a given amount.
*   **Edit Distance (Levenshtein Distance):** Find the minimum number of edits (insertions, deletions, substitutions) needed to transform one string into another.

## Use Cases

Dynamic programming is used in a wide variety of applications, including:

*   **Optimization problems:** Finding the best solution among many possibilities.
*   **Combinatorial problems:** Counting the number of ways to do something.
*   **Graph algorithms:** Finding shortest paths, minimum spanning trees, etc.
*   **Sequence alignment:** Bioinformatics (e.g., aligning DNA sequences).
*   **Compiler design:**  Parsing and code optimization.

## Advantages

*   **Efficiency:**  Avoids redundant computations by storing and reusing solutions to subproblems.  Can drastically reduce time complexity (often from exponential to polynomial).
*   **Optimality:**  Guarantees finding the optimal solution for problems with optimal substructure.

## Disadvantages

*   **Memory Usage:**  Requires extra memory to store the solutions to subproblems (the memo or table).
*   **Complexity:**  Can be more difficult to design and implement than simple recursive solutions. Identifying the subproblems and the correct order of computation can be challenging.
* **Overhead:** For smaller input the overhead added from creating a table can overcome the benefit from DP.

## Related LeetCode Problems
* [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
*   [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (can be solved with DP)
*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
*   [120. Triangle](https://leetcode.com/problems/triangle/)
*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Kadane's Algorithm can be seen as a form of DP)
*   [322. Coin Change](https://leetcode.com/problems/coin-change/)
*   [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
*   [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
*   [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)
* [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
* [198. House Robber](https://leetcode.com/problems/house-robber/)
* [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
* [139. Word Break](https://leetcode.com/problems/word-break/)

```

```
# Recursion

Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. It's a powerful and elegant way to solve problems that can be broken down into smaller, self-similar subproblems.

## Key Concepts

*   **Base Case(s):**  One or more conditions that stop the recursion.  Without base cases, a recursive function would call itself infinitely, leading to a stack overflow error.
*   **Recursive Step:**  The part of the function where it calls itself with a modified input, moving towards the base case.
*   **Call Stack:**  A data structure that stores the state of each active function call (local variables, return address).  Each recursive call adds a new frame to the call stack.

## How Recursion Works

1.  **Function Call:** When a function calls itself, a new frame is pushed onto the call stack.
2.  **Execution:** The code within the recursive call is executed with the new input.
3.  **Base Case Check:**  The function first checks if the base case is met.
    *   If the base case is met, the function returns a value (or performs some final action) without making further recursive calls.
    *   If the base case is not met, the function proceeds to the recursive step.
4.  **Recursive Step:** The function calls itself with a modified input, making progress towards the base case.
5.  **Return Values:** As each recursive call completes, it returns a value (or performs an action) to its caller. The return values are "unwound" from the call stack until the initial function call returns its final result.

## Examples

*   **Factorial:** Calculating the factorial of a number (n! = n * (n-1) * ... * 1).
*   **Fibonacci Sequence:** Generating the nth Fibonacci number (F(n) = F(n-1) + F(n-2)).
*   **Tree Traversal:**  Visiting all nodes in a tree (pre-order, in-order, post-order).
*   **Graph Traversal:**  Visiting all nodes in a graph (depth-first search).
*   **Quicksort/Mergesort:** Sorting algorithms that use recursion.
* **Tower of Hanoi:** Classic problem solved efficiently through recursion.

## Types of Recursion

*   **Direct Recursion:** A function calls itself directly.
*   **Indirect Recursion:**  A function calls another function, which eventually calls the original function (e.g., function A calls function B, which calls function A).
*   **Tail Recursion:**  The recursive call is the *last* operation performed in the function.  Some compilers can optimize tail-recursive functions to avoid stack overflow errors for very deep recursion, turning the recursion to loop (Tail Call Optimization). Python *does not* perform tail call optimization.
* **Non-tail Recursion:** A recursion where additional operations are done after returning from recursive calls.

## Use Cases

Recursion is well-suited for problems that have a natural recursive structure, such as:

*   Tree and graph algorithms.
*   Divide-and-conquer algorithms.
*   Parsing (e.g., compilers, language interpreters).
*   Mathematical problems with recursive definitions (e.g., factorial, Fibonacci).
* Backtracking problems.

## Advantages

*   **Elegance and Readability:**  Recursive solutions can be more concise and easier to understand than iterative solutions for problems with a recursive structure.
*   **Natural Fit for Some Problems:** Some problems are inherently recursive, making recursion a natural and intuitive approach.

## Disadvantages

*   **Stack Overflow:**  Excessive recursion (too many nested function calls) can lead to a stack overflow error if the call stack exceeds its maximum size.
*   **Performance Overhead:**  Function calls have some overhead (creating stack frames, passing arguments, etc.).  In some cases, an iterative solution might be more efficient.
*   **Complexity:**  Understanding and debugging recursive functions can sometimes be more challenging than with iterative solutions.
* **Repetitive calculations**: The same sub-problems may be calculated several times.

## Recursion vs. Iteration

*   **Recursion:** Uses function calls and the call stack.
*   **Iteration:** Uses loops (e.g., `for`, `while`).

In many cases, a problem that can be solved recursively can also be solved iteratively, and vice-versa.  The choice between recursion and iteration often depends on:

*   Problem structure: Does the problem have a natural recursive structure?
*   Readability and maintainability: Which approach leads to clearer and more maintainable code?
*   Performance: In some cases, one approach might be significantly more efficient than the other.

## Related LeetCode Problems
*   [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
*   [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
*   [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (can be done recursively)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (can be solved recursively with memoization)
* [77. Combinations](https://leetcode.com/problems/combinations/)
* [46. Permutations](https://leetcode.com/problems/permutations)
* [78. Subsets](https://leetcode.com/problems/subsets/)
* [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
```
This completes the generation of the LeetCode repository for problem 62. It includes three solution files (dynamic programming, recursion with memoization, and combinatorial), a detailed README, and the topic files `Dynamic Programming.md` and `Recursion.md`. The explanations cover all the required aspects, including algorithms, data structures, time/space complexity, trade-offs, and related LeetCode problems. The code is well-commented. This provides a comprehensive and educational resource.
