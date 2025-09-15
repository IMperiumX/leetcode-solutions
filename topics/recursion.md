# Recursion

Recursion is a programming technique where a function calls itself within its own definition. A recursive function typically consists of two main parts:

1. **Base Case(s):** One or more conditions that stop the recursion. Without a base case, the function would call itself infinitely, leading to a stack overflow error.
2. **Recursive Step:** The part of the function where it calls itself with a modified input, moving towards the base case.

## How Recursion Works

Each time a function calls itself, a new frame is added to the call stack. This frame contains the function's local variables and parameters for that particular call. When the base case is reached, the function returns a value, and the corresponding frame is removed from the stack. The process continues until the initial call returns, and the stack is empty.

## Advantages of Recursion

* **Elegance and Readability:** Recursive solutions can be more concise and easier to understand for problems that have a naturally recursive structure (e.g., tree traversal, factorial).
* **Problem Decomposition:** Recursion allows you to break down complex problems into smaller, self-similar subproblems.

## Disadvantages of Recursion

* **Stack Overflow:** Excessive recursion depth can lead to a stack overflow error, especially if the base case is not reached or the problem size is too large.
* **Performance Overhead:** Function calls have overhead, so recursive solutions can sometimes be slower than iterative solutions.
* **Memory Usage:** Each recursive call adds a new frame to the call stack, which can consume significant memory for deep recursion.

## Types of Recursion

* **Direct Recursion:** A function calls itself directly.
* **Indirect Recursion:** A function calls another function, which eventually calls the original function.
* **Tail Recursion:** The recursive call is the very last operation performed in the function. Some compilers can optimize tail-recursive functions to avoid stack overflow errors.

## When to Use Recursion

Recursion is well-suited for problems that have a recursive structure, such as:

* Tree and graph traversals
* Divide and conquer algorithms (e.g., merge sort, quicksort)
* Fractals and other self-similar structures
* Combinatorial problems

## LeetCode Problems Related to Recursion

* [21. Merge Two Sorted Lists](0021-merge-two-sorted-lists/README.md)
* [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
* [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
* [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
* [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (Can be done recursively)
* [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
