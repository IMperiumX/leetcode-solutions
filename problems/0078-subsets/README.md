# 78. Subsets, Difficulty: Medium

## Problem Description

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

**Example 1:**

**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

**Example 2:**

**Input:** nums = [0]
**Output:** [[],[0]]

**Constraints:**

* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All the numbers of `nums` are unique.

## Approach(es)

### Iterative Approach

* Algorithm:
  * Start with an empty subset `[]` in the result list.
  * Iterate through each number in the input `nums`.
  * For each number, create new subsets by adding the current number to each existing subset in the result list.
  * Extend the result list with these new subsets.
* Data Structures:
  * A list of lists to store the subsets.
* Time Complexity:
  * O(2^N), where N is the number of elements in `nums`. We generate all possible subsets, and there are 2^N subsets in total.
* Space Complexity:
  * O(2^N), as we store all generated subsets in the result list.
* Trade-offs:
  * The iterative approach is relatively easy to understand and implement.
  * It has a space complexity that grows exponentially with the input size.

### Backtracking Approach

* Algorithm:
  * Use a recursive function `backtrack(index, current_subset)` to explore all possible subsets.
  * In each recursive call:
    * Add a copy of the `current_subset` to the result list.
    * Iterate through the remaining elements in `nums` starting from `index`.
    * Include the current element in the `current_subset`.
    * Recursively call `backtrack` with the next index and the updated `current_subset`.
    * Backtrack by removing the current element from `current_subset` (to explore other possibilities).
* Data Structures:
  * A list of lists to store the subsets.
  * A list to represent the current subset being built.
* Time Complexity:
  * O(2^N), where N is the number of elements in `nums`. Each element has two choices: either be included or excluded from a subset.
* Space Complexity:
  * O(2^N), to store all the subsets. The recursion depth is at most N, but the space used for storing subsets dominates.
* Trade-offs:
  * Backtracking provides a more structured way to explore the solution space, especially for problems with more complex constraints.
  * It might have a slightly higher overhead due to recursion.

### Bit Manipulation Approach

* Algorithm:
  * Each subset can be represented by a unique binary string of length N (where N is the number of elements in `nums`).
  * Each bit in the binary string corresponds to an element in `nums`. If the bit is 1, the element is included in the subset; otherwise, it's not.
  * Iterate through all possible binary strings from 0 to 2^N - 1.
  * For each binary string, create the corresponding subset based on the set bits.
* Data Structures:
  * A list of lists to store the subsets.
* Time Complexity:
  * O(2^N * N), where N is the number of elements in `nums`. We iterate through 2^N possible subsets and spend O(N) time to build each subset.
* Space Complexity:
  * O(2^N), to store all the subsets.
* Trade-offs:
  * The bit manipulation approach is often considered more concise and efficient in terms of implementation.
  * It might be less intuitive to understand than the iterative or backtracking approaches.

## Code

[Iterative Approach](solution.py)

[Backtracking Approach](solution_backtracking.py))

[Bit Manipulation Approach](solution_bitwise.py))
