"""
235. Lowest Common Ancestor of a Binary Search Tree - Iterative Approach

Given a binary search tree (BST), find the lowest common ancestor (LCA)
node of two given nodes in the BST.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    # Value of p
    p_val = p.val

    # Value of q
    q_val = q.val

    # Start from the root node of the tree
    node = root

    # Traverse the tree
    while node:
        # Value of current node or parent node.
        parent_val = node.val

        if p_val > parent_val and q_val > parent_val:
            # If both p and q are greater than parent
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            # If both p and q are lesser than parent
            node = node.left
        else:
            # We have found the split point, i.e. the LCA node.
            return node
