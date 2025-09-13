# Breadth-First Search (BFS)

## Description

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key') and explores the neighbor nodes first, before moving to the next level neighbors. In other words, BFS explores the nodes level by level, visiting all nodes at a given level before moving on to the next level.

## Algorithm

The BFS algorithm is typically implemented using an iterative approach with a queue. Here's a high-level overview:

1. Start at the root node (or any selected node).
2. Initialize a queue with the starting node.
3. While the queue is not empty:
    * Dequeue a node from the queue.
    * If the node has not been visited:
        * Mark the node as visited.
        * Process the node (e.g., print its value).
        * Enqueue all unvisited neighbors of the node.

## Key Concepts

* **Traversal:** BFS can be used to traverse all nodes in a tree or graph.
* **Search:** BFS can be used to search for a specific node or path in a tree or graph.
* **Level Order:** BFS visits nodes level by level, ensuring that all nodes at a given distance from the starting node are visited before moving to nodes farther away.
* **Queue:** BFS uses a queue to keep track of the nodes to visit. Nodes are added to the rear of the queue and removed from the front.

## Time Complexity

The time complexity of BFS is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph or tree. In the case of a tree, the time complexity is O(n), where n is the number of nodes.

## Space Complexity

The space complexity of BFS is O(w), where w is the maximum width (number of nodes at the widest level) of the tree or graph. In the worst case (e.g., a complete binary tree), the space complexity can be O(n), where n is the number of nodes.

## Advantages

* **Finds the shortest path** in an unweighted graph or tree.
* **Guaranteed to find a solution** if one exists (in a finite graph).
* **Useful for finding connected components** in a graph.

## Disadvantages

* **Can be memory-intensive** for graphs or trees with a large branching factor, as it needs to store all nodes at a given level in the queue.
* **May not be suitable for very deep trees or graphs** where memory is a constraint.

## Example (Python)

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)  # Process the node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage with a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bfs(root)  # Output: 1 2 3 4 5
```

## Related LeetCode Problems

* [104. Maximum Depth of Binary Tree](./0104-maximum-depth-of-binary-tree/README.md)
* [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
* [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
* [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
* [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
* [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
* [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

# Breadth-First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm that explores a graph level by level. It starts at a source node and visits all its immediate neighbors before moving on to their neighbors, and so on. BFS is fundamental for many graph algorithms.

## Key Concepts

* **Traversal:** BFS systematically visits all reachable nodes in a graph.
* **Queue:** BFS uses a queue data structure to maintain the order of nodes to visit.
* **Level-by-Level Exploration:** BFS explores nodes in layers, visiting all nodes at a given distance from the source node before moving to nodes that are farther away.
* **Visited Set:**  A data structure (usually a set or an array) is used to keep track of visited nodes to avoid cycles and redundant visits.

## Algorithm

1. **Start Node:** Choose a starting node (source node).
2. **Initialize Queue:** Create an empty queue and enqueue the starting node.
3. **Mark Visited:** Mark the starting node as visited.
4. **Iterate:** While the queue is not empty:
    * Dequeue a node from the front of the queue.
    * For each unvisited neighbor of the dequeued node:
        * Mark the neighbor as visited.
        * Enqueue the neighbor.

## Applications of BFS

* **Shortest Path (Unweighted Graphs):**  BFS finds the shortest path (in terms of the number of edges) from a source node to all other reachable nodes in an unweighted graph.
* **Connectivity Checking:**  Determining if a graph is connected.
* **Level Order Traversal (Trees):**  Visiting all nodes of a tree level by level.
* **Finding Minimum Depth of Binary Tree**
* **Web Crawling:**  Exploring web pages by following links.
* **Network Broadcasting**
* **Social Network Analysis**

## Advantages of BFS

* **Finds Shortest Path (Unweighted Graphs):** Guaranteed to find the shortest path in an unweighted graph.
* **Complete:**  Will always find a solution if one exists (in a finite graph).

## Disadvantages of BFS

* **Memory Usage:** Can use more memory than DFS, especially for graphs with high branching factors (many neighbors per node), as it needs to store all nodes at a given level in the queue.

## Related LeetCode Problems

* [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
* [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
* [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree) (iterative solution)
* [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
* [207. Course Schedule](./0207-course-schedule) (Topological Sort using BFS)
