Okay, let's generate the LeetCode solution repository for problem 287, "Find the Duplicate Number."

**Step 1: Problem Identification**

The provided input gives us:

*   **Problem Number:** 287
*   **Problem Name:** Find the Duplicate Number
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

We'll create a directory named `0287-find-the-duplicate-number`.

**Step 3: Solution File Generation**

Since a solution was not provided, we will create one.  The constraints ("without modifying the array" and "using only constant extra space") rule out approaches like sorting or using a hash set. The most efficient and appropriate solution is Floyd's Tortoise and Hare (cycle detection) algorithm.

```python
# 0287. Find the Duplicate Number - Floyd's Cycle Detection (Tortoise and Hare)

def findDuplicate(nums):
    # Phase 1: Find the intersection point of the two pointers.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]  # Move one step
        hare = nums[nums[hare]]  # Move two steps
        if tortoise == hare:
            break

    # Phase 2: Find the "entrance" to the cycle (the duplicate number).
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
```

This code is saved as `0287-find-the-duplicate-number/solution.py`.  Here's a version with more extensive comments:

```python
# 0287. Find the Duplicate Number - Floyd's Cycle Detection (Detailed Explanation)

def findDuplicate(nums):
    """
    Finds the duplicate number in an array using Floyd's cycle detection.

    Args:
        nums: An array of integers with a single duplicate.

    Returns:
        The duplicate number.
    """

    # The core idea is to treat the array as a linked list, where the value
    # at each index represents the index of the next node.  Because there's
    # a duplicate number, there will be a cycle in this "linked list."
    # Floyd's algorithm (Tortoise and Hare) is used to detect and find the
    # start of this cycle, which corresponds to the duplicate number.

    # Phase 1: Find the intersection point of the two pointers (tortoise and hare).
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]  # Tortoise moves one step at a time.
        hare = nums[nums[hare]]  # Hare moves two steps at a time.
        if tortoise == hare:
            break  # They meet at some point within the cycle.

    # Phase 2: Find the "entrance" to the cycle (which is the duplicate number).
    # Reset the tortoise to the beginning of the array.
    tortoise = nums[0]
    # Now, move both tortoise and hare one step at a time.  They will meet
    # at the entrance of the cycle.
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    # The meeting point is the duplicate number.
    return hare
```

This is saved as `0287-find-the-duplicate-number/solution_floyd.py`. We'll also include a binary search based solution.

```python
# 0287. Find the Duplicate Number - Binary Search

def findDuplicate(nums):
    low = 1
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        count = 0
        # Count numbers less than or equal to mid
        for num in nums:
            if num <= mid:
                count += 1

        # If count is greater than mid, the duplicate is in the lower half
        if count > mid:
            high = mid - 1
        else:
            low = mid + 1

    return low
```
This is stored as `0287-find-the-duplicate-number/solution_binarysearch.py`.

**Step 4: Problem README Generation**

```markdown
# 287. Find the Duplicate Number, Difficulty: Medium

## Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without modifying the array** `nums` and using only **constant extra space**.

**Example 1:**

Input: `nums = [1,3,4,2,2]`
Output: `2`

**Example 2:**

Input: `nums = [3,1,3,4,2]`
Output: `3`

**Constraints:**

*   `1 <= n <= 10^5`
*   `nums.length == n + 1`
*   `1 <= nums[i] <= n`
*   All the integers in `nums` appear only once except for precisely one integer which appears two or more times.

**Follow up:**

*   How can we prove that at least one duplicate number must exist in `nums`?
*   Can you solve the problem in linear runtime complexity?

## Approach(es)

### Floyd's Cycle Detection (Tortoise and Hare)

This approach cleverly uses the idea of cycle detection in a linked list. We treat the input array `nums` as a linked list where `nums[i]` points to the next node's index.  Since there's a duplicate, a cycle must exist.

**Algorithm:**

1.  **Phase 1: Find Intersection Point:**
    *   Initialize two pointers, `tortoise` and `hare`, both starting at `nums[0]`.
    *   Move `tortoise` one step at a time: `tortoise = nums[tortoise]`.
    *   Move `hare` two steps at a time: `hare = nums[nums[hare]]`.
    *   Repeat until `tortoise` and `hare` meet.  They are guaranteed to meet within the cycle.

2.  **Phase 2: Find Cycle Entrance (Duplicate Number):**
    *   Reset `tortoise` to `nums[0]`.
    *   Move both `tortoise` and `hare` one step at a time until they meet again.
    *   The meeting point is the duplicate number.

**Data Structures:**

*   No extra data structures are needed, just two integer variables (`tortoise` and `hare`).

**Time Complexity:** O(n) -  Both phases of Floyd's algorithm take linear time.

**Space Complexity:** O(1) - Constant extra space.

**Trade-offs:**

*   This method is very efficient (O(n) time and O(1) space) and meets the problem constraints.
*   The underlying concept (treating the array as a linked list and using cycle detection) is not immediately obvious.

### Binary Search

We can also use binary search to find the duplicate number. The key idea is to count the number of elements in `nums` that are less than or equal to a chosen `mid` value.

**Algorithm:**

1.  **Initialization:**
    *   Set `low = 1` and `high = len(nums) - 1`.
2.  **Binary Search:**
    *   While `low <= high`:
        *   Calculate `mid = (low + high) // 2`.
        *   Count the number of elements in `nums` that are less than or equal to `mid`.
        *   If `count > mid`, the duplicate number must be in the lower half (`low` to `mid - 1`).  Set `high = mid - 1`.
        *   Otherwise, the duplicate number must be in the upper half (`mid + 1` to `high`). Set `low = mid + 1`.
3. Return `low`.

**Data Structures:**

*   No extra data structure

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

**Trade-offs:**

*   Binary Search is less efficient than floyd but still a valid solution.
*   It is easier to understand.

## Code

[Floyd's Cycle Detection](./solution_floyd.py)
[Binary Search](./solution_binarysearch.py)

## Notes

*   **Proof of Existence of Duplicate:** The Pigeonhole Principle guarantees that at least one duplicate must exist.  We have `n + 1` integers (pigeons) and only `n` possible values (pigeonholes). Therefore, at least one value must be repeated.
*   The Floyd's cycle detection approach is a clever and efficient solution that satisfies all the problem constraints.
* Binary Search approach is a valid solution but it's less efficient than the floyd's solution.

```

**Step 5: Topics Extraction**

Since we have used Cycle Detection and Binary Search, we will create a file for Cycle Detection (Binary Search was created previously).

```markdown
# Cycle Detection (Floyd's Tortoise and Hare Algorithm)

Cycle detection is the problem of finding a cycle in a sequence of iterated function values.  Floyd's Tortoise and Hare algorithm is a classic and efficient algorithm for detecting cycles in linked lists (or any sequence that can be treated like a linked list).  It uses two pointers, one moving at twice the speed of the other.

## Key Concepts

*   **Linked List Representation:**  The algorithm is often explained in terms of linked lists, but it can be applied to any situation where you have a sequence of values where each value "points to" the next value in the sequence.
*   **Tortoise and Hare:** The algorithm uses two pointers:
    *   **Tortoise:** Moves one step at a time.
    *   **Hare:** Moves two steps at a time.
*   **Cycle Detection:** If there's a cycle, the tortoise and hare are guaranteed to meet within the cycle.  This is because the hare will eventually "lap" the tortoise.
*   **Finding the Cycle Start (Entrance):**  After the tortoise and hare meet, you can find the start of the cycle (the "entrance" to the cycle) with a second phase of the algorithm.

## How Floyd's Algorithm Works

1.  **Initialization:**
    *   Initialize both the tortoise and hare pointers to the starting point (e.g., the head of the linked list, or the first element of an array).

2.  **Cycle Detection (Phase 1):**
    *   Move the tortoise one step at a time: `tortoise = next(tortoise)`.
    *   Move the hare two steps at a time: `hare = next(next(hare))`.
    *   Repeat until the tortoise and hare meet (`tortoise == hare`) or you reach the end of the sequence (no cycle).

3.  **Finding the Cycle Start (Phase 2):**
    *   If the tortoise and hare met in Phase 1, reset the tortoise to the starting point.
    *   Keep the hare at the meeting point.
    *   Move both the tortoise and hare one step at a time until they meet again.
    *   The point where they meet again is the *start* of the cycle.

## Example (Python - Linked List)

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    if not head or not head.next:
        return None  # No cycle if the list is empty or has only one node

    # Phase 1: Find intersection point
    tortoise = head
    hare = head
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            break  # Cycle detected
    else:
        return None # No cycle

    # Phase 2: Find cycle start
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next

    return tortoise

# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Create the cycle

cycle_start = detectCycle(head)
if cycle_start:
    print(f"Cycle starts at node with value: {cycle_start.val}")  # Output: 3
else:
    print("No cycle detected")

```

## Example (Python - Array as Implicit Linked List - LeetCode 287)

```python
# 0287. Find the Duplicate Number - Floyd's Cycle Detection

def findDuplicate(nums):
    # Phase 1: Find the intersection point of the two pointers.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]  # Move one step
        hare = nums[nums[hare]]  # Move two steps
        if tortoise == hare:
            break

    # Phase 2: Find the "entrance" to the cycle (the duplicate number).
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
```
## Time and Space Complexity

*   **Time Complexity:** O(n), where n is the length of the sequence (or the number of nodes in the linked list).  In the worst case, both phases of the algorithm take linear time.
*   **Space Complexity:** O(1) - Constant extra space.  We only use a fixed number of pointers (tortoise and hare).

## Applications

*   **Linked List Cycle Detection:** The most common application.
*   **Finding Duplicates in an Array (LeetCode 287):**  As shown in the example above.
*   **Detecting Loops in Programs:**  Can be used to detect infinite loops in code.
*   **Cryptography:**  Used in some algorithms for finding collisions in hash functions.
* **Pollard's rho algorithm for integer factorization:** Used in number theory.

## Example LeetCode Problems

*   **Linked List Cycle:** [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy)
*   **Linked List Cycle II:** [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium)
*   **Find the Duplicate Number:** [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium)
*    **Happy Number:** [202. Happy Number](https://leetcode.com/problems/happy-number/) (Easy)

## Tips

*   **Understand the Linked List Analogy:** Even when working with arrays, think of the problem in terms of a linked list where the value at each index points to the next index.
*   **Two Phases:** Remember that Floyd's algorithm has two distinct phases: finding the intersection point and finding the cycle start.
*   **Constant Space:** The key advantage of Floyd's algorithm is its constant space complexity.

Floyd's Tortoise and Hare algorithm is a clever and efficient technique for cycle detection. It's a valuable tool for solving problems involving linked lists, arrays, and other sequences.
```
This will be saved as `Cycle Detection.md`.
All files have been generated.
