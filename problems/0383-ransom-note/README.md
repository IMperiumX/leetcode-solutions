# 383. Ransom Note, Difficulty: Easy

**Link:** [https://leetcode.com/problems/ransom-note/](https://leetcode.com/problems/ransom-note/)

## Problem Description

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

```python
Input: ransomNote = "a", magazine = "b"
Output: false
```

Example 2:

```python
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

Example 3:

```python
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

Constraints:

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Solution Approach (Hash Map)

The [`solution.py`](./solution.py) file contains a Python solution using a hash map to count character frequencies. We need to ensure that the magazine has at least as many of each character as required by the ransom note.

1. Count the frequency of each character in the magazine.
2. Iterate through the ransom note and for each character:
   - Check if the character exists in the magazine count
   - If it exists and count > 0, decrement the count
   - If it doesn't exist or count is 0, return false
3. If we successfully process all characters in ransom note, return true.

**Time Complexity:** O(m + n) where m is length of magazine and n is length of ransom note
**Space Complexity:** O(k) where k is the number of unique characters in magazine (at most 26 for lowercase letters)

Alternative approaches:
- **Sorting:** Sort both strings and use two pointers - O(m log m + n log n) time
- **Array Count:** Use fixed-size array for character counts since only lowercase letters - O(m + n) time, O(1) space