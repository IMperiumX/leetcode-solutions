# 206. Reverse Linked List - Iterative


class Solution:
    def reverseList(self, head):
        """
        Reverses a singly linked list iteratively.

        Args:
          head: The head of the linked list.

        Returns:
          The head of the reversed linked list.
        """
        prev = None  # Initialize the previous node to None
        curr = head  # Initialize the current node to the head

        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev to the current node
            curr = next_node  # Move curr to the next node

        return prev  # prev will be the new head of the reversed list
