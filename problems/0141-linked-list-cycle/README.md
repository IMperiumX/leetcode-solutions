# 141. Linked List Cycle, Difficulty: Easy

## Problem Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Example 1:**

**Input:** head = \[3,2,0,-4], pos = 1
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

**Input:** head = \[1,2], pos = 0
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:**

**Input:** head = \[1], pos = -1
**Output:** false
**Explanation:** There is no cycle in the linked list.

**Constraints:**

* The number of the nodes in the list is in the range `[0, 10^4]`.
* `-10^5 <= Node.val <= 10^5`
* `pos` is `-1` or a valid index in the linked-list.

**Follow up:** Can you solve it using O(1) (i.e. constant) memory?

## Approach: Floyd's Cycle-Finding Algorithm (Tortoise and Hare)

* **Algorithm:**
    1. Initialize two pointers, `slow` and `fast`, both starting at the `head` of the linked list.
    2. Move `slow` one step at a time (`slow = slow.next`).
    3. Move `fast` two steps at a time (`fast = fast.next.next`).
    4. If there is a cycle, `slow` and `fast` will eventually meet inside the cycle.
    5. If `fast` reaches the end of the list (`fast` or `fast.next` becomes `None`), there is no cycle.

* **Data Structures:**
  * `ListNode` (for the linked list nodes)
  * Two pointers: `slow` and `fast`

* **Time Complexity:**
  * O(n), where n is the number of nodes in the linked list. In the worst case, we might traverse the entire list once.
  * **Best Case:** O(1) - If there's a cycle that starts very close to the head
  * **Average Case:** O(n) - We still need to potentially traverse a significant part of the list
* **Space Complexity:**
  * O(1), constant extra space is used (only two pointers).

* **Trade-offs:**
  * Floyd's Cycle-Finding Algorithm is the most efficient way to detect cycles in a linked list using constant space. It's a clever and widely used algorithm for this purpose.

## Code

* [soltion](solution.py)
