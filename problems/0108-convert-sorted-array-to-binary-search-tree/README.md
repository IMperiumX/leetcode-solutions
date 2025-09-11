**Step 1: Problem Identification**

*   **Prompt 1:** The problem describes converting a sorted array into a height-balanced Binary Search Tree (BST). This corresponds to LeetCode problem 108, "Convert Sorted Array to Binary Search Tree," which is classified as Easy.

    *   **Output:** Problem Number: 108, Problem Name: Convert Sorted Array to Binary Search Tree, Difficulty: Easy

**Step 2: Problem File Creation**

*   Create a directory named `0108-convert-sorted-array-to-binary-search-tree`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:** Since no solution was provided, I will generate a Python solution. The most efficient and common approach is to use recursion, selecting the middle element of the array as the root for each subtree.

*File: 0108-convert-sorted-array-to-binary-search-tree/solution.py*

```python
# 108. Convert Sorted Array to Binary Search Tree - Recursive Approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    Converts a sorted array to a height-balanced binary search tree.

    Args:
        nums: The sorted array.

    Returns:
        The root of the height-balanced BST.
    """
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root
```

**Step 4: Create Related Topic Files**

*File: 0108-convert-sorted-array-to-binary-search-tree/Trees.md*
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
*    **Construction:** Creating a tree from a given data structure, like an array.

## Related LeetCode Problems
* [108. Convert Sorted Array to Binary Search Tree](./0108-convert-sorted-array-to-binary-search-tree)
*   [100. Same Tree](https://leetcode.com/problems/same-tree/)
*   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
*   [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

```

*File: 0108-convert-sorted-array-to-binary-search-tree/Binary_Search_Trees.md*
```markdown
# Binary Search Trees (BSTs)

A Binary Search Tree (BST) is a specialized type of binary tree that has the following properties:

1.  **Binary Tree Property:** Each node has at most two children (referred to as the left child and the right child).
2.  **BST Property (Ordering Property):**
    *   For every node in the tree, the value of all nodes in its left subtree are less than the node's value.
    *   For every node in the tree, the value of all nodes in its right subtree are greater than the node's value.
    *   (Some definitions allow duplicate values, often placing them in either the left or right subtree consistently.)

## Key Concepts

*   **Ordered Data:** BSTs maintain an ordered structure, enabling efficient searching, insertion, and deletion operations.
*   **Recursive Structure:** The BST property applies recursively to all subtrees within the tree.

## Advantages of BSTs

*   **Efficient Search:**  On average, searching for a value in a balanced BST takes O(log n) time, where n is the number of nodes. This is significantly faster than searching in an unsorted array (O(n)).
*   **Efficient Insertion and Deletion:**  Similar to searching, insertion and deletion in a balanced BST take O(log n) time on average.
*   **Ordered Traversal:**  An inorder traversal of a BST visits the nodes in sorted order.

## Disadvantages of BSTs

*   **Worst-Case Performance:** If a BST becomes unbalanced (e.g., by inserting elements in sorted order), it can degenerate into a linked list, resulting in O(n) time complexity for search, insertion, and deletion.
*   **Requires Ordered Data:** BSTs are only suitable for data that can be ordered.

## Common BST Operations

*   **search(value):**  Finds a node with a specific value.
*   **insert(value):** Adds a new node with the given value, maintaining the BST property.
*   **delete(value):** Removes the node with the given value, maintaining the BST property.
*   **findMin():** Returns the node with the smallest value (leftmost node).
*   **findMax():** Returns the node with the largest value (rightmost node).
*   **inorderTraversal():** Visits the nodes in sorted order (left subtree, root, right subtree).
*   **preorderTraversal():** Visits the nodes in root, left subtree, right subtree order.
*   **postorderTraversal():** Visits the nodes in left subtree, right subtree, root order.

## Balanced BSTs

To avoid the worst-case O(n) performance, various self-balancing BST algorithms have been developed, including:

*   **AVL Trees:**  Maintain balance by ensuring that for every node, the height difference between its left and right subtrees is at most 1.
*   **Red-Black Trees:** Use "color" properties (red and black) for nodes to ensure that the tree remains approximately balanced.
*   **B-Trees:**  A generalization of BSTs where each node can have more than two children (often used in databases and file systems).

## Related LeetCode Problems
* [108. Convert Sorted Array to Binary Search Tree](./0108-convert-sorted-array-to-binary-search-tree)
*    [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
*   [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
*   [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
*   [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

```

*File: 0108-convert-sorted-array-to-binary-search-tree/Recursion.md*

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

* [108. Convert Sorted Array to Binary Search Tree](./0108-convert-sorted-array-to-binary-search-tree)
*   [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
*   [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
*    [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)
*    [100. Same Tree](https://leetcode.com/problems/same-tree)
*    [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (can be solved recursively with memoization)

```

**Step 5: Problem README Generation**

*File: 0108-convert-sorted-array-to-binary-search-tree/README.md*

```markdown
# 108. Convert Sorted Array to Binary Search Tree, Difficulty: Easy

## Problem Description

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

## Approach(es)

### Recursive Approach (Divide and Conquer)

Algorithm:

1.  **Base Case:** If the input array `nums` is empty, return `None` (representing an empty subtree).
2.  **Find the Middle Element:** Find the middle index of the array: `mid = len(nums) // 2`.  The element at this index will be the root of the current subtree.
3.  **Create the Root Node:** Create a new `TreeNode` with the value `nums[mid]`.
4.  **Recursive Calls:**
    *   Recursively build the left subtree using the elements before the middle element: `root.left = sortedArrayToBST(nums[:mid])`.
    *   Recursively build the right subtree using the elements after the middle element: `root.right = sortedArrayToBST(nums[mid+1:])`.
5.  **Return the Root:** Return the newly created `root` node.

Data Structures:

*   Uses the implicit call stack for recursion.
*   The binary search tree itself.

Time Complexity:

*   O(n), where n is the length of the input array. We visit each element of the array once to create a corresponding node in the BST.

Space Complexity:

*   O(log n) on average for a balanced tree, representing the height of the tree and the depth of the recursive calls.
*    O(n) in the worst case (although this is very unlikely given how we are constructing it)

Trade-offs:

*   This recursive approach is very efficient and directly implements the divide-and-conquer strategy.  By choosing the middle element as the root, we ensure that the resulting BST is height-balanced.

## Code

[Recursive Approach](./solution.py)

## Notes

This problem is a classic example of how to build a balanced BST from sorted data.  The key idea is to recursively select the middle element as the root, which naturally leads to a balanced structure.  This guarantees O(log n) height and efficient search, insertion, and deletion operations in the resulting BST.
```
Final file structure:
```
0108-convert-sorted-array-to-binary-search-tree/
├── solution.py
├── README.md
├── Binary_Search_Trees.md
├── Recursion.md
└── Trees.md

```
