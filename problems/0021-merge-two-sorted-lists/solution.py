# 21. Merge Two Sorted Lists - Iterative Approach


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    dummy_head = ListNode()  # Dummy node to simplify the code
    tail = dummy_head

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Append the remaining nodes of either list1 or list2 (if any)
    tail.next = list1 if list1 else list2

    return dummy_head.next
