Okay, let's generate the LeetCode solution repository for "Kth Smallest Element in a BST" (Problem 230).

**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem from the following input: `230. Kth Smallest Element in a BST ... [problem description]`."
*   **Output:** "Problem Number: 230, Problem Name: Kth Smallest Element in a BST, Difficulty: Medium"

**Step 2: Problem File Creation**

*   Create a directory named `0230-kth-smallest-element-in-a-bst`.

**Step 3: Solution File Generation**

We will generate two primary solutions: one using in-order traversal (iterative) and another using in-order traversal (recursive). We'll also address the follow-up question in the README.

* **Prompt 3.2:** "Generate solutions in Python for the LeetCode problem: `Kth Smallest Element in a BST` (Number: `230`). ... Create files named `solution_iterative.py`, and `solution_recursive.py`."
* We will need a TreeNode Class to define the tree.

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
*   Create `solution_iterative.py`:

```python
# 230. Kth Smallest Element in a BST - Iterative In-Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest_iterative(root, k):
    """
    Finds the kth smallest element in a BST using iterative in-order traversal.

    Args:
        root: The root of the BST.
        k: The kth smallest element to find (1-indexed).

    Returns:
        The value of the kth smallest element.
    """
    stack = []
    node = root
    count = 0

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        count += 1
        if count == k:
            return node.val

        node = node.right
```

*   Create `solution_recursive.py`:

```python
# 230. Kth Smallest Element in a BST - Recursive In-Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest_recursive(root, k):
    """
    Finds the kth smallest element in a BST using recursive in-order traversal.

    Args:
        root: The root of the BST.
        k: The kth smallest element to find (1-indexed).

    Returns:
        The value of the kth smallest element.
    """
    result = None
    count = 0

    def inorder(node):
        nonlocal result, count  # Use nonlocal to modify variables in the outer scope.
        if not node or result is not None:
            return

        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return  # Stop traversal once the kth element is found.
        inorder(node.right)

    inorder(root)
    return result

```

**Step 4: Problem README Generation**

*   **Prompt 4:** "Generate a `README.md` file for the problem: `Kth Smallest Element in a BST` (Number: `230`, Difficulty: `Medium`)."

```markdown
# 230. Kth Smallest Element in a BST, Difficulty: Medium

## Problem Description

Given the root of a binary search tree, and an integer k, return the *k*th smallest value (**1-indexed**) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

*   The number of nodes in the tree is n.
*   1 <= k <= n <= 10<sup>4</sup>
*   0 <= Node.val <= 10<sup>4</sup>

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Approach(es)

### In-Order Traversal (Iterative)

Algorithm:

1.  **Initialize:** Create an empty stack `stack` and set the current `node` to the `root`.
2.  **Iterate:** While `node` is not None or the `stack` is not empty:
    *   **Traverse Left:** While `node` is not None:
        *   Push `node` onto the `stack`.
        *   Move `node` to its left child (`node = node.left`).
    *   **Process Node:** Pop the top node from the `stack`.
    *   **Increment Count:** Increment a `count` variable.
    *   **Check kth Element:** If `count` equals `k`, return the value of the popped node.
    *   **Traverse Right:** Set `node` to the right child of the popped node (`node = node.right`).

Data Structures:

*   A stack to simulate the in-order traversal.

Time Complexity:

*   O(H + k), where H is the height of the tree.  In the worst case (skewed tree), H can be equal to n (number of nodes).  We visit at most H nodes to reach the leftmost node, and then visit k nodes. On average for balanced tree: O(log n + k)

Space Complexity:

*   O(H) - The maximum size of the stack is proportional to the height of the tree. In the worst case (skewed tree), this can be O(n). In a balanced BST, it would be O(log n).

Trade-offs:

*   This approach avoids recursion, which can be beneficial for very deep trees (to prevent stack overflow).  The space complexity is still dependent on the tree's height.

### In-Order Traversal (Recursive)

Algorithm:

1.  **Initialize:** Use `result` (initialized to None) and `count` (initialized to 0) to store the result and keep track of visited nodes.
2.  **Recursive Function (`inorder`):**
    *   **Base Case:** If the current `node` is None or the `result` is already found, return.
    *   **Left Subtree:** Recursively call `inorder` on the left subtree (`node.left`).
    *   **Process Node:** Increment `count`. If `count` equals `k`, set `result` to the current node's value and return (to stop further traversal).
    *   **Right Subtree:** Recursively call `inorder` on the right subtree (`node.right`).
3. Call inorder function with root node
4. return the result

Data Structures:

*   No explicit extra data structures are used, but the call stack implicitly stores the state of the recursive calls.

Time Complexity:

*   O(H + k), similar to the iterative approach. In the worst case O(n) and in best case O(log n + k)

Space Complexity:

*   O(H) - The maximum depth of the recursion is proportional to the height of the tree, due to the call stack. Worst case O(n), average case O(log n) for balanced BST.

Trade-offs:

*   This approach is often more concise and easier to read than the iterative approach for tree traversals.  However, it uses the call stack, which can lead to stack overflow for very deep trees.

## Follow-up: Optimization for Frequent Modifications

If the BST is modified frequently and we need to find the kth smallest element often, we can augment each node in the BST with an additional field, `left_size`, which stores the number of nodes in its left subtree.

**Modified Node Structure:**

```python
class AugmentedTreeNode:
    def __init__(self, val=0, left=None, right=None, left_size=0):
        self.val = val
        self.left = left
        self.right = right
        self.left_size = left_size
```
**Algorithm:**

1. **Insert/Delete:** Whenever we insert or delete a node, we need to update the `left_size` of all affected ancestor nodes. This takes O(H) time, where H is the height of the tree.

2.  **Find kth Smallest:**
    *   Start at the root.
    *   If `k == node.left_size + 1`, the current node is the kth smallest.
    *   If `k <= node.left_size`, recursively search for the kth smallest in the left subtree.
    *   If `k > node.left_size + 1`, recursively search for the `(k - node.left_size - 1)`th smallest element in the right subtree.

**Time Complexity (Find kth Smallest):**

*   O(H).  With a balanced BST (e.g., AVL tree, Red-Black tree), H is O(log n), so finding the kth smallest element takes O(log n) time.

**Space Complexity:**

*   O(1) extra space for the search (excluding the augmented tree itself).

**Trade-offs:**
* **Insert/Delete become O(H)** instead of constant time.
* **Finding the kth smallest element significantly improved to O(H) (O(log n) for balanced BST)**.
* **Space:** We're using O(n) extra space in total to store the counts, but we are *not* using any additional space *per operation*.

This augmentation makes finding the kth smallest element much more efficient when frequent modifications are involved.  Maintaining a balanced BST (e.g., using AVL trees or Red-Black trees) is crucial for achieving O(log n) performance for all operations.

## Code

[In-Order Traversal (Iterative)](./solution_iterative.py)

[In-Order Traversal (Recursive)](./solution_recursive.py)

## Notes

Key topics associated with question:
* Tree
* Binary Search Tree
* Binary Tree
* Depth-First Search
* Stack
```
**Step 5: Related Topics:**

* Create `Tree.md`, `Binary Search Tree.md`, `Binary Tree.md`, `Depth-First Search.md`, `Stack.md`

```
# Tree

A tree is a hierarchical data structure that consists of nodes connected by edges. It is a non-linear data structure, unlike arrays, linked lists, stacks, and queues. Trees are widely used to represent hierarchical relationships, such as file systems, organizational structures, and decision trees.

## Key Concepts

*   **Node:**  A fundamental unit of a tree, containing data and links to other nodes.
*   **Root:** The topmost node in the tree.  There is only one root node.
*   **Parent:** A node that has a direct connection (edge) to another node (its child).
*   **Child:** A node that is directly connected to another node (its parent).
*   **Leaf (External Node):** A node that has no children.
*   **Internal Node:** A node that has at least one child.
*   **Edge:** A connection between two nodes.
*   **Path:** A sequence of nodes and edges connecting a node to a descendant.
*   **Depth of a Node:** The length of the path from the root to that node.
*   **Height of a Node:** The length of the longest path from that node to a leaf.
*   **Height of a Tree:** The height of the root node.
*   **Level:** All nodes at a given depth.
*   **Subtree:** A tree formed by a node and all its descendants.
*   **Ancestor:** A node reachable by repeatedly proceeding from child to parent.
*   **Descendant:** A node reachable by repeatedly proceeding from parent to child.

## Types of Trees

*   **Binary Tree:** Each node has at most two children (left child and right child).
*   **Binary Search Tree (BST):** A binary tree with the property that for each node, all values in its left subtree are less than its value, and all values in its right subtree are greater than its value.
*   **AVL Tree:** A self-balancing BST where the heights of the two child subtrees of any node differ by at most one.
*   **Red-Black Tree:** A self-balancing BST with more complex balancing rules, ensuring logarithmic time complexity for most operations.
*   **B-Tree:** A self-balancing tree designed for disk-based data structures, optimized for minimizing disk I/O.
*   **Trie (Prefix Tree):** A tree-like structure used to store a dynamic set of strings, where the keys are usually strings.
*   **Heap:** A specialized tree-based data structure that satisfies the heap property (either min-heap or max-heap).
*   **N-ary Tree:**  A tree where each node can have up to N children.

## Common Tree Operations

*   **Traversal:** Visiting all nodes in the tree in a specific order:
    *   **Pre-order:** Root, Left, Right
    *   **In-order:** Left, Root, Right (primarily used for BSTs)
    *   **Post-order:** Left, Right, Root
    *   **Level-order (Breadth-First Search):** Visit nodes level by level.
*   **Search:** Finding a specific node in the tree.
*   **Insertion:** Adding a new node to the tree.
*   **Deletion:** Removing a node from the tree.
*   **Height Calculation:** Finding the height of the tree.
*   **Depth Calculation:**  Finding the depth of a node.

## Use Cases

Trees are used in many applications, including:

*   **File Systems:**  Representing directory structures.
*   **Databases:**  Indexing and organizing data (e.g., B-trees).
*   **Compilers:**  Representing the syntax of programming languages (parse trees).
*   **Decision Trees:**  Machine learning models for classification and regression.
*   **Network Routing:**  Representing network topologies.
*   **HTML/XML Parsing:** Representing the structure of documents.

## Advantages

*   **Hierarchical Representation:**  Naturally represent hierarchical data.
*   **Efficient Search (for balanced trees):**  Binary search trees and self-balancing trees allow for efficient searching (O(log n) for balanced trees).
*   **Dynamic Size:**  Trees can grow and shrink dynamically as needed.

## Disadvantages

*   **Unbalanced Trees:**  If a tree becomes unbalanced, search operations can degrade to O(n) in the worst case.
*   **Complexity:**  Implementing some tree operations (especially deletion and balancing) can be complex.
* Overhead for maintaining balance in self-balancing trees.

## Related LeetCode Problems

* [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
*   [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
*   [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
*   [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
*   [100. Same Tree](https://leetcode.com/problems/same-tree/)
*   [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
*   [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
*   [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
*   [112. Path Sum](https://leetcode.com/problems/path-sum/)

```

```
# Binary Search Tree

A Binary Search Tree (BST) is a specialized type of binary tree that has the following properties:

1.  **Binary Tree Property:** Each node has at most two children (referred to as the left child and the right child).
2.  **BST Property (Ordering Property):**
    *   For every node in the tree:
        *   All values in the node's left subtree are *less than* the node's value.
        *   All values in the node's right subtree are *greater than* the node's value.
    * There are no duplicate nodes.

## Key Concepts

*   **Root:** The topmost node in the tree.
*   **Left Child:** The child node whose value is less than its parent's value.
*   **Right Child:** The child node whose value is greater than its parent's value.
*   **Leaf Node:** A node with no children.
*   **Internal Node:** A node with at least one child.
*   **Subtree:** A tree formed by a node and all its descendants.
* **Balanced BST:** The height of the left and right subtrees of every node never differ by more than 1.

## Common Operations and Time Complexities (for a Balanced BST)

| Operation      | Description                                                  | Time Complexity (Average) | Time Complexity (Worst Case - Skewed Tree) |
|----------------|--------------------------------------------------------------|---------------------------|--------------------------------------------|
| Search         | Find a node with a specific value.                           | O(log n)                  | O(n)                                       |
| Insertion      | Add a new node with a given value.                          | O(log n)                  | O(n)                                       |
| Deletion       | Remove a node with a given value.                           | O(log n)                  | O(n)                                       |
| Find Minimum   | Find the node with the smallest value.                        | O(log n)                  | O(n)                                       |
| Find Maximum   | Find the node with the largest value.                         | O(log n)                  | O(n)                                       |
| In-order Traversal | Visit all nodes in sorted order (ascending).                  | O(n)                      | O(n)                                       |
| Pre-order Traversal| Visit all nodes: root, left, right.                      | O(n)                      | O(n)                                       |
|Post-order Traversal| Visit all nodes: left, right, root                       |      O(n)                 |                O(n)                        |

*   **n:** The number of nodes in the tree.

## Time Complexity Notes

*   **Average Case (Balanced BST):**  The average time complexity for search, insertion, and deletion is O(log n) because the height of a balanced BST is logarithmic with respect to the number of nodes.
*   **Worst Case (Skewed Tree):**  In the worst case, a BST can become skewed (like a linked list), where all nodes are either in the left subtree or the right subtree.  In this case, the height of the tree becomes n, and the time complexity for search, insertion, and deletion degrades to O(n).

## Advantages

*   **Efficient Search:**  Provides efficient searching (O(log n) on average) compared to unsorted arrays or linked lists.
*   **Ordered Data:**  Maintains data in sorted order, making it easy to retrieve elements in ascending or descending order.
*   **Dynamic:**  Can efficiently handle insertions and deletions (compared to sorted arrays).

## Disadvantages

*   **Worst-Case Performance:**  Performance can degrade to O(n) if the tree becomes unbalanced (skewed).
*   **Complexity:**  Implementing deletion can be more complex than in other data structures.

## Self-Balancing BSTs

To avoid the worst-case O(n) performance, self-balancing BSTs are used.  These trees automatically adjust their structure during insertion and deletion to maintain a balanced height (O(log n)).  Common examples include:

*   **AVL Trees:**  The heights of the two child subtrees of any node differ by at most one.
*   **Red-Black Trees:**  Use a more complex set of rules to ensure balance, allowing for slightly more imbalance than AVL trees but with potentially faster insertion/deletion.

## Related LeetCode Problems
* [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
*   [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
*   [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
* [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
*   [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)
*   [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
* [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
```

```
# Binary Tree

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. It is a special case of a tree where the maximum degree of any node is 2.

## Key Concepts

*   **Node:** A fundamental unit of a binary tree, containing data and references to its left and right children (which can be None).
*   **Root:** The topmost node in the tree.
*   **Left Child:** The child node to the left of a parent node.
*   **Right Child:** The child node to the right of a parent node.
*   **Leaf Node (External Node):** A node with no children (both left and right children are None).
*   **Internal Node:** A node with at least one child.
*   **Parent:** A node that has one or two child nodes.
*   **Subtree:** A tree formed by a node and all its descendants.
*   **Depth of a Node:** The length of the path (number of edges) from the root to that node.
*   **Height of a Node:** The length of the longest path from that node to a leaf.
*   **Height of a Tree:** The height of the root node.
*   **Level:** All nodes at a given depth.
*   **Full Binary Tree:** Every node has either 0 or 2 children (no node has exactly 1 child).
*   **Complete Binary Tree:** All levels are completely filled except possibly the last level, which is filled from left to right.
*   **Perfect Binary Tree:** All internal nodes have two children and all leaf nodes are at the same level.
* **Balanced Binary Tree:** The height of left and right subtree of every node differ by no more than 1.

## Common Binary Tree Operations

*   **Traversal:** Visiting all nodes in a specific order:
    *   **Pre-order:** Root, Left, Right
    *   **In-order:** Left, Root, Right
    *   **Post-order:** Left, Right, Root
    *   **Level-order (Breadth-First Search):** Visit nodes level by level.
*   **Search:** Finding a specific node (usually in the context of a Binary Search Tree).
*   **Insertion:** Adding a new node.
*   **Deletion:** Removing a node.
*   **Height Calculation:** Finding the height of the tree.
*   **Depth Calculation:** Finding the depth of a specific node.

## Use Cases

Binary trees (and their variations like Binary Search Trees, AVL Trees, Red-Black Trees) are used in:

*   **Binary Search Trees (BSTs):** Efficient searching, insertion, and deletion (when balanced).
*   **Expression Trees:** Representing mathematical expressions.
*   **Huffman Coding Trees:** Data compression.
*   **Heaps:** Implementing priority queues.
*   **Syntax Trees:**  Compilers and interpreters.
*   **Tries:** Storing and searching for strings.
*   **Decision Trees (in a broader sense):** Machine learning

## Advantages

*   **Hierarchical Structure:**  Naturally represent hierarchical data.
*   **Efficient Operations (especially with balanced BSTs):**  Logarithmic time complexity for many operations in balanced trees.
*   **Flexibility:**  Can be used for a wide variety of applications.

## Disadvantages

*   **Unbalanced Trees:**  If a binary tree becomes unbalanced (e.g., skewed), operations like search, insertion, and deletion can degrade to O(n) time complexity in the worst case.
*   **Complexity:**  Implementing some operations (like deletion in BSTs) can be more complex than in simpler data structures like arrays or linked lists.

## Related LeetCode Problems

* [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
*   [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
*   [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
*   [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
*   [100. Same Tree](https://leetcode.com/problems/same-tree/)
*   [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
*   [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
*   [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
```

```
# Depth-First Search

Depth-First Search (DFS) is a graph traversal algorithm that explores a graph (or tree) by going as deep as possible along each branch before backtracking. It's a fundamental algorithm with many applications.

## Key Concepts

*   **Traversal:**  Visiting all reachable nodes in a graph or tree.
*   **Recursion (or Stack):** DFS is typically implemented using recursion, which implicitly uses the call stack. It can also be implemented iteratively using an explicit stack.
*   **Visited Set:** A set (or other data structure) to keep track of visited nodes to avoid cycles and redundant visits.
*   **Backtracking:**  When a dead end is reached (no unvisited neighbors), the algorithm backtracks to the previous node and explores other branches.

## Algorithm (Recursive Implementation)

```python
def dfs_recursive(graph, node, visited):
    """
    Performs a depth-first search on a graph.

    Args:
        graph: The graph represented as an adjacency list (dictionary).
        node: The starting node.
        visited: A set to keep track of visited nodes.
    """
    if node in visited:
        return

    visited.add(node)
    print(node)  # Process the node (e.g., print it)

    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor, visited)
```
## Algorithm (Iterative using stack)
```python
def dfs_iterative(graph, start_node):
   visited = set()
   stack = [start_node]

   while stack:
      node = stack.pop()
      if node not in visited:
        print(node)
        visited.add(node)

        # Add unvisited neighbors to the stack
        for neighbor in reversed(graph[node]): # Reverse to match the recursive version
            if neighbor not in visited:
               stack.append(neighbor)

```

## Algorithm (Tree Traversal - Pre-order, In-order, Post-order)

For trees, DFS is often used to perform pre-order, in-order, or post-order traversals.  These are special cases of DFS where the order of visiting the node and its children is defined:

*   **Pre-order:**  Visit the root, then the left subtree, then the right subtree.
*   **In-order:**  Visit the left subtree, then the root, then the right subtree (used primarily for binary search trees).
*   **Post-order:** Visit the left subtree, then the right subtree, then the root.

```python
# Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root:
        print(root.val)  # Process root
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)  # Process root
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)  # Process root
```
## Use Cases

DFS is used in a wide range of applications, including:

*   **Tree Traversal:** Pre-order, in-order, post-order traversals.
*   **Graph Traversal:**  Visiting all reachable nodes in a graph.
*   **Cycle Detection:** Determining if a graph contains cycles.
*   **Topological Sorting:** Ordering nodes in a directed acyclic graph (DAG) such that for every directed edge from node A to node B, node A comes before node B in the ordering.
*   **Path Finding:** Finding a path between two nodes in a graph (although not necessarily the shortest path).
*   **Solving Puzzles:**  Many puzzles (e.g., mazes, Sudoku) can be solved using DFS.
*   **Connectivity Check:** Determine whether a graph is connected.
* **Web crawlers:**

## Advantages

*   **Simple Implementation (especially recursive):** DFS is relatively easy to implement, particularly the recursive version.
*   **Memory Efficient (for some applications):**  For tree traversal, the space complexity is proportional to the height of the tree (due to the call stack), which can be logarithmic for balanced trees.
* **Suited for deep exploration:**

## Disadvantages

*   **Not Guaranteed to Find Shortest Path:** DFS does *not* guarantee finding the shortest path between two nodes.  Breadth-First Search (BFS) is used for finding shortest paths.
*   **Stack Overflow (for very deep recursion):**  The recursive implementation can lead to a stack overflow error if the recursion depth is too large.
* **Can get stuck in long path (infinite loop)** if not using visited set.

## Related LeetCode Problems

* [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
*   [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
*   [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
*   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
*   [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
*   [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
* [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
*   [100. Same Tree](https://leetcode.com/problems/same-tree/)
* [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
```

```
# Stack

A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. This means that the last element added to the stack is the first element to be removed.  Think of it like a stack of plates: you can only add or remove plates from the top.

## Key Concepts

*   **LIFO (Last-In, First-Out):** The last element added is the first element removed.
*   **Push:** Adding an element to the top of the stack.
*   **Pop:** Removing the element from the top of the stack.
*   **Peek (or Top):**  Looking at the top element of the stack without removing it.
*   **isEmpty:** Checking if the stack is empty.
*   **isFull:** Checking if the stack is full (relevant for fixed-size stack implementations).
* **Underflow**: Occurs when trying to pop from empty stack.
* **Overflow**: Occurs when trying to push into full stack (fixed size).

## Common Operations and Time Complexities

| Operation | Description                       | Time Complexity |
|-----------|-----------------------------------|-----------------|
| Push      | Add an element to the top         | O(1)            |
| Pop       | Remove the top element            | O(1)            |
| Peek/Top  | View the top element              | O(1)            |
| isEmpty   | Check if the stack is empty      | O(1)            |
| isFull    | Check if the stack is full       | O(1)            |
| Size      | Get the number of elements       | O(1)            |

## Implementations

Stacks can be implemented using:

1.  **Arrays:**
    *   Use a fixed-size array.
    *   Keep track of the index of the