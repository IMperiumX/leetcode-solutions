Okay, let's create the solution, README, and topic files for LeetCode problem 133: "Clone Graph". This is a classic graph problem that can be solved using either Depth-First Search (DFS) or Breadth-First Search (BFS).

**Step 1: Problem Identification**

*   **Problem Number:** 133
*   **Problem Name:** Clone Graph
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

I will create a folder named `0133-clone-graph`.

**Step 3: Solution File Generation**

I'll provide solutions using both DFS (recursive) and BFS (iterative). A crucial part of both solutions is using a hash map (dictionary in Python) to keep track of visited nodes and their corresponding clones.  This prevents infinite loops in cyclic graphs and ensures we create only one copy of each node.

*   **File 1: `solution_dfs.py`**

```python
"""
133. Clone Graph - DFS (Recursive) Solution
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph_dfs(node: 'Node') -> 'Node':
    """
    Creates a deep copy of a connected undirected graph using DFS.

    Args:
      node: A reference to a node in the original graph.

    Returns:
      A reference to the corresponding node in the cloned graph.
    """
    if not node:
        return None

    visited = {}  # Dictionary to store {original_node: cloned_node}

    def dfs(original_node):
        # If we've already cloned this node, return the clone
        if original_node in visited:
            return visited[original_node]

        # Create a new node with the same value
        clone_node = Node(original_node.val)
        visited[original_node] = clone_node  # Mark as visited *before* recursion

        # Recursively clone neighbors
        for neighbor in original_node.neighbors:
            clone_node.neighbors.append(dfs(neighbor))

        return clone_node

    return dfs(node)
```

*   **File 2: `solution_bfs.py`**

```python
"""
133. Clone Graph - BFS (Iterative) Solution
"""

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph_bfs(node: 'Node') -> 'Node':
    """
    Creates a deep copy of a connected undirected graph using BFS.

    Args:
      node: A reference to a node in the original graph.

    Returns:
      A reference to the corresponding node in the cloned graph.
    """
    if not node:
        return None

    visited = {}  # Dictionary to store {original_node: cloned_node}
    queue = deque([node])  # Start with the given node
    visited[node] = Node(node.val)  # Create a clone for the starting node

    while queue:
        original_node = queue.popleft()
        clone_node = visited[original_node]

        for neighbor in original_node.neighbors:
            if neighbor not in visited:
                # Create a clone for the neighbor and add it to visited
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)  # Add the neighbor to the queue
            # Add the cloned neighbor to the clone_node's neighbors list
            clone_node.neighbors.append(visited[neighbor])

    return visited[node] # Return the clone of the original starting node
```

**Step 4: Problem README Generation**

**File: `README.md`**

```markdown
# 133. Clone Graph, Difficulty: Medium

## Problem Description

Given a reference of a node in a **connected** undirected graph, return a *deep copy* (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```python
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**Test case format:** (See problem description for details - adjacency list representation)

**Example 1:** (See problem description)

**Example 2:** (See problem description)

**Example 3:** (See problem description)

**Constraints:**

-   The number of nodes in the graph is in the range `[0, 100]`.
-   `1 <= Node.val <= 100`
-   `Node.val` is unique for each node.
-   There are no repeated edges and no self-loops in the graph.
-   The Graph is connected and all nodes can be visited starting from the given node.

## Approach(es)

### Depth-First Search (DFS) - Recursive

**Algorithm:**

1.  **Base Case:** If the input `node` is `None`, return `None`.
2.  **Visited Hash Map:** Create a dictionary `visited` to store mappings from original nodes to their corresponding cloned nodes. This prevents cycles and ensures we don't create duplicate nodes.
3.  **Recursive `dfs` function:**
    -   If the current `original_node` is already in `visited`, return its cloned counterpart from `visited`.
    -   Create a new `clone_node` with the same value as `original_node`.
    -   Add the mapping `original_node: clone_node` to `visited`.  **Crucially, do this *before* making recursive calls.**
    -   Iterate through the `neighbors` of the `original_node`:
        -   Recursively call `dfs` on each `neighbor` to get its clone.
        -   Append the cloned neighbor to the `neighbors` list of the `clone_node`.
    -   Return the `clone_node`.
4.  Call the `dfs` function with the initial input `node` and return the result.

**Data Structures:**

-   Hash Map (`visited`):  `{original_node: cloned_node}`
-   Recursion (call stack)

**Time Complexity:**

-   O(N + E), where N is the number of nodes and E is the number of edges in the graph. We visit each node and each edge once.

**Space Complexity:**

-   O(N) in the worst case.  This is due to:
    -   The `visited` dictionary, which stores a mapping for each node.
    -   The recursion stack, which can go as deep as the number of nodes in the worst case (e.g., a linear graph).

**Trade-offs:**

-   Elegant and concise recursive solution.
-   Uses the call stack for traversal, which can be less intuitive than BFS for some.

### Breadth-First Search (BFS) - Iterative

**Algorithm:**

1.  **Base Case:** If the input `node` is `None`, return `None`.
2.  **Visited Hash Map:**  Create a dictionary `visited` to store mappings from original nodes to their corresponding cloned nodes.
3.  **Queue:** Create a queue `queue` and initialize it with the input `node`.
4.  **Create Clone of Starting Node:**  Create a clone of the input `node` and add it to `visited`.
5.  **BFS Traversal:**
    -   While the `queue` is not empty:
        -   Dequeue an `original_node` from the `queue`.
        -   Get the corresponding `clone_node` from `visited`.
        -   Iterate through the `neighbors` of the `original_node`:
            -   If a `neighbor` is *not* in `visited`:
                -   Create a clone of the `neighbor`.
                -   Add the mapping `neighbor: cloned_neighbor` to `visited`.
                -   Enqueue the `neighbor` into the `queue`.
            -   Append the cloned neighbor (obtained from `visited`) to the `neighbors` list of the `clone_node`.
6.  Return the clone of the original starting node (which is stored in `visited`).

**Data Structures:**

-   Hash Map (`visited`): `{original_node: cloned_node}`
-   Queue (`queue`)

**Time Complexity:**

-   O(N + E), where N is the number of nodes and E is the number of edges.

**Space Complexity:**

-   O(N) in the worst case, due to:
    -   The `visited` dictionary.
    -   The `queue`, which can hold up to all nodes in the worst case (e.g., a complete graph).

**Trade-offs:**

-   Iterative solution, which can be easier to understand for some.
-   Uses a queue for traversal, which can be more intuitive than the call stack for BFS.

## Code

[DFS (Recursive)](./solution_dfs.py)
[BFS (Iterative)](./solution_bfs.py)

## Notes

-   The key to solving this problem is using a hash map (`visited`) to track cloned nodes.  This prevents infinite loops in cyclic graphs and ensures that we create only one copy of each node.
-   Both DFS and BFS are valid approaches, and they have the same time and space complexity.  The choice between them is often a matter of personal preference or coding style.
-   The problem emphasizes the concept of a *deep copy*, where not only the node itself but also all its neighbors (and their neighbors, and so on) are copied.  A *shallow copy* would only copy the top-level node, and the neighbors would still point to the original nodes.
-   The adjacency list representation used in the test cases is a common way to represent graphs.
```

**Topic Extraction and Files:**

*   **Graph.md**

```markdown
# Graph

A graph is a non-linear data structure consisting of nodes (vertices) and edges that connect pairs of nodes. Graphs are used to represent relationships between objects.

## Key Concepts

-   **Node (Vertex):** A fundamental unit of a graph.
-   **Edge:** A connection between two nodes.
-   **Directed Graph (Digraph):** Edges have a direction (from one node to another).
-   **Undirected Graph:** Edges have no direction (connection is bidirectional).
-   **Weighted Graph:** Edges have associated weights (costs).
-   **Unweighted Graph:** Edges have no weights (or all edges have the same weight).
-   **Connected Graph:** There is a path between any two nodes in the graph.
-   **Disconnected Graph:** There are at least two nodes with no path between them.
-   **Cycle:** A path that starts and ends at the same node.
-   **Acyclic Graph:** A graph with no cycles.
-   **Directed Acyclic Graph (DAG):** A directed graph with no cycles.
-   **Degree of a Node (Undirected Graph):** The number of edges connected to the node.
-   **In-degree of a Node (Directed Graph):** The number of edges pointing *to* the node.
-   **Out-degree of a Node (Directed Graph):** The number of edges pointing *away from* the node.
- **Adjacency Matrix:** A 2D array where `matrix[i][j]` represents the presence (or weight) of an edge between node `i` and node `j`.
- **Adjacency List:** A collection of lists, where each list stores the neighbors of a node.

## Representations

-   **Adjacency Matrix:**
    -   A 2D array (e.g., list of lists in Python).
    -   `matrix[i][j] == 1` (or the weight) if there's an edge from node `i` to node `j`; otherwise, `matrix[i][j] == 0` (or some special value like infinity).
    -   Space Complexity: O(V^2), where V is the number of nodes.
    -   Good for dense graphs (many edges).
    -   Fast to check if an edge exists between two nodes (O(1)).
-   **Adjacency List:**
    -   A list (or array) of lists.
    -   `adj_list[i]` is a list containing all nodes adjacent to node `i`.
    -   Space Complexity: O(V + E), where V is the number of nodes and E is the number of edges.
    -   Good for sparse graphs (few edges).
    -   Efficient for iterating through neighbors of a node.

## Traversals

-   **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking. Uses a stack (or recursion).
-   **Breadth-First Search (BFS):** Explores all neighbors of a node before moving to the next level. Uses a queue.

## Common Graph Algorithms

-   **Shortest Path:**
    -   **BFS (Unweighted Graphs):** Finds the shortest path in terms of the number of edges.
    -   **Dijkstra's Algorithm (Weighted Graphs, Non-negative Weights):** Finds the shortest path with the minimum total weight.
    -   **Bellman-Ford Algorithm (Weighted Graphs, Can Handle Negative Weights):** Finds the shortest path, and can detect negative cycles.
-   **Minimum Spanning Tree (MST):**
    -   **Prim's Algorithm:**  Grows the MST from a starting node.
    -   **Kruskal's Algorithm:**  Sorts edges by weight and adds them to the MST if they don't create a cycle.
-   **Topological Sort (DAGs):**  Linear ordering of nodes such that for every directed edge from node A to node B, node A comes before node B in the ordering.
-   **Cycle Detection:**  Determining if a graph contains cycles.
-   **Connected Components:**  Finding groups of connected nodes in a graph.

## Time and Space Complexity (Common Operations)

| Operation          | Adjacency Matrix | Adjacency List |
| ------------------ | ---------------- | -------------- |
| Add Vertex         | O(V^2)           | O(1)           |
| Add Edge           | O(1)             | O(1)           |
| Remove Vertex      | O(V^2)           | O(V + E)        |
| Remove Edge        | O(1)             | O(E)           |
| Check Edge         | O(1)             | O(V)           |
| Get Neighbors      | O(V)             | O(degree(v))   |
| DFS/BFS Traversal  | O(V^2)          | O(V + E)      |

## Applications

-   **Social Networks:** Representing connections between people.
-   **Maps and Navigation:** Representing roads and locations.
-   **Network Routing:** Finding the best path for data packets.
-   **Recommendation Systems:**  Suggesting items based on user connections and preferences.
-   **Dependency Resolution:**  Determining the order in which tasks must be performed.
-   **Game AI:**  Pathfinding, decision-making.

## Related LeetCode Problems

-   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
-   [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
-   [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
-   [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
-   [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Union Find is often used)
-   [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
-   [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
-   [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)
-   [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
-   [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
-   [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

```

*   **Depth-First Search (DFS).md**

```markdown
# Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by going as deep as possible along each branch before backtracking. It's like exploring a maze by going all the way down one path before trying another.

## Key Concepts

-   **Stack (or Recursion):** DFS is typically implemented using a stack (explicitly or implicitly via recursion).
-   **Visited Set/Array:** A set (or array) is used to keep track of visited nodes to avoid cycles and redundant visits.
-   **Backtracking:** When a dead end (or a previously visited node) is reached, the algorithm backtracks to the previous node and explores a different branch.

## Algorithm (Recursive)

```python
def dfs_recursive(graph, node, visited):
    if node in visited:
        return  # Already visited

    visited.add(node)
    # Process the current node (e.g., print it)
    print(node)

    for neighbor in graph[node]:  # Iterate through neighbors
        dfs_recursive(graph, neighbor, visited)
```

## Algorithm (Iterative - using a Stack)

```python
def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()  # Get the last added node (LIFO)

        if node not in visited:
            visited.add(node)
            # Process the current node
            print(node)

            for neighbor in reversed(graph[node]): # Reverse to maintain similar to recursive order
                if neighbor not in visited:
                  stack.append(neighbor)

```

## Time Complexity

-   O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. Each node and each edge is visited at most once.

## Space Complexity

-   O(V) in the worst case, where V is the number of vertices.
    -   **Recursive:**  The call stack can grow up to the height of the graph, which can be O(V) in the worst case (e.g., a skewed tree or a linear graph).
    -   **Iterative:** The stack can also hold up to O(V) nodes in the worst case.
    - **Visited Set**: Stores up to V nodes.

## Applications

-   **Finding Connected Components:**  DFS can be used to identify all connected components in a graph.
-   **Topological Sorting (DAGs):**  A modified DFS can be used to perform topological sorting on directed acyclic graphs.
-   **Cycle Detection:**  DFS can be used to detect cycles in a graph.
-   **Path Finding:**  DFS can be used to find a path between two nodes (although it doesn't guarantee the shortest path).
-   **Solving Mazes:**  DFS can be used to find a path through a maze.
-   **Tree Traversals (Pre-order, In-order, Post-order):**  These are variations of DFS on trees.

## Trade-offs

-   **Advantages:**
    -   Relatively simple to implement, especially the recursive version.
    -   Can be used to find paths, detect cycles, and perform topological sorting.
-   **Disadvantages:**
    -   Doesn't necessarily find the shortest path (use BFS for that in unweighted graphs).
    -   Can be less memory-efficient than BFS for very wide graphs (where the breadth is much larger than the depth).

## Related LeetCode Problems

-   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
-   [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
-   [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
-   [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
-   [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
-   [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
-   [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)
-   [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (Can be solved using either BFS or DFS. BFS more natural, though)
-   [1162. As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) (Can be solved using either BFS or DFS. BFS is more typical for shortest path)

```

* **Breadth-First Search (BFS).md:** (This was defined in the 01 Matrix Problem)

The `0133-clone-graph` folder is now complete, containing both DFS and BFS solution files, a detailed README, and the Graph, Depth-First Search (DFS) and Breadth-First Search (BFS) topic files. This provides a comprehensive and well-organized learning resource.
