# Array

An array is a fundamental data structure in computer science that stores a collection of elements of the same data type in contiguous memory locations. Each element in an array can be accessed directly using its index, which represents its position within the array.

## Key Characteristics

- **Homogeneous Elements:** All elements in an array must be of the same data type (e.g., all integers, all floating-point numbers, or all characters).
- **Contiguous Memory:** Array elements are stored in consecutive memory addresses, which allows for efficient access and traversal.
- **Fixed Size (Typically):** In many programming languages, arrays have a fixed size that is determined at the time of creation. This means the number of elements an array can hold is predetermined and cannot be changed easily during runtime. However, some languages offer dynamic arrays (like Python's lists) that can grow or shrink as needed.
- **Random Access:** Elements can be accessed directly using their index in constant time, O(1). This is because the memory address of any element can be calculated directly from the starting address of the array and the element's index.
- **Zero-Based Indexing:** In most programming languages, array indices start at 0. The first element is at index 0, the second at index 1, and so on.

## Common Operations

- **Access:** Retrieve the value of an element at a specific index.
- **Update:** Modify the value of an element at a specific index.
- **Insertion:** Add a new element at a specific position (this can be complex and inefficient in fixed-size arrays, often requiring shifting existing elements).
- **Deletion:** Remove an element from a specific position (similar to insertion, this can be inefficient in fixed-size arrays).
- **Search:** Find the index of a specific element within the array.
- **Traversal:** Iterate through all elements of the array, typically using a loop.
- **Sorting:** Arrange the elements of the array in a specific order (e.g., ascending or descending).

## Advantages of Arrays

- **Fast Element Access:** Constant-time access to elements using their index.
- **Efficient Traversal:** Iterating through all elements is straightforward and efficient.
- **Simple Implementation:** Arrays are relatively easy to implement and understand.
- **Foundation for Other Data Structures:** Arrays serve as the building blocks for more complex data structures like stacks, queues, and hash tables.

## Disadvantages of Arrays

- **Fixed Size (in many cases):** Resizing an array can be computationally expensive.
- **Inefficient Insertions and Deletions:** Inserting or deleting elements in the middle of an array can require shifting many elements, which is inefficient.
- **Memory Overhead (potentially):** If an array is allocated with a large size but only a small portion is used, it can lead to wasted memory.

## When to Use Arrays

- When you need to store and access a collection of elements of the same data type.
- When fast element access is a priority.
- When the number of elements is known in advance (for fixed-size arrays).
- When you need a simple and efficient data structure for basic operations.

## Related LeetCode Problems

- [1. Two Sum](./../problems/0001-two-sum/README.md)
- [15. 3Sum](./0015-3sum/README.md)
- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [27. Remove Element](https://leetcode.com/problems/remove-element/)

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [238. Product of Array Except Self](./../problems/0238-product-of-array-except-self/README.md)
- [36. Valid Sudoku](./../problems/0036-valid-sudoku/README.md)
- [128. Longest Consecutive Sequence](./../problems/0128-longest-consecutive-sequence/README.md)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](./../problems/0689-maximum-sum-of-3-non-overlapping-subarrays/README.md)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)
