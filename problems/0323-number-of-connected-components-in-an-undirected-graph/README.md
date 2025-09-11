Okay, let's generate the LeetCode solution repository for this problem.

**Step 1: Problem Identification**

The input is the URL: `https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph`

From this, we identify:

*   **Problem Number:** 323 (This is a premium problem and we assume this is its number).
*   **Problem Name:** Number of Connected Components in an Undirected Graph
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

We'll create the directory `0323-number-of-connected-components-in-an-undirected-graph`.

**Step 3: Solution File Generation**

We'll provide solutions using both Depth-First Search (DFS) and Union-Find (Disjoint Set).

**solution_dfs.py:**

```python
# 0323. Number of Connected Components in an Undirected Graph - DFS Approach

def countComponents(n: int, edges: list[list[int]]) -> int:
    """
    Counts the number of connected components in an undirected graph.

    Uses Depth-First Search (DFS).

    Args:
        n: The number of nodes (labeled from 0 to n-1).
        edges: A list of edges, where each edge is a list of two node labels.

    Returns:
        The number of connected components.
    """
    if not n:
        return 0

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    count = 0

    def dfs(node