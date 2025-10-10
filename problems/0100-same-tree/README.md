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

1. **Base Cases:**
    * If both `p` and `q` are `None`, they are the same (empty trees), so return `True`.
    * If only one of `p` or `q` is `None`, they are different, so return `False`.
2. **Check Current Node:**
    * If `p.val` is not equal to `q.val`, the trees are different, so return `False`.
3. **Recursive Calls:**
    * Recursively check if the left subtrees are the same: `isSameTree(p.left, q.left)`.
    * Recursively check if the right subtrees are the same: `isSameTree(p.right, q.right)`.
4. **Combine Results:**
    * Return `True` if and only if both the left and right subtrees are the same (using the `and` operator).

Data Structures:

* Uses the implicit call stack for recursion.

Time Complexity:

* O(n), where n is the minimum number of nodes in the two trees. We visit each node in the smaller tree at most once.

Space Complexity:

* O(h) in the average case (for a balanced tree), where h is the height of the tree. This is due to the recursive call stack.
* O(n) in the worst case (for a skewed tree), where the height of the tree is equal to the number of nodes.

Trade-offs:

* This recursive approach is concise, readable, and directly reflects the problem's structure. It's the most common and natural way to solve this problem.

## Code

[Recursive Approach](./solution.py)

## Notes

This problem is a fundamental example of tree traversal and recursion.  It's a good building block for understanding more complex tree problems. The key is to handle the base cases correctly and to make sure both the structure and the node values are compared.
