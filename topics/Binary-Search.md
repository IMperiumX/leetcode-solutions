
# Binary Search

## Introduction

**Binary Search** is an efficient algorithm for finding a target value within a **sorted** array or list. It works by repeatedly dividing the search interval in half. If the middle element of the interval matches the target, the search is successful. If the target is smaller than the middle element, the search continues in the left half of the interval. If the target is larger, the search continues in the right half. This process is repeated until the target is found or the interval becomes empty.

## Algorithm

1. **Initialization:**
    * Set `left` to the start index of the search interval (usually 0).
    * Set `right` to the end index of the search interval (usually `len(array) - 1`).

2. **Iteration:**
    * While `left <= right`:
        * Calculate the middle index: `mid = (left + right) // 2` (or `mid = left + (right - left) // 2` to prevent potential overflow for very large arrays).
        * Compare the middle element `array[mid]` with the `target`:
            * If `array[mid] == target`, the target is found; return `mid`.
            * If `array[mid] < target`, the target must be in the right half. Update `left = mid + 1`.
            * If `array[mid] > target`, the target must be in the left half. Update `right = mid - 1`.

3. **Not Found:**
    * If the loop finishes without finding the target (i.e., `left > right`), the target is not present in the array. Return -1 (or an appropriate indicator).

## Example (Python)

```python
def binary_search(array, target):
    """
    Performs a binary search on a sorted array.

    Args:
        array: The sorted array to search in.
        target: The value to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevent potential overflow

        if array[mid] == target:
            return mid  # Target found
        elif array[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found
```

## Time and Space Complexity

* **Time Complexity:** O(log N), where N is the number of elements in the array. Each comparison effectively halves the search space.
* **Space Complexity:**
  * **Iterative Implementation:** O(1) (constant extra space).
  * **Recursive Implementation:** O(log N) in the worst case due to the function call stack, though tail-call optimization can sometimes reduce this to O(1) in languages that support it.

## Advantages

* **Efficiency:** Very efficient for searching in sorted data, significantly faster than linear search for large datasets.
* **Widely Applicable:** Used in many algorithms and data structures (e.g., searching in balanced binary search trees).

## Disadvantages

* **Requires Sorted Data:** The data must be sorted for binary search to work correctly.
* **Not Suitable for Unordered Data:** If the data is not sorted, a linear search or other techniques must be used.

## Variations

* **Finding First/Last Occurrence:** Modified to find the first or last occurrence of a target value in an array that may contain duplicates.
* **Recursive Binary Search:** The algorithm can be implemented recursively, though the iterative version is often preferred for its space efficiency.
* **Lower Bound/Upper Bound:** Finding the index of the first element greater than or equal to (lower bound) or strictly greater than (upper bound) a target value.

## Topic: Binary Search

**Binary Search** is a highly efficient search algorithm that works on **sorted** data structures. It follows a "divide and conquer" strategy to quickly narrow down the possible locations of a target value. 🕵️‍♂️

### Algorithm

1. Compare the target value with the middle element of the sorted collection.
2. If the target matches the middle element, its position is found.
3. If the target is less than the middle element, continue the search on the left half of the collection.
4. If the target is greater than the middle element, continue the search on the right half.
5. Repeat until the value is found or the search interval is empty.

### Complexity

* **Time Complexity:** $O(\\log n)$. With each step, the algorithm halves the size of the search space, making it incredibly fast for large datasets.
* **Space Complexity:** $O(1)$ for the iterative version.

### Prerequisites

* The data collection (e.g., array) **must be sorted**. If it's not sorted, you must sort it first, which typically adds an $O(n \\log n)$ preprocessing step.

## Problems Related to Binary Search

* [209. Minimum Size Subarray Sum](../problems/0209-minimum-size-subarray-sum/README.md)

1. [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
2. [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
3. [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
4. [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
5. [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
6. [704. Binary Search](https://leetcode.com/problems/binary-search/)
7. [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
8. [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
9. [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
