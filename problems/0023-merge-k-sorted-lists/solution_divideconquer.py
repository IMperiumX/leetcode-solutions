"""
1.  Merge k Sorted Lists - Divide and Conquer Approach
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists_divideconquer(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists using a divide and conquer (merge sort-like) approach.

    Args:
      lists: A list of sorted linked lists.

    Returns:
      The head of the merged sorted linked list.
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = mergeKLists_divideconquer(lists[:mid])
    right = mergeKLists_divideconquer(lists[mid:])

    return mergeTwoLists(left, right)


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists.

    Args:
      l1: The head of the first sorted linked list.
      l2: The head of the second sorted linked list.

    Returns:
      The head of the merged sorted linked list.
    """
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next
