# Stack

A stack is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed. Think of it like a stack of plates – you add new plates to the top and remove plates from the top as well.

## Key Concepts

- **LIFO (Last-In, First-Out):** The most recently added element is the first to be removed.
- **Push:** The operation of adding an element to the top of the stack.
- **Pop:** The operation of removing the top element from the stack.
- **Peek/Top:** The operation of viewing the top element without removing it.
- **isEmpty:** Checks if the stack is empty.
- **isFull:** Checks if the stack is full (relevant in array-based implementations with a fixed size).

## Operations

- `push(element)`: Adds an element to the top of the stack.
- `pop()`: Removes and returns the top element from the stack.
- `peek()`: Returns the top element without removing it.
- `isEmpty()`: Returns `True` if the stack is empty, `False` otherwise.
- `isFull()`: Returns `True` if the stack is full, `False` otherwise (in fixed-size implementations).

## Time Complexity

- `push()`: O(1)
- `pop()`: O(1)
- `peek()`: O(1)
- `isEmpty()`: O(1)
- `isFull()`: O(1)

## Space Complexity

- O(n), where n is the number of elements in the stack.

## Applications

- **Function Call Stack:** Managing function calls in programming languages.
- **Undo/Redo Functionality:** Implementing undo/redo operations in applications.
- **Expression Evaluation:** Evaluating mathematical expressions (e.g., using postfix notation).
- **Backtracking Algorithms:** Solving problems that involve exploring different paths or choices.
- **Browser History:** Managing the back and forward navigation in web browsers.
- **Depth-First Search (DFS):** Traversing graphs and trees.

## Implementations

- **Array-based:** Using an array to store the elements. Can have a fixed size or be dynamically resizable.
- **Linked List-based:** Using a linked list to store the elements. Allows for dynamic resizing.

## Related LeetCode Problems

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [155. Min Stack](https://leetcode.com/problems/min-stack/)
- [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [3223. Minimum Length of String After Operations](https://leetcode.com/problems/minimum-length-of-string-after-operations/)
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. This means that the last element added to the stack is the first element to be removed.  Think of it like a stack of plates: you add plates to the top, and you remove plates from the top.

## Key Operations

- **Push:** Adds an element to the top of the stack.
- **Pop:** Removes the element from the top of the stack.
- **Peek (or Top):** Returns the value of the element at the top of the stack without removing it.
- **isEmpty:** Checks if the stack is empty.
- **Size:** Returns the number of elements in the stack.

## Common Uses

- **Function Call Stack:**  Stacks are used to manage function calls in most programming languages. When a function is called, its information (local variables, return address, etc.) is pushed onto the stack. When the function returns, its information is popped off the stack.
- **Expression Evaluation:** Stacks can be used to evaluate arithmetic expressions (e.g., infix, postfix, prefix notations).
- **Backtracking Algorithms:** Stacks are often used in backtracking algorithms, where you need to keep track of the path you've taken and potentially "undo" steps.
- **Undo/Redo Functionality:**  Many applications use stacks to implement undo/redo functionality.  Each action is pushed onto a stack, and undoing an action involves popping it from the stack.
- **Balanced Symbol Checking:** As seen in the "Valid Parentheses" problem, stacks are excellent for checking if symbols (parentheses, brackets, braces) are balanced.

## Implementations

Stacks can be implemented using arrays or linked lists.

### Array-Based Implementation

- Fixed or dynamic size.

- Push and pop operations are typically O(1), but resizing an array can be O(n) in some cases.

### Linked List-Based Implementation

- Dynamic size.

- Push and pop operations are O(1).

## LeetCode Problems Related to Stacks

- [20. Valid Parentheses](0020-valid-parentheses/README.md)
- [155. Min Stack](https://leetcode.com/problems/min-stack/)
- [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (Hard)
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)
