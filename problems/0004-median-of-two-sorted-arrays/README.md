**Step 1: Problem Identification**

*   **Prompt 1:** The input describes the "Median of Two Sorted Arrays" problem, requiring an O(log(m+n)) solution. This is LeetCode problem 4, classified as Hard.

    *   **Output:** Problem Number: 4, Problem Name: Median of Two Sorted Arrays, Difficulty: Hard

**Step 2: Problem File Creation**

*   Create a directory named `0004-median-of-two-sorted-arrays`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:** I'll generate a Python solution. The O(log(m+n)) time complexity requirement strongly suggests a binary search-based approach.

*File: 0004-median-of-two-sorted-arrays/solution.py*

```python
# 4. Median of Two Sorted Arrays - Binary Search Approach

def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the shorter array

    m, n = len(nums1), len(nums2)
    low = 0
    high = m

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX

        maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
        minRightX = nums1[partitionX] if partitionX < m else float('inf')

        maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
        minRightY = nums2[partitionY] if partitionY < n else float('inf')

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:  # Even total length
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:  # Odd total length
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
```

**Step 4: Create Related Topics File**

*File: 0004-median-of-two-sorted-arrays/Arrays.md* (Similar to previous ones, but included)
```markdown
# Arrays

Arrays are fundamental data structures in computer science. They store collections of elements of the same data type, accessed using indices.  Understanding arrays is crucial for solving a wide variety of problems, particularly on platforms like LeetCode.

## Key Concepts

*   **Contiguous Memory:** Array elements are stored in contiguous memory locations. This allows for efficient access to elements using their index (O(1) access time).
*   **Zero-Based Indexing:**  In most programming languages, array indices start at 0.  The first element is at index 0, the second at index 1, and so on.
*   **Fixed Size (in some languages):**  In languages like C/C++, arrays have a fixed size determined at compile time.  Dynamic arrays (like Python lists) can resize automatically.
*   **Mutability:** Arrays are typically mutable, meaning you can change the values of their elements after they are created.

## Common Array Operations

*   **Accessing Elements:**  Retrieving the value at a specific index (e.g., `arr[3]`).
*   **Updating Elements:**  Changing the value at a specific index (e.g., `arr[2] = 5`).
*   **Iteration:**  Looping through all elements of the array.
*   **Searching:**  Finding a specific element within the array (linear search, binary search on sorted arrays).
*   **Sorting:**  Arranging the elements in a specific order (ascending, descending).  Common sorting algorithms include bubble sort, insertion sort, merge sort, and quicksort.
*   **Insertion/Deletion:** Adding or removing elements (more complex in fixed-size arrays, easier with dynamic arrays).

## Common Array Patterns in LeetCode

*   **Two Pointers:** Using two indices to traverse the array, often from opposite ends or moving at different speeds.
*   **Sliding Window:** Maintaining a "window" of elements within the array and moving it across the array.
*   **Prefix Sum:** Calculating the cumulative sum of elements up to each index, useful for range queries.
*   **Kadane's Algorithm:** Finding the maximum sum of a contiguous subarray.

## Related LeetCode Problems

*   [4. Median of Two Sorted Arrays](./0004-median-of-two-sorted-arrays)
*   [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
*   [15. 3Sum](https://leetcode.com/problems/3sum/)
*    [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
*   [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
```

*File: 0004-median-of-two-sorted-arrays/Binary_Search.md*

```markdown
# Binary Search

Binary Search is a highly efficient search algorithm used to find the position of a target value within a **sorted** array (or list). It works by repeatedly dividing the search interval in half. If the middle element matches the target, the search is successful. If the target is less than the middle element, the search continues in the left half; otherwise, it continues in the right half.

## Key Concepts

*   **Sorted Input:** Binary search *requires* the input array to be sorted.
*   **Divide and Conquer:** The algorithm repeatedly divides the search interval in half.
*   **Logarithmic Time Complexity:**  The time complexity of binary search is O(log n), where n is the number of elements in the array.  This makes it significantly faster than linear search (O(n)) for large datasets.

## Algorithm

1.  **Initialization:**
    *   Set `low` to 0 (the index of the first element).
    *   Set `high` to n-1 (the index of the last element).
2.  **Iteration:** While `low` is less than or equal to `high`:
    *   Calculate the middle index: `mid = (low + high) // 2`  (using integer division).
    *   **Comparison:**
        *   If `arr[mid]` is equal to the target, return `mid` (target found).
        *   If `arr[mid]` is less than the target, set `low = mid + 1` (search in the right half).
        *   If `arr[mid]` is greater than the target, set `high = mid - 1` (search in the left half).
3.  **Target Not Found:** If the loop finishes without finding the target (i.e., `low` becomes greater than `high`), return -1 (or another appropriate indicator that the target is not present).

## Advantages of Binary Search

*   **Efficiency:**  O(log n) time complexity makes it very fast for large sorted arrays.
*   **Simple Implementation:** Relatively straightforward to implement, both iteratively and recursively.

## Disadvantages of Binary Search

*   **Requires Sorted Input:** The input array must be sorted, which may require a pre-processing step (e.g., sorting the array).
* **Not applicable on linked lists**

## Variations

*   **Finding the First/Last Occurrence:**  Modified versions of binary search can be used to find the first or last occurrence of a target value in an array that may contain duplicates.
*   **Finding the Closest Element:**  Binary search can be adapted to find the element closest to a given target value.
*   **Searching in Rotated Sorted Arrays:**  Specialized binary search techniques can be used to search in arrays that have been sorted and then rotated.

## Related LeetCode Problems
*   [4. Median of Two Sorted Arrays](./0004-median-of-two-sorted-arrays)
*   [704. Binary Search](https://leetcode.com/problems/binary-search/)
*   [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
*   [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
*   [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
*   [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
*    [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

```

*File: 0004-median-of-two-sorted-arrays/Divide_and_Conquer.md*

```markdown
# Divide and Conquer

Divide and Conquer is a powerful algorithmic paradigm that solves a problem by recursively breaking it down into smaller subproblems of the same type, solving those subproblems, and then combining their solutions to solve the original problem.

## Key Concepts

*   **Divide:** Break the problem into smaller, independent subproblems of the same type.
*   **Conquer:** Solve the subproblems recursively.  If the subproblems are small enough, solve them directly (this is the base case of the recursion).
*   **Combine:** Combine the solutions of the subproblems to obtain the solution to the original problem.

## Common Characteristics of Divide and Conquer Algorithms

*   **Recursive Structure:**  Divide and Conquer algorithms are naturally expressed recursively.
*   **Independent Subproblems:** The subproblems should be independent of each other; there should be no overlap between them.  (If there is overlap, dynamic programming might be a better approach.)
*   **Non-Trivial Combination Step:** The step of combining the subproblem solutions is often non-trivial and requires careful design.

## Examples of Divide and Conquer Algorithms

*   **Merge Sort:** Sorts an array by recursively dividing it into two halves, sorting each half, and then merging the sorted halves.
*   **Quicksort:** Sorts an array by selecting a pivot element, partitioning the array into elements less than and greater than the pivot, and recursively sorting the two partitions.
*   **Binary Search:** Searches for a target value in a sorted array by repeatedly dividing the search interval in half.
*   **Closest Pair of Points:** Finds the closest pair of points in a set of points in a plane.
*   **Strassen's Matrix Multiplication:** Multiplies two matrices faster than the naive algorithm.

## Advantages of Divide and Conquer

*   **Efficiency:**  Can often lead to more efficient algorithms than brute-force approaches.  For example, merge sort and quicksort have O(n log n) time complexity, which is significantly better than the O(n^2) complexity of simple sorting algorithms like bubble sort.
*   **Parallelism:**  The independent subproblems can often be solved in parallel, leading to further performance improvements on multi-core processors.
*   **Conceptual Clarity:**  Can provide a clear and elegant way to solve complex problems.

## Disadvantages of Divide and Conquer

*   **Recursion Overhead:**  Recursive calls have some overhead, which can be significant for very small subproblems.
*   **Complexity of Combination Step:** The combination step can sometimes be complex to implement.
*   **Not Always Applicable:** Not all problems can be efficiently solved using Divide and Conquer.

## Related LeetCode Problems

*    [4. Median of Two Sorted Arrays](./0004-median-of-two-sorted-arrays)
*   [169. Majority Element](https://leetcode.com/problems/majority-element/) (can be solved with Divide and Conquer, though Boyer-Moore is more efficient)
*   [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (tree traversals can be viewed as Divide and Conquer)
*   [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
* [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (can be solved with Divide and Conquer, though Kadane's Algorithm is more efficient)
```

**Step 5: Problem README Generation**

*File: 0004-median-of-two-sorted-arrays/README.md*

```markdown
# 4. Median of Two Sorted Arrays, Difficulty: Hard

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

## Approach(es)

### Binary Search Approach

Algorithm:

1.  **Handle Unequal Lengths:** Ensure that `nums1` is the shorter array (swap them if necessary).  This simplifies the logic.
2.  **Binary Search on Shorter Array:** Perform binary search on the shorter array (`nums1`).  The goal is to find the correct "partition" in both arrays.
    *   `low = 0`, `high = m` (length of `nums1`)
3.  **Partition Calculation:** In each iteration of the binary search:
    *   `partitionX = (low + high) // 2` (partition index in `nums1`)
    *   `partitionY = (m + n + 1) // 2 - partitionX` (corresponding partition index in `nums2`).  The `(m + n + 1) // 2` ensures correct handling of both even and odd total lengths.
4.  **Find Max/Min Elements:**  Find the following four elements:
    *   `maxLeftX`: The maximum element in the left partition of `nums1` (or negative infinity if the partition is empty).
    *   `minRightX`: The minimum element in the right partition of `nums1` (or positive infinity if the partition is empty).
    *   `maxLeftY`: The maximum element in the left partition of `nums2`.
    *   `minRightY`: The minimum element in the right partition of `nums2`.
5.  **Check for Correct Partition:**  If `maxLeftX <= minRightY` and `maxLeftY <= minRightX`, we have found the correct partition.  This means all elements in the left partitions are less than or equal to all elements in the right partitions.
    *   **Even Total Length:** If `(m + n)` is even, the median is the average of `max(maxLeftX, maxLeftY)` and `min(minRightX, minRightY)`.
    *   **Odd Total Length:** If `(m + n)` is odd, the median is `max(maxLeftX, maxLeftY)`.
6.  **Adjust Search Range:** If the partition is not correct:
    *   If `maxLeftX > minRightY`, it means we need to move the partition in `nums1` to the left (decrease `high`).
    *   Else (`maxLeftY > minRightX`), move the partition in `nums1` to the right (increase `low`).
7.  **Loop Termination:** The loop continues until `low <= high`.

Data Structures:

*   No extra data structures are used beyond a few variables.

Time Complexity:

*   O(log(min(m, n))), where m and n are the lengths of the input arrays.  We perform binary search on the shorter array.

Space Complexity:

*   O(1), as we use only a constant amount of extra space.

Trade-offs:

*   This binary search approach is the most efficient way to solve this problem, achieving the required logarithmic time complexity. It can be a bit tricky to implement correctly, especially handling edge cases and the partitioning logic.

## Code

[Binary Search Approach](./solution.py)

## Notes

This problem is a classic example of using binary search in a non-obvious way.  The key idea is to find the correct partition in the two sorted arrays such that all elements to the left of the partitions are less than or equal to all elements to the right.  Understanding the partitioning logic and how to adjust the search range based on the comparison of `maxLeftX`, `minRightX`, `maxLeftY`, and `minRightY` is crucial.
```
Final File Structure:

```
0004-median-of-two-sorted-arrays/
├── solution.py
├── README.md
├── Arrays.md
├── Binary_Search.md
└── Divide_and_Conquer.md
```
