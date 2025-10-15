# 200. Number of Islands, Difficulty: Medium

## Problem Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the *number of islands*.

An *island* is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

```

**Example 2:**

```

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Approach(es)

Solutions using both DFS (recursive) and BFS (iterative).  The core idea is to traverse the grid, and whenever we find a '1' (land), we perform a DFS or BFS to "sink" the entire island (mark all connected '1's as visited, often by changing them to '0' or some other marker).  Each time we start a new DFS/BFS, we increment the island count.

### Depth-First Search (DFS)

**Algorithm:**

1. **Iterate:** Iterate through each cell of the grid.
2. **Find Land:** If a cell contains '1' (land):
    - Increment the `num_islands` counter.
    - Call a `dfs` function to "sink" the entire island connected to this cell.
3. **DFS (Sink Island):**
    - **Base Cases:**
        - If the current cell is out of bounds, or the cell is water ('0'), return.
    - **Mark as Visited:** Mark the current cell as visited (e.g., change '1' to '0').  This prevents infinite loops and ensures we don't count the same island multiple times.
    - **Recursive Calls:** Recursively call `dfs` on the four neighboring cells (up, down, left, right).

**Data Structures:**

- 2D Array (the input `grid`) - We modify the grid in place to mark visited cells.

**Time Complexity:**

- O(m \* n), where m is the number of rows and n is the number of columns.  We visit each cell at most once.

**Space Complexity:**

- O(m \* n) in the worst case, due to the recursion stack.  This worst case occurs when the entire grid is filled with land (one giant island), and the DFS calls stack up to the maximum depth.  In the average case, the space complexity will be much less than O(m\*n).

**Trade-offs:**

- Simple and intuitive recursive approach.
- The space complexity can be significant in the worst case due to the recursion stack.

### Breadth-First Search (BFS)

**Algorithm:**

1. **Iterate:** Iterate through each cell of the grid.
2. **Find Land:** If a cell contains '1' (land):
    - Increment the `num_islands` counter.
    - Call a `bfs` function to "sink" the entire island connected to this cell.
3. **BFS (Sink Island):**
    - Create a queue and enqueue the starting cell (row, col).
    - Mark the starting cell as visited (e.g., change '1' to '0').
    - While the queue is not empty:
        - Dequeue a cell (row, col).
        - For each of the four neighbors (up, down, left, right):
            - If the neighbor is within bounds and is land ('1'):
                - Mark the neighbor as visited.
                - Enqueue the neighbor.

**Data Structures:**

- 2D Array (the input `grid`) - Modified in place.
- Queue (for BFS)

**Time Complexity:**

- O(m \* n), same as DFS.

**Space Complexity:**

- O(min(m, n)). In the worst-case scenario where the grid is filled with land, the BFS queue might contain, at most, all the cells from either one row or one column. So it takes the minimum value between `m` and `n`. In practice it's usually much less.

**Trade-offs:**

- Iterative approach, which avoids the potential for deep recursion and stack overflow.
- Often preferred for finding shortest paths, but in this case, both DFS and BFS are equally suitable for counting islands.

## Code

- [DFS Solution](./solution_dfs.py)
- [BFS Solution](./solution_bfs.py)

## Notes

- This problem is a classic example of graph traversal, where the grid cells are nodes and adjacent land cells are connected by edges.
- Both DFS and BFS are effective for solving this problem. The choice between them is often a matter of preference.
- The key idea is to "sink" or mark visited land cells to avoid counting the same island multiple times.
- The problem highlights the importance of handling boundary conditions (checking if row and column indices are within the grid bounds).
- Modifying the input grid in place (changing '1' to '0') is a common technique to mark visited cells and save space. If you cannot modify the original input, you can use a separate 2D boolean array to mark the visited cells.
