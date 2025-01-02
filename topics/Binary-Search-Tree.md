# Binary Search Tree (BST)

## Description

A Binary Search Tree (BST) is a specialized type of binary tree that follows a specific ordering property. In a BST, for each node:

1. The value of the node is greater than or equal to all values in its left subtree.
2. The value of the node is less than or equal to all values in its right subtree.

This ordering property allows for efficient searching, insertion, and deletion of nodes.

## Key Properties

- **Ordered:** Nodes in a BST are ordered based on their values.
- **Unique Values (Typically):**  While not strictly required, most BST implementations assume that all node values are unique. This simplifies operations like insertion and deletion.
- **Recursive Structure:** Each subtree of a BST is also a BST, following the same ordering property.

## Common Operations

- **Search:** Find a node with a specific value.
  - Start at the root.
  - Compare the target value with the current node's value.
  - If the target is smaller, move to the left child.
  - If the target is larger, move to the right child.
  - Repeat until the target is found or a null node is reached.
- **Insertion:** Add a new node with a given value.
  - Perform a search for the value.
  - When a null node is reached (where the value would be if it existed), create a new node with the given value and attach it as the appropriate child (left or right).
- **Deletion:** Remove a node with a specific value.
  - Find the node to be deleted.
  - **Case 1: Node is a leaf (no children):** Simply remove the node.
  - **Case 2: Node has one child:** Replace the node with its child.
  - **Case 3: Node has two children:**
    - Find the inorder successor (smallest node in the right subtree) or inorder predecessor (largest node in the left subtree).
    - Replace the node's value with the inorder successor/predecessor's value.
    - Recursively delete the inorder successor/predecessor (which will have at most one child).
- **Traversal:** Visit all nodes in a specific order (inorder, preorder, postorder, level order). Inorder traversal of a BST yields the nodes in sorted order.
- **Minimum/Maximum:** Find the node with the smallest/largest value.
  - **Minimum:** Traverse left until a null node is reached.
  - **Maximum:** Traverse right until a null node is reached.

## Time Complexity

- **Search, Insertion, Deletion:**
  - Average Case: O(log n), where n is the number of nodes (assuming a balanced tree).
  - Worst Case: O(n) for a skewed tree (e.g., all nodes in a single path).
- **Traversal:** O(n) - all nodes are visited.
- **Minimum/Maximum:** O(h), where h is the height of the tree.

## Space Complexity

- **Data Storage:** O(n) - space is required to store the nodes.
- **Operations:**
  - Iterative: O(1) for most operations (except for some traversal methods).
  - Recursive: O(h) in the worst case due to the call stack.

## Advantages

- **Efficient Search, Insertion, Deletion:** Especially when the tree is balanced.
- **Ordered Data:** Inorder traversal provides sorted data.
- **Range Queries:** Can efficiently find all nodes within a specific range of values.

## Disadvantages

- **Performance degrades with unbalanced trees:**  Worst-case time complexity becomes O(n) for skewed trees.
- **Requires balancing mechanisms:** To maintain good performance, self-balancing BSTs (e.g., AVL trees, Red-Black trees) are often used, but they add complexity.

## Example (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        return node

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.val)
            self._inorder_recursive(node.right)

# Example Usage
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder Traversal:")
bst.inorder_traversal()

print("\nSearch for 4:", bst.search(4))
print("Search for 9:", bst.search(9))
```

## Related LeetCode Problems

- [235. Lowest Common Ancestor of a Binary Search Tree](./0235-lowest-common-ancestor-of-a-binary-search-tree/README.md)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
