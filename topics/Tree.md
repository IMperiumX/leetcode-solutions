# Tree

## Description

A tree is a hierarchical, non-linear data structure that consists of nodes connected by edges. It is called a "tree" because its structure resembles an upside-down tree, with the root at the top and branches extending downward. Trees are used to represent hierarchical relationships between data elements and are widely used in computer science for various applications, such as file systems, organizational charts, and decision trees.

## Key Concepts

* **Node:** A fundamental unit of a tree, which stores data and may have links (edges) to other nodes.
* **Root:** The topmost node in the tree, which has no parent.
* **Parent:** A node that is directly connected to another node below it.
* **Child:** A node that is directly connected to a node above it (its parent).
* **Siblings:** Nodes that share the same parent.
* **Leaf:** A node that has no children.
* **Subtree:** A portion of the tree that is itself a tree, rooted at one of the nodes of the original tree.
* **Edge:** A connection between two nodes (parent and child).
* **Path:** A sequence of nodes and edges connecting a node to a descendant.
* **Depth (or Level):** The distance of a node from the root. The root has a depth of 0, its children have a depth of 1, and so on.
* **Height:** The maximum depth of any node in the tree. It represents the length of the longest path from the root to a leaf.

## Types of Trees

* **Binary Tree:** Each node has at most two children, referred to as the left child and the right child.
* **Binary Search Tree (BST):** A special type of binary tree where the left subtree contains only nodes with smaller values than the parent, and the right subtree contains only nodes with larger values.
* **Balanced Tree:** A tree in which the heights of the subtrees of any node differ by at most 1. Examples include AVL trees and Red-Black trees.
* **N-ary Tree:** Each node can have up to N children.
* **Trie (Prefix Tree):** A tree-like structure used to store a dynamic set of strings, where the keys are usually strings.

## Common Operations

* **Traversal:** Visiting each node in the tree in a specific order. Common traversal methods include:
  * **Inorder:** Traverse the left subtree, visit the current node, then traverse the right subtree (for binary trees).
  * **Preorder:** Visit the current node, traverse the left subtree, then traverse the right subtree.
  * **Postorder:** Traverse the left subtree, traverse the right subtree, then visit the current node.
  * **Level Order (Breadth-First):** Visit nodes level by level, from left to right.
* **Insertion:** Adding a new node to the tree.
* **Deletion:** Removing a node from the tree.
* **Search:** Finding a node with a specific value in the tree.

## Advantages

* **Efficient for representing hierarchical data.**
* **Fast search, insertion, and deletion operations (especially in balanced trees like BSTs).**
* **Flexible and can be adapted to various applications.**

## Disadvantages

* **Performance can degrade if the tree becomes unbalanced (e.g., skewed).**
* **Implementation can be more complex than linear data structures like arrays or linked lists.**

## Example (Python - Binary Tree)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder traversal
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)

inorder_traversal(root)  # Output: 4 2 5 1 3
```

## Related LeetCode Problems

* [104. Maximum Depth of Binary Tree](./0104-maximum-depth-of-binary-tree/README.md)
* [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
* [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
* [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
* [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
* [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
* [100. Same Tree](https://leetcode.com/problems/same-tree/)
* [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
* [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
* [112. Path Sum](https://leetcode.com/problems/path-sum/)
