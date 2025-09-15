# 21. Merge Two Sorted Lists, Difficulty: Easy

## Problem Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

## Approach(es)

### Iterative Approach

Algorithm:

1. Create a dummy node.  This simplifies the code, especially when handling the head of the merged list.
2. Initialize a `tail` pointer to the dummy node.  This pointer will always point to the last node of the merged list.
3. Iterate while both `list1` and `list2` are not empty:
    * Compare the values of the current nodes of `list1` and `list2`.
    * Append the node with the smaller value to the `tail.next`.
    * Move the pointer of the list from which the node was appended to the next node.
    * Move the `tail` pointer to the newly appended node.
4. After one of the lists becomes empty, append the remaining nodes of the other list (if any) to `tail.next`.
5. Return `dummy_head.next`, which is the head of the merged list.

Data Structures:

* Linked List: The input and output are linked lists.

Time Complexity:

* O(m + n), where m and n are the lengths of `list1` and `list2`, respectively. We traverse both lists at most once.

Space Complexity:

* O(1) -  We use constant extra space (dummy node and tail pointer). We are modifying the existing lists in place.  The iterative solution does *not* create new nodes for the merged list (except for the dummy head, which is constant space).

Trade-offs:

* Iterative approach good balance between time and memory.

### Recursive Approach

Algorithm:

1. Base Cases:
    * If `list1` is empty, return `list2`.
    * If `list2` is empty, return `list1`.
2. Recursive Step:
    * Compare the values of the current nodes of `list1` and `list2`.
    * If `list1.val` is smaller or equal, recursively merge `list1.next` and `list2`, and set the result as `list1.next`.  Return `list1`.
    * Otherwise, recursively merge `list1` and `list2.next`, and set the result as `list2.next`. Return `list2`.

Data Structures:

* Linked List

Time Complexity:

* O(m + n), where m and n are the lengths of `list1` and `list2`.  Each node is visited once.

Space Complexity:

* O(m + n) - due to recursive calls. In the worst-case scenario (e.g., highly skewed lists), the recursion depth can be equal to the sum of the lengths of the two lists.  This is because each recursive call adds a new frame to the call stack.

Trade-offs:

* The recursive approach can be more concise and easier to read for some people, but it uses more space due to the call stack.
* The iterative solution is generally preferred for its constant space complexity.

## Code

[Iterative Approach](./solution.py)
[Recursive Approach](./solution_recursive.py)

## Notes

* Both iterative and recursive approaches are common solutions.
* The iterative approach is generally preferred due to its O(1) space complexity.
* The dummy node technique is a useful pattern for simplifying linked list manipulation.

* The time complexity of the provided `mergeTwoLists` function is **O(n + m)**, where:
* **n** is the number of nodes in `list1`.
* **m** is the number of nodes in `list2`.

### Explanation

  The function merges two sorted singly linked lists into one sorted linked list. Here's why the time complexity is O(n + m):

  1. **Initialization**:

* A dummy node is created to simplify edge cases, and a `current` pointer is initialized to this dummy node.

   2. **Merging Process**:

* The `while` loop runs as long as both `list1` and `list2` have nodes.
* In each iteration:
  * It compares the values of the current nodes of `list1` and `list2`.
  * Appends the smaller node to the merged list by setting `current.next`.
  * Moves the pointer (`list1` or `list2`) forward.
  * Advances the `current` pointer.

    3. **Appending Remaining Nodes**:
* After one of the lists is exhausted, the remaining nodes of the other list are appended to the merged list.
* This ensures that all nodes from both lists are included.

### Time Complexity Breakdown

* **Comparisons and Node Linking**:
  * Each node from both lists is visited exactly once.
  * For each node, only constant time operations are performed (comparison and pointer assignment).
* **Total Operations**:
  * The total number of iterations in the `while` loop is proportional to the total number of nodes in both lists.
  * After the loop, appending the remaining nodes is also proportional to the number of remaining nodes.
* **Overall Complexity**:
  * Since each of the **n** and **m** nodes is processed once, the total time complexity is **O(n + m)**.

### Conclusion

  The function efficiently merges the two lists by only traversing each node once, leading to a linear time complexity relative to the sizes of the input lists.

  **Answer:** O(n + m), where n and m are the lengths of the input lists; each node is processed once.

---

* The space complexity of the provided `mergeTwoLists` function is **O(1)**, which means it uses constant extra space regardless of the input sizes.

### Explanation

  The function merges two sorted singly linked lists into one sorted linked list by rearranging the existing nodes. Here's a detailed breakdown of the space usage:

1. **Initialization**:

* **Dummy Node**: A single dummy node is created using `ListNode(0)`. This node serves as the starting point of the merged list and simplifies edge cases.
* **Pointers**:
  * `current`: A pointer initialized to the dummy node. It is used to build the merged list.
  * `list1`, `list2`: Pointers to traverse the input lists.
* All these pointers and the dummy node consume **constant space**.

2. **Merging Process**:

* The function uses a `while` loop to iterate through the nodes of `list1` and `list2`.
* It compares the values of the current nodes and adjusts the `next` pointers to build the merged list.
* **No new nodes are created during this process**; the existing nodes from `list1` and `list2` are rearranged.
* All operations within the loop are done **in-place**, using existing nodes and pointers.

3. **Appending Remaining Nodes**:

* After one of the lists is exhausted, the function appends the remaining nodes of the other list to the merged list.
* This is done by pointing `current.next` to the remaining nodes.
* Again, **no additional space** is required for this step.

### Space Complexity Breakdown

* **Extra Space Used**:
  * **Dummy Node**: One node (`ListNode`) is created, which requires constant space **O(1)**.
  * **Pointers/Variables**: The function uses a fixed number of variables (`current`, `list1`, `list2`), each consuming constant space.
* **In-Place Operations**:
  * The function rearranges the `next` pointers of existing nodes. It doesn't allocate additional space proportional to the input sizes.
  * All modifications are made directly on the input lists' nodes.
* **Overall Space Complexity**:
  * Since the extra space used does not depend on the lengths of `list1` or `list2`, it is considered **constant space**.
  * **Space Complexity: O(1)**.

### Conclusion

  The function effectively merges two lists by reusing and rearranging existing nodes without allocating significant additional space. It only uses a small, constant amount of extra space for the dummy node and a few pointers.
