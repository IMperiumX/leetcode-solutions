**Step 1: Problem Identification**

*   **Prompt 1:** The problem statement corresponds to "Longest Increasing Path in a Matrix," LeetCode problem 329.
*   **Output:** "Problem Number: 329, Problem Name: Longest Increasing Path in a Matrix, Difficulty: Hard"

**Step 2: Problem File Creation**

*   Create a directory named `329-longest-increasing-path-in-a-matrix`.

**Step 3: Solution File Generation**

*   **Prompt 3.2 (No provided solution):** We'll generate a Python solution. The optimal approach uses Depth-First Search (DFS) with memoization (dynamic programming) to avoid redundant calculations.

*   **`329-longest-increasing-path-in-a-matrix/solution_dfs_memo.py`:**

```python
# 329. Longest Increasing Path in a Matrix - DFS with Memoization

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = {}  # (row, col) -> length of longest increasing path starting at (row, col)

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            max_path_len = 1  # Initialize with 1 (the current cell itself)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_path_len = max(max_path_len, 1 + dfs(new_row, new_col))

            memo[(row, col)] = max_path_len
            return max_path_len

        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path
```

* **`329-longest-increasing-path-in-a-matrix/Depth-First Search.md`:**
```markdown
# Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal algorithm that explores a graph (or tree) by going as deep as possible along each branch before backtracking. It starts at a chosen node (often called the "root" in a tree) and explores as far as possible along each branch before backtracking.

## How DFS Works (Recursive Implementation)

1.  **Start at a node:** Choose a starting node (the root in a tree).
2.  **Mark as Visited:** Mark the current node as visited.
3.  **Explore Neighbors:** For each unvisited neighbor of the current node:
    *   Recursively call DFS on that neighbor.
4.  **Backtrack:** Once all neighbors of the current node have been visited (and their subtrees explored), the function returns (backtracks).

## How DFS Works (Iterative Implementation - Using a Stack)

1. **Initialization:**
    * Create a Stack.
    * Mark start node as visited, and add it to the Stack.
2. **Iteration:**
    * While Stack is not empty:
        * Pop a node from the Stack.
        * Process the node.
        * For each unvisited neighbor:
            * Mark it as visited
            * Push it to the stack

## Key Concepts

*   **Recursion (or Stack):** DFS is naturally recursive.  Each recursive call explores a deeper level of the graph.  An iterative implementation using a stack can also be used, explicitly managing the order of node visits.
*   **Visited Set:** A data structure (often a set or an array) is used to keep track of visited nodes to avoid cycles and redundant visits. This is crucial for graphs; for trees, it's less critical (unless there are cycles due to a faulty tree representation).

## Example (Tree)

Consider a simple binary tree:

```
    1
   / \
  2   3
 / \
4   5
```

A DFS traversal (preorder) starting from node 1 would visit the nodes in this order: 1, 2, 4, 5, 3.

## Time Complexity

*   **O(V + E)**, where V is the number of vertices (nodes) and E is the number of edges in the graph. Each node and each edge is visited at most once.  For a tree, this simplifies to O(V) or O(n), where n is the number of nodes.

## Space Complexity

*   **O(h)** in the average case recursive, where h is the height of the tree (depth of the recursion). In the worst case (a skewed tree), h can be equal to n (the number of nodes), leading to O(n) space complexity.
*  **O(w)** in the average case iterative, where w is width of the tree. In worst case it can be O(n).

## Advantages of DFS

*   **Simple to Implement (Recursively):** The recursive implementation is often very concise.
*   **Memory Efficient (for some problems):**  For problems where you only need to find *a* path (not necessarily the shortest), DFS can be more memory-efficient than Breadth-First Search (BFS) because it doesn't need to store all nodes at a given level.
*   **Suitable for Detecting Cycles:** Can be easily modified to detect cycles in a graph.
*  **Finding a path:** Good to use if a path exists deep inside the graph

## Disadvantages of DFS

*   **Doesn't Guarantee Shortest Path:** DFS does *not* necessarily find the shortest path in a graph (BFS does, for unweighted graphs).
*   **Can Get Stuck in Deep Branches:**  In very deep or infinite graphs, DFS might get "stuck" exploring a single branch indefinitely (unless there's a mechanism to limit the depth).

## Use Cases

*   **Tree Traversals (Preorder, Inorder, Postorder):**  DFS is the basis for these common tree traversal methods.
*   **Path Finding (not necessarily shortest):** Finding *any* path between two nodes.
*   **Cycle Detection:** Determining if a graph contains cycles.
*   **Topological Sorting:** Ordering nodes in a directed acyclic graph (DAG) such that for every directed edge from node A to node B, node A comes before node B in the ordering.
*   **Solving Puzzles (Mazes, Sudoku):**  Exploring possible solutions.
* **Connected component:** Finding connected components in a graph.

## Related LeetCode Problems

*    [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (BFS is generally preferred, but DFS can also be used)
*    [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)
*    [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
*    [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
*   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
*   [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
*    [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
```
*   **`329-longest-increasing-path-in-a-matrix/Dynamic Programming.md`:**
```markdown
# Dynamic Programming

Dynamic Programming (DP) is an algorithmic technique for solving optimization problems by breaking them down into smaller overlapping subproblems, solving each subproblem only once, and storing their solutions to avoid redundant computations. DP is particularly effective for problems that exhibit the following properties:

1.  **Optimal Substructure:** An optimal solution to the problem can be constructed from optimal solutions to its subproblems.
2.  **Overlapping Subproblems:** The same subproblems are encountered multiple times during the recursive solution of the problem.

## Approaches to Dynamic Programming

There are two main approaches to dynamic programming:

1.  **Top-Down (Memoization):**
    *   Start with the original problem and recursively break it down into subproblems.
    *   Use a cache (usually a hash table or an array) to store the solutions to subproblems as they are computed.
    *   Before solving a subproblem, check if its solution is already present in the cache. If so, return the cached solution; otherwise, compute the solution, store it in the cache, and then return it.
    *   This approach is often implemented using recursion with a helper function.

2.  **Bottom-Up (Tabulation):**
    *   Start with the smallest subproblems and build up solutions to larger subproblems iteratively.
    *   Use a table (usually an array or a matrix) to store the solutions to subproblems.
    *   Fill the table in a specific order, ensuring that the solutions to all required subproblems are available before solving a larger subproblem.
    *   This approach is typically implemented using loops.

## Example: Fibonacci Sequence

The Fibonacci sequence is a classic example that can be solved efficiently with DP.

*   **Recursive (without DP):**
    ```python
    def fib_recursive(n):
        if n <= 1:
            return n
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    ```
    This is highly inefficient (exponential time complexity) due to redundant calculations.

*   **Top-Down (Memoization):**

    ```python
    def fib_memoization(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
        return memo[n]
    ```

*   **Bottom-Up (Tabulation):**

    ```python
    def fib_tabulation(n):
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    ```

Both the memoization and tabulation approaches have a time complexity of O(n) and a space complexity of O(n).

## Advantages of Dynamic Programming

*   **Efficiency:** Avoids redundant computations, leading to significant performance improvements for problems with overlapping subproblems.
*   **Optimality:** Guarantees finding the optimal solution for problems with optimal substructure.

## Disadvantages of Dynamic Programming

*   **Memory Usage:** Can require significant memory to store the solutions to subproblems (especially with tabulation).
*   **Implementation Complexity:**  Can be more challenging to design and implement than simpler recursive solutions, especially for complex problems.
* **Not Always Applicable:** Not efficient for all problems.

## Use Cases

*   **Shortest Path Problems:**  Dijkstra's algorithm, Floyd-Warshall algorithm.
*   **Sequence Alignment:**  Needleman-Wunsch algorithm, Smith-Waterman algorithm.
*   **Knapsack Problem:**  Finding the most valuable combination of items to include in a knapsack with limited capacity.
*   **Longest Common Subsequence:** Finding the longest subsequence common to two sequences.
*   **Matrix Chain Multiplication:**  Finding the most efficient way to multiply a chain of matrices.
* **Game playing**
* **String algorithms**

## Related LeetCode Problems

*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
*   [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
*   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
*   [198. House Robber](https://leetcode.com/problems/house-robber/)
*   [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
*   [322. Coin Change](https://leetcode.com/problems/coin-change/)
*   [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)
*   [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
*   [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
```

**Step 4: Problem README Generation**

*   **Prompt 4:** Generate the `README.md`.

```markdown
# 329. Longest Increasing Path in a Matrix, Difficulty: Hard

## Problem Description

Given an `m x n` integers `matrix`, return *the length of the longest increasing path in* `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

**Example 1:**

```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**

```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: 1
```

**Constraints:**

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= m, n <= 200`
*   `0 <= matrix[i][j] <= 2^31 - 1`

## Approach(es)

### DFS with Memoization (Dynamic Programming)

Algorithm:

1.  **Memoization:** Create a memoization table (dictionary in Python) `memo` to store the length of the longest increasing path starting from each cell `(row, col)`.  `memo[(row, col)]` will store the result of `dfs(row, col)`.
2.  **DFS Function (`dfs(row, col)`):**
    *   **Base Case (Memoized):** If `(row, col)` is already in `memo`, return the stored value `memo[(row, col)]`.
    *   **Initialize:** Initialize `max_path_len` to 1 (the current cell itself contributes 1 to the path length).
    *   **Explore Neighbors:** Iterate through the four possible directions (up, down, left, right):
        *   Calculate the coordinates of the neighboring cell (`new_row`, `new_col`).
        *   **Validity Check:** Check if the neighbor is within the matrix bounds *and* if the neighbor's value is strictly greater than the current cell's value (to ensure increasing order).
        *   **Recursive Call:** If the neighbor is valid, recursively call `dfs(new_row, new_col)` and update `max_path_len` with `1 + dfs(new_row, new_col)` (1 for the current cell + the result from the neighbor).
    *   **Memoize and Return:** Store the calculated `max_path_len` in `memo[(row, col)]` and return it.
3.  **Main Loop:**
    *   Initialize `longest_path` to 0.
    *   Iterate through all cells in the matrix:
        *   For each cell `(i, j)`, call `dfs(i, j)` and update `longest_path` with the maximum path length found so far.
4.  **Return:** Return the final `longest_path`.

Data Structures:

*   Dictionary (Hash Map): Used for memoization (`memo`).

Time Complexity:

*   O(m * n), where m is the number of rows and n is the number of columns in the matrix.  Due to memoization, each cell is visited and processed at most once by the `dfs` function. Without memoization, the time complexity would be exponential.

Space Complexity:

*   O(m * n) - The `memo` dictionary can store up to `m * n` entries (one for each cell).  The recursion depth can also be up to `m * n` in the worst case (although memoization significantly reduces the number of actual recursive calls).

Trade-offs:

*   This approach combines DFS for exploring paths with memoization (a form of dynamic programming) to avoid redundant calculations. The memoization drastically reduces the time complexity from exponential to polynomial.

## Code

[DFS with Memoization](./solution_dfs_memo.py)

## Notes (Optional)

*   The key to solving this problem efficiently is to use memoization. Without it, the DFS would repeatedly explore the same subpaths, leading to exponential time complexity.
*   The problem explicitly prohibits diagonal moves and moving outside the boundary.
* The approach can be easily adapted to find the actual longest increasing path (not just its length) by storing the path information in the `memo` table along with the length.

```

This provides a complete, well-structured, and thoroughly explained solution, including detailed explanations of the algorithms and concepts used (DFS, Dynamic Programming), making it an excellent LeetCode solution repository.
