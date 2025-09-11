**Step 1: Problem Identification**

*   **Prompt 1:** The problem describes the "Min Stack" problem, requiring a stack implementation that supports constant-time retrieval of the minimum element, in addition to standard stack operations. This corresponds to LeetCode problem 155, which is classified as Medium.

    *   **Output:** Problem Number: 155, Problem Name: Min Stack, Difficulty: Medium

**Step 2: Problem File Creation**

*   Create a directory named `0155-min-stack`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:** Since no code was provided, I will generate a Python solution. The key to achieving O(1) for all operations is to maintain an auxiliary stack that tracks the minimum elements.  I'll present two main approaches:
    1.  **Two Stacks:**  A standard stack and a separate stack to keep track of minimums.
    2.  **One Stack with (value, min) pairs:**  Store both the value and the current minimum in a single stack.  This approach can save space in some cases.

*File: 0155-min-stack/solution_two_stacks.py*

```python
# 155. Min Stack - Two Stacks Approach

class MinStack:

    def __init__(self):
        """
        Initializes the stack object.
        """
        self.stack = []
        self.min_stack = []  # Stores minimums

    def push(self, val):
        """
        Pushes the element val onto the stack.
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Removes the element on the top of the stack.
        :rtype: None
        """
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        Gets the top element of the stack.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]

```

*File: 0155-min-stack/solution_one_stack.py*

```python
# 155. Min Stack - One Stack with (value, min) Pairs

class MinStack:

    def __init__(self):
        """
        Initializes the stack object.
        """
        self.stack = []  # Stores (value, current_minimum) pairs

    def push(self, val):
        """
        Pushes the element val onto the stack.
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self):
        """
        Removes the element on the top of the stack.
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        Gets the top element of the stack.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]


    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
```

**Step 4: Create Related Topics File**

*File: 0155-min-stack/Stacks.md*

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

*   [155. Min Stack](./0155-min-stack)
*   [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
*   [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
*   [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
```

**Step 5: Problem README Generation**

*File: 0155-min-stack/README.md*

```markdown
# 155. Min Stack, Difficulty: Medium

## Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

*   `MinStack()` initializes the stack object.
*   `void push(int val)` pushes the element `val` onto the stack.
*   `void pop()` removes the element on the top of the stack.
*   `int top()` gets the top element of the stack.
*   `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

## Approach(es)

### Two Stacks Approach

Algorithm:

1.  Use two stacks:
    *   `stack`:  The main stack to store all elements.
    *   `min_stack`: An auxiliary stack to store the minimum elements encountered so far.
2.  **push(val):**
    *   Push `val` onto `stack`.
    *   If `min_stack` is empty or `val` is less than or equal to the top element of `min_stack`, push `val` onto `min_stack`.
3.  **pop():**
    *   Pop from `stack`.
    *   If the popped value is equal to the top element of `min_stack`, pop from `min_stack` as well.
4.  **top():**
    *   Return the top element of `stack`.
5.  **getMin():**
    *   Return the top element of `min_stack`.

Data Structures:

*   Two stacks: `stack` and `min_stack`.

Time Complexity:

*   All operations (push, pop, top, getMin): O(1).

Space Complexity:

*   O(n) in the worst case, where n is the number of elements pushed onto the stack. This occurs when all elements are pushed in decreasing order, causing all elements to be stored in both `stack` and `min_stack`.  On average, the space complexity might be less than O(n) if there are many increasing sequences.

Trade-offs:

*   This approach is straightforward and achieves the required O(1) time complexity for all operations. It uses extra space for the `min_stack`.

### One Stack with (value, min) Pairs

Algorithm:

1.  Use a single stack (`stack`) to store pairs of values: `(value, current_minimum)`.
2.  **push(val):**
    *   If `stack` is empty, push `(val, val)` onto the stack.
    *   Otherwise, get the current minimum from the top of the stack (`stack[-1][1]`).  Push `(val, min(val, current_minimum))` onto the stack.
3.  **pop():**
    *   Pop from `stack`.
4.  **top():**
    *   Return the first element of the top pair on the stack (`stack[-1][0]`).
5.  **getMin():**
    *   Return the second element of the top pair on the stack (`stack[-1][1]`).

Data Structures:

*   A single stack to store (value, current_minimum) pairs.

Time Complexity:

*   All operations (push, pop, top, getMin): O(1).

Space Complexity:

*   O(n), where n is the number of elements pushed onto the stack.  We store two values (value and current minimum) for each element.

Trade-offs:

*  This approach also achieves O(1) time complexity for all operations. It might save space compared to the two-stack approach if there are long increasing sequences of numbers, but in the worst case it will use roughly same memory.

## Code

[Two Stacks Approach](./solution_two_stacks.py)

[One Stack with (value, min) Pairs](./solution_one_stack.py)

## Notes

The key to solving this problem efficiently is to find a way to track the minimum element without having to search the entire stack. Both the two-stack and one-stack approaches achieve this by storing additional information alongside the main stack elements. The two-stacks approach is often slightly more intuitive, while the one-stack approach can be more space-efficient in some scenarios.
```
Final Folder Structure:
```
0155-min-stack/
├── solution_one_stack.py
├── solution_two_stacks.py
├── README.md
└── Stacks.md
```
