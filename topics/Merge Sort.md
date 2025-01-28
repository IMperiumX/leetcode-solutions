# Merge Sort

Merge Sort is an efficient, general-purpose, comparison-based sorting algorithm. It is a divide-and-conquer algorithm that was invented by John von Neumann in 1945.

## Key Concepts

- **Divide and Conquer:** Merge Sort follows the divide-and-conquer paradigm:
  - **Divide:** Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
  - **Conquer:** Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
- **Merging:** The core operation of Merge Sort is the merging of two sorted sublists into a single sorted list. This is done by repeatedly comparing the smallest elements of the two sublists and adding the smaller one to the merged list.

## Algorithm

1. **Divide:** If the list has more than one element, divide it into two halves.
2. **Conquer:** Recursively sort the two halves using Merge Sort.
3. **Combine (Merge):** Merge the two sorted halves into a single sorted list.

```python
def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)  # Recursive sort on the left half
    merge_sort(right_half) # Recursive sort on the right half

    i = j = k = 0  # Pointers for left_half, right_half, and merged array

    # Merge the two sorted halves
    while i < len(left_half) and j < len(right_half):
      if left_half[i] <= right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
      k += 1

    # Copy any remaining elements from the left half
    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1

    # Copy any remaining elements from the right half
    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1
```

## Time Complexity

- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n)

## Space Complexity

- **Standard Implementation:** O(n) (due to the temporary arrays used in the merge step)
- **Optimized (in-place) Implementations:** O(log n) or O(1) (more complex to implement)

## Applications

- **General-purpose sorting:** Merge Sort is a stable and efficient sorting algorithm suitable for various data types.
- **External sorting:** When the data to be sorted does not fit in memory, Merge Sort can be adapted to work with data stored on disk.
- **Inversion counting:** Merge Sort can be modified to count the number of inversions in a list (pairs of elements that are out of order).

## Trade-offs

- **Advantages:**
  - Stable sort (preserves the relative order of equal elements).
  - Guaranteed O(n log n) time complexity in all cases.
  - Suitable for external sorting.
- **Disadvantages:**
  - Higher space complexity than some other in-place sorting algorithms (e.g., QuickSort) in the standard implementation.
  - Can be slightly slower than QuickSort in practice for some inputs, especially for small arrays or nearly sorted arrays.

## Related LeetCode Problems

- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [148. Sort List](https://leetcode.com/problems/sort-list/)
- [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
- [327. Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)
- [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
