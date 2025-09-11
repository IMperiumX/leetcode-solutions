# 876. Middle of the Linked List, Difficulty: Easy

**Link:** [https://leetcode.com/problems/middle-of-the-linked-list/](https://leetcode.com/problems/middle-of-the-linked-list/)

## Problem Description

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

```python
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

Example 2:

```python
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

Constraints:

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

## Solution Approach (Two Pointers - Tortoise and Hare)

The [`solution.py`](./solution.py) file contains a Python solution using the two-pointer technique, also known as the "tortoise and hare" algorithm.

1. Initialize two pointers: slow and fast, both pointing to the head.
2. Move slow pointer one step at a time and fast pointer two steps at a time.
3. When the fast pointer reaches the end, the slow pointer will be at the middle.
4. Return the slow pointer.

**Time Complexity:** O(n) where n is the number of nodes
**Space Complexity:** O(1) - constant space

Why this works:
- Fast pointer moves twice as fast as slow pointer
- When fast reaches the end, slow will be at the middle
- For even-length lists, this returns the second middle node as required

Alternative approach:
- **Two Pass:** First pass to count nodes, second pass to find middle - O(n) time, O(1) space
- **Array:** Convert to array and return middle element - O(n) time, O(n) space