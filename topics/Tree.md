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

# Trees

Trees are a fundamental non-linear data structure in computer science. They consist of nodes connected by edges, forming a hierarchical structure. Unlike linear data structures like arrays or linked lists, trees can represent relationships between data elements in a more complex and intuitive way.

## Key Concepts

* **Node:** The basic building block of a tree. Each node contains data and may have links (pointers) to other nodes.
* **Root:** The topmost node in a tree.  It is the only node without a parent.
* **Parent:** A node that has one or more child nodes.
* **Child:** A node that is connected to a parent node.
* **Leaf:** A node with no children.
* **Edge:** A connection between two nodes.
* **Depth (of a node):** The number of edges from the root to the node.
* **Height (of a node):** The number of edges on the longest path from the node to a leaf.  The height of a tree is the height of its root.
* **Subtree:** A tree consisting of a node and all its descendants.

## Types of Trees

* **Binary Tree:** Each node has at most two children (left and right). This is a very common type of tree.
* **Binary Search Tree (BST):** A binary tree with the property that for each node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value. This allows for efficient searching, insertion, and deletion.
* **Balanced Tree:** A tree where the heights of the left and right subtrees of any node differ by at most 1 (e.g., AVL trees, Red-Black trees).  Balanced trees help prevent worst-case scenarios for operations like searching in BSTs.
* **N-ary Tree:** Each node can have up to N children.
* **Trie (Prefix Tree):**  A specialized tree used for storing strings, where each node represents a character and paths from the root to a node represent prefixes.

## Common Tree Traversals

* **Inorder Traversal (for Binary Trees):** Visit the left subtree, then the current node, then the right subtree.  For BSTs, this visits nodes in sorted order.
* **Preorder Traversal:** Visit the current node, then the left subtree, then the right subtree.
* **Postorder Traversal:** Visit the left subtree, then the right subtree, then the current node.
* **Level Order Traversal (Breadth-First Search):** Visit nodes level by level, from top to bottom and left to right.

## Common Tree Operations

* **Insertion:** Adding a new node to the tree.
* **Deletion:** Removing a node from the tree.
* **Search:** Finding a node with a specific value.
* **Traversal:** Visiting all nodes in a specific order.
* **Checking for properties:** Determining if the tree satisfies certain conditions, such as being balanced or being a valid BST.

## Related LeetCode Problems

* [100. Same Tree](./0100-same-tree)
* [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
* [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
* [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
* [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
