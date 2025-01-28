# 23. Merge k Sorted Lists, Difficulty: Hard

## Problem Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:**

```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

```

**Example 2:**

```text

Input: lists = []
Output: []

```

**Example 3:**

```text

Input: lists = [[]]
Output: []

```

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in **ascending** order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Approach(es)

### Brute-Force (Concatenate and Sort)

**Algorithm:**

1. Create an empty list `nodes` to store all node values.
2. Iterate through each linked list in `lists`:
    - Traverse the linked list and append each node's value to `nodes`.
3. Sort the `nodes` list in ascending order.
4. Create a new linked list from the sorted `nodes` list.
5. Return the head of the new linked list.

**Data Structures:**

- `nodes` list (to store all node values)
- A new linked list (to store the merged sorted list)

**Time Complexity:**

- O(N log N), where N is the total number of nodes in all linked lists. This is due to the sorting of the `nodes` list.

**Space Complexity:**

- O(N) to store the `nodes` list and the new linked list.

**Trade-offs:**

- Simple and easy to understand.
- Not very efficient for large values of N due to the sorting step.

### Divide and Conquer (Merge Sort-like)

**Algorithm:**

1. If `lists` is empty, return `None`.
2. If `lists` has only one element, return that element (linked list).
3. Divide `lists` into two halves: `left` and `right`.
4. Recursively merge the `left` half using `mergeKLists_divideconquer(left)`.
5. Recursively merge the `right` half using `mergeKLists_divideconquer(right)`.
6. Merge the two sorted halves using a helper function `mergeTwoLists(left, right)`.
7. Return the head of the merged list from step 6.

**Data Structures:**

- Recursion (call stack)
- New linked lists during the merging process

**Time Complexity:**

- O(N log k), where N is the total number of nodes and k is the number of linked lists. We perform log k merge operations, and each merge operation takes O(N) time in total.

**Space Complexity:**

- O(log k) for the recursion depth (call stack). The merging of two lists can be done in-place or with O(1) extra space if we are careful.

**Trade-offs:**

- More efficient than the brute-force approach for larger k.
- Requires a recursive helper function `mergeTwoLists`.

### Min-Heap (Priority Queue)

**Algorithm:**

1. Create an empty min-heap `min_heap`.
2. Push the first node of each linked list (along with its list index) onto the `min_heap`. The heap will store tuples of (node value, list index, node).
3. Create a dummy node `dummy` and a `current` pointer, initially pointing to `dummy`.
4. While the `min_heap` is not empty:
    - Pop the smallest element (node value, list index, node) from the `min_heap`.
    - Append the popped node to the `current` pointer's `next`.
    - Move the `current` pointer to the newly appended node.
    - If the popped node has a `next` node, push the `next` node (along with its list index) onto the `min_heap`.
5. Return `dummy.next` (the head of the merged list).

**Data Structures:**

- `min_heap` (priority queue)
- A new linked list (to store the merged sorted list)

**Time Complexity:**

- O(N log k), where N is the total number of nodes and k is the number of linked lists. We perform N heap operations (push and pop), and each heap operation takes O(log k) time.

**Space Complexity:**

- O(k) to store the `min_heap` (in the worst case, we might have one node from each list in the heap).

**Trade-offs:**

- Efficient for larger k.
- Requires using a heap data structure.
- Conceptually more complex than the brute-force approach.

## Code

[Brute-Force Approach](./solution_bruteforce.py)

[Divide and Conquer Approach](./solution_divideconquer.py)

[Min-Heap Approach](./solution_minheap.py)

## Notes

- This problem is a classic example of merging sorted data structures.
- The choice of approach depends on factors like the number of linked lists (k), the total number of nodes (N), and the desired balance between code complexity and efficiency.
- The divide and conquer and min-heap approaches are generally preferred for larger inputs due to their better time complexity.
- The min-heap approach is particularly useful when k is large, as it avoids the overhead of recursion.
