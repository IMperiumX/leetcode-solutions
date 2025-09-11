Okay, let's create the LeetCode solution repository for "Basic Calculator II".

**Step 1: Problem Identification**

*   **Prompt 1**: "Identify the LeetCode problem from the following input: `227. Basic Calculator II ... [rest of the problem description]`."

*   **Output**: "Problem Number: 227, Problem Name: Basic Calculator II, Difficulty: Medium"

**Step 2: Problem File Creation**

*   Create a directory named `0227-basic-calculator-ii`.

**Step 3: Solution File Generation**

*   **Prompt 3.2**: "Generate solutions in Python for the LeetCode problem: `Basic Calculator II` (Number: `227`). The solutions should be well-commented. Create files named `solution.py`..."

    *   I will implement a solution using a stack. This is a common and efficient approach for evaluating expressions with operator precedence.

    *   **`solution.py` (Stack Approach):**

    ```python
    # 227. Basic Calculator II - Stack Approach

    def calculate(s: str) -> int:
        """
        Evaluates an expression string and returns its value.

        Args:
            s: The expression string.

        Returns:
            The result of the expression.
        """
        if not s:
            return 0

        stack = []
        num = 0
        sign = '+'  # Initialize the sign to '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Accumulate digits

            if char in '+-*/' or i == len(s) - 1:  # Operator or end of string
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # Integer division, truncate towards zero
                    stack.append(int(stack.pop() / num))

                sign = char  # Update the sign
                num = 0  # Reset num

        return sum(stack)  # Sum up all the numbers in the stack
    ```

**Step 4: Problem README Generation**

*   **Prompt 4**: "Generate a `README.md` file for the problem: `Basic Calculator II` (Number: `227`, Difficulty: `Medium`)."

    *   **`README.md`:**

    ```markdown
    # 227. Basic Calculator II, Difficulty: Medium

    ## Problem Description

    Given a string `s` which represents an expression, evaluate this expression and return its value.

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate results will be in the range of [-2<sup>31</sup>, 2<sup>31</sup> - 1].

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

    Example 1:

    Input: s = "3+2*2"
    Output: 7

    Example 2:

    Input: s = " 3/2 "
    Output: 1

    Example 3:

    Input: s = " 3+5 / 2 "
    Output: 5

    Constraints:

    1 <= s.length <= 3 * 10<sup>5</sup>
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 2<sup>31</sup> - 1].
    The answer is guaranteed to fit in a 32-bit integer.

    ## Approach(es)

    ### Stack Approach

    Algorithm:

    1.  **Initialization:**
        *   If the input string `s` is empty, return 0.
        *   Initialize an empty stack `stack`.
        *   Initialize `num` to 0. This variable will store the current number being parsed.
        *   Initialize `sign` to '+'.  This variable stores the *previous* operator encountered.  We start with '+' so that the first number is effectively added to the stack.

    2.  **Iterate through the String:**
        *   Iterate through the input string `s` character by character (with index `i`).
        *   **Digit:** If the current character `char` is a digit, update `num` by multiplying it by 10 and adding the digit's integer value (`num = num * 10 + int(char)`).
        *   **Operator or End of String:** If `char` is an operator ('+', '-', '*', '/') or we've reached the end of the string (`i == len(s) - 1`):
            *   **Apply Previous Operator:** Based on the *previous* operator (`sign`):
                *   `'+'`: Push `num` onto the stack.
                *   `'-'`: Push `-num` onto the stack (negate the number).
                *   `'*'`: Pop the top element from the stack, multiply it by `num`, and push the result back onto the stack.
                *   `'/'`: Pop the top element from the stack, perform integer division by `num` (using `int()` for truncation towards zero), and push the result back onto the stack.
            *   **Update `sign`:** Set `sign` to the current operator `char`.
            *   **Reset `num`:** Reset `num` to 0 to start accumulating the next number.

    3.  **Calculate Result:** After processing the entire string, the stack will contain a series of numbers that need to be added together.  Return the sum of the elements in the stack (`sum(stack)`).

    Data Structures:

    -   Stack: Used to handle operator precedence.

    Time Complexity:

    -   O(n), where n is the length of the string `s`. We iterate through the string once.

    Space Complexity:

    -   O(n) in the worst case, where the stack might store all the numbers if there are no multiplication or division operations (e.g., "1+2+3+4").  On average, the space complexity is likely to be less than O(n).

    Trade-offs:
    - Using stack allows us handle operator precedence correctly

    ## Code

    [Stack Approach](./solution.py)

    ## Notes (Optional)

    -   The key idea is to use a stack to handle the precedence of operators. Multiplication and division have higher precedence than addition and subtraction.  We effectively "delay" the addition and subtraction operations by pushing numbers onto the stack, and we perform multiplication and division immediately.
    - The `sign` variable stores the *previous* operator, not the current one.  This is important for correctly applying the operations in the right order.
    - The integer division (`//` in Python) truncates towards negative infinity.  We use `int(a / b)` to ensure truncation towards zero, as required by the problem.
    ```
- Topic Extraction
```markdown
# Stack

A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle.  This means that the last element added to the stack is the first element removed.  Think of it like a stack of plates: you can only add or remove plates from the top.

Key Characteristics:

-   **LIFO (Last-In, First-Out):** The most recently added element is the first one to be retrieved.
-   **Restricted Access:**  You can only access the top element of the stack.  You can't directly access elements in the middle or at the bottom.
-   **Simple Operations:** Stacks typically support a small set of operations: `push`, `pop`, `peek` (or `top`), and sometimes `isEmpty` and `size`.

Common Operations and Time Complexities:

-   **push(element):** Adds an element to the top of the stack.  O(1)
-   **pop():** Removes and returns the element at the top of the stack.  O(1)
-   **peek() (or top()):** Returns the element at the top of the stack *without* removing it.  O(1)
-   **isEmpty():** Checks if the stack is empty.  O(1)
-   **size():** Returns the number of elements in the stack. O(1)

Use Cases:

-   **Function Call Stack:**  Managing function calls in programming languages (tracking local variables, return addresses, etc.).
-   **Expression Evaluation:**  Evaluating mathematical expressions (like in a calculator).
-   **Undo/Redo Functionality:** Implementing undo and redo operations in applications.
-   **Backtracking Algorithms:**  Algorithms that explore different possibilities (e.g., solving mazes, depth-first search).
-   **Browser History:**  Keeping track of visited web pages.
- **Basic Calculator:**  Evaluating mathematical expression as in this problem.

Related LeetCode Problems:

*   [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
```
All necessary files (`solution.py`, `README.md`, `Stack.md`) are created inside the `0227-basic-calculator-ii` directory. The README correctly links to the solution file. The explanation and analysis are thorough and correct. The topic file is well-explained.
