# Recursion

Recursion is a powerful programming technique where a function calls itself within its own definition. It's a fundamental concept in computer science, often used to solve problems that can be broken down into smaller, self-similar subproblems.

A recursive function typically consists of two main parts:

1. **Base Case(s):** One or more conditions that stop the recursion. Without a base case, the function would call itself infinitely, leading to a stack overflow error.
2. **Recursive Step:** The part of the function where it calls itself with a modified input, moving towards the base case.

## How Recursion Works

Each time a function calls itself, a new frame is added to the call stack. This frame contains the function's local variables and parameters for that particular call. When the base case is reached, the function returns a value, and the corresponding frame is removed from the stack. The process continues until the initial call returns, and the stack is empty.

1. **Function Call:** When a recursive function is called, a new frame is added to the call stack. This frame stores the function's local variables and parameters for that particular invocation.
2. **Recursive Calls:** The function calls itself repeatedly, with each call creating a new stack frame.
3. **Base Case Reached:** When the base case is met, the function returns a value without making further recursive calls.
4. **Unwinding the Stack:** As each recursive call returns, its corresponding stack frame is removed from the call stack, and the execution flow returns to the previous call.  Values are returned up the stack until the initial call is reached.

## Advantages of Recursion

* **Elegance and Readability:** Recursive solutions can be more concise and easier to understand for problems that have a naturally recursive structure (e.g., tree traversal, factorial).
* **Problem Decomposition:** Recursion allows you to break down complex problems into smaller, self-similar subproblems.

## Disadvantages of Recursion

* **Stack Overflow:** Excessive recursion depth can lead to a stack overflow error, especially if the base case is not reached or the problem size is too large.
* **Performance Overhead:** Function calls have overhead, so recursive solutions can sometimes be slower than iterative solutions.
* **Memory Usage:** Each recursive call adds a new frame to the call stack, which can consume significant memory for deep recursion.
* **Debugging:** Debugging recursive functions can be more challenging than debugging iterative code.

## Types of Recursion

* **Direct Recursion:** A function calls itself directly.
* **Indirect Recursion:** A function calls another function, which eventually calls the original function.
* **Tail Recursion:** The recursive call is the very last operation performed in the function. Some compilers can optimize tail-recursive functions to avoid stack overflow errors.

## Common Recursive Patterns

* **Divide and Conquer:** Breaking a problem into smaller subproblems, solving them recursively, and combining the results (e.g., merge sort, quicksort).
* **Tree Traversal:** Visiting all nodes in a tree using inorder, preorder, or postorder traversal.
* **Backtracking:** Exploring all possible solutions by trying out different choices and undoing them if they don't lead to a solution (e.g., solving Sudoku, N-Queens problem).
* **Dynamic Programming (with Memoization):** Storing the results of expensive function calls and reusing them for the same inputs, often used in recursive solutions to improve performance.

## When to Use Recursion

Recursion is well-suited for problems that have a recursive structure, such as:

* Tree and graph traversals
* Divide and conquer algorithms (e.g., merge sort, quicksort)
* Fractals and other self-similar structures
* Combinatorial problems

## LeetCode Problems Related to Recursion

* [21. Merge Two Sorted Lists](../problems/0021-merge-two-sorted-lists/README.md)
* [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (Can be done recursively)
* [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (can be solved recursively with memoization)
* [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
* [100. Same Tree](../problems/0100-same-tree/README.md)
* [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
* [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)
* [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

# Recursion

## Explanation

Recursion is a programming technique where a function calls itself within its own definition.  It's a powerful way to solve problems that can be broken down into smaller, self-similar subproblems.

**Key Components:**

1. **Base Case(s):**  One or more conditions that stop the recursion.  Without base cases, the function would call itself indefinitely, leading to a stack overflow error.
2. **Recursive Step:** The part of the function where it calls itself, usually with modified input that brings it closer to a base case.

**How it Works:**

Each time a function calls itself, a new "frame" is added to the call stack.  This frame stores the function's local variables and the point to return to after the recursive call completes. When a base case is reached, the function returns a value, and the frames are popped off the stack one by one, with each return value potentially being used in the calling function.

**Example: Factorial**

```python
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive step: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)
```

**Advantages:**

* **Elegance and Readability:** Recursive solutions can often be more concise and easier to understand than iterative solutions for problems with a naturally recursive structure.
* **Problem Decomposition:** Recursion naturally breaks down complex problems into smaller, more manageable subproblems.

**Disadvantages:**

* **Stack Overflow:**  Excessive recursion (too many nested calls) can lead to a stack overflow error if the call stack runs out of space.
* **Performance Overhead:** Function calls can have some overhead, so recursive solutions can sometimes be slower than iterative solutions, especially if the recursion depth is large.  However, tail-call optimization (available in some languages) can mitigate this.
* **Debugging:**  Debugging recursive functions can sometimes be more challenging than debugging iterative code.

**Types of Recursion:**

* **Direct Recursion:** A function calls itself directly.
* **Indirect Recursion:**  A function calls another function, which eventually calls the first function (forming a cycle).
* **Tail Recursion:**  The recursive call is the very last operation performed in the function.  Tail-recursive functions can often be optimized by compilers to avoid stack growth.
* **Non-Tail Recursion:** The recursive call is not the last operation (e.g., there's a calculation after the recursive call).

**Common Applications:**

* **Tree Traversal:** (Preorder, Inorder, Postorder)
* **Graph Traversal:** (Depth-First Search)
* **Divide and Conquer Algorithms:** (Merge Sort, Quick Sort)
* **Fractals:** Generating self-similar patterns.
* **Mathematical Functions:** (Factorial, Fibonacci sequence)
* **Backtracking.**

**Example Problem**

* [22. Generate Parentheses](./0022-generate-parentheses/README.md)
