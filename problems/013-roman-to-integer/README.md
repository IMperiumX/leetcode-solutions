**Step 1: Problem Identification**

*   **Prompt 1:** The problem description clearly defines the "Roman to Integer" conversion problem. A LeetCode search confirms this is problem number 13.
*   **Output:** "Problem Number: 13, Problem Name: Roman to Integer, Difficulty: Easy"

**Step 2: Problem File Creation**

*   Create a directory named `013-roman-to-integer`.

**Step 3: Solution File Generation**

*   **Prompt 3.2 (No provided solution):** We'll generate a Python solution. The standard approach involves iterating through the Roman numeral string and handling the subtractive cases.

*   **`013-roman-to-integer/solution.py`:**

```python
# 13. Roman to Integer - Standard Approach

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            current_value = roman_map[s[i]]

            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result

```
* **`013-roman-to-integer/solution_iterative.py`:**

```python
# 13. Roman to Integer - Iterative approach
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        i = 0
        while i < len(s):
            # If this is a subtractive case.
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total += roman_values[s[i + 1]] - roman_values[s[i]]
                i += 2
            # Else this is NOT a subtractive case.
            else:
                total += roman_values[s[i]]
                i += 1
        return total
```

* **`013-roman-to-integer/Hash Table.md`:**
Since this problem use a hash table to map the values, let's add it:
```markdown
# Hash Table

A hash table (also known as a hash map) is a data structure that implements an associative array or dictionary, which is a collection of key-value pairs. It allows for efficient retrieval, insertion, and deletion of elements based on their unique keys.  Hash tables use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

## How it Works

1.  **Hash Function:**  A hash function takes a key as input and returns an integer, called a hash code.  A good hash function should:
    *   Be deterministic (same key always produces the same hash code).
    *   Distribute keys uniformly across the hash table's buckets to minimize collisions.
    *   Be computationally efficient.

2.  **Buckets:** The hash table is typically implemented as an array of buckets.  Each bucket can store one or more key-value pairs.

3.  **Collision Handling:**  When two different keys produce the same hash code (a collision), the hash table needs a mechanism to handle it.  Common methods include:
    *   **Separate Chaining:** Each bucket stores a linked list (or other data structure) of key-value pairs that hash to that bucket.
    *   **Open Addressing:**  If a collision occurs, the algorithm probes for the next available slot in the array, using techniques like linear probing, quadratic probing, or double hashing.

## Operations

*   **Insertion:**
    1.  Compute the hash code of the key.
    2.  Use the hash code to determine the bucket index.
    3.  Insert the key-value pair into the bucket (handling collisions as needed).

*   **Retrieval (Lookup):**
    1.  Compute the hash code of the key.
    2.  Use the hash code to determine the bucket index.
    3.  Search the bucket for the key (handling collisions as needed). If found, return the associated value.

*   **Deletion:**
    1.  Compute the hash code of the key.
    2.  Use the hash code to determine the bucket index.
    3.  Search the bucket for the key (handling collisions as needed). If found, remove the key-value pair.

## Time Complexity

*   **Average Case:** O(1) for insertion, retrieval, and deletion, assuming a good hash function and collision handling strategy.
*   **Worst Case:** O(n), where n is the number of elements, if all keys hash to the same bucket (e.g., with a very poor hash function).  In practice, with a good hash function, this is very rare.

## Space Complexity

O(n), where n is the number of elements stored in the hash table. The space used depends on the number of buckets and the collision handling method.

## Advantages

*   **Fast Lookups:**  Hash tables provide very fast average-case performance for lookups, insertions, and deletions.
*   **Efficient for Key-Value Data:**  Ideal for storing and retrieving data based on unique keys.

## Disadvantages

*   **Worst-Case Performance:**  Can degrade to O(n) in the worst case (though this is uncommon with good hash functions).
*   **Unordered:** Hash tables do not maintain the order of elements.
*   **Hash Function Dependence:** Performance heavily relies on the quality of the hash function.

## Use Cases

*   **Dictionaries and Associative Arrays:**  Implementing dictionaries or maps in programming languages.
*   **Caching:**  Storing recently accessed data for quick retrieval.
*   **Symbol Tables:**  Used in compilers and interpreters to store information about identifiers.
*   **Database Indexing:**  Speeding up database queries.
*   **Sets:** Implementing sets (collections of unique elements).

## Related LeetCode Problems

*   [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
*   [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

```

**Step 4: Problem README Generation**

*   **Prompt 4:** Generate the `README.md`.

```markdown
# 13. Roman to Integer, Difficulty: Easy

## Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

*   `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
*   `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
*   `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**Constraints:**

*   `1 <= s.length <= 15`
*   `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
*   It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## Approach(es)

### Standard Approach (Right-to-Left Iteration)

Algorithm:

1.  **Create a Mapping:** Create a dictionary (hash map) `roman_map` to store the integer values of each Roman numeral symbol.
2.  **Initialize:**
    *   Initialize `result` to 0 (to store the final integer value).
    *   Initialize `prev_value` to 0 (to keep track of the value of the previous symbol).
3.  **Iterate Backwards:** Iterate through the input string `s` from right to left.
4.  **Current Value:** Get the integer value of the current symbol from `roman_map`.
5.  **Subtractive Case:**
    *   If the `current_value` is less than `prev_value`, it means we have a subtractive case (like IV or IX). Subtract `current_value` from `result`.
    *   Otherwise, add `current_value` to `result`.
6.  **Update Previous Value:** Update `prev_value` to `current_value` for the next iteration.
7.  **Return:** Return the final `result`.

Data Structures:

*   Hash Map (Dictionary):  Used to store the mapping between Roman numeral symbols and their integer values.

Time Complexity:

*   O(n), where n is the length of the Roman numeral string. We iterate through the string once.

Space Complexity:

*   O(1) - The hash map has a constant size (7 entries), so the space used is constant.

Trade-offs:

*   This approach is efficient and relatively easy to implement. The right-to-left iteration simplifies the logic for handling subtractive cases.

### Iterative approach (Left-to-Right Iteration)

Algorithm:
1.  **Create a Mapping:** Create a dictionary (hash map) `roman_map` to store the integer values of each Roman numeral symbol.
2.  **Initialize:** Initialize `total` to zero.
3.  **Iterate over the string:**
    * If the current value is less than next value (subtractive case) add to the total the subtraction of the next value from the current, then skip the next char.
    * If the current value is not from the subtractive cases, then just add it to the total.
4. **Return**: the `total`.

Data Structures:

* Hash Map (Dictionary): Used to store the mapping between Roman numeral symbols and their integer values.

Time Complexity:

* O(n), where n is the length of the Roman numeral string. We iterate through the string once.

Space Complexity:

*   O(1) - The hash map has a constant size (7 entries), so the space used is constant.

Trade-offs:

*   This approach is efficient and relatively easy to implement.

## Code

[Standard Approach](./solution.py)
[Iterative approach](./solution_iterative.py)

## Notes

* The right-to-left approach is generally preferred because the logic to handle subtractive cases is simpler when processing from right to left.
* The problem statement guarantees that the input is a valid Roman numeral, so we don't need to include extensive validation logic.
```

This completes the generation of the repository, providing a well-structured solution, a clear explanation of the approach, and a related topic file.
