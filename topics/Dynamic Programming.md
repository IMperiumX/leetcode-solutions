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
