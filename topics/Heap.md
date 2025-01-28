# Heap (Priority Queue)

A heap is a specialized tree-based data structure that satisfies the heap property. It is commonly used to implement priority queues. The heap property states that for a **min-heap**, the value of each node is less than or equal to the value of its children. For a **max-heap**, the value of each node is greater than or equal to the value of its children.

## Key Concepts

- **Heap Property:**
  - **Min-Heap:** The value of each node is less than or equal to the value of its children. The minimum element is at the root.
  - **Max-Heap:** The value of each node is greater than or equal to the value of its children. The maximum element is at the root.
- **Complete Binary Tree:** A binary tree in which all levels are completely filled except possibly the last level, which is filled from left to right. Heaps are typically implemented using complete binary trees.
- **Array Representation:** Heaps are often efficiently represented using arrays, where:
  - The root is at index 0.
  - The children of the node at index `i` are at indices `2i + 1` (left child) and `2i + 2` (right child).
  - The parent of the node at index `i` is at index `(i - 1) // 2`.

## Operations

- **insert(element):** Inserts an element into the heap.
    1. Add the element to the end of the array (bottom of the heap).
    2. "Bubble up" the element to its correct position by repeatedly comparing it with its parent and swapping if necessary (to maintain the heap property).
- **extractMin() / extractMax():** Removes and returns the minimum/maximum element (root) from the heap.
    1. Swap the root with the last element in the array.
    2. Remove the last element (which was the original root).
    3. "Bubble down" (or "heapify") the new root to its correct position by repeatedly comparing it with its children and swapping with the smaller/larger child if necessary (to maintain the heap property).
- **peek():** Returns the minimum/maximum element (root) without removing it.
- **heapify(array):** Builds a heap from an unsorted array.
    1. Start from the last non-leaf node (index `n//2 - 1`).
    2. "Bubble down" each node from that point down to the root to its correct position to satisfy the heap property.

## Time Complexity

- **insert(element):** O(log n)
- **extractMin() / extractMax():** O(log n)
- **peek():** O(1)
- **heapify(array):** O(n)

## Space Complexity

- O(n) to store the heap (in the array representation).

## Applications

- **Priority Queues:** Implementing priority queues, where elements are processed based on their priority.
- **Heap Sort:** A sorting algorithm that uses a heap to sort an array.
- **Finding the kth smallest/largest element in an array.**
- **Graph algorithms (e.g., Dijkstra's shortest path, Prim's minimum spanning tree).**
- **Load balancing.**
- **Median maintenance.**

## Trade-offs

- **Advantages:**
  - Efficient insertion and extraction of the minimum/maximum element (O(log n)).
  - Relatively efficient to build a heap from an unsorted array (O(n)).
- **Disadvantages:**
  - Searching for an arbitrary element is not efficient (O(n)).
  - Not as versatile as other data structures like balanced binary search trees for operations other than finding/removing the minimum/maximum.

## Related LeetCode Problems

- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
