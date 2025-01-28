"""
23. Merge k Sorted Lists - Brute Force Approach
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists_bruteforce(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists using a brute-force approach (concatenate and sort).

    Args:
      lists: A list of sorted linked lists.

    Returns:
      The head of the merged sorted linked list.
    """
    nodes = []
    for head in lists:
        while head:
            nodes.append(head.val)
            head = head.next

    nodes.sort()

    dummy = ListNode()
    current = dummy
    for val in nodes:
        current.next = ListNode(val)
        current = current.next

    return dummy.next
