# 226. Invert Binary Tree, Difficulty: Easy

## Problem Description

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

Input: `root = [4,2,7,1,3,6,9]`
Output: `[4,7,2,9,6,3,1]`

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

Input: `root = [2,1,3]`
Output: `[2,3,1]`

Example 3:

Input: `root = []`
Output: `[]`

Constraints:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Approach(es)

### Recursive Approach

Algorithm:

1. **Base Case:** If the current node `root` is `None`, return `None`.
2. **Recursive Step:**
    - Swap the left and right children of the current node: `root.left, root.right = root.right, root.left`.
    - Recursively invert the left subtree: `invertTree(root.left)`.
    - Recursively invert the right subtree: `invertTree(root.right)`.
3. Return the current node `root`.

Data Structures:

- Implicit call stack used during recursion.

Time Complexity:

- O(n), where n is the number of nodes in the tree. Each node is visited once.

Space Complexity:

- O(h) in the worst case (skewed tree), where h is the height of the tree. This is due to the recursive call stack.
- O(log n) in the average case (balanced tree).

Trade-offs:

- Simple and concise implementation.
- Space complexity can be O(n) in the worst case for highly unbalanced trees.

### Iterative Approach (BFS)

Algorithm:

1. If the root is `None`, return `None`.
2. Initialize a queue `queue` with the root node.
3. While the queue is not empty:
    - Dequeue a node `node` from the queue.
    - Swap the left and right children of the `node`.
    - If the left child is not `None`, enqueue the left child.
    - If the right child is not `None`, enqueue the right child.
4. Return the `root`.

Data Structures:

- Queue to store nodes at each level.

Time Complexity:

- O(n), where n is the number of nodes in the tree. Each node is visited and enqueued/dequeued once.

Space Complexity:

- O(w), where w is the maximum width of the tree (maximum number of nodes at any level). In the worst case (complete binary tree), w can be up to n/2, so the space complexity can be O(n).

Trade-offs:

- Avoids function call overhead associated with recursion.
- Space complexity can be O(n) in the worst case for wide trees.

## Code

[Recursive Approach](./solution_recursive.py)

[Iterative Approach](./solution_iterative.py)

## Notes

- The recursive approach is generally more intuitive and easier to read for this problem.
- The iterative approach using BFS might be preferred if you are concerned about stack overflow issues for very deep trees (although this is unlikely given the constraints of this problem).
- Both approaches have the same time complexity, but the iterative approach might have slightly higher space complexity in the worst case for wide trees.
- This problem is a classic example of tree traversal and manipulation.
