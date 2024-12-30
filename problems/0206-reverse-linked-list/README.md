# 206. Reverse Linked List, Difficulty: Easy

## Problem Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

**Input:** head = \[1,2,3,4,5]
**Output:** \[5,4,3,2,1]

**Example 2:**

**Input:** head = \[1,2]
**Output:** \[2,1]

**Example 3:**

**Input:** head = \[
**Output:** \[

**Constraints:**

* The number of nodes in the list is the range `[0, 5000]`.
* `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Approach(es)

### Iterative Approach

* **Algorithm:**
    1. Initialize three pointers: `prev` (initially `None`), `curr` (initially `head`), and `next_node` (initially `None`).
    2. Iterate through the linked list using a `while` loop that continues as long as `curr` is not `None`.
    3. In each iteration:
        * Store the `next` node of `curr` in `next_node`.
        * Reverse the link of `curr` by setting `curr.next` to `prev`.
        * Move `prev` one step forward to `curr`.
        * Move `curr` one step forward to `next_node`.
    4. After the loop finishes, `prev` will be the new head of the reversed list. Return `prev`.

* **Data Structures:**
  * `ListNode` (for the linked list nodes)
  * Three pointers: `prev`, `curr`, `next_node`

* **Time Complexity:**
  * O(n), where n is the number of nodes in the linked list. We traverse the list once.

* **Space Complexity:**
  * O(1), constant extra space is used.

* **Trade-offs:**
  * The iterative approach is generally preferred for its efficiency and constant space usage. It is a straightforward and in-place reversal.

### Recursive Approach

* **Algorithm:**
    1. **Base Case:** If the list is empty (`head` is `None`) or has only one node (`head.next` is `None`), return `head` (as it is already reversed).
    2. **Recursive Step:**
        * Recursively call `reverseList` on the rest of the list (`head.next`) to get the reversed tail. Let's call the returned head of the reversed tail `new_head`.
        * Set the `next` of the next node (`head.next`) to the current `head`. This effectively reverses the link between the current node and the next node.
        * Set the `next` of the current `head` to `None`. This makes the current `head` the new tail of the reversed list.
        * Return `new_head`.

* **Data Structures:**
  * `ListNode` (for the linked list nodes)
  * Recursive call stack

* **Time Complexity:**
  * O(n), where n is the number of nodes. Each node is visited once.

* **Space Complexity:**
  * O(n) in the worst case due to the recursive call stack. In the best case (tail recursion optimized by the compiler), it could be O(1).

* **Trade-offs:**
  * The recursive approach can be more concise but might be less intuitive to grasp for some.
  * It has a higher space complexity due to the function call stack, which can be a concern for very large lists.

## Code

### Python - Iterative

* [iterative](./solution_iterative.py)
* [recursive](./solution.py)
