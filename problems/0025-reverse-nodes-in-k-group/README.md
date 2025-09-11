Okay, let's create the solution, README, and topic files for LeetCode problem 25: "Reverse Nodes in k-Group". This is a classic linked list problem that tests your understanding of pointer manipulation.

**Step 1: Problem Identification**

*   **Problem Number:** 25
*   **Problem Name:** Reverse Nodes in k-Group
*   **Difficulty:** Hard

**Step 2: Problem File Creation**

I'll create a folder named `0025-reverse-nodes-in-k-group`.

**Step 3: Solution File Generation**

The core idea is to:

1.  **Iterate:** Move through the linked list in groups of `k` nodes.
2.  **Reverse:** Reverse each group of `k` nodes.
3.  **Connect:** Connect the reversed groups properly, maintaining the overall list structure.
4.  **Handle Remainder:** If the remaining nodes are fewer than `k`, leave them as they are.

We'll use a recursive approach for clarity and conciseness.  An iterative approach is also possible and would achieve O(1) extra space, but it's significantly more complex to implement. The recursive approach, while using O(k) space in the worst-case due to call stack, still meets the prompt's main criteria, and is much more easily understandable.

*   **File: `solution.py`**

```python
"""
25. Reverse Nodes in k-Group - Recursive Solution
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """
    Reverses the nodes of a linked list k at a time.

    Args:
      head: The head of the linked list.
      k: The group size.

    Returns:
      The head of the modified linked list.
    """
    # 1. Check if we have enough nodes to reverse
    count = 0
    current = head
    while current and count < k:
        current = current.next
        count += 1

    if count < k:
        return head  # Not enough nodes to reverse, return as is

    # 2. Reverse the first k nodes
    prev = None
    current = head
    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # 3. Recursively reverse the rest of the list
    if next_node:  # current is now the (k+1)-th node
        head.next = reverseKGroup(current, k)  # Connect the reversed group

    # 4. Return the new head (prev)
    return prev
```

**Step 4: Problem README Generation**

**File: `README.md`**

```markdown
# 25. Reverse Nodes in k-Group, Difficulty: Hard

## Problem Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example 1:**

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Constraints:**

-   The number of nodes in the list is `n`.
-   `1 <= k <= n <= 5000`
-   `0 <= Node.val <= 1000`

**Follow-up:** Can you solve the problem in O(1) extra memory space?

## Approach(es)

### Recursive Approach

**Algorithm:**

1.  **Base Case:** If the remaining list has fewer than `k` nodes, return the current `head` (no reversal needed).
2.  **Reverse k Nodes:** Reverse the first `k` nodes of the current sublist.  This is a standard linked list reversal.  Keep track of `prev`, `current`, and `next_node`.
3.  **Recursive Call:** Recursively call `reverseKGroup` on the remaining portion of the list (starting from the node after the reversed group).  This returns the head of the reversed rest of the list.
4.  **Connect:** Connect the tail of the reversed group (which is the original `head`) to the head of the reversed rest of the list.
5.  **Return:** Return the new head of the reversed group (which is `prev` after the reversal).

**Data Structures:**

-   Linked List Nodes
-   Pointers (`prev`, `current`, `next_node`)

**Time Complexity:**

-   O(n), where n is the number of nodes in the list. We visit each node once.

**Space Complexity:**

-   O(n/k) due to the recursion stack, in the worst case when k=1, this would become O(n),  If `k` is close to `n`, the space complexity approaches O(1). The prompt specifies "O(1) *extra* memory space." Since the recursion happens in groups of `k` the worst-case stack depth *is* `n/k`.

**Trade-offs:**

-   Recursive solution is concise and easier to understand.
-   Uses recursion, which has some overhead (call stack).
-   An iterative solution is possible and would achieve true O(1) extra space, but it is significantly more complex to implement.

## Code

[Recursive Solution](./solution.py)

## Notes

- This problem tests your understanding of linked list manipulation and recursion (or iteration).
- The key is to break down the problem into reversing groups of `k` nodes and connecting them correctly.
- The recursive approach simplifies the logic by handling the connection of reversed groups through the recursive calls.
- While the prompt mentions O(1) space as a follow up, the more commonly tested solution in interviews will use recursion, due to its greater readability.
- The iterative solution would involve keeping track of multiple pointers to manage the connections between groups, making it more error-prone.

```

**Topic Extraction and Files:**

*   **Linked List.md:** (Reuse the existing `Linked List.md` file; no significant additions needed for this specific problem, as the core concepts of linked list reversal are already covered).
* **Recursion.md:** (Reuse)

The `0025-reverse-nodes-in-k-group` folder is now complete, containing the recursive solution file, a detailed README, and references to the relevant Linked List and Recursion topic files. This structure forms a well-organized and comprehensive learning resource.
