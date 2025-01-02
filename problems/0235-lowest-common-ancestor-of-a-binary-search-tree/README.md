# 235. Lowest Common Ancestor of a Binary Search Tree, Difficulty: Medium

## Problem Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

Input: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8`
Output: `6`
Explanation: The LCA of nodes `2` and `8` is `6`.

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

Input: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4`
Output: `2`
Explanation: The LCA of nodes `2` and `4` is `2`, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: `root = [2,1], p = 2, q = 1`
Output: `2`

Constraints:

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the BST.

## Approach(es)

### Iterative Approach

Algorithm:

1. Start from the root node.
2. Compare the values of `p` and `q` with the current node's value.
3. If both `p` and `q` are greater than the current node's value, move to the right subtree.
4. If both `p` and `q` are smaller than the current node's value, move to the left subtree.
5. If `p` and `q` are on different sides of the current node (or one of them is equal to the current node), then the current node is the LCA.

Data Structures:

- None (only tree node pointers are used).

Time Complexity:

- O(h), where h is the height of the BST. In the worst case (skewed tree), h can be n (number of nodes).
- O(log n) on average for a balanced BST.

Space Complexity:

- O(1) - Constant extra space is used.

Trade-offs:

- Efficient in terms of space.
- Time complexity depends on the height of the tree.

### Recursive Approach

Algorithm:

1. Compare the values of `p` and `q` with the current node's value (`root.val`).
2. If both `p.val` and `q.val` are greater than `root.val`, recursively call the function on the right subtree.
3. If both `p.val` and `q.val` are smaller than `root.val`, recursively call the function on the left subtree.
4. If `p.val` and `q.val` are on different sides of `root.val` (or one of them is equal to `root.val`), then the current node `root` is the LCA.

Data Structures:

- Implicit call stack used during recursion.

Time Complexity:

- O(h), where h is the height of the BST. In the worst case (skewed tree), h can be n (number of nodes).
- O(log n) on average for a balanced BST.

Space Complexity:

- O(h) in the worst case (skewed tree) due to recursive call stack.
- O(log n) on average for a balanced BST.

Trade-offs:

- More concise code compared to the iterative approach.
- Space complexity can be O(n) in the worst case for highly unbalanced trees due to the call stack.

## Code

[Iterative Approach](./solution_iterative.py)

[Recursive Approach](./solution_recursive.py)

## Notes

- Both iterative and recursive approaches take advantage of the properties of a Binary Search Tree (BST) to efficiently find the LCA.
- The iterative approach is generally preferred for its O(1) space complexity, while the recursive approach might be considered more readable.
- These solutions assume that both `p` and `q` are present in the BST, as stated in the problem constraints.
- The concept of LCA is important in various tree-related problems and algorithms.
