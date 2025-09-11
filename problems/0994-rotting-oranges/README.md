Okay, let's create the LeetCode solution repository for the "Rotting Oranges" problem.

**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem... You are given an m x n grid... Return the minimum number of minutes that must elapse until no cell has a fresh orange..."

*   **Analysis:** This accurately describes the "Rotting Oranges" problem (LeetCode #994).

*   **Output:** Problem Number: 994, Problem Name: Rotting Oranges, Difficulty: Medium

**Step 2: Problem File Creation**

*   Create directory: `0994-rotting-oranges`

**Step 3: Solution File Generation**

*   **Prompt 3.2:** Generate Python solutions. The standard approach for this is Breadth-First Search (BFS).

*   **File: `0994-rotting-oranges/solution.py`** (BFS Approach)

```python
# 994. Rotting Oranges - BFS Approach
from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    """
    Calculates the minimum time for all oranges to rot using BFS.
    """
    rows, cols = len(grid), len(grid[0])
    fresh_count = 0
    queue = deque()

    # Find all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))  # Add rotten oranges to the queue
            elif grid[r][c] == 1:
                fresh_count += 1

    # If there are no fresh oranges initially, return 0
    if fresh_count == 0:
        return 0

    minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4-directional neighbors

    while queue:
        for _ in range(len(queue)):  # Process all oranges at the current time step
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2  # Rot the fresh orange
                    fresh_count -= 1
                    queue.append((new_row, new_col))  # Add newly rotten orange to queue
        if len(queue) > 0:
            minutes += 1  # Increment time after each level of BFS

    # If there are still fresh oranges left, it's impossible to rot all
    return minutes if fresh_count == 0 else -1

```

**Step 4: Problem README Generation**

*   **Prompt 4:** Generate `README.md`.

*   **File: `0994-rotting-oranges/README.md`**

```markdown
# 994. Rotting Oranges, Difficulty: Medium

## Problem Description

You are given an `m x n` grid where each cell can have one of three values:

*   `0` representing an empty cell,
*   `1` representing a fresh orange, or
*   `2` representing a rotten orange.

Every minute, any fresh orange that is *4-directionally* adjacent to a rotten orange becomes rotten.

Return the *minimum number of minutes* that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

## Approach(es)

### Breadth-First Search (BFS) Approach

Algorithm:

1.  **Initialization:**
    *   Get the dimensions of the grid (`rows`, `cols`).
    *   Initialize `fresh_count = 0` (to count the number of fresh oranges).
    *   Initialize a queue `queue` (using `collections.deque` for efficient FIFO).
    *   Iterate through the grid:
        *   If a cell contains a rotten orange (`grid[r][c] == 2`), add its coordinates `(r, c)` to the `queue`.
        *   If a cell contains a fresh orange (`grid[r][c] == 1`), increment `fresh_count`.
2.  **Handle Initial No Fresh Oranges Case**:
    * If fresh_count == 0 return 0.
3.  **BFS Traversal:**
    *   Initialize `minutes = 0` (to track the time elapsed).
    *   Define `directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]` (for 4-directional neighbors).
    *   While the `queue` is not empty:
        * Iterate 'level by level':
          * Get current queue length to process only the rotten oranges present at the start of the current time step.
          * Iterate from 0 to current queue length:
            * Dequeue a rotten orange `(row, col)` from the `queue`.
            *   For each of the four `directions`:
                *   Calculate the coordinates of the neighboring cell (`new_row`, `new_col`).
                *   If the neighbor is within bounds *and* contains a fresh orange (`grid[new_row][new_col] == 1`):
                    *   Change the neighbor to a rotten orange (`grid[new_row][new_col] = 2`).
                    *   Decrement `fresh_count`.
                    *   Enqueue the neighbor's coordinates `(new_row, new_col)` to the `queue`.
        *  If `queue` is not empty:
           * `minutes += 1` (Increment time after processing all rotten oranges at the current level).
4.  **Check for Remaining Fresh Oranges:**
    *   After the BFS traversal, if `fresh_count > 0`, it means there are still fresh oranges that couldn't be reached, so return `-1`.
    *   Otherwise, return `minutes`.

Data Structures:

*   Queue (for BFS)
*   2D List (the grid)

Time Complexity:

*   O(m * n), where `m` is the number of rows and `n` is the number of columns. We visit each cell at most once.

Space Complexity:

*   O(m * n) in the worst case.  This can happen if all oranges are initially rotten, and the queue will hold all the cell coordinates.

Trade-offs:
* BFS is suitable for this problem, because it explores the grid level by level.

## Code

[BFS Approach](./solution.py)

## Notes

*   This problem is a classic application of Breadth-First Search (BFS).
*   BFS is used to simulate the rotting process level by level (minute by minute).
*   The use of a queue ensures that we process all rotten oranges at a given time step before moving on to the next time step.
*   The `fresh_count` variable is crucial for determining if all fresh oranges can be rotten.
* It is important to process elements in the queue in 'level by level' fashion.

```

**Step 5: Topic Extraction and Files**

*Prompt:* Topic extraction.
*Analysis:* The key topics are "Breadth-First Search (BFS)", "Queue", and "Array".

*   `Queue.md`: (This was created in previous responses, we'll reuse it.)
*   `Arrays.md`: (already exists, reuse)
*   `Graph Traversal.md`: (already exists, reuse – BFS is a graph traversal algorithm)

This completes the repository, providing a BFS-based solution, a comprehensive README with clear explanations of the algorithm and its complexity, and links to the relevant topic files. It correctly addresses the problem's requirements and uses best practices.
