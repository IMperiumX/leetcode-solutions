# Depth-First Search (DFS)

## Description

Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. In other words, DFS explores the nodes in a "depthward" motion, going as deep as possible down each branch before moving on to the next branch.

## Algorithm

The DFS algorithm can be implemented using either recursion or an iterative approach with a stack. Here's a high-level overview of both approaches:

### Recursive Approach

1. Start at the root node (or any selected node).
2. Mark the current node as visited.
3. For each unvisited neighbor of the current node:
    * Recursively call DFS on the neighbor.

### Iterative Approach

1. Start at the root node (or any selected node).
2. Initialize a stack with the starting node.
3. While the stack is not empty:
    * Pop a node from the stack.
    * If the node has not been visited:
        * Mark the node as visited.
        * Push all unvisited neighbors of the node onto the stack.

## Key Concepts

* **Traversal:** DFS can be used to traverse all nodes in a tree or graph.
* **Search:** DFS can be used to search for a specific node or path in a tree or graph.
* **Backtracking:** When DFS reaches a dead end (a node with no unvisited neighbors), it backtracks to the previous node and continues exploring other branches.
* **Stack:** The iterative implementation of DFS uses a stack to keep track of the nodes to visit.
* **Recursion:** The recursive implementation of DFS implicitly uses the call stack to manage the traversal.

## Time Complexity

The time complexity of DFS is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph or tree. In the case of a tree, the time complexity is O(n), where n is the number of nodes.

## Space Complexity

The space complexity of DFS depends on the implementation:

* **Recursive:** O(h) in the worst case, where h is the height of the tree or the maximum depth of the graph. This is due to the call stack.
* **Iterative:** O(h) in the worst case, where h is the height of the tree or the maximum depth of the graph. This is due to the stack storing the nodes.

In the average case for balanced trees, the space complexity can be O(log n).

## Advantages

* **Simple to implement,** especially the recursive version.
* **Can be used to find a path** between two nodes.
* **Memory-efficient** for deep, narrow trees or graphs compared to Breadth-First Search (BFS).

## Disadvantages

* **May not find the shortest path** in an unweighted graph (BFS is better for this).
* **Can get stuck in an infinite loop** in cyclic graphs if not implemented carefully (need to mark visited nodes).
* **Recursive implementation can lead to stack overflow** errors for very deep trees or graphs.

## Example (Python - Recursive)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_recursive(node):
    if not node:
        return

    print(node.val)  # Process the node
    dfs_recursive(node.left)  # Traverse left subtree
    dfs_recursive(node.right)  # Traverse right subtree

# Example usage with a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

dfs_recursive(root)  # Output: 1 2 4 5 3
```

## Example (Python - Iterative)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_iterative(root):
    if not root:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)  # Process the node

        # Push right child first so that left child is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Example usage with a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

dfs_iterative(root)  # Output: 1 2 4 5 3
```

## Related LeetCode Problems

* [104. Maximum Depth of Binary Tree](./0104-maximum-depth-of-binary-tree/README.md)
* [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
* [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
* [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
* [112. Path Sum](https://leetcode.com/problems/path-sum/)
* [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
* [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
* [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

# Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by going as deep as possible along each branch before backtracking. It's a fundamental algorithm used in many graph-related problems.

## Key Concepts

* **Traversal:** DFS systematically visits all reachable nodes in a graph.
* **Recursion (or Explicit Stack):** DFS is typically implemented recursively, which implicitly uses the call stack.  It can also be implemented iteratively using an explicit stack.
* **Visited Set:**  A data structure (usually a set or an array) is used to keep track of visited nodes to avoid cycles and redundant visits.
* **Backtracking:** When DFS reaches a node with no unvisited neighbors, it backtracks to the previous node and explores other branches.

## Algorithm (Recursive)

1. **Start Node:** Choose a starting node.
2. **Mark Visited:** Mark the current node as visited.
3. **Explore Neighbors:** For each unvisited neighbor of the current node:
    * Recursively call DFS on the neighbor.
4. **Backtrack:**  Once all neighbors have been explored, the function returns (backtracks).

## Algorithm (Iterative - using a stack)

1. **Start Node:** Choose a starting node.
2. **Initialize Stack:** Create an empty stack and push the starting node onto it.
3. **Mark Visited Set** Initialize a visited set
4. **Iterate:** While the stack is not empty:
    * Pop a node from the stack.
    * If the node has not been visited:
        * Mark the node as visited.
        * Push all unvisited neighbors of the node onto the stack.

## Applications of DFS

* **Cycle Detection:**  Detecting cycles in a graph.
* **Topological Sorting:** Finding a linear ordering of nodes in a directed acyclic graph (DAG).
* **Path Finding:** Finding a path between two nodes.
* **Connectivity Checking:** Determining if a graph is connected.
* **Solving Mazes and Puzzles:** Exploring possible solutions in a systematic way.
* **Tree Traversals (Preorder, Inorder, Postorder):**  DFS forms the basis of these tree traversal methods.

## Advantages of DFS

* **Simple Implementation:**  Relatively easy to implement, especially recursively.
* **Memory Efficiency (in some cases):** For tree-like structures, DFS can use less memory than BFS.
* **Detecting cycles**

## Disadvantages of DFS

* **Not Optimal for Shortest Paths:** DFS does not guarantee finding the shortest path between two nodes.  BFS is better suited for that purpose.
* **Can Get Stuck in Deep Branches:**  In very large or infinite graphs, DFS might get stuck exploring a very deep branch without finding a solution.

## Related LeetCode Problems

* [207. Course Schedule](./0207-course-schedule)
* [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
* [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
* [100. Same Tree](https://leetcode.com/problems/same-tree)
* [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree)
