# Floyd's Cycle-Finding Algorithm (Tortoise and Hare Algorithm)

## Overview

Floyd's Cycle-Finding Algorithm, also known as the Tortoise and Hare Algorithm, is an algorithm that uses two pointers, moving at different speeds, to determine if a linked list (or any sequence with a next element function) has a cycle.

## Algorithm

1. **Initialization:**
    * Start with two pointers, often called `slow` (or tortoise) and `fast` (or hare), both initially pointing to the head of the linked list.

2. **Iteration:**
    * Move the `slow` pointer one step at a time: `slow = slow.next`
    * Move the `fast` pointer two steps at a time: `fast = fast.next.next`
    * Continue this process until one of the following conditions is met:
        * **Cycle Detected:** If the `slow` and `fast` pointers meet at any point (`slow == fast`), it indicates that there is a cycle in the linked list.
        * **No Cycle:** If the `fast` pointer reaches the end of the list (i.e., `fast` becomes `None` or `fast.next` becomes `None`), it means there is no cycle.

## Why it Works

* **If there's a cycle:**
  * Imagine the linked list as having a "tail" leading into a "loop" (the cycle).
  * The `fast` pointer will enter the loop first.
  * Since the `fast` pointer moves twice as fast as the `slow` pointer, it will inevitably start lapping the `slow` pointer within the loop.
  * Eventually, they will meet at some point inside the loop.

* **If there's no cycle:**
  * The `fast` pointer will simply reach the end of the list before the `slow` pointer.

## Example

Let's consider a linked list with a cycle:

```md
1 -> 2 -> 3 -> 4 -> 5
^ |
| v
8 <- 7 <- 6
```

1. `slow` and `fast` both start at 1.
2. `slow` moves to 2, `fast` moves to 3.
3. `slow` moves to 3, `fast` moves to 5.
4. `slow` moves to 4, `fast` moves to 7.
5. `slow` moves to 5, `fast` moves to 4 (fast has entered the loop).
6. `slow` moves to 6, `fast` moves to 6 (they meet!). Cycle detected.

## Python Code

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    """
    Detects if a linked list has a cycle using Floyd's Cycle-Finding Algorithm.

    Args:
      head: The head of the linked list.

    Returns:
      True if there's a cycle, False otherwise.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

Time and Space Complexity
Time Complexity: O(n), where n is the number of nodes in the linked list. In the worst case, we might traverse the entire list once.

Space Complexity: O(1), constant extra space is used (only two pointers).

Advantages
Efficiency: It's an efficient algorithm with linear time complexity.

Constant Space: It uses only a constant amount of extra space, making it suitable for situations with memory constraints.

Disadvantages
Specific Application: It's primarily designed for cycle detection and might not be directly applicable to other types of problems.

Modification of the List: If you need to find the start of the cycle or remove the cycle, the basic algorithm needs to be modified.

Applications
Linked List Cycle Detection: The primary application is finding cycles in linked lists.

Detecting Loops in Arrays: It can be adapted to find repeating sequences or cycles in arrays where the array elements represent "next" pointers.

Cryptography: Used in some cryptographic algorithms for tasks like finding collisions in hash functions.

Computer Science Theory: It's a fundamental algorithm used in various theoretical computer science problems related to sequences and state machines.

Related LeetCode Problems
141. Linked List Cycle (Detecting a cycle)

142. Linked List Cycle II (Finding the start of the cycle)
