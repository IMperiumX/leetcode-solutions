Okay, let's create the LeetCode solution repository for problem 981, "Time Based Key-Value Store."

**Step 1: Problem Identification**

The input clearly defines:

*   **Problem Number:** 981
*   **Problem Name:** Time Based Key-Value Store
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

We'll create a directory named `0981-time-based-key-value-store`.

**Step 3: Solution File Generation**

The user didn't provide a solution, so we'll generate a Python solution using a dictionary and binary search.

```python
# 0981. Time Based Key-Value Store - Hash Map and Binary Search Approach

class TimeMap:

    def __init__(self):
        self.store = {}  # key: [(value, timestamp), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        # Binary search to find the largest timestamp_prev <= timestamp
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]  # Store the value
                left = mid + 1  # Try to find a larger timestamp
            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

This code is saved as `0981-time-based-key-value-store/solution.py`.  Here's the same solution, with a slightly different variable name and a bit more explanation in comments, saved as `0981-time-based-key-value-store/solution_binarysearch.py`:
```python
# 0981. Time Based Key-Value Store - Hash Map and Binary Search (Descriptive)

class TimeMap:

    def __init__(self):
        # Use a dictionary to store key-value pairs.
        # The value for each key is a list of (value, timestamp) tuples.
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist, create a new list for it.
        if key not in self.data:
            self.data[key] = []
        # Append the (value, timestamp) tuple to the list associated with the key.
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return an empty string.
        if key not in self.data:
            return ""

        # Get the list of (value, timestamp) tuples for the given key.
        values = self.data[key]

        # Perform binary search to find the largest timestamp_prev <= timestamp.
        left, right = 0, len(values) - 1
        best_value = ""  # Initialize the result to an empty string.

        while left <= right:
            mid = (left + right) // 2
            value_at_mid, timestamp_at_mid = values[mid]

            if timestamp_at_mid <= timestamp:
                # If the timestamp at mid is less than or equal to the target timestamp,
                # we've found a potential match.  Update best_value and move the left
                # pointer to search for a larger timestamp.
                best_value = value_at_mid
                left = mid + 1
            else:
                # If the timestamp at mid is greater than the target timestamp,
                # move the right pointer to search in the left half.
                right = mid - 1

        return best_value
```

**Step 4: Problem README Generation**

Here's the `README.md` content:

```markdown
# 981. Time Based Key-Value Store, Difficulty: Medium

## Problem Description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

*   `TimeMap()` Initializes the object of the data structure.
*   `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
*   `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

**Example 1:**

```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

**Constraints:**

*   `1 <= key.length, value.length <= 100`
*   `key` and `value` consist of lowercase English letters and digits.
*   `1 <= timestamp <= 107`
*   All the timestamps `timestamp` of `set` are strictly increasing.
*   At most `2 * 105` calls will be made to `set` and `get`.

## Approach(es)

### Hash Map and Binary Search

We use a hash map (dictionary in Python) to store the key-value pairs.  The value for each key is a list of `(value, timestamp)` tuples. Since the timestamps are strictly increasing, we can use binary search on the list of tuples to efficiently find the value associated with the largest `timestamp_prev` that is less than or equal to the given `timestamp`.

**Algorithm:**

1.  **Initialization:**
    *   Create a dictionary `store` (or `data`) to store the data.

2.  **`set(key, value, timestamp)`:**
    *   If `key` is not in `store`, initialize an empty list for it: `store[key] = []`.
    *   Append the tuple `(value, timestamp)` to `store[key]`.

3.  **`get(key, timestamp)`:**
    *   If `key` is not in `store`, return an empty string `""`.
    *   Get the list of `(value, timestamp)` tuples associated with `key`: `values = store[key]`.
    *   Perform binary search on `values`:
        *   Initialize `left = 0` and `right = len(values) - 1`.
        *   Initialize `result = ""`.
        *   While `left <= right`:
            *   Calculate `mid = (left + right) // 2`.
            *   If `values[mid][1] <= timestamp`:
                *   Set `result = values[mid][0]` (store the value).
                *   Move `left = mid + 1` (search for a larger timestamp).
            *   Else:
                *   Move `right = mid - 1`.
        *   Return `result`.

**Data Structures:**

*   Hash Map (Dictionary): To store key-value pairs, where the value is a list of (value, timestamp) tuples.
*   List:  To store the (value, timestamp) tuples for each key.

**Time Complexity:**

*   `set`: O(1) - Appending to a list is amortized O(1).
*   `get`: O(log n) - Binary search on the list of timestamps, where n is the number of entries for a given key.

**Space Complexity:**

*   O(N), where N is the total number of `set` operations.  In the worst case, we store all the values and timestamps.

**Trade-offs:**

*   The binary search provides efficient retrieval (O(log n)) for the `get` operation.
*   Space usage is proportional to the number of entries.

## Code

[Hash Map and Binary Search](./solution_binarysearch.py)

## Notes (Optional)

*   The problem specifies that timestamps are strictly increasing, which is crucial for the binary search approach.
*    We could use other data structures like a balanced binary search tree, but for this specific constraints and the problem statement using a simple list and performing binary search is a perfect solution.
```

**Step 5: Topics Extraction**
```markdown
# Hash Tables

Hash tables (also known as hash maps, dictionaries, or associative arrays) are one of the most important and widely used data structures in computer science. They provide a way to store and retrieve key-value pairs efficiently.

## Key Concepts

*   **Key-Value Pairs:** Hash tables store data in the form of key-value pairs.  Each key is unique, and it maps to a corresponding value.
*   **Hash Function:** A hash function is a crucial component of a hash table. It takes a key as input and returns an integer, called a *hash code*. The hash code is used as an index into an array (called the *hash table* or *buckets*).
*   **Collision Handling:**  Multiple keys can potentially hash to the same index (this is called a *collision*). Hash tables have mechanisms to handle collisions. Common methods include:
    *   **Separate Chaining:** Each bucket in the hash table stores a linked list (or another data structure) of all key-value pairs that hash to that index.
    *   **Open Addressing:** If a collision occurs, the algorithm probes for another available slot in the hash table.  Common probing techniques include:
        *   **Linear Probing:**  Check the next consecutive slot.
        *   **Quadratic Probing:**  Check slots with increasing offsets (i, i+1, i+4, i+9, ...).
        *   **Double Hashing:** Use a second hash function to determine the probing sequence.
*   **Load Factor:** The load factor is the ratio of the number of key-value pairs (n) to the number of buckets (m) in the hash table (n/m).  A high load factor can lead to more collisions and reduced performance.  Hash tables often *resize* (increase the number of buckets) when the load factor exceeds a certain threshold.
* **Amortized Analysis**:  The concept of *amortized* time complexity is important for understanding hash table performance.  While a single operation (like insertion) might occasionally take O(n) time due to resizing, the *average* time complexity over a sequence of operations is typically O(1).

## Common Hash Table Operations and Time Complexities

| Operation       | Average Time Complexity | Worst-Case Time Complexity | Description                                                                         |
| --------------- | ----------------------- | -------------------------- | ----------------------------------------------------------------------------------- |
| Insertion (set) | O(1) (amortized)        | O(n)                       | Add a new key-value pair to the hash table.                                          |
| Retrieval (get) | O(1) (amortized)        | O(n)                       | Retrieve the value associated with a given key.                                    |
| Deletion        | O(1) (amortized)        | O(n)                       | Remove a key-value pair from the hash table.                                       |
| Search (contains key)          | O(1) (amortized)        | O(n)                 | Checks if a key is exists in the hash table.                       |

*   **Worst-Case Scenarios:** The worst-case time complexity for hash table operations can be O(n) if all keys hash to the same bucket (in the case of separate chaining) or if a poor collision resolution strategy leads to excessive probing (in the case of open addressing).  However, with a good hash function and proper resizing, these worst-case scenarios are rare.

## Python Dictionaries

Python's built-in `dict` type is a highly optimized implementation of a hash table.  It uses open addressing with a sophisticated probing strategy and automatic resizing.

*   **Key Uniqueness:** Dictionary keys must be unique and *hashable*.  Hashable objects have a `__hash__()` method that returns an integer hash code and a `__eq__()` method for equality comparison.  Immutable types like numbers, strings, and tuples are hashable.  Mutable types like lists and dictionaries are not hashable (and therefore cannot be used as dictionary keys).
*   **Iteration:**  You can iterate over the keys, values, or key-value pairs of a dictionary using `keys()`, `values()`, and `items()` methods, respectively.
*   **Dictionary Comprehensions:**  Python provides concise syntax for creating dictionaries using dictionary comprehensions.

## Example LeetCode Problems

*   **Two Sum:** [1. Two Sum](https://leetcode.com/problems/two-sum/) (Easy)
*   **Contains Duplicate:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy)
*   **Group Anagrams:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium)
*   **Valid Anagram:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy)
*   **Longest Substring Without Repeating Characters:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium)
* **Time Based Key-Value Store**: [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store) (Medium)

## Tips for LeetCode Hash Table Problems

*   **Consider Hash Tables First:**  When you encounter a problem that involves searching, counting frequencies, or checking for duplicates, think about using a hash table.
*   **Choose the Right Key:**  Carefully choose what to use as the key in your hash table.  The key should be something that allows you to efficiently access the information you need.
*   **Handle Collisions:**  Be aware of how collisions are handled in the hash table implementation you are using.  In most cases, you don't need to worry about the details, but it's good to understand the underlying concepts.
*   **Use Built-in Functions:** Take advantage of built-in hash table functions and methods (like `in` for checking key existence in Python dictionaries).

Hash tables are a powerful and versatile data structure that can significantly improve the efficiency of your code. Mastering hash tables is crucial for success on LeetCode and in software development in general.
```
This will be saved as `Hash Tables.md`
```markdown
# Binary Search

Binary search is a highly efficient search algorithm that finds the position of a target value within a **sorted** array (or a sorted, searchable data structure). It works by repeatedly dividing the search interval in half.  If the middle element is the target, the search is successful.  If the target is less than the middle element, the search continues in the left half; otherwise, it continues in the right half.

## Key Concepts

*   **Sorted Input:** Binary search *requires* the input array to be sorted.  This is fundamental to how it works.
*   **Divide and Conquer:** Binary search is a classic example of a "divide and conquer" algorithm. It repeatedly divides the problem into smaller subproblems.
*   **Logarithmic Time Complexity:**  The key advantage of binary search is its logarithmic time complexity, O(log n). This means that the number of operations required to find the target grows very slowly as the size of the array increases.
* **Iterative vs. Recursive Implementation:** Binary search can be implemented iteratively (using loops) or recursively.  Both approaches have the same time and space complexity.

## How Binary Search Works (Iterative Approach)

1.  **Initialization:**
    *   Set `left` to 0 (the index of the first element).
    *   Set `right` to `n - 1` (the index of the last element), where `n` is the length of the array.

2.  **Iteration:** While `left <= right`:
    *   Calculate the middle index: `mid = (left + right) // 2` (using integer division).
    *   **Comparison:**
        *   If `array[mid] == target`:  Return `mid` (target found).
        *   If `array[mid] < target`:  Set `left = mid + 1` (search the right half).
        *   If `array[mid] > target`:  Set `right = mid - 1` (search the left half).

3.  **Target Not Found:** If the loop finishes without finding the target (i.e., `left > right`), return -1 (or another appropriate indicator).

## Example (Python)

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found

# Example usage:
arr = [2, 5, 7, 8, 11, 12]
target = 11
index = binary_search(arr, target)

if index != -1:
    print(f"Element is present at index {index}")
else:
    print("Element is not present in array")

```

## Time and Space Complexity

*   **Time Complexity:** O(log n) -  The search interval is halved in each step.
*   **Space Complexity:**
    *   O(1) for the iterative approach (constant extra space).
    *   O(log n) for the recursive approach (due to the call stack).

## Variations and Considerations

*   **Finding First/Last Occurrence:**  If the array contains duplicate elements, you can modify binary search to find the first or last occurrence of the target.
*   **Searching in Rotated Sorted Arrays:**  Binary search can be adapted to work with rotated sorted arrays (e.g., `[4, 5, 6, 7, 0, 1, 2]`).
*   **Finding the Closest Element:** You can modify binary search to find the element in the array that is closest to the target value.
*   **Floating-Point Numbers:**  When working with floating-point numbers, be careful about equality comparisons due to potential precision issues. You might need to use a tolerance value for comparisons.
* **Lower Bound/ Upper Bound**: Find the lower bound mean find the first element greater or equal to the target, Find the upper bound means find the first element strictly greater than the target.

## Example LeetCode Problems (with links)

*   **Binary Search:** [704. Binary Search](https://leetcode.com/problems/binary-search/) (Easy)
*   **Search in Rotated Sorted Array:** [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium)
*   **Find First and Last Position of Element in Sorted Array:** [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)
*   **Sqrt(x):** [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy)
*   **Guess Number Higher or Lower:** [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) (Easy)
*  **Time Based Key-Value Store**: [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store) (Medium)
*   **Find Minimum in Rotated Sorted Array:** [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium)
*    **Search a 2D Matrix**:[74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (Medium)

## Tips for LeetCode Binary Search Problems

*   **Recognize Sorted Input:**  The most important clue is that the input array (or a relevant part of it) is sorted.
*   **Identify the Search Space:** Clearly define what you are searching for (e.g., the target value, the first occurrence, the insertion point).
*   **Handle Edge Cases:**  Consider empty arrays, arrays with one element, and cases where the target is not present.
*   **Avoid Infinite Loops:** Make sure your `left` and `right` pointers are updated correctly to prevent infinite loops.  The condition `left <= right` (rather than `left < right`) is often necessary to handle cases where the target might be at the boundaries.
*   **Integer Overflow:** Be mindful of potential integer overflow when calculating `mid`.  The safer way to calculate the middle index is `mid = left + (right - left) // 2` (in Python) or  `mid = left + (right - left) / 2` (in C++/Java).
*   **Practice Variations:** Practice variations of binary search, such as finding the first/last occurrence, closest element, and searching in rotated arrays.

Binary search is a fundamental algorithm with broad applications. Understanding it thoroughly is essential for solving many LeetCode problems and for algorithmic thinking in general. Its logarithmic time complexity makes it extremely efficient for searching in large sorted datasets.
```
This will be saved as `Binary Search.md`. All files are created.
