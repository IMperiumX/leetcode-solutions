**Step 1: Problem Identification**

*   **Prompt 1:** The problem statement defines the "First Missing Positive" problem, seeking the smallest positive integer *not* present in an unsorted array, with O(n) time and O(1) space constraints. This is LeetCode problem 41, classified as Hard.

    *   **Output:** Problem Number: 41, Problem Name: First Missing Positive, Difficulty: Hard

**Step 2: Problem File Creation**

*   Create a directory named `0041-first-missing-positive`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:**  I will generate a Python solution. The key to solving this in O(n) time and O(1) space is to use the array itself as a hash table (or a similar structure). We leverage the fact that we are looking for a *positive* integer.

*File: 0041-first-missing-positive/solution.py*

```python
# 41. First Missing Positive - In-Place Modification Approach

def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in an unsorted array.

    Args:
        nums: The input list of integers.

    Returns:
        The smallest missing positive integer.
    """
    n = len(nums)

    # 1. Check if 1 is present. If not, we're done.
    if 1 not in nums:
        return 1

    # 2. Replace negative numbers, zeros, and numbers larger than n with 1s.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # 3. Use index as a hash key and the sign of the number as a presence detector.
    # For example, if nums[1] is negative, it means that number `1` is present in the array.
    # If nums[2] is positive, the number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet number a in the array, change the sign of the a-th element.
        # Be careful with duplicates: do it only once.
        if a == n:
            nums[0] = - abs(nums[0])
        else:
            nums[a] = - abs(nums[a])

    # 4. Now the index of the first positive number is equal to the first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1

```

**Step 4: Create Related Topics Files**

*File: 0041-first-missing-positive/Arrays.md* (Similar content, included for completeness)

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
* **In-place modification**: Utilizing the given array to reduce space complexity.

## Related LeetCode Problems
*   [41. First Missing Positive](./0041-first-missing-positive)
*   [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
*   [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
*   [15. 3Sum](https://leetcode.com/problems/3sum/)
*   [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
*    [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
```

**Step 5: Problem README Generation**

*File: 0041-first-missing-positive/README.md*

```markdown
# 41. First Missing Positive, Difficulty: Hard

## Problem Description

Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

## Approach(es)

### In-Place Modification Approach

Algorithm:

1.  **Check for 1:**  If 1 is not present in the array, we've found the answer (return 1). This is a quick check.
2.  **Clean Up the Array:** Replace negative numbers, zeros, and numbers greater than `n` (the length of the array) with 1s.  These numbers are irrelevant to finding the *smallest missing positive*.
3.  **Use Index as Hash Key:** Iterate through the array. For each number `a = abs(nums[i])`:
    *   If `a == n`, change the sign of the *first* element (`nums[0]`) to negative.  We use the first element because we might not have an index `n` in the array (if `n == len(nums)`).
    *   Otherwise (if `a < n`), change the sign of the `a`-th element (`nums[a]`) to negative.  This marks the presence of the number `a`.  Be careful to do this only *once* for each number (handle duplicates).
4.  **Find the First Positive:** Iterate through the array again (starting from index 1):
    *   If you find a positive number (`nums[i] > 0`), it means the number `i` is missing. Return `i`.
5.  **Handle Edge Cases:**
    *   If `nums[0]` is positive, it means `n` is missing. Return `n`.
    *   If you reach the end of the array without finding a positive number (and `nums[0]` is negative), it means all numbers from 1 to `n` are present, so the missing positive is `n + 1`. Return `n + 1`.

Data Structures:

*   The input array `nums` itself is used as a hash table.

Time Complexity:

*   O(n), where n is the length of the `nums` array.  We iterate through the array a constant number of times.

Space Complexity:

*   O(1).  We use constant extra space (in-place modification).

Trade-offs:

*   This approach is highly efficient, achieving the required O(n) time and O(1) space. The core idea is to cleverly use the array indices and the sign of the numbers to track which positive integers are present.

## Code

[In-Place Modification Approach](./solution.py)

## Notes

This is a classic interview problem that tests your ability to think creatively about using an array's indices.  The in-place modification technique is key to achieving the O(1) space complexity.  It's important to understand *why* we can replace irrelevant numbers with 1s and *how* the sign of the numbers acts as a presence/absence indicator.  The edge cases (when 1 is not present, or when all numbers from 1 to n are present) are also crucial to handle correctly.
```
Final File Structure:

```
0041-first-missing-positive/
├── solution.py
└── README.md
└── Arrays.md
```
