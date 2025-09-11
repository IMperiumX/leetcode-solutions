Okay, let's generate the LeetCode solution repository for "Add Two Numbers" (Problem 2).

**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem from the following input: `2. Add Two Numbers ... [rest of the problem description]`."

*   **Response:** "Problem Number: 2, Problem Name: Add Two Numbers, Difficulty: Medium"

**Step 2: Problem File Creation**

*   Create a directory named `0002-add-two-numbers`.

**Step 3: Solution File Generation**

*   Since the user didn't provide a solution, we'll generate one. The standard approach is to iterate through both linked lists simultaneously, adding corresponding digits and carrying over any overflow.

*   **Prompt 3.2:** "Generate solutions in Python for the LeetCode problem: `Add Two Numbers` (Number: `2`). The solutions should be well-commented. Create files named `solution.py`."
    "If you know of multiple common approaches to solve the problem, generate separate solution files for each approach (e.g., `solution_iterative.py`, `solution_recursive.py`)."
*   We will create a single file, `solution_iterative.py`, as a recursive solution is less common and less efficient for this problem.

    *   **`solution_iterative.py`**

    ```python
    # 2. Add Two Numbers - Iterative Approach

    class ListNode:  # Provided by LeetCode
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two numbers represented as linked lists, returning the sum as a new linked list.

        Args:
            l1: The first linked list.
            l2: The second linked list.

        Returns:
            The head of the linked list representing the sum.
        """
        dummy_head = ListNode(0)  # Create a dummy head for the result list
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_digits = val1 + val2 + carry
            carry = sum_digits // 10  # Calculate the carry
            new_digit = sum_digits % 10  # Calculate the digit to add to the result

            current.next = ListNode(new_digit)  # Create a new node and append it
            current = current.next

            # Move to the next nodes in the input lists (if they exist)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the actual head (skip the dummy node)

    ```

**Step 4: Problem README Generation**

*   **Prompt 4:** "Generate a `README.md` file for the problem: `Add Two Numbers` (Number: `2`, Difficulty: `Medium`)."

*   Here's the generated `README.md`:

```markdown
# 2. Add Two Numbers, Difficulty: Medium

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

**Example 2:**

Input: l1 = [0], l2 = [0]
Output: [0]

**Example 3:**

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

## Approach(es)

### Iterative Approach
 - **Algorithm:**
    - Initialize a dummy head for the result linked list and a `carry` variable to 0.
    - Iterate through both input linked lists simultaneously.
    - In each iteration:
      - Get the values of the current nodes (or 0 if a list has ended).
      - Calculate the sum of the digits and the carry.
      - Update the carry (sum // 10).
      - Create a new node with the value (sum % 10) and append it to the result list.
      - Move to the next nodes in the input lists (if they exist).
    - Continue iterating as long as either input list has more nodes or there's a carry remaining.
    - Return the `next` pointer of the dummy head (to skip the initial dummy node).

  - **Data Structures:**
   - Linked List (ListNode)

  - **Time Complexity:**
    - O(max(m, n)), where m and n are the lengths of the two input linked lists.  We iterate through the longer list.

 - **Space Complexity:**
   - O(max(m, n)). The length of the new list is at most max(m,n) + 1 (in the case of a carry-over at the most significant digit).
   - **Trade-offs:**

    - The iterative approach is straightforward and generally preferred for its clarity and efficiency.

## Code

[Iterative Approach](./solution_iterative.py)

## Notes (Optional)
- A recursive solution is possible but generally less efficient due to function call overhead. It's also less intuitive for this problem.
- It is important to handle the carry properly to ensure correct addition.
- Using a dummy head simplifies the code by avoiding special cases for the first node of the result list.
- The input linked lists store digits in *reverse* order, which makes the addition process easier since we can start from the least significant digit.
```
- Step 5: Topics Extraction
```markdown
# Linked List

A linked list is a linear data structure where elements, called **nodes**, are not stored in contiguous memory locations (unlike arrays). Instead, each node contains:

1.  **Data:** The value stored in the node.
2.  **Pointer/Reference:** A link to the next node in the sequence.

## Key Concepts

*   **Node:** The fundamental building block of a linked list.
*   **Head:** The first node in the linked list.
*   **Tail:** The last node in the linked list.  The tail's `next` pointer is usually `None` (or `null`).
*   **Singly Linked List:** Each node has a pointer only to the *next* node.
*   **Doubly Linked List:** Each node has pointers to both the *next* and *previous* nodes. This allows for bidirectional traversal.
*   **Circular Linked List:** The last node's `next` pointer points back to the head, forming a cycle.
*   **Dummy Node (Sentinel Node):**  An extra node added at the beginning (or sometimes the end) of a linked list to simplify certain operations (like insertion and deletion) by avoiding special cases for the head or tail.

## Common Operations and Time Complexities

| Operation        | Description                                     | Singly Linked List (Time) | Doubly Linked List (Time) |
| ---------------- | ----------------------------------------------- | -------------------------- | -------------------------- |
| Access (by index) | Retrieving the element at a given position.      | O(n)                       | O(n)                       |
| Search           | Finding an element by value.                   | O(n)                       | O(n)                       |
| Insertion (head) | Adding a new node at the beginning.           | O(1)                       | O(1)                       |
| Insertion (tail) | Adding a new node at the end.                 | O(n) (Singly) / O(1) (Doubly) | O(1)                       |
| Insertion (mid) | Adding after a specific node.                 | O(1)                       | O(1)                       |
| Deletion (head)  | Removing the first node.                      | O(1)                       | O(1)                       |
| Deletion (tail)  | Removing the last node.                      | O(n) (Singly) / O(1) (Doubly) | O(1)                       |
| Deletion (mid)  | Removing a specific node.                      | O(1)                       | O(1)                       |

*   **Access:**  Accessing an element by index requires traversing the list from the head, making it O(n).  Linked lists are *not* efficient for random access.
*   **Search:**  Searching also requires traversal, resulting in O(n) time complexity.
*   **Insertion/Deletion:**
    *   *At the Head:*  Inserting or deleting at the head is very fast (O(1)) because it only involves updating a few pointers.
    *   *At the Tail:*  With a *singly* linked list, inserting/deleting at the tail requires traversing to the *second-to-last* node (O(n)).  With a *doubly* linked list, this is O(1) because we have a direct pointer to the tail.
    *   *In the Middle:*  If you already have a pointer/reference to the node *before* the insertion/deletion point, the operation is O(1) (just update pointers).  If you need to *search* for the node first, it becomes O(n).

## Advantages of Linked Lists

*   **Dynamic Size:** Linked lists can grow or shrink easily as needed, unlike static arrays.
*   **Efficient Insertion/Deletion:** Inserting or deleting elements at the beginning or in the middle (given a pointer to the previous node) is very efficient (O(1)).
*   **No Wasted Memory:**  Linked lists only allocate memory for the nodes they actually use, unlike arrays which might pre-allocate more space than needed.

## Disadvantages of Linked Lists

*   **Slow Access:** Accessing an element by index is slow (O(n)) because it requires traversal.
*   **Search Overhead:** Searching is also linear (O(n)).
*   **Memory Overhead:** Each node requires extra memory to store the pointer(s) to the next (and potentially previous) nodes.  This overhead can be significant for small data elements.
*   **Not Cache-Friendly:**  Because nodes are not stored contiguously in memory, linked lists tend to have poor cache locality compared to arrays, potentially leading to slower performance in some cases.

## Use Cases

*   **Dynamic Memory Allocation:** Linked lists can be used to implement memory allocation schemes.
*   **Implementing Stacks and Queues:**  Linked lists are a natural choice for implementing stacks and queues.
*   **Polynomial Representation:**  Each node can represent a term in a polynomial.
*   **Hash Tables (Chaining):**  Linked lists are used in chaining, a collision resolution technique in hash tables.
*   **Undo/Redo Functionality:**  A doubly linked list can be used to track actions for undo/redo operations.
*   **Sparse Matrices:** Representing sparse matrices (matrices with many zero elements).

## Related LeetCode Problems

[2. Add Two Numbers (Medium)](0002-add-two-numbers/README.md)
[206. Reverse Linked List (Easy)](https://leetcode.com/problems/reverse-linked-list/)
[21. Merge Two Sorted Lists (Easy)](https://leetcode.com/problems/merge-two-sorted-lists/)
[141. Linked List Cycle (Easy)](https://leetcode.com/problems/linked-list-cycle/)
[160. Intersection of Two Linked Lists (Easy)](https://leetcode.com/problems/intersection-of-two-linked-lists/)
[234. Palindrome Linked List (Easy)](https://leetcode.com/problems/palindrome-linked-list/)
[24. Swap Nodes in Pairs (Medium)](https://leetcode.com/problems/swap-nodes-in-pairs/)
[19. Remove Nth Node From End of List (Medium)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
[23. Merge k Sorted Lists (Hard)](https://leetcode.com/problems/merge-k-sorted-lists/)
[148. Sort List (Medium)](https://leetcode.com/problems/sort-list/)

```
This completes the generation of the LeetCode solution repository. The response includes the code, a well-structured README, and the topic file, adhering to all the specified guidelines and prompts. The explanations are comprehensive and accurate.
