# 167. Two Sum II - Input Array Is Sorted, Difficulty: Medium

## Problem Description

Given a **1-indexed** array of integers `numbers` that is **already sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not use the same element twice**.

Your solution must use only **constant extra space**.

**Example 1:**

**Input:** numbers = [2,7,11,15], target = 9
**Output:** [1,2]
**Explanation:** The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

**Example 2:**

**Input:** numbers = [2,3,4], target = 6
**Output:** [1,3]
**Explanation:** The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

**Example 3:**

**Input:** numbers = [-1,0], target = -1
**Output:** [1,2]
**Explanation:** The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

**Constraints:**

* `2 <= numbers.length <= 3 * 10^4`
* `-1000 <= numbers[i] <= 1000`
* `numbers` is sorted in **non-decreasing order**.
* `-1000 <= target <= 1000`
* The tests are generated such that there is **exactly one solution**.

## Approach(es)

### Two Pointers Approach

* Algorithm:
    1. Initialize two pointers, `left` at the beginning of the array (index 0) and `right` at the end of the array (index `len(numbers) - 1`).
    2. While `left < right`:
        * Calculate the `current_sum = numbers[left] + numbers[right]`.
        * If `current_sum == target`, return `[left + 1, right + 1]` (1-indexed indices).
        * If `current_sum < target`, increment `left` to consider a larger number.
        * If `current_sum > target`, decrement `right` to consider a smaller number.
    3. If the loop finishes without finding a solution (which should not happen based on the problem constraints), return an empty list `[]`.
* Data Structures:
  * No extra data structures are used.
* Time Complexity:
  * O(N), where N is the length of the `numbers` array. We iterate through the array at most once.
* Space Complexity:
  * O(1), constant extra space is used.
* Trade-offs:
  * This approach is very efficient in terms of both time and space, especially since the array is already sorted.
  * It takes advantage of the sorted nature of the input to avoid nested loops or using extra space.

### Binary Search Approach

* Algorithm:
    1. Iterate through the `numbers` array using a loop with index `i`.
    2. For each `numbers[i]`, calculate the `complement` needed to reach the `target`: `complement = target - numbers[i]`.
    3. Use binary search to find the `complement` in the rest of the array (from index `i + 1` to the end).
    4. If the `complement` is found at index `mid` using binary search, return `[i + 1, mid + 1]` (1-indexed indices).
    5. If the loop finishes without finding a solution, return an empty list `[]`.
* Data Structures:
  * No extra data structures are used.
* Time Complexity:
  * O(N log N), where N is the length of the `numbers` array. We iterate through the array once (O(N)), and for each element, we perform a binary search (O(log N)).
* Space Complexity:
  * O(1), constant extra space is used.
* Trade-offs:
  * While this approach still utilizes the sorted nature of the array, it is less efficient than the two-pointers approach due to the binary search in each iteration.
  * It is still a valid solution, especially if you were asked to implement a solution using binary search.

## Code

[Two Pointers Approach](./solution_two_pointers.py)
[Binary Search Approach](./solution_binary_search.py))
