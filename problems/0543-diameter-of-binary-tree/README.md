# 543. Diameter of Binary Tree, Difficulty: Easy

## Problem Description

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

Input: `root = [1,2,3,4,5]`
Output: `3`
Explanation: `3` is the length of the path `[4,2,1,3]` or `[5,2,1,3]`.

Example 2:

Input: `root = [1,2]`
Output: `1`

Constraints:

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Approach(es)

### Recursive Approach

Algorithm:

1. Initialize a variable `diameter` to 0. This variable will store the maximum diameter found so far.
2. Define a recursive function `depth(node)` that does the following:
    - **Base Case:** If `node` is `None`, return 0 (depth of an empty subtree is 0).
    - Recursively calculate the depth of the left subtree: `left_depth = depth(node.left)`.
    - Recursively calculate the depth of the right subtree: `right_depth = depth(node.right)`.
    - Update `diameter` with the maximum of the current `diameter` and `left_depth + right_depth` (this represents the longest path that passes through the current node).
    - Return the maximum depth of the left and right subtrees plus 1 (to account for the current node): `max(left_depth, right_depth) + 1`.
3. Call the `depth` function with the `root` node.
4. Return the final `diameter`.

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

## Code

[Recursive Approach](./solution_recursive.py)

## Notes

- The key idea is to calculate the depth of each node's left and right subtrees and update the diameter accordingly.
- The diameter of a tree is either:
  - The maximum depth of the left subtree + the maximum depth of the right subtree (when the longest path passes through the root).
  - The diameter of the left subtree (when the longest path is entirely within the left subtree).
  - The diameter of the right subtree (when the longest path is entirely within the right subtree).
- This problem demonstrates a common pattern in tree problems: using recursion to calculate a value (depth in this case) and updating a global variable (diameter in this case) based on the results of recursive calls.
