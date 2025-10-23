# Dynamic Programming

Dynamic Programming (DP) is a powerful algorithmic technique used to solve optimization problems by breaking them down into smaller overlapping subproblems, solving each subproblem only once, and storing their solutions to avoid redundant computations.

## Key Concepts

1. **Overlapping Subproblems:**
    * A problem exhibits overlapping subproblems if it can be divided into smaller subproblems that are reused multiple times.
    * For example, in the Fibonacci sequence, to calculate `fib(5)`, you need `fib(4)` and `fib(3)`. To calculate `fib(4)`, you need `fib(3)` and `fib(2)`. Notice that `fib(3)` is needed multiple times.

2. **Optimal Substructure:**
    * A problem has optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
    * Again, in the Fibonacci sequence, the optimal solution for `fib(n)` is the sum of the optimal solutions for `fib(n-1)` and `fib(n-2)`.

## Approaches to Dynamic Programming

There are two main approaches to implementing dynamic programming:

1. **Memoization (Top-Down):**
    * This approach starts with the original problem and recursively breaks it down into subproblems.
    * It stores the solution to each subproblem in a table (usually an array or a hash map) as it is computed.
    * When a subproblem is encountered again, its solution is looked up in the table instead of recomputing it.
    * Memoization is essentially recursion with caching.

2. **Tabulation (Bottom-Up):**
    * This approach starts by solving the smallest subproblems and builds up the solution to the original problem iteratively.
    * It uses a table to store the solutions to subproblems, filling the table in a specific order (usually from the base cases to the larger subproblems).
    * Tabulation avoids recursion, and in some cases, it can be more efficient than memoization due to the overhead of function calls in recursion.

## Steps to Solve a Problem Using Dynamic Programming

1. **Identify Overlapping Subproblems and Optimal Substructure:**
    * Determine if the problem can be broken down into smaller subproblems that are reused and if the optimal solution to the problem can be constructed from the optimal solutions to its subproblems.

2. **Define the Subproblem:**
    * Clearly define the subproblem in terms of its parameters. For example, in the Fibonacci sequence, the subproblem is `fib(i)`, where `i` is the input to the Fibonacci function.

3. **Formulate the Recurrence Relation:**
    * Express the solution to the subproblem in terms of solutions to smaller subproblems. This is the core of the dynamic programming approach. For example, the recurrence relation for the Fibonacci sequence is `fib(i) = fib(i-1) + fib(i-2)`.

4. **Choose an Approach (Memoization or Tabulation):**
    * Decide whether to use memoization (top-down) or tabulation (bottom-up) based on the problem and your preference.

5. **Implement the Solution:**
    * Write the code to implement the chosen approach, using a table to store the solutions to subproblems.

## Advantages of Dynamic Programming

* **Efficiency:** By storing and reusing solutions to subproblems, dynamic programming can significantly reduce the time complexity of algorithms, often from exponential to polynomial.
* **Optimality:** It guarantees finding the optimal solution to problems that exhibit optimal substructure.

## Disadvantages of Dynamic Programming

* **Memory Usage:** Storing the solutions to subproblems can require significant memory, especially for problems with a large number of subproblems.
* **Complexity:** Designing and implementing dynamic programming solutions can be more complex than simpler approaches like greedy algorithms or divide and conquer.

## When to Use Dynamic Programming

* When you encounter optimization problems that can be broken down into overlapping subproblems.
* When the problem exhibits optimal substructure.
* When you need to find the optimal solution and are willing to invest time in designing and implementing a more complex solution.

## Kadane's Algorithm

## Overview

Kadane's Algorithm is a dynamic programming algorithm that efficiently finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers. It's a classic algorithm known for its simplicity and efficiency.

## Algorithm

The algorithm works by iterating through the array and maintaining two variables:

1. **`current_max`:** The maximum sum of a subarray ending at the current position.
2. **`global_max`:** The overall maximum sum found so far.

**Steps:**

1. Initialize `current_max` and `global_max` to the first element of the array (or 0 if you prefer to handle arrays with all negative numbers by returning 0).
2. Iterate through the array from the second element.
3. For each element:
    * Update `current_max` by taking the maximum between:
        * The current element itself (starting a new subarray).
        * The sum of the current element and the previous `current_max` (extending the current subarray).
    * Update `global_max` by taking the maximum between the current `global_max` and the updated `current_max`.
4. Return `global_max`.

## Example

Consider the array: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| Index | Element | `current_max` | `global_max` | Explanation                                                     |
| :---- | :------ | :------------ | :----------- | :-------------------------------------------------------------- |
| 0     | -2      | -2            | -2           | Initialize `current_max` and `global_max` to -2.               |
| 1     | 1       | 1             | 1            | `current_max` = max(1, -2 + 1) = 1, `global_max` = max(-2, 1) = 1 |
| 2     | -3      | -2            | 1            | `current_max` = max(-3, 1 + (-3)) = -2, `global_max` = max(1, -2) = 1 |
| 3     | 4       | 4             | 4            | `current_max` = max(4, -2 + 4) = 4, `global_max` = max(1, 4) = 4 |
| 4     | -1      | 3             | 4            | `current_max` = max(-1, 4 + (-1)) = 3, `global_max` = max(4, 3) = 4 |
| 5     | 2       | 5             | 5            | `current_max` = max(2, 3 + 2) = 5, `global_max` = max(4, 5) = 5 |
| 6     | 1       | 6             | 6            | `current_max` = max(1, 5 + 1) = 6, `global_max` = max(5, 6) = 6 |
| 7     | -5      | 1             | 6            | `current_max` = max(-5, 6 + (-5)) = 1, `global_max` = max(6, 1) = 6 |
| 8     | 4       | 5             | 6            | `current_max` = max(4, 1 + 4) = 5, `global_max` = max(6, 5) = 6 |

The maximum sum of a contiguous subarray is 6 (from the subarray \[4, -1, 2, 1]).

## Related LeetCode Problems

* [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
* [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
* [689. Maximum Sum of 3 Non-Overlapping Subarrays](./../problems/0689-maximum-sum-of-3-non-overlapping-subarrays/README.md) This problem can be solved efficiently using dynamic programming. We can break down the problem into smaller overlapping subproblems: finding the maximum sum of one subarray, then two non-overlapping subarrays, and finally three. By storing the solutions to these subproblems, we can avoid redundant calculations and build up the solution for three subarrays. Specifically, we can use two additional arrays to store the best starting position of a subarray to the left and to the right of every index.
* [2466. Count Ways To Build Good Strings](./../problems/2466-count-ways-to-build-good-strings/README.md) This problem can be solved using dynamic programming to count the number of good strings of different lengths. By storing the number of good strings for each length, we can avoid redundant calculations and sum up the counts within the desired length range.
* [983 Minimum Cost For Tickets](./../problems/0983-minimum-cost-for-tickets/README.md) This problem can be solved by storing the minimum cost for each day, we can avoid redundant calculations and build up the solution for the entire period. Specifically, we can use an array to store the minimum cost for each day, considering the cost of buying a ticket for 1, 7, or 30 days.

# Dynamic Programming (DP)

Dynamic Programming (DP) is an algorithmic technique for solving optimization problems by breaking them down into simpler overlapping subproblems and storing the solutions to these subproblems to avoid redundant computations.

## Key Concepts

* **Optimal Substructure:** A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
* **Overlapping Subproblems:** A problem has overlapping subproblems if the same subproblems are solved multiple times during the recursive solution.  DP avoids recomputing these subproblems by storing their solutions.
* **Memoization (Top-Down):**  A recursive approach where we store the results of subproblems in a table (usually a hash map or array) to avoid recomputation.  We "memoize" the results.
* **Tabulation (Bottom-Up):**  An iterative approach where we build up a table of solutions to subproblems in a bottom-up manner, starting with the smallest subproblems and working our way up to the original problem.

## Steps to Solve DP Problems

1. **Identify Optimal Substructure:** Determine how an optimal solution to the problem can be constructed from optimal solutions to its subproblems.  Define the recursive relationship.
2. **Identify Overlapping Subproblems:**  Observe if the same subproblems are being solved repeatedly in the recursive approach.
3. **Choose Memoization (Top-Down) or Tabulation (Bottom-Up):**
    * **Memoization:**  Start with the original problem and recursively break it down, storing the results of subproblems as you go.
    * **Tabulation:**  Start with the smallest subproblems and build up the solution iteratively, filling a table.
4. **Define the Table (Memoization or Tabulation):**
    * Determine the dimensions and meaning of the table entries.  `dp[i]`, `dp[i][j]`, etc.
5. **Base Cases:**  Identify the base cases for the recursion (memoization) or the initial values for the table (tabulation).
6. **Iterative/Recursive Relation:**  Define the formula or logic for calculating the solution to a subproblem based on the solutions to smaller subproblems.
7. **Return the Result:**  Identify the entry in the table (or the result of the top-level recursive call) that represents the solution to the original problem.

## Example: Fibonacci Sequence (Tabulation)

```python
def fibonacci_tabulation(n):
    dp = [0] * (n + 1)  # dp[i] stores the i-th Fibonacci number
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Recurrence relation
    return dp[n]
```

## Example: Fibonacci Sequence (Memoization)

```python
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]
```

## Time and Space Complexity

* The time and space complexity of DP solutions depend on the size of the table and the number of subproblems.
* Often, the time complexity is O(size of the table) and the space complexity is O(size of the table).

## Applications

* **Shortest Path Problems:**  Dijkstra's algorithm, Floyd-Warshall algorithm.
* **Knapsack Problem:**  Finding the most valuable subset of items that can fit in a knapsack with a limited capacity.
* **Longest Common Subsequence (LCS):**  Finding the longest subsequence common to two sequences.
* **Longest Increasing Subsequence (LIS):**  Finding the longest increasing subsequence in a sequence.
* **Edit Distance (Levenshtein Distance):**  Finding the minimum number of edits (insertions, deletions, substitutions) to transform one string into another.
* **Coin Change:**  Finding the fewest number of coins to make up a given amount.
* **Matrix Chain Multiplication:**  Finding the most efficient way to multiply a chain of matrices.
* **Fibonacci Numbers**

## Trade-offs

* **Advantages:**
  * Can significantly improve the efficiency of algorithms by avoiding redundant computations.
  * Often leads to polynomial-time solutions for problems that would otherwise have exponential time complexity.
* **Disadvantages:**
  * Can require significant memory to store the table of subproblem solutions.
  * Can be more complex to design and implement than simple recursive solutions.  Identifying the optimal substructure and recurrence relation can be challenging.

## Related LeetCode Problems

* [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
* [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
* [198. House Robber](https://leetcode.com/problems/house-robber/)
* [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
* [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
* [120. Triangle](https://leetcode.com/problems/triangle/)
* [322. Coin Change](https://leetcode.com/problems/coin-change/)
* [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)
* [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
* [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
* [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
* [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
* [0-1 Knapsack Problem](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) (Classic DP problem, not directly on LeetCode)
