**Step 1: Problem Identification**

*   **Prompt 1:** The input clearly describes the "Same Tree" problem, where we compare two binary trees for structural and value equality. This is LeetCode problem 100, an Easy problem.

    *   **Output:** Problem Number: 100, Problem Name: Same Tree, Difficulty: Easy

**Step 2: Problem File Creation**

*   Create a directory named `0100-same-tree`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:** I'll generate a Python solution using recursion, which is the most natural approach for this problem.

*File: 0100-same-tree/solution.py*

```python
# 100. Same Tree - Recursive Approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    """
    Checks if two binary trees are the same (structurally identical with same node values).

    Args:
        p: The root of the first binary tree.
        q: The root of the second binary tree.

    Returns:
        True if the trees are the same, False otherwise.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```
**Step 4: Create Related Topics**
*File: 0100-same-tree/Recursion.md*

```markdown
# Recursion

Recursion is a powerful programming technique where a function calls itself within its own definition. It's a fundamental concept in computer science, often used to solve problems that can be broken down into smaller, self-similar subproblems.

## Key Concepts

*   **Base Case:** A condition that stops the recursion. Without a base case, the function would call itself infinitely, leading to a stack overflow error.
*   **Recursive Step:** The part of the function where it calls itself with a modified input, moving towards the base case.

## How Recursion Works

1.  **Function Call:** When a recursive function is called, a new frame is added to the call stack. This frame stores the function's local variables and parameters for that particular invocation.
2.  **Recursive Calls:** The function calls itself repeatedly, with each call creating a new stack frame.
3.  **Base Case Reached:** When the base case is met, the function returns a value without making further recursive calls.
4.  **Unwinding the Stack:** As each recursive call returns, its corresponding stack frame is removed from the call stack, and the execution flow returns to the previous call.  Values are returned up the stack until the initial call is reached.

## Advantages of Recursion

*   **Elegance and Readability:** Recursive solutions can be more concise and easier to understand for problems with a naturally recursive structure (e.g., tree traversals, factorials).
*   **Problem Decomposition:** Recursion naturally breaks down complex problems into smaller, more manageable subproblems.

## Disadvantages of Recursion

*   **Stack Overflow:** Excessive recursion can lead to a stack overflow error if the call stack becomes too large.
*   **Performance Overhead:** Function calls have overhead, so recursive solutions can sometimes be slower than iterative solutions, especially for deep recursion.
*   **Debugging:** Debugging recursive functions can be more challenging than debugging iterative code.

## Common Recursive Patterns

*   **Divide and Conquer:** Breaking a problem into smaller subproblems, solving them recursively, and combining the results (e.g., merge sort, quicksort).
*   **Tree Traversal:** Visiting all nodes in a tree using inorder, preorder, or postorder traversal.
*   **Backtracking:** Exploring all possible solutions by trying out different choices and undoing them if they don't lead to a solution (e.g., solving Sudoku, N-Queens problem).
*   **Dynamic Programming (with Memoization):** Storing the results of expensive function calls and reusing them for the same inputs, often used in recursive solutions to improve performance.

## Related LeetCode Problems
*   [100. Same Tree](./0100-same-tree)
*   [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
*   [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
*    [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)
*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (can be solved recursively with memoization)

```
*File: 0100-same-tree/Trees.md*

```markdown
# Trees

Trees are a fundamental non-linear data structure in computer science. They consist of nodes connected by edges, forming a hierarchical structure. Unlike linear data structures like arrays or linked lists, trees can represent relationships between data elements in a more complex and intuitive way.

## Key Concepts

*   **Node:** The basic building block of a tree. Each node contains data and may have links (pointers) to other nodes.
*   **Root:** The topmost node in a tree.  It is the only node without a parent.
*   **Parent:** A node that has one or more child nodes.
*   **Child:** A node that is connected to a parent node.
*   **Leaf:** A node with no children.
*   **Edge:** A connection between two nodes.
*   **Depth (of a node):** The number of edges from the root to the node.
*   **Height (of a node):** The number of edges on the longest path from the node to a leaf.  The height of a tree is the height of its root.
*   **Subtree:** A tree consisting of a node and all its descendants.

## Types of Trees

*   **Binary Tree:** Each node has at most two children (left and right). This is a very common type of tree.
*   **Binary Search Tree (BST):** A binary tree with the property that for each node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value. This allows for efficient searching, insertion, and deletion.
*   **Balanced Tree:** A tree where the heights of the left and right subtrees of any node differ by at most 1 (e.g., AVL trees, Red-Black trees).  Balanced trees help prevent worst-case scenarios for operations like searching in BSTs.
*   **N-ary Tree:** Each node can have up to N children.
*   **Trie (Prefix Tree):**  A specialized tree used for storing strings, where each node represents a character and paths from the root to a node represent prefixes.

## Common Tree Traversals

*   **Inorder Traversal (for Binary Trees):** Visit the left subtree, then the current node, then the right subtree.  For BSTs, this visits nodes in sorted order.
*   **Preorder Traversal:** Visit the current node, then the left subtree, then the right subtree.
*   **Postorder Traversal:** Visit the left subtree, then the right subtree, then the current node.
*   **Level Order Traversal (Breadth-First Search):** Visit nodes level by level, from top to bottom and left to right.

## Common Tree Operations

*   **Insertion:** Adding a new node to the tree.
*   **Deletion:** Removing a node from the tree.
*   **Search:** Finding a node with a specific value.
*   **Traversal:** Visiting all nodes in a specific order.
*    **Checking for properties:** Determining if the tree satisfies certain conditions, such as being balanced or being a valid BST.

## Related LeetCode Problems

*   [100. Same Tree](./0100-same-tree)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
*   [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

```

**Step 5: Problem README Generation**

*File: 0100-same-tree/README.md*

```markdown
# 100. Same Tree, Difficulty: Easy

## Problem Description

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

## Approach(es)

### Recursive Approach

Algorithm:

1.  **Base Cases:**
    *   If both `p` and `q` are `None`, they are the same (empty trees), so return `True`.
    *   If only one of `p` or `q` is `None`, they are different, so return `False`.
2.  **Check Current Node:**
    *   If `p.val` is not equal to `q.val`, the trees are different, so return `False`.
3.  **Recursive Calls:**
    *   Recursively check if the left subtrees are the same: `isSameTree(p.left, q.left)`.
    *   Recursively check if the right subtrees are the same: `isSameTree(p.right, q.right)`.
4.  **Combine Results:**
    *   Return `True` if and only if both the left and right subtrees are the same (using the `and` operator).

Data Structures:

*   Uses the implicit call stack for recursion.

Time Complexity:

*   O(n), where n is the minimum number of nodes in the two trees. We visit each node in the smaller tree at most once.

Space Complexity:

*   O(h) in the average case (for a balanced tree), where h is the height of the tree. This is due to the recursive call stack.
*   O(n) in the worst case (for a skewed tree), where the height of the tree is equal to the number of nodes.

Trade-offs:

*   This recursive approach is concise, readable, and directly reflects the problem's structure. It's the most common and natural way to solve this problem.

## Code

[Recursive Approach](./solution.py)

## Notes

This problem is a fundamental example of tree traversal and recursion.  It's a good building block for understanding more complex tree problems. The key is to handle the base cases correctly and to make sure both the structure and the node values are compared.

```
Final File Structure:
```
0100-same-tree/
├── solution.py
├── README.md
├── Recursion.md
└── Trees.md
```
