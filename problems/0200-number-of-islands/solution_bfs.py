"""
200. Number of Islands - BFS Solution
"""

from collections import deque


def numIslands_bfs(grid: list[list[str]]) -> int:
    """
    Calculates the number of islands in a 2D grid using BFS.

    Args:
      grid: The 2D grid representing land ('1') and water ('0').

    Returns:
      The number of islands.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def bfs(row, col):
        queue = deque([(row, col)])
        grid[row][col] = "0"  # Mark as visited

        while queue:
            r, c = queue.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and grid[new_r][new_c] == "1"
                ):
                    grid[new_r][new_c] = "0"  # Mark as visited
                    queue.append((new_r, new_c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                num_islands += 1
                bfs(r, c)  # Sink the entire island

    return num_islands
