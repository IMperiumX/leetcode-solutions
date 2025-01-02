# 104. Maximum Depth of Binary Tree, Difficulty: Easy

## Problem Description

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

Input: `root = [3,9,20,null,null,15,7]`
Output: `3`

Example 2:

Input: `root = [1,null,2]`
Output: `2`

Constraints:

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Approach(es)

### Recursive Approach

Algorithm:

1. **Base Case:** If the current node is `null`, return 0 (depth of an empty subtree is 0).
2. **Recursive Step:**
    - Recursively calculate the maximum depth of the left subtree: `left_depth = maxDepth(root.left)`.
    - Recursively calculate the maximum depth of the right subtree: `right_depth = maxDepth(root.right)`.
    - Return the maximum of `left_depth` and `right_depth` plus 1 (to account for the current node): `max(left_depth, right_depth) + 1`.

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

### Iterative Breadth-First Search (BFS) Approach

Algorithm:

1. Initialize a queue `q` with the root node and a `level` counter to 0.
2. While the queue is not empty:
    - Increment the `level` counter.
    - Iterate through all nodes at the current level (current size of the queue):
        - Dequeue a node from the queue.
        - If the node has a left child, enqueue the left child.
        - If the node has a right child, enqueue the right child.
3. Return the final `level`.

Data Structures:

- Queue to store nodes at each level.

Time Complexity:

- O(n), where n is the number of nodes in the tree. Each node is visited and enqueued/dequeued once.

Space Complexity:

- O(w), where w is the maximum width of the tree (maximum number of nodes at any level). In the worst case (complete binary tree), w can be up to n/2, so the space complexity can be O(n).

Trade-offs:

- Iterative solution avoids function call overhead.
- Space complexity can be O(n) in the worst case for wide trees.

### Iterative Depth-First Search (DFS) Approach

Algorithm:

1. Initialize a stack `s` with the root node and its depth (1), and a `max_depth` variable to 0.
2. While the stack is not empty:
    - Pop a node and its depth from the stack.
    - Update `max_depth` with the maximum of `max_depth` and the current depth.
    - If the node has a left child, push the left child and its depth (current depth + 1) onto the stack.
    - If the node has a right child, push the right child and its depth (current depth + 1) onto the stack.
3. Return `max_depth`.

Data Structures:

- Stack to store nodes and their depths during traversal.

Time Complexity:

- O(n), where n is the number of nodes in the tree. Each node is visited and pushed/popped from the stack once.

Space Complexity:

- O(h) in the worst case (skewed tree), where h is the height of the tree. This is due to the stack storing nodes along a single path.
- O(log n) in the average case (balanced tree).

Trade-offs:

- Iterative solution avoids function call overhead.
- Space complexity can be O(n) in the worst case for highly unbalanced trees, similar to the recursive approach.

## Code

[Recursive Approach](./solution_recursive.py)

[Iterative BFS Approach](./solution_iterative_bfs.py)

[Iterative DFS Approach](./solution_iterative_dfs.py)

## Notes

- The recursive approach is generally the most straightforward to implement for this problem.
- The iterative BFS approach might be preferred if the tree is very wide and you are concerned about space complexity.
- The iterative DFS approach is similar to the recursive approach in terms of space complexity but avoids function call overhead.
- The choice between iterative BFS and DFS often depends on personal preference or specific constraints of the problem.
