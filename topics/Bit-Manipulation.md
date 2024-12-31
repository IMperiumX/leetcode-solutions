# Bit Manipulation

## Introduction

**Bit manipulation** is the process of using bitwise operators to manipulate individual bits within a binary representation of data. It is a powerful technique used in various computer science applications, including algorithms, data structures, cryptography, and embedded systems.

## Bitwise Operators

The following are the common bitwise operators:

| Operator | Description                                          | Example      | Result (Binary) | Result (Decimal) |
| -------- | ---------------------------------------------------- | ------------ | --------------- | ---------------- |
| `&`      | **AND:** Sets each bit to 1 if both bits are 1.      | `5 & 3`      | `0101 & 0011`   | `1`              |
| `\|`     | **OR:** Sets each bit to 1 if at least one bit is 1. | `5 \| 3`     | `0101 \| 0011`  | `7`              |
| `^`      | **XOR:** Sets each bit to 1 if only one bit is 1.     | `5 ^ 3`      | `0101 ^ 0011`   | `6`              |
| `~`      | **NOT:** Inverts all the bits (0 becomes 1, 1 becomes 0). | `~5`       | `~0101`        | `-6`             |
| `<<`     | **Left Shift:** Shifts bits to the left, filling with 0s on the right. | `5 << 1`    | `0101 << 1`     | `10`             |
| `>>`     | **Right Shift:** Shifts bits to the right. For unsigned numbers, fills with 0s on the left. For signed numbers, fills with the sign bit (arithmetic shift) or 0s (logical shift). | `5 >> 1` | `0101 >> 1`     | `2`              |

## Common Bit Manipulation Techniques

### 1. Get Bit

**Purpose:** Determine if a specific bit at a given position is set (1) or not (0).

**Method:**

1. Shift `1` to the left by the bit position.
2. Perform a bitwise AND (`&`) between the number and the shifted `1`.
3. If the result is non-zero, the bit is set; otherwise, it's not.

**Example:**

```python
def get_bit(num, pos):
  """Gets the bit at the specified position in the number.

  Args:
    num: The number to check.
    pos: The bit position (0-based from the right).

  Returns:
    True if the bit is set, False otherwise.
  """
  return (num & (1 << pos)) != 0
```

### 2. Set Bit

**Purpose:** Set a specific bit at a given position to 1.

**Method:**

1. Shift `1` to the left by the bit position.
2. Perform a bitwise OR (`|`) between the number and the shifted `1`.

**Example:**

```python
def set_bit(num, pos):
  """Sets the bit at the specified position in the number to 1.

  Args:
    num: The number to modify.
    pos: The bit position (0-based from the right).

  Returns:
    The modified number.
  """
  return num | (1 << pos)
```

### 3. Clear Bit

**Purpose:** Clear a specific bit at a given position (set it to 0).

**Method:**

1. Shift `1` to the left by the bit position.
2. Invert the shifted `1` using the NOT operator (`~`).
3. Perform a bitwise AND (`&`) between the number and the inverted shifted `1`.

**Example:**

```python
def clear_bit(num, pos):
  """Clears the bit at the specified position in the number (sets it to 0).

  Args:
    num: The number to modify.
    pos: The bit position (0-based from the right).

  Returns:
    The modified number.
  """
  return num & ~(1 << pos)
```

### 4. Toggle Bit

**Purpose:** Toggle a specific bit at a given position (flip it from 0 to 1 or 1 to 0).

**Method:**

1. Shift `1` to the left by the bit position.
2. Perform a bitwise XOR (`^`) between the number and the shifted `1`.

**Example:**

```python
def toggle_bit(num, pos):
  """Toggles the bit at the specified position in the number.

  Args:
    num: The number to modify.
    pos: The bit position (0-based from the right).

  Returns:
    The modified number.
  """
  return num ^ (1 << pos)
```

### 5. Check if a Number is a Power of 2

**Purpose:** Determine if a given number is a power of 2.

**Method:**

1. Perform a bitwise AND (`&`) between the number and the number minus 1.
2. If the result is 0, the number is a power of 2; otherwise, it's not.

**Example:**

```python
def is_power_of_two(num):
  """Checks if a number is a power of 2.

  Args:
    num: The number to check.

  Returns:
    True if the number is a power of 2, False otherwise.
  """
  return (num > 0) and ((num & (num - 1)) == 0)
```

### 6. Count Set Bits (Hamming Weight)

**Purpose:** Count the number of set bits (1s) in a number.

**Method:**

1. Iterate through the bits of the number.
2. For each bit, check if it's set using the `get_bit` method or a similar technique.
3. Increment a counter if the bit is set.

**Example:**

```python
def count_set_bits(num):
  """Counts the number of set bits (1s) in a number.

  Args:
    num: The number to check.

  Returns:
    The number of set bits.
  """
  count = 0
  while num > 0:
    count += num & 1
    num >>= 1
  return count
```

## Applications of Bit Manipulation

* **Cryptography:** Encryption, decryption, and hashing algorithms often use bit manipulation.
* **Error Detection and Correction:** Parity bits and checksums rely on bit manipulation.
* **Networking:** IP addressing, subnet masking, and packet manipulation.
* **Graphics:** Image processing and manipulation.
* **Embedded Systems:** Controlling hardware devices at the bit level.
* **Algorithms and Data Structures:** Efficient algorithms and data structures can be designed using bit manipulation.
* **Bitsets and Bit Arrays:** Representing sets and arrays using individual bits.

## Advantages of Bit Manipulation

* **Efficiency:** Bitwise operations are often faster than arithmetic or logical operations.
* **Conciseness:** Bit manipulation can express complex logic in a compact way.
* **Low-Level Control:** Provides fine-grained control over data at the bit level.

## Disadvantages of Bit Manipulation

* **Readability:** Bit manipulation code can be harder to read and understand than code that uses higher-level operations.
* **Portability:** Some bit manipulation techniques might be platform-dependent.
* **Error-Prone:** Mistakes in bit manipulation can lead to subtle bugs that are difficult to track down.

## Problems Related to Bit Manipulation

1. [136. Single Number](https://leetcode.com/problems/single-number/)
2. [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
3. [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
4. [231. Power of Two](https://leetcode.com/problems/power-of-two/)
5. [268. Missing Number](https://leetcode.com/problems/missing-number/)
6. [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
7. [78. Subsets](https://leetcode.com/problems/subsets/)
