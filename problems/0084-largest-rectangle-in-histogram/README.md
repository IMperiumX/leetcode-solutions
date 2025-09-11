**Step 1: Problem Identification**

*   **Prompt 1:** The input describes the "Largest Rectangle in Histogram" problem. This is LeetCode problem 84, classified as Hard.

    *   **Output:** Problem Number: 84, Problem Name: Largest Rectangle in Histogram, Difficulty: Hard

**Step 2: Problem File Creation**

*   Create a directory named `0084-largest-rectangle-in-histogram`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:** I will generate a Python solution. The most efficient approach for this problem uses a monotonic stack.

*File: 0084-largest-rectangle-in-histogram/solution.py*

```python
# 84. Largest Rectangle in Histogram - Monotonic Stack Approach

def largestRectangleArea(heights):
    """
    Calculates the area of the largest rectangle in the histogram.

    Args:
        heights: A list of integers representing the histogram's bar heights.

    Returns:
        The area of the largest rectangle.
    """
    stack = [-1]  # Initialize stack with a sentinel value
    max_area = 0

    for i in range(len(heights)):
        # While the current height is less than the height at the top of the stack,
        # we can calculate the area of a rectangle with the stack top as the smallest height.
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            current_height = heights[stack.pop()]
            current_width = i - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        stack.append(i)

    # Process remaining elements in the stack
    while stack[-1] != -1:
        current_height = heights[stack.pop()]
        current_width = len(heights) - stack[-1] - 1
        max_area = max(max_area, current_height * current_width)

    return max_area
```

**Step 4: Create Related Topic Files**

*File: 0084-largest-rectangle-in-histogram/Arrays.md* (Again, similar to previous files)
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

*   [84. Largest Rectangle in Histogram](./0084-largest-rectangle-in-histogram)
*   [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
*   [15. 3Sum](https://leetcode.com/problems/3sum/)
*    [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
*   [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
```

*File: 0084-largest-rectangle-in-histogram/Stacks.md*
```markdown
# Stacks

Stacks are a fundamental linear data structure that follows the Last-In, First-Out (LIFO) principle.  The last element added to the stack is the first element removed.  Think of a stack of plates – you add plates to the top and remove plates from the top.

## Key Concepts

*   **LIFO (Last-In, First-Out):** The element most recently added to the stack is the first one to be removed.
*   **Push:**  Adding an element to the top of the stack.
*   **Pop:** Removing the element from the top of the stack.
*   **Peek (or Top):**  Retrieving the value of the top element without removing it.
*   **isEmpty:** Checking if the stack is empty.
*   **isFull:** Checking if the stack is full (relevant for array-based implementations with a fixed size).

## Common Stack Operations

*   **push(element):** Adds an element to the top of the stack.
*   **pop():** Removes and returns the top element of the stack.  Raises an error if the stack is empty.
*   **peek():** Returns the top element of the stack without removing it.  Raises an error if the stack is empty.
*   **empty():** Returns `True` if the stack is empty, `False` otherwise.
*   **size():** Returns the number of elements in the stack.

## Implementations

*   **Array-based:** Stacks can be implemented using arrays.  In this case, the stack has a fixed capacity.
*   **Linked List-based:** Stacks can also be implemented using linked lists.  This allows for dynamic resizing.  Each node in the linked list represents an element in the stack.

## Common Stack Applications

*   **Function Call Stack:**  Used by programming languages to manage function calls.
*   **Undo/Redo Functionality:**  Storing previous states of an application.
*   **Expression Evaluation:**  Evaluating arithmetic expressions (e.g., converting infix to postfix notation).
*   **Backtracking Algorithms:**  Exploring different solution paths (e.g., solving mazes).
*   **Depth-First Search (DFS):**  Traversing graphs and trees.
*   **Design Problems:** Implementing specialized stacks, like the Min Stack.

## Related LeetCode Problems
*    [84. Largest Rectangle in Histogram](./0084-largest-rectangle-in-histogram)
*   [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
*   [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
* [155. Min Stack](https://leetcode.com/problems/min-stack/)
*    [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
```
*File: 0084-largest-rectangle-in-histogram/Monotonic_Stack.md*
```markdown
# Monotonic Stack

A monotonic stack is a stack data structure that maintains a specific ordering property among its elements: either monotonically increasing or monotonically decreasing. This means that the elements in the stack are either always increasing (or non-decreasing) from bottom to top, or always decreasing (or non-increasing) from bottom to top.

## Key Concepts

*   **Monotonicity:** The defining characteristic of a monotonic stack is its ordered nature.
*   **Increasing/Decreasing:**  A monotonic stack can be either increasing or decreasing.
    *   **Monotonically Increasing Stack:**  Elements are in increasing (or non-decreasing) order from bottom to top.  If a new element is smaller than the top of the stack, elements are popped from the stack until the new element can be inserted while maintaining the increasing order.
    *   **Monotonically Decreasing Stack:** Elements are in decreasing (or non-increasing) order from bottom to top. If a new element is larger than the top of the stack, elements are popped from the stack until the new element can be inserted while maintaining the decreasing order.
* **Use Cases**: Used to find next greater element or previous greater element

## How Monotonic Stacks Work (Example: Monotonically Increasing)

1.  **Initialization:** Start with an empty stack.
2.  **Iteration:**  Iterate through the input sequence (e.g., an array).
3.  **Comparison:** For each element in the input sequence:
    *   While the stack is not empty and the current element is *smaller* than the element at the top of the stack:
        *   Pop elements from the stack.  (This is where you typically perform calculations or logic related to the problem you're solving.)
    *   Push the current element onto the stack.  (This maintains the increasing order.)

## Applications of Monotonic Stacks

*   **Next Greater Element:** Finding the next greater element for each element in an array.
*   **Previous Greater Element:**  Finding the previous greater element for each element in an array.
*   **Largest Rectangle in Histogram:**  Finding the largest rectangular area in a histogram (LeetCode 84).
*   **Trapping Rain Water:**  Calculating the amount of trapped rainwater (LeetCode 42) - can be solved using other approaches, but a monotonic stack is one option.
*   **Stock Span Problem:**  Calculating the span of stock prices for each day.
*   **Removing K Digits to make smallest number.**

## Advantages of Monotonic Stacks

*   **Efficiency:** Can often solve problems in linear time (O(n)) where a naive approach might take O(n^2).
*   **Maintain Order:**  The inherent ordering property makes them suitable for problems where relative order matters.

## Related LeetCode Problems
*   [84. Largest Rectangle in Histogram](./0084-largest-rectangle-in-histogram)
*   [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
*   [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
*   [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
*   [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/)
*    [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
*  [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits)

```

**Step 5: Problem README Generation**

*File: 0084-largest-rectangle-in-histogram/README.md*

```markdown
# 84. Largest Rectangle in Histogram, Difficulty: Hard

## Problem Description

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

## Approach(es)

### Monotonic Stack Approach

Algorithm:

1.  Initialize an empty stack `stack`. Push a sentinel value -1 onto the stack.  This simplifies the handling of the end of the array.
2.  Initialize `max_area` to 0.
3.  Iterate through the `heights` array (index `i`):
    *   While the stack is not empty and the current height `heights[i]` is less than or equal the height of the bar at the top of the stack (`heights[stack[-1]]`):
        *   Pop the index from the stack (`current_index`).
        *   Calculate the height of the rectangle: `current_height = heights[current_index]`.
        *   Calculate the width of the rectangle: `current_width = i - stack[-1] - 1`.  The width is the distance between the current index `i` and the index of the next smaller element on the left (which is now at the top of the stack).
        *   Update `max_area` with the maximum of its current value and `current_height * current_width`.
    *   Push the current index `i` onto the stack.
4.  After iterating through the entire `heights` array, process any remaining elements in the stack (these represent bars for which we haven't found a smaller bar to their right):
    *   While the stack is not empty and top of stack is not the sentinel value
        *   Pop the index from the stack (`current_index`).
        *   Calculate the height: `current_height = heights[current_index]`.
        *   Calculate the width: `current_width = len(heights) - stack[-1] - 1`. The width extends to the end of the array.
        *   Update `max_area`.
5.  Return `max_area`.

Data Structures:

*   A stack (to maintain a monotonically increasing sequence of bar indices).

Time Complexity:

*   O(n), where n is the length of the `heights` array.  Each element is pushed onto and popped from the stack at most once.

Space Complexity:

*   O(n) in the worst case, where n is the length of the array. This occurs when the heights are in increasing order, and all indices are pushed onto the stack.  On average, the space complexity will be less than O(n).

Trade-offs:

*   The monotonic stack approach is the most efficient solution for this problem, achieving linear time and, on average, less than linear space complexity. It's a clever technique that avoids brute-force comparisons.

## Code

[Monotonic Stack Approach](./solution.py)

## Notes

The core idea behind the monotonic stack approach is to maintain a stack where the bar heights are in increasing order (from bottom to top). When we encounter a bar that is shorter than the bar at the top of the stack, we know that the popped bar's height is the limiting factor for a rectangle extending to the current bar. The stack helps us efficiently find the boundaries (left and right) of that rectangle.  The sentinel value (-1) simplifies the logic by ensuring that the stack is never truly empty and that we process all bars at the end of the iteration.
```

Final Folder Structure

```
0084-largest-rectangle-in-histogram/
├── solution.py
├── README.md
├── Arrays.md
├── Monotonic_Stack.md
└── Stacks.md
```
