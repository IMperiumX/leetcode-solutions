# 141. Linked List Cycle - Floyd's Cycle-Finding Algorithm (Tortoise and Hare)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Determines if a linked list has a cycle using Floyd's Cycle-Finding Algorithm.

        Args:
          head: The head of the linked list.

        Returns:
          True if the linked list has a cycle, False otherwise.
        """
        slow = head  # Slow pointer (tortoise)
        fast = head  # Fast pointer (hare)

        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step
            fast = fast.next.next  # Fast pointer moves two steps

            if slow == fast:  # If they meet, there's a cycle
                return True

        return False  # No cycle found
