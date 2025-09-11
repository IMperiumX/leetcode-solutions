Okay, let's process this according to the defined steps.

**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem from the following input: `[User Input]`."
    The user input is:

    ```
    Given a binary tree, determine if it is
    height-balanced
    .

    Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: true
    Example 2:

    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false
    Example 3:

    Input: root = []
    Output: true

    Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
    ```

    From the problem description ("Given a binary tree, determine if it is height-balanced"), this is the "Balanced Binary Tree" problem on LeetCode.  Searching on LeetCode, this corresponds to problem number 110, and it's an Easy problem.

    *   **Output:** Problem Number: 110, Problem Name: Balanced Binary Tree, Difficulty: Easy

**Step 2: Problem File Creation**

*   Create a directory named `0110-balanced-binary-tree`.

**Step 3: Solution File Generation**

*   **Prompt 3.2** (No user-provided solution): "Generate solutions in Python...". I will generate a recursive solution, which is the most common approach for this problem.

*File: 0110-balanced-binary-tree/solution.py*

```python
# 110. Balanced Binary Tree - Recursive Approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    """
    Determines if a binary tree is height-balanced.

    Args:
        root: The root of the binary tree.

    Returns:
        True if the tree is height-balanced, False otherwise.
    """

    def height(node):
        """
        Calculates the height of a subtree.  Returns -1 for imbalanced subtrees.
        """
        if not node:
            return 0
        left_height = height(node.left)
        if left_height == -1:
            return -1
        right_height = height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return height(root) != -1
```
**Step 4: Create Topic Files**

*File: 0110-balanced-binary-tree/Trees.md*

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

## Related LeetCode Problems

*   [110. Balanced Binary Tree](./0110-balanced-binary-tree)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
*    [100. Same Tree](https://leetcode.com/problems/same-tree/)

```
*File: 0110-balanced-binary-tree/Recursion.md*

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

*   [110. Balanced Binary Tree](./0110-balanced-binary-tree)
*   [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
*   [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (can be solved recursively with memoization)

```

**Step 5: Problem README Generation**

*   **Prompt 4:** "Generate a `README.md` file...".

*File: 0110-balanced-binary-tree/README.md*

```markdown
# 110. Balanced Binary Tree, Difficulty: Easy

## Problem Description

Given a binary tree, determine if it is
height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

## Approach(es)

### Recursive Approach

Algorithm:

1.  Define a helper function `height(node)` that calculates the height of a subtree.
2.  If the `node` is `None`, return 0 (base case for an empty subtree).
3.  Recursively calculate the height of the left subtree: `left_height = height(node.left)`.
4.  If `left_height` is -1 (indicating the left subtree is unbalanced), return -1.
5.  Recursively calculate the height of the right subtree: `right_height = height(node.right)`.
6.  If `right_height` is -1 (indicating the right subtree is unbalanced), return -1.
7.  If the absolute difference between `left_height` and `right_height` is greater than 1, return -1 (indicating the current subtree is unbalanced).
8.  Otherwise, return 1 plus the maximum of `left_height` and `right_height` (the height of the current subtree).
9. The main function `isBalanced(root)` returns true if the result from height function is not equal -1.

Data Structures:

*   Uses the implicit call stack for recursion.  No other explicit data structures are used.

Time Complexity:

*   O(n), where n is the number of nodes in the tree. In the worst case, we visit each node once.

Space Complexity:

*   O(h) in the average case (for a balanced tree), where h is the height of the tree.  This is due to the recursive call stack.
*   O(n) in the worst case (for a skewed tree), where the height of the tree is equal to the number of nodes.

Trade-offs:

*   This recursive approach is concise and easy to understand. It efficiently checks for balance while calculating heights.

## Code

[Recursive Approach](./solution.py)

## Notes

This problem highlights the importance of understanding tree properties and recursion. The key idea is to efficiently combine height calculation with balance checking in a single recursive traversal.
```

The resulting directory structure is:

```
0110-balanced-binary-tree/
├── solution.py
├── README.md
├── Recursion.md
└── Trees.md
```
