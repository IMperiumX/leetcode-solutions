# Two Pointers Technique

## Introduction

The **two pointers** technique is a common algorithmic approach used to solve problems involving arrays, strings, or linked lists. It typically involves using two pointers (indices or references) that traverse the data structure in a coordinated way. This technique is often used to optimize solutions in terms of time complexity, especially when dealing with sorted data or when searching for specific pairs or patterns.

## Patterns and Variations

There are several common variations of the two pointers technique:

### 1. Pointers Moving Towards Each Other

* **Description:** Two pointers start at opposite ends of the data structure and move towards each other until they meet or a specific condition is met.
* **Use Cases:**
  * Finding pairs that sum to a target value in a sorted array.
  * Checking for palindromes in a string.
  * Reversing an array or a string in place.

### 2. Pointers Moving in the Same Direction

* **Description:** Two pointers start at the beginning of the data structure and move in the same direction, but potentially at different speeds.
* **Use Cases:**
  * Finding the middle element of a linked list (fast and slow pointers).
  * Detecting cycles in a linked list (fast and slow pointers).
  * Removing duplicates from a sorted array.
  * Sliding window problems.

### 3. Pointers on Different Data Structures

* **Description:** Two pointers are used to traverse two different data structures simultaneously.
* **Use Cases:**
  * Merging two sorted arrays.
  * Comparing elements in two arrays or strings.

## Examples

### 1. Finding a Pair with a Target Sum (Pointers Moving Towards Each Other)

**Problem:** Given a sorted array of integers and a target sum, find if there exists a pair of elements in the array that add up to the target sum.

**Solution (Python):**

```python
def has_pair_with_sum(arr, target):
  """
  Checks if there exists a pair of elements in a sorted array that add up to the target sum.

  Args:
    arr: The sorted array of integers.
    target: The target sum.

  Returns:
    True if a pair exists, False otherwise.
  """
  left = 0
  right = len(arr) - 1

  while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
      return True
    elif current_sum < target:
      left += 1  # Move the left pointer to increase the sum
    else:
      right -= 1  # Move the right pointer to decrease the sum

  return False
```

### 2. Finding the Middle Element of a Linked List (Pointers Moving in the Same Direction)

**Problem:** Given a singly linked list, find the middle element.

**Solution (Python):**

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def find_middle_element(head):
  """
  Finds the middle element of a singly linked list using the two-pointer technique.

  Args:
    head: The head of the linked list.

  Returns:
    The middle element (Node) of the linked list.
  """
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow
```

## Advantages of the Two Pointers Technique

* **Efficiency:** Can often reduce the time complexity from O(n^2) to O(n) or from O(n log n) to O(n) in some cases.
* **Space Optimization:** In-place operations can often be performed with minimal extra space.
* **Simplicity:** The technique is relatively easy to understand and implement in many cases.

## Disadvantages of the Two Pointers Technique

* **Applicability:** Not suitable for all types of problems. It works best when there is some inherent order or structure that can be exploited.
* **Sorted Data:** Often requires the data to be sorted for optimal performance.

## Problems Related to Two Pointers

1. [1. Two Sum](../problems/0001-two-sum/README.md)
2. [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
3. [15. 3Sum](https://leetcode.com/problems/3sum/)
4. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
5. [27. Remove Element](https://leetcode.com/problems/remove-element/)
6. [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
7. [125. Valid Palindrome](./../problems/0125-valid-palindrome/README.md)
8. [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
9. [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
10. [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
11. [344. Reverse String](https://leetcode.com/problems/reverse-string/)
12. [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

# Two Pointers

The Two Pointers technique is a common algorithmic approach used to solve problems involving arrays, strings, or linked lists. It involves using two pointers (variables that hold indices or references) to traverse the data structure, often in a coordinated way.

## Common Two Pointers Patterns

* **Opposite Directions:** The two pointers start at opposite ends of the data structure (e.g., beginning and end of an array) and move towards each other. This is often used for problems involving sorted arrays or palindromes.
* **Same Direction:** Both pointers start at the same position (e.g., the beginning of the data structure) and move in the same direction, but potentially at different speeds. This is common in problems like finding cycles in linked lists or sliding window problems.
* **Fast and Slow Pointers:** A variation of the "Same Direction" pattern where one pointer (the fast pointer) moves faster than the other (the slow pointer). This is very useful for linked list problems, such as finding the middle node or detecting cycles.
* **Maintain a window**: When there is a need to keep a track of sub-array.

## Advantages of Two Pointers

* **Efficiency:** Two pointers can often reduce time complexity from O(n^2) to O(n) or from O(n log n) to O(n) by avoiding nested loops or unnecessary sorting.
* **Space Efficiency:** Two pointers typically use constant extra space (O(1)), as they only store a few pointer variables.

## When to Use Two Pointers

* Problems involving sorted arrays or linked lists.
* Problems where you need to find a pair, triplet, or subarray that satisfies a certain condition.
* Problems involving reversing or manipulating a data structure in place.
* Problems that can be solved by comparing or tracking elements from different parts of the data structure.
* Find a pair in sorted array which gives sum X.

## LeetCode Problems Related to Two Pointers

* [21. Merge Two Sorted Lists](0021-merge-two-sorted-lists/README.md) (used in iterative)
* [1. Two Sum](https://leetcode.com/problems/two-sum/) (can be solved with two pointers if the array is sorted)
* [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
* [15. 3Sum](https://leetcode.com/problems/3sum/)
* [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
* [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (fast and slow pointers)
* [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
* [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
