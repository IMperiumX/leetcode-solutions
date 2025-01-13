
# String

## Definition

A string is a sequence of characters. In many programming languages, strings are represented as arrays of characters, typically using an encoding like ASCII or UTF-8. Strings are fundamental data types used to represent text, data manipulation, and communication..

## Key Concepts

- **Encoding:** Strings are typically encoded using character encodings like ASCII or UTF-8, which map characters to numerical representations.

- **Immutability (in many languages):** In languages like Python and Java, strings are immutable, meaning their contents cannot be changed after creation. Any operation that appears to modify a string actually creates a new string.

## Operations

Common string operations include:

- **Concatenation:** Joining two or more strings together.
- **Substring:** Extracting a portion of a string.
- **Length:** Finding the number of characters in a string.
- **Searching:** Finding the occurrence of a substring within a string.
- **Comparison:** Comparing two strings lexicographically.
- **Transformation:** Modifying a string, such as converting to uppercase or lowercase, trimming whitespace, or replacing characters.
- **Splitting:** Dividing a string into a list of substrings based on a delimiter.
- **Joining:** Combining a list of strings into a single string using a delimiter.

## Immutability

In many languages (like Python and Java), strings are immutable. This means that once a string object is created, it cannot be changed. Any operation that appears to modify a string actually creates a new string object.

## Time Complexity of Common Operations

- **Concatenation:**
  - In languages with immutable strings (e.g., Python, Java): O(n), where n is the total length of the strings being concatenated (due to creating a new string).
  - In languages with mutable strings (e.g., C++ `std::string` in some cases): Amortized O(1) or O(n) depending on the implementation.
- **Substring:**
  - O(k), where k is the length of the substring (need to copy k characters).
- **Length:**
  - O(1) in most languages (the length is usually stored as part of the string object).
- **Searching:**
  - Naive approach: O(mn), where m is the length of the string being searched and n is the length of the substring being searched for.
  - More efficient algorithms (e.g., KMP, Boyer-Moore): O(m+n) in the best and average cases, but can still be O(mn) in the worst case.
- **Comparison:**
  - O(min(m, n)), where m and n are the lengths of the strings being compared.

## Space Complexity

The space complexity of a string is typically O(n), where n is the number of characters in the string.

## Use Cases

Strings are used extensively in programming for a wide variety of tasks, including:

- **Text Processing:** Manipulating and analyzing text data.
- **User Input:** Handling input from users.
- **Data Serialization:** Converting data structures to and from string representations (e.g., JSON, XML).
- **Web Development:** Representing HTML, CSS, and JavaScript code.
- **File I/O:** Reading and writing text files.
- **Database Queries:** Storing and querying text data in databases.

## Related LeetCode Problems

- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [271. Encode and Decode Strings](./../problems/0271-encode-and-decode-strings/README.md)
- [1930. Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/)
- [3223. Minimum Length of String After Operations](https://leetcode.com/problems/minimum-length-of-string-after-operations/)
