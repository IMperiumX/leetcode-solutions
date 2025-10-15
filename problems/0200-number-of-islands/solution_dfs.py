"""
200. Number of Islands - DFS Solution
"""


def numIslands_dfs(grid: list[list[str]]) -> int:
    """
    Calculates the number of islands in a 2D grid using DFS.

    Args:
      grid: The 2D grid representing land ('1') and water ('0').

    Returns:
      The number of islands.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
            return

        # Mark the current cell as visited (sink the island)
        grid[row][col] = "0"

        # Explore adjacent cells
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                num_islands += 1
                dfs(r, c)  # Sink the entire island

    return num_islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

if __name__ == "__main__":
    from pprint import pprint

    pprint(grid)
    print("\nNumber of Icelands: ", numIslands_dfs(grid))
