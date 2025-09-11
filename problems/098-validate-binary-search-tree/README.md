**Step 1: Problem Identification**

*   **Prompt 1:** The problem is clearly "Validate Binary Search Tree," LeetCode problem 98.
*   **Output:** "Problem Number: 98, Problem Name: Validate Binary Search Tree, Difficulty: Medium"

**Step 2: Problem File Creation**

*   Create a directory named `098-validate-binary-search-tree`.

**Step 3: Solution File Generation**

*   **Prompt 3.2 (No provided solution):** We'll generate Python solutions. The most common and efficient approach is to use an inorder traversal with bounds checking, or alternatively, a recursive approach with explicit lower and upper bounds.

*   **`098-validate-binary-search-tree/solution_inorder.py`:**

```python
# 98. Validate Binary Search Tree - Inorder Traversal with Implicit Bounds

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = float('-inf')  # Initialize previous value to negative infinity

        def inorder(node):
            nonlocal prev
            if not node:
                return True

            if not inorder(node.left):
                return False

            if node.val <= prev:
                return False
            prev = node.val

            return inorder(node.right)

        return inorder(root)
```

*   **`098-validate-binary-search-tree/solution_recursive.py`:**

```python
# 98. Validate Binary Search Tree - Recursive Approach with Explicit Bounds

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))
```

* **`098-validate-binary-search-tree/Tree.md`:**

```markdown
# Trees

Trees are hierarchical data structures that consist of nodes connected by edges. They are widely used in computer science to represent relationships between data elements.  Unlike linear data structures (like arrays, linked lists, stacks, and queues), trees organize data in a non-linear fashion.

## Basic Tree Terminology

*   **Node:**  A fundamental unit of a tree, containing data and links to other nodes.
*   **Root:** The topmost node in a tree.  There is only one root node.
*   **Parent:** A node that has a direct connection to another node (its child).
*   **Child:** A node that is directly connected to another node (its parent).
*   **Leaf:** A node with no children.
*   **Edge:** A connection between two nodes.
*   **Depth (of a node):** The length of the path (number of edges) from the root to that node.
*   **Height (of a tree):** The maximum depth of any node in the tree (length of the longest path from the root to a leaf).
*   **Subtree:** A tree formed by a node and all its descendants.
* **Sibling:** Nodes with the same parent.

## Types of Trees

There are many different types of trees, each with specific properties and use cases. Some common ones include:

*   **Binary Tree:**  Each node has at most two children (referred to as the left child and the right child).
*   **Binary Search Tree (BST):**  A binary tree with the property that for each node:
    *   All values in the left subtree are less than the node's value.
    *   All values in the right subtree are greater than the node's value.
*   **AVL Tree:**  A self-balancing BST where the heights of the left and right subtrees of any node differ by at most 1. This ensures that the tree remains balanced, preventing worst-case scenarios for operations.
*   **Red-Black Tree:** Another type of self-balancing BST, using "color" properties (red or black) for nodes to maintain balance.
*   **Trie (Prefix Tree):**  A tree used to store a dynamic set or associative array where the keys are usually strings.
*   **Heap:**  A specialized tree-based data structure that satisfies the heap property (either min-heap or max-heap).

## Binary Tree Traversals

Traversals are methods for visiting all nodes in a tree in a specific order.  Common traversal methods for binary trees include:

*   **Inorder Traversal:**  Visit left subtree, then the current node, then the right subtree.  For a BST, this visits the nodes in sorted order.
*   **Preorder Traversal:** Visit the current node, then the left subtree, then the right subtree.
*   **Postorder Traversal:** Visit the left subtree, then the right subtree, then the current node.
*   **Level Order Traversal (Breadth-First Search):** Visit nodes level by level, from left to right.

## Advantages of Trees

*   **Hierarchical Representation:**  Naturally represent hierarchical relationships.
*   **Efficient Searching (for balanced trees):**  BSTs, AVL trees, and Red-Black trees provide efficient search, insertion, and deletion operations (O(log n) on average).
*   **Flexibility:**  Can be used to implement various other data structures and algorithms.

## Disadvantages of Trees

*   **Unbalanced Trees:**  If a tree becomes unbalanced, operations can degrade to O(n) complexity (similar to a linked list).
*   **Implementation Complexity:**  Some tree types (like self-balancing trees) can be more complex to implement than simpler data structures.

## Use Cases

*   **File Systems:** Representing directories and files.
*   **Databases:**  Indexing and organizing data.
*   **Compilers:**  Syntax trees.
*   **Expression Evaluation:**  Representing mathematical expressions.
*   **Network Routing:**  Finding optimal paths in a network.
*   **Decision Trees (Machine Learning):** Representing decision-making processes.
* **Game AI:**

## Related LeetCode Problems
*    [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
*    [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*    [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
*    [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)
*    [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
*    [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
*    [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
*    [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree)
```

**Step 4: Problem README Generation**

*   **Prompt 4:** Generate the `README.md`.

```markdown
# 98. Validate Binary Search Tree, Difficulty: Medium

## Problem Description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

*   The left subtree of a node contains only nodes with keys **less than** the node's key.
*   The right subtree of a node contains only nodes with keys **greater than** the node's key.
*   Both the left and right subtrees must also be binary search trees.

**Example 1:**

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 10^4]`.
*   `-2^31 <= Node.val <= 2^31 - 1`

## Approach(es)

### Inorder Traversal (with Implicit Bounds)

Algorithm:

1.  **Inorder Traversal:** Perform an inorder traversal of the binary tree.  In a valid BST, an inorder traversal will visit the nodes in ascending order.
2.  **Previous Value:** Keep track of the value of the previously visited node (`prev`). Initialize `prev` to negative infinity.
3.  **Check During Traversal:**  During the inorder traversal:
    *   If the current node's value is less than or equal to `prev`, the tree is not a valid BST. Return `False`.
    *   Otherwise, update `prev` to the current node's value.
4.  **Return:** If the entire traversal completes without finding any violations, return `True`.

Data Structures:

*   Recursion (implicit stack).

Time Complexity:

*   O(n), where n is the number of nodes in the tree.  We visit each node once.

Space Complexity:

*   O(h) in the average case (balanced tree) and O(n) in worst case (skewed tree) for recursion, where h is the height of the tree, which is proportional to the call stack depth during the recursive traversal.

Trade-offs:

*   This approach is concise and leverages the property of inorder traversal for BSTs.

### Recursive Approach (with Explicit Bounds)

Algorithm:

1.  **Helper Function:** Create a recursive helper function `validate(node, low, high)` that takes a node and the lower and upper bounds for the node's value.
2.  **Base Case:** If the `node` is `None`, return `True` (empty subtree is valid).
3.  **Check Bounds:** If the current node's value is not within the `low` and `high` bounds (exclusive), return `False`.
4.  **Recursive Calls:** Recursively call `validate` for the left subtree, updating the upper bound to the current node's value, and for the right subtree, updating the lower bound to the current node's value.
5.  **Return:** Return the result of the logical AND of the recursive calls for the left and right subtrees.
6.  **Initial Call:** Call the `validate` function initially with the `root`, negative infinity as the lower bound, and positive infinity as the upper bound.

Data Structures:

* Recursion.

Time Complexity:

*   O(n), where n is the number of nodes in the tree. We visit each node once.

Space Complexity:

* O(h) in average case where h is the height of the tree.

Trade-offs:

* This approach explicitly checks the bounds at each node, making the logic very clear.
* It avoids the use of a global variable (like `prev` in the inorder approach), which can sometimes be considered cleaner.

## Code

[Inorder Traversal with Implicit Bounds](./solution_inorder.py)

[Recursive Approach with Explicit Bounds](./solution_recursive.py)

## Notes (Optional)

*   The key to solving this problem is understanding the definition of a BST and applying it recursively or iteratively.
*   Both approaches are efficient, with O(n) time complexity.  The choice between them often comes down to personal preference or coding style. The inorder traversal approach can be slightly more concise, while the explicit bounds approach can be clearer.

```

This completes the repository, including two different solutions, detailed explanations, a relevant topic file, and a comprehensive `README.md`. All requirements are addressed effectively.
