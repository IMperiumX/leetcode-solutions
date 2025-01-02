"""
226. Invert Binary Tree - Recursive Approach

Given the root of a binary tree, invert the tree, and return its root.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)
    return root
