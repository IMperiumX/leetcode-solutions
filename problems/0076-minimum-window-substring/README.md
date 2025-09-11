Okay, let's create the LeetCode solution repository for problem 76, "Minimum Window Substring".

**Step 1: Problem Identification**

*   **Problem Number:** 76
*   **Problem Name:** Minimum Window Substring
*   **Difficulty:** Hard

**Step 2: Problem File Creation**

Create the directory `0076-minimum-window-substring`.

**Step 3: Solution File Generation**

We'll provide a solution using the Sliding Window technique. This is the most efficient and standard approach for this problem.

**solution_sliding_window.py:**

```python
# 0076. Minimum Window Substring - Sliding Window Approach
from collections import Counter

def minWindow(s: str, t: str) -> str:
    """
    Finds the minimum window substring of s that contains all characters of t.

    Uses the sliding window technique.

    Args:
        s: The source string.
        t: The target string.

    Returns:
        The minimum window substring, or "" if no such substring exists.
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)  # Count characters in t
    required = len(dict_t)  # Number of unique characters in t
    formed = 0  # Number of unique characters from t found in the current window

    # left and right pointers for the sliding window
    l, r = 0, 0

    # Dictionary to keep track of characters in the current window
    window_counts = {}

    # (window length, left, right) - to store the answer
    ans = float("inf"), None, None

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the current character is in t and its count in the window matches
        # its count in t, increment formed.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Contract the window while all characters in t are present
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the left pointer is no longer part of the window
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, shrinking the window
            l += 1

        # Expand the window
        r += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

```

**Step 4: README.md Generation**

```markdown
# 76. Minimum Window Substring, Difficulty: Hard

## Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window substring** of* `s` *such that every character in* `t` *(including duplicates) is included in the window*. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

**Example 1:**

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:**

Input: s = "a", t = "a"
Output: "a"

**Example 3:**

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.

**Constraints:**

*   m == s.length
*   n == t.length
*   1 <= m, n <= 10^5
*   s and t consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in O(m + n) time?

## Approach(es)

### Sliding Window

The sliding window technique is the most efficient way to solve this problem.

**Algorithm:**

1.  **Initialization:**
    *   Create a `Counter` (`dict_t`) for the characters in `t`.
    *   `required`: The number of unique characters in `t`.
    *   `formed`: The number of unique characters from `t` that are currently satisfied in the window.
    *   `window_counts`: A dictionary to store the counts of characters in the current window.
    *   `l` (left) and `r` (right) pointers, initially at 0.
    *   `ans`: A tuple `(window_length, left, right)` to store the minimum window found so far, initialized to `(float("inf"), None, None)`.

2.  **Expand Window (Move `r`):**
    *   Move the right pointer (`r`) to expand the window.
    *   Update `window_counts` with the new character at `s[r]`.
    *   If the new character is in `dict_t` and its count in `window_counts` now equals its count in `dict_t`, increment `formed`.

3.  **Contract Window (Move `l`):**
    *   While `l <= r` and `formed == required` (meaning the current window contains all characters of `t`):
        *   Update `ans` if the current window is smaller than the best found so far.
        *   Decrement the count of `s[l]` in `window_counts`.
        *   If `s[l]` is in `dict_t` and its count in `window_counts` is now *less than* its count in `dict_t`, decrement `formed`.
        *   Move the left pointer (`l`) to shrink the window.

4.  **Repeat:**  Continue expanding and contracting the window until `r` reaches the end of `s`.

5.  **Return:** Return the substring `s[ans[1]:ans[2]+1]` if a valid window was found (`ans[0] != float("inf")`), otherwise return "".

**Data Structures:**

*   `Counter` (`dict_t`): For efficient character counting in `t`.
*   Dictionary (`window_counts`): For efficient character counting in the current window.

**Time Complexity:**

*   O(m + n), where m is the length of `s` and n is the length of `t`.  We iterate through `s` at most twice (with `l` and `r`), and building `dict_t` takes O(n).

**Space Complexity:**

*   O(m + n) in the worst case.  `dict_t` can store up to *n* unique characters, and `window_counts` can potentially store all characters of `s` in the worst case (if `t` contains all unique characters of `s`).  In practice, if the character set is limited (e.g., only uppercase/lowercase English letters), this can be considered O(1) or O(k), where k is the size of character set.

**Trade-offs:**

*   This sliding window approach is highly efficient for this problem, meeting the O(m + n) time complexity requirement.
*   It uses extra space for the dictionaries, but this is generally acceptable.

## Code

[Sliding Window Approach](./solution_sliding_window.py)

```

**Step 5: Topic Extraction and Files**

*   **String:** The problem deals with strings.
*   **Sliding Window:**  The core technique used.
*   **Hash Table (Dictionary/Counter):**  Used for efficient character counting.
*   **Two Pointers:** The `l` and `r` pointers define the sliding window.

Create files: `String.md`, `Sliding Window.md`, `Hash Table.md`, `Two Pointers.md`.

**String.md:**

```markdown
# String

Strings are sequences of characters.  They are a fundamental data type in most programming languages.

**Common String Operations:**

*   Concatenation: Joining strings together.
*   Slicing: Extracting substrings.
*   Searching: Finding patterns or substrings within a string.
*   Comparison: Comparing strings lexicographically.
*   Length: Finding the number of characters in a string.
* **Transformation**: Converting between upper case and lower case.

## Related Problems
* [76. Minimum Window Substring](0076-minimum-window-substring/README.md)
```

**Sliding Window.md:**

```markdown
# Sliding Window

The sliding window technique is a common algorithmic pattern used to solve problems involving arrays or strings. It involves maintaining a "window" of elements that moves through the data, typically from left to right.  The window size can be fixed or variable.

**Key Concepts:**

*   **Window:**  A contiguous subsequence of elements.
*   **Expansion:**  Moving the right boundary of the window.
*   **Contraction:**  Moving the left boundary of the window.
*   **Window Properties:**  Maintaining information about the elements within the window (e.g., sum, count, minimum, maximum).

**Applications:**

*   Finding subarrays/substrings that satisfy certain conditions (e.g., maximum sum, minimum window containing all target characters).
*   Processing data streams.

## Related Problems

* [76. Minimum Window Substring](0076-minimum-window-substring/README.md)
```

**Hash Table.md:**

```markdown
# Hash Table (Dictionary/Counter)

A hash table (also known as a hash map, dictionary, or associative array) is a data structure that implements a key-value store.  It uses a hash function to compute an index (hash code) for each key, which is then used to store and retrieve the associated value.

**Key Concepts:**

*   **Hash Function:**  A function that maps keys to indices in the hash table.
*   **Collision:**  When two different keys map to the same index.  Collision resolution techniques (e.g., chaining, open addressing) are used to handle this.
*   **Load Factor:** The ratio of the number of keys to the size of the hash table.  A high load factor can lead to more collisions and slower performance.

**Advantages:**

*   **Fast Lookup:**  On average, hash tables provide O(1) time complexity for insertion, deletion, and lookup operations.
*   **Efficient Storage:**  Hash tables can efficiently store large amounts of data.

**Disadvantages:**

*   **Worst-Case Performance:** In the worst case (e.g., with many collisions), operations can degrade to O(n) time, where n is the number of keys.
*   **Order Not Preserved:**  Hash tables generally do not maintain the order of insertion.

## Related Problems

* [76. Minimum Window Substring](0076-minimum-window-substring/README.md)
```

**Two Pointers.md:**

```markdown
# Two Pointers

The two-pointers technique is a common algorithmic pattern used to solve problems involving arrays or strings. It involves using two pointers (indices) to traverse the data, often from opposite ends or in the same direction.

**Common Two-Pointer Patterns:**

*   **Opposite Ends:**  Two pointers start at the beginning and end of the array/string and move towards each other. (e.g., reversing an array, finding a pair with a specific sum).
*   **Same Direction (Sliding Window):** Two pointers move in the same direction, defining a "window" of elements. (e.g., finding a subarray with a maximum sum, minimum window substring).
*   **Fast and Slow Pointers:** One pointer moves faster than the other. (e.g., detecting cycles in a linked list).

## Related Problems
* [76. Minimum Window Substring](0076-minimum-window-substring/README.md)
```

This provides a complete, well-documented, and organized LeetCode solution repository for problem 76, addressing all the requirements, including a detailed explanation of the sliding window approach, time/space complexity analysis, and relevant topic files.
