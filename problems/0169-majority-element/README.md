**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem from the following input: `[User Input]`."
    The problem description clearly defines the "Majority Element" problem, where we need to find the element that appears more than `n/2` times in an array of size `n`.  This is LeetCode problem 169, which is classified as Easy.

    *   **Output:** Problem Number: 169, Problem Name: Majority Element, Difficulty: Easy

**Step 2: Problem File Creation**

*   Create a directory named `0169-majority-element`.

**Step 3: Solution File Generation**

*   **Prompt 3.2** (No user-provided solution):  I will generate solutions in Python. I'll implement three approaches:
    1.  **Boyer-Moore Voting Algorithm (O(1) space):** This addresses the follow-up question.
    2.  **Hash Map (O(n) space):**  A common and straightforward approach.
    3. **Sorting**

*File: 0169-majority-element/solution_boyer_moore.py*

```python
# 169. Majority Element - Boyer-Moore Voting Algorithm

def majorityElement(nums):
    """
    Finds the majority element using the Boyer-Moore Voting Algorithm.

    Args:
        nums: The input list of numbers.

    Returns:
        The majority element.
    """
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```

*File: 0169-majority-element/solution_hash_map.py*

```python
# 169. Majority Element - Hash Map Approach

def majorityElement(nums):
    """
    Finds the majority element using a hash map.

    Args:
        nums: The input list of numbers.

    Returns:
        The majority element.
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count > len(nums) // 2:
            return num

```
*File: 0169-majority-element/solution_sorting.py*
```python
# 169. Majority Element - Sorting Approach
def majorityElement(nums):
    """
    Find the majority element in a list of numbers using sorting.
    Args:
        nums (List[int]): A list of integers

    Returns:
        int: The majority element
    """
    nums.sort()
    return nums[len(nums)//2]
```

**Step 4: Create Related Topic Files**

*File: 0169-majority-element/Hash_Tables.md*
```markdown
# Hash Tables

Hash tables (also known as hash maps, dictionaries, or associative arrays) are a fundamental data structure that provides efficient key-value storage and retrieval. They use a hash function to map keys to indices in an array, allowing for average O(1) time complexity for insertion, deletion, and lookup operations.

## Key Concepts

*   **Key:** A unique identifier used to access a value.
*   **Value:** The data associated with a key.
*   **Hash Function:** A function that takes a key as input and returns an integer, called a hash code.  The hash code is used as an index into the underlying array.
*   **Collision:** When two different keys produce the same hash code.  Collision handling is a crucial aspect of hash table design.
*   **Load Factor:** The ratio of the number of elements stored in the hash table to the size of the underlying array.  A high load factor can lead to increased collisions and degraded performance.

## Collision Handling Techniques

*   **Separate Chaining:** Each index in the array stores a linked list (or another data structure) of key-value pairs that hash to the same index.
*   **Open Addressing:** If a collision occurs, the algorithm probes for an empty slot in the array.  Common probing techniques include:
    *   **Linear Probing:**  Check consecutive slots until an empty slot is found.
    *   **Quadratic Probing:** Check slots with increasing quadratic offsets.
    *   **Double Hashing:**  Use a secondary hash function to determine the probing interval.

## Common Hash Table Operations

*   **put(key, value):** Inserts a key-value pair into the hash table.
*   **get(key):** Retrieves the value associated with a key.  Returns `None` (or a similar value) if the key is not found.
*   **remove(key):** Deletes the key-value pair associated with a key.
*   **containsKey(key):** Returns `True` if the hash table contains the key, `False` otherwise.
*   **size():** Returns the number of key-value pairs in the hash table.
*   **isEmpty():** Checks whether hash table is empty.

## Advantages of Hash Tables

*   **Fast Average-Case Performance:**  O(1) for insertion, deletion, and lookup, on average.
*   **Efficient Key-Based Access:**  Ideal for scenarios where you need to quickly retrieve data based on a unique key.

## Disadvantages of Hash Tables

*   **Worst-Case Performance:**  O(n) for all operations in the worst case (when all keys hash to the same index).
*   **Unordered Data:**  Hash tables do not maintain the order of elements.
*   **Hash Function Dependence:** The performance of a hash table heavily relies on the quality of the hash function.  A poor hash function can lead to frequent collisions and poor performance.

## Related Leetcode Problems

*   [169. Majority Element](./0169-majority-element)
*   [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
*   [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
```

*File: 0169-majority-element/Arrays.md* (This file will be quite similar to the one in the previous example, but I'll create it for completeness)
```markdown
# Arrays

Arrays are fundamental data structures in computer science. They store collections of elements of the same data type, accessed using indices.  Understanding arrays is crucial for solving a wide variety of problems, particularly on platforms like LeetCode.

## Key Concepts

*   **Contiguous Memory:** Array elements are stored in contiguous memory locations. This allows for efficient access to elements using their index (O(1) access time).
*   **Zero-Based Indexing:**  In most programming languages, array indices start at 0.  The first element is at index 0, the second at index 1, and so on.
*   **Fixed Size (in some languages):**  In languages like C/C++, arrays have a fixed size determined at compile time.  Dynamic arrays (like Python lists) can resize automatically.
*   **Mutability:** Arrays are typically mutable, meaning you can change the values of their elements after they are created.

## Common Array Operations

*   **Accessing Elements:**  Retrieving the value at a specific index (e.g., `arr[3]`).
*   **Updating Elements:**  Changing the value at a specific index (e.g., `arr[2] = 5`).
*   **Iteration:**  Looping through all elements of the array.
*   **Searching:**  Finding a specific element within the array (linear search, binary search on sorted arrays).
*   **Sorting:**  Arranging the elements in a specific order (ascending, descending).  Common sorting algorithms include bubble sort, insertion sort, merge sort, and quicksort.
*   **Insertion/Deletion:** Adding or removing elements (more complex in fixed-size arrays, easier with dynamic arrays).

## Common Array Patterns in LeetCode

*   **Two Pointers:** Using two indices to traverse the array, often from opposite ends or moving at different speeds.
*   **Sliding Window:** Maintaining a "window" of elements within the array and moving it across the array.
*   **Prefix Sum:** Calculating the cumulative sum of elements up to each index, useful for range queries.
*   **Kadane's Algorithm:** Finding the maximum sum of a contiguous subarray.

## Related LeetCode Problems

*   [169. Majority Element](./0169-majority-element)
*   [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
*   [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
*   [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

```
*File: 0169-majority-element/Divide_and_Conquer.md*
```markdown
# Divide and Conquer

Divide and Conquer is a powerful algorithmic paradigm that solves a problem by recursively breaking it down into smaller subproblems of the same type, solving those subproblems, and then combining their solutions to solve the original problem.

## Key Concepts

*   **Divide:** Break the problem into smaller, independent subproblems of the same type.
*   **Conquer:** Solve the subproblems recursively.  If the subproblems are small enough, solve them directly (this is the base case of the recursion).
*   **Combine:** Combine the solutions of the subproblems to obtain the solution to the original problem.

## Common Characteristics of Divide and Conquer Algorithms

*   **Recursive Structure:**  Divide and Conquer algorithms are naturally expressed recursively.
*   **Independent Subproblems:** The subproblems should be independent of each other; there should be no overlap between them.  (If there is overlap, dynamic programming might be a better approach.)
*   **Non-Trivial Combination Step:** The step of combining the subproblem solutions is often non-trivial and requires careful design.

## Examples of Divide and Conquer Algorithms

*   **Merge Sort:** Sorts an array by recursively dividing it into two halves, sorting each half, and then merging the sorted halves.
*   **Quicksort:** Sorts an array by selecting a pivot element, partitioning the array into elements less than and greater than the pivot, and recursively sorting the two partitions.
*   **Binary Search:** Searches for a target value in a sorted array by repeatedly dividing the search interval in half.
*   **Closest Pair of Points:** Finds the closest pair of points in a set of points in a plane.
*   **Strassen's Matrix Multiplication:** Multiplies two matrices faster than the naive algorithm.

## Advantages of Divide and Conquer

*   **Efficiency:**  Can often lead to more efficient algorithms than brute-force approaches.  For example, merge sort and quicksort have O(n log n) time complexity, which is significantly better than the O(n^2) complexity of simple sorting algorithms like bubble sort.
*   **Parallelism:**  The independent subproblems can often be solved in parallel, leading to further performance improvements on multi-core processors.
*   **Conceptual Clarity:**  Can provide a clear and elegant way to solve complex problems.

## Disadvantages of Divide and Conquer

*   **Recursion Overhead:**  Recursive calls have some overhead, which can be significant for very small subproblems.
*   **Complexity of Combination Step:** The combination step can sometimes be complex to implement.
*   **Not Always Applicable:** Not all problems can be efficiently solved using Divide and Conquer.

## Related LeetCode Problems
*   [169. Majority Element](./0169-majority-element)
*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (can be solved with Divide and Conquer, though Kadane's Algorithm is more efficient)
*   [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
*   [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (tree traversals can be viewed as Divide and Conquer)
*   [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
```
**Step 5: Problem README Generation**

*File: 0169-majority-element/README.md*

```markdown
# 169. Majority Element, Difficulty: Easy

## Problem Description

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?

## Approach(es)

### Boyer-Moore Voting Algorithm

Algorithm:

1.  Initialize a `candidate` variable to `None` and a `count` variable to 0.
2.  Iterate through the `nums` array:
    *   If `count` is 0, set `candidate` to the current number.
    *   Increment `count` if the current number is equal to `candidate`; otherwise, decrement `count`.
3.  Return `candidate`.

Data Structures:

*   No extra data structures are used.

Time Complexity:

*   O(n), where n is the length of the `nums` array. We iterate through the array once.

Space Complexity:

*   O(1), as we only use a constant amount of extra space.

Trade-offs:

*   This algorithm is extremely efficient in both time and space. It leverages the fact that the majority element appears more than n/2 times, ensuring that it will eventually "outvote" all other elements.

### Hash Map Approach

Algorithm:

1.  Create a hash map (dictionary) to store the counts of each number.
2.  Iterate through the `nums` array:
    *   Increment the count for the current number in the hash map.
3.  Iterate through the hash map:
    *   If any number has a count greater than `len(nums) // 2`, return that number.

Data Structures:

*   A hash map (dictionary) to store element counts.

Time Complexity:

*   O(n), where n is the length of the `nums` array. We iterate through the array once to build the hash map and then iterate through the hash map (which, in the worst case, can have up to n entries).

Space Complexity:

*   O(n) in the worst case, where n is the length of the array.  This occurs if all elements are distinct.  On average, the space complexity will be less than O(n) if there are duplicate elements.

Trade-offs:

* This approach is straightforward and easy to understand. However, it uses extra space for the hash map, unlike the Boyer-Moore algorithm.

### Sorting Approach
Algorithm:
1. Sort the input `nums` array
2. Return the element at index `len(nums)//2`.

Data Structures:
* No extra data structures are used.

Time Complexity:
* O(n log n) Sorting takes n log n time

Space Complexity
* O(1) or O(n) depending on the sorting algorithm in place sorting or not.

Trade-offs:
* Clean and simple solution, using the property of majority element and sorting. Not the optimal time complexity

## Code

[Boyer-Moore Voting Algorithm](./solution_boyer_moore.py)

[Hash Map Approach](./solution_hash_map.py)

[Sorting Approach](./solution_sorting.py)

## Notes

The Boyer-Moore Voting Algorithm is a clever and efficient solution for this problem. It's worth understanding how it works, as it demonstrates a non-intuitive way to find the majority element without using extra space. The follow-up question specifically encourages finding an O(1) space solution, which the Boyer-Moore algorithm achieves.
```

Final Directory Structure:

```
0169-majority-element/
├── solution_boyer_moore.py
├── solution_hash_map.py
├── solution_sorting.py
├── README.md
├── Arrays.md
├── Divide_and_Conquer.md
└── Hash_Tables.md
```
