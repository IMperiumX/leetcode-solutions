"""
235. Lowest Common Ancestor of a Binary Search Tree - Recursive Approach

Given a binary search tree (BST), find the lowest common ancestor (LCA)
node of two given nodes in the BST.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    # Value of current node or parent node.
    parent_val = root.val

    # Value of p
    p_val = p.val

    # Value of q
    q_val = q.val

    if p_val > parent_val and q_val > parent_val:
        # If both p and q are greater than parent
        return lowestCommonAncestor(root.right, p, q)
    elif p_val < parent_val and q_val < parent_val:
        # If both p and q are lesser than parent
        return lowestCommonAncestor(root.left, p, q)
    else:
        # We have found the split point, i.e. the LCA node.
        return root
