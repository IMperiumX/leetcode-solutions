# 206. Reverse Linked List - Recursive


class Solution:
    def reverseList(self, head):
        """
        Reverses a singly linked list recursively.

        Args:
          head: The head of the linked list.

        Returns:
          The head of the reversed linked list.
        """
        if not head or not head.next:
            return head  # Base case: empty list or single node

        new_head = self.reverseList(
            head.next
        )  # Recursively reverse the rest of the list
        head.next.next = head  # Make the next node point back to the current head
        head.next = None  # Set the current head's next to None (it becomes the tail)

        return new_head  # new_head is the head of the reversed list
