Okay, let's create the LeetCode solution repository for problem 50, "Pow(x, n)".

**Step 1: Problem Identification**

*   **Problem Number:** 50
*   **Problem Name:** Pow(x, n)
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

Create directory: `0050-powx-n`

**Step 3: Solution File Generation**

We'll provide two solutions:

1.  **Binary Exponentiation (Iterative):**  A very efficient approach.
2.  **Binary Exponentiation (Recursive):** The same core logic, but implemented recursively.

**solution_iterative.py:**

```python
# 0050. Pow(x, n) - Binary Exponentiation (Iterative)

def myPow(x: float, n: int) -> float:
    """
    Calculates x raised to the power n (x^n) using iterative binary exponentiation.

    Args:
        x: The base.
        n: The exponent.

    Returns:
        x^n
    """
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    current_product = x
    while n > 0:
        if n % 2 == 1:  # If n is odd
            result *= current_product
        current_product *= current_product  # Square the current product
        n //= 2  # Integer division (equivalent to right bit shift)

    return result
```

**solution_recursive.py:**

```python
# 0050. Pow(x, n) - Binary Exponentiation (Recursive)

def myPow(x: float, n: int) -> float:
    """
    Calculates x raised to the power n (x^n) using recursive binary exponentiation.

    Args:
        x: The base.
        n: The exponent.

    Returns:
        x^n
    """
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / myPow(x, -n)

    half = myPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
```

**Step 4: README.md Generation**

```markdown
# 50. Pow(x, n), Difficulty: Medium

## Problem Description

Implement `pow(x, n)`, which calculates *x* raised to the power *n* (i.e., x<sup>n</sup>).

**Example 1:**

Input: x = 2.00000, n = 10
Output: 1024.00000

**Example 2:**

Input: x = 2.10000, n = 3
Output: 9.26100

**Example 3:**

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25

**Constraints:**

*   -100.0 < x < 100.0
*   -2<sup>31</sup> <= n <= 2<sup>31</sup>-1
*   n is an integer.
*   Either x is not zero or n > 0.
*   -10<sup>4</sup> <= x<sup>n</sup> <= 10<sup>4</sup>

## Approach(es)

### Binary Exponentiation (Iterative and Recursive)

The key idea behind binary exponentiation (also known as exponentiation by squaring) is to break down the exponent *n* into its binary representation.  This significantly reduces the number of multiplications required.

**Algorithm (Iterative):**

1.  **Handle Negative Exponent:** If *n* is negative, replace *x* with 1/*x* and *n* with -*n*.
2.  **Initialize:** Set `result = 1` and `current_product = x`.
3.  **Iterate (while n > 0):**
    *   If *n* is odd (i.e., the last bit of *n* is 1), multiply `result` by `current_product`.
    *   Square `current_product` (i.e., `current_product *= current_product`).
    *   Integer-divide *n* by 2 (equivalent to a right bit shift: `n //= 2`).
4.  **Return:** Return `result`.

**Algorithm (Recursive):**

1.  **Base Case:** If *n* is 0, return 1.
2.  **Handle Negative Exponent:** If *n* is negative, return 1 / `myPow(x, -n)`.
3.  **Recursive Step:**
    *   Calculate `half = myPow(x, n // 2)`.
    *   If *n* is even, return `half * half`.
    *   If *n* is odd, return `half * half * x`.

**Example (x=3, n=5):**

*   Binary representation of 5: 101
*   Iterative:
    *   n is odd (1), result = 1 * 3 = 3, current_product = 3 * 3 = 9, n = 2
    *   n is even (0), result = 3, current_product = 9 * 9 = 81, n = 1
    *   n is odd (1), result = 3 * 81 = 243, current_product = 81 * 81, n = 0
*   Recursive:
    *   half = myPow(3, 2)
        *   half = myPow(3, 1)
            *   half = myPow(3, 0) = 1
            *   return 1 * 1 * 3 = 3
        *   return 3 * 3 = 9
    *   return 9 * 9 * 3 = 243

**Data Structures:**

*   No extra data structures are used.

**Time Complexity:**

*   O(log n) - The number of operations is proportional to the number of bits in the binary representation of *n*.

**Space Complexity:**

*   **Iterative:** O(1) - Constant extra space.
*   **Recursive:** O(log n) - Due to the recursive call stack (depth is proportional to the number of bits in *n*).

**Trade-offs:**

*   Binary exponentiation is significantly more efficient than repeatedly multiplying *x* by itself *n* times (which would be O(n)).
*   The iterative version is generally preferred due to its constant space complexity.

## Code

[Binary Exponentiation (Iterative)](./solution_iterative.py)
[Binary Exponentiation (Recursive)](./solution_recursive.py)
```

**Step 5: Topic Extraction and Files**

*   **Math:** This problem is fundamentally a mathematical operation.
*   **Binary:** The efficient solution uses the binary representation of the exponent.
*   **Recursion:** One solution uses recursion.
* **Divide and Conquer:** The approach is based on divide and conquer paradigm

Create files: `Math.md`, `Binary.md`, `Recursion.md`, `Divide and Conquer.md`

**Math.md:**

```markdown
# Math

This category encompasses problems that primarily involve mathematical concepts and operations.  These problems often require understanding of:

*   Arithmetic operations (addition, subtraction, multiplication, division)
*   Exponentiation
*   Modulo operation
*   Number theory (primes, divisibility, etc.)
*   Geometry
*   Probability and statistics
*   Combinatorics

## Related Problems

* [50. Pow(x, n)](0050-powx-n/README.md)
```

**Binary.md:**

```markdown
# Binary

Binary refers to the base-2 number system, which uses only two digits: 0 and 1.  It's the foundation of how computers store and process data.  Many algorithms leverage binary representations for efficiency.

**Key Concepts:**

*   **Bitwise Operations:**  Operations that manipulate individual bits of a number (AND, OR, XOR, NOT, left shift, right shift).
*   **Binary Representation:**  Expressing a number in base-2.
* **Bit Manipulation**: Many problems requires bit manipulation to acheive the optimal performance.

## Related Problems

* [50. Pow(x, n)](0050-powx-n/README.md)
```

**Recursion.md:**

```markdown
# Recursion
... (Content from previous Recursion.md, but with the addition of the new problem) ...
## Related Problems
* [113. Path Sum II](0113-path-sum-ii/README.md)
* [50. Pow(x, n)](0050-powx-n/README.md)

```

**Divide and Conquer.md:**

```markdown
# Divide and Conquer
... (Content from previous Divide and Conquer.md, but with the addition of the new problem) ...
## Related Problems
* [215. Kth Largest Element in an Array](0215-kth-largest-element-in-an-array/README.md)
* [50. Pow(x, n)](0050-powx-n/README.md)
```

This completes the repository generation for LeetCode problem 50, with detailed explanations, multiple solution approaches, and related topic files.
