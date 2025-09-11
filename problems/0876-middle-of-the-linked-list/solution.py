# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        """
        Find the middle node of a linked list using two pointers.
        
        Args:
            head: ListNode - head of the linked list
        
        Returns:
            ListNode - the middle node (second middle if even length)
        """
        slow = fast = head
        
        # Move slow one step, fast two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


def create_linked_list(values):
    """Helper function to create linked list from list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],      # Expected: [3, 4, 5]
        [1, 2, 3, 4, 5, 6],   # Expected: [4, 5, 6]
        [1],                   # Expected: [1]
        [1, 2],               # Expected: [2]
    ]
    
    for i, values in enumerate(test_cases):
        head = create_linked_list(values)
        middle = solution.middleNode(head)
        result = linked_list_to_list(middle)
        print(f"Test case {i + 1}: {values} -> {result}")