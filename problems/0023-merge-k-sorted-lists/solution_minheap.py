"""
23. Merge k Sorted Lists - Min-Heap Approach
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists_minheap(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists using a min-heap (priority queue).

    Args:
      lists: A list of sorted linked lists.

    Returns:
      The head of the merged sorted linked list.
    """
    min_heap = []

    # Push the first node of each list onto the heap along with its list index
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(min_heap, (head.val, i, head))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, list_index, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, list_index, node.next))

    return dummy.next
