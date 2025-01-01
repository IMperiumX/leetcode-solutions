
# 125. Valid Palindrome, Difficulty: Easy

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

**Example 2:**

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

**Example 3:**

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**

* 1 <= s.length <= 2 \* 10^5
* s consists only of printable ASCII characters.

## Approach(es)

### Two Pointers Approach

* Algorithm:
  * Initialize two pointers, `left` at the beginning of the string and `right` at the end of the string.
  * Move the `left` pointer to the right, skipping any non-alphanumeric characters.
  * Move the `right` pointer to the left, skipping any non-alphanumeric characters.
  * Compare the characters at `left` and `right` (case-insensitive). If they are different, return `false`.
  * Continue this process until `left` and `right` cross each other (`left >= right`).
  * If the loop finishes without returning `false`, it means the string is a palindrome, so return `true`.
* Data Structures:
  * No extra data structures are needed.
* Time Complexity:
  * O(N), where N is the length of the string. We iterate through the string at most once.
* Space Complexity:
  * O(1), constant extra space is used.
* Trade-offs:
  * This approach is efficient in terms of both time and space.
  * It directly manipulates the input string without creating new strings or data structures.

### Reverse String Approach

* Algorithm:
    1. Create a new string that contains only the alphanumeric characters from the input string, converted to lowercase.
    2. Reverse the new string.
    3. Compare the processed string with its reversed version. If they are the same, the original string is a palindrome; otherwise, it is not.
* Data Structures:
  * A new string to store the processed alphanumeric characters.
* Time Complexity:
  * O(N), where N is the length of the string. Creating the processed string and reversing it both take linear time.
* Space Complexity:
  * O(N), where N is the length of the string. We create a new string that, in the worst case, could be the same length as the original string.
* Trade-offs:
  * This approach is more straightforward to implement but uses extra space to store the processed string.
  * It might be slightly less efficient than the two-pointers approach in terms of space.

## Code

[Two Pointers Approach](./solution_two_pointers.py)

[Reverse String Approach](./solution_reverse_string.py)
