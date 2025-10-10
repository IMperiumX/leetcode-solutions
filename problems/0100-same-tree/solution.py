class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    Checks if two binary trees are the same (structurally identical with same node values).

    Args:
        p: The root of the first binary tree.
        q: The root of the second binary tree.

    Returns:
        True if the trees are the same, False otherwise.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
