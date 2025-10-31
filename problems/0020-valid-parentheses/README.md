# 20. Valid Parentheses, Difficulty: Easy

## Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

## Approach(es)

### Stack Approach

Algorithm:

1. Initialize an empty stack.
2. Create a mapping (dictionary/hash map) that stores closing brackets as keys and their corresponding opening brackets as values.  For example: `mapping = {')': '(', '}': '{', ']': '['}`
3. Iterate through the input string `s`, character by character.
4. If the current character is a closing bracket (i.e., it's a key in the `mapping`):
    * Check if the stack is empty. If it is, it means there's no corresponding opening bracket, so return `False`.
    * If the stack is not empty, pop the top element from the stack.
    * Compare the popped element with the expected opening bracket (obtained from `mapping[char]`). If they don't match, return `False`.
5. If the current character is an opening bracket:
    * Push it onto the stack.
6. After iterating through the entire string, check if the stack is empty.
    * If the stack is empty, it means all opening brackets have been matched with their corresponding closing brackets, so return `True`.
    * If the stack is not empty, it means there are unmatched opening brackets, so return `False`.

Data Structures:

* Stack:  Used to store opening brackets in the order they appear.  The LIFO (Last-In, First-Out) nature of the stack is crucial for ensuring correct bracket order.
* Dictionary (Hash Map): Used for efficient lookup of corresponding opening brackets for each closing bracket.

Time Complexity:

* O(n), where n is the length of the string `s`.  We iterate through the string once. Stack operations (push, pop, peek) and dictionary lookups take constant time on average.

Space Complexity:

* O(n) in the worst case.  This happens when the input string consists only of opening brackets (e.g., "((((((((((("). In this case, the stack will store all the opening brackets. In the best case, the space complexity can be O(1) if no opening brackets are added to the stack (invalid parentheses string, starting with closing bracket)

Trade-offs:

* The stack approach provides a good balance between time and space complexity.  It's efficient and relatively easy to implement.

## Code

[Stack Approach](./solution.py)

## Notes

This problem is a classic example of using a stack to solve problems related to balanced symbols or expressions. The key idea is to use the stack to keep track of the "open" symbols and ensure they are closed in the correct order.
