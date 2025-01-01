# 15. 3Sum, Difficulty: Medium

## Problem Description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: `nums = [-1,0,1,2,-1,-4]`
Output: `[[-1,-1,2],[-1,0,1]]`
Explanation:
`nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`.
`nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`.
`nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`.
The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`.
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: `nums = [0,1,1]`
Output: `[]`
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: `nums = [0,0,0]`
Output: `[[0,0,0]]`
Explanation: The only possible triplet sums up to 0.

Constraints:

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Approach(es)

### Two Pointers Approach

Algorithm:

1. Sort the input array `nums`.
2. Iterate through the array from left to right. For each element `nums[i]`:
    *   If `nums[i]` is greater than 0, break the loop (because the array is sorted, there won't be any triplets that sum to 0 if the first element is positive).
    *   If `nums[i]` is the same as the previous element `nums[i-1]`, skip it to avoid duplicate triplets.
    *   Use two pointers, `lo` (starting at `i+1`) and `hi` (starting at the end of the array), to find two numbers that sum to `-nums[i]`.
    *   Move the pointers towards each other based on the sum of the three numbers:
        *   If the sum is less than 0, increment `lo`.
        *   If the sum is greater than 0, decrement `hi`.
        *   If the sum is equal to 0, add the triplet `[nums[i], nums[lo], nums[hi]]` to the result. Increment `lo` and decrement `hi`. Skip any duplicate elements at `lo` and `hi` to avoid duplicate triplets.

Data Structures:

- Sorted array for efficient two-pointer traversal.

Time Complexity:

- O(n^2), where n is the length of the input array. Sorting takes O(n log n), and the two-pointer traversal takes O(n^2) in the worst case.

Space Complexity:

- O(log n) to O(n) depending on which sorting algorithm is used.

Trade-offs:

- Sorting the array is necessary for the two-pointer approach to work efficiently. This adds a logarithmic factor to the time complexity.
- The space complexity depends on the sorting algorithm used.

### Hash Set Approach

Algorithm:

1. Sort the input array `nums`.
2. Iterate through the array from left to right. For each element `nums[i]`:
 - If `nums[i]` is greater than 0, break the loop.
 - If `nums[i]` is the same as the previous element `nums[i-1]`, skip it.
 - Use a hash set `seen` to store the numbers encountered so far in the inner loop.
 - Iterate from `j = i + 1` to the end of the array. For each element `nums[j]`:
  - Calculate the `complement` needed to reach a sum of 0: `complement = -nums[i] - nums[j]`.
  - If the `complement` is found in the `seen` set, a triplet is found. Add `[nums[i], nums[j], complement]` to the result.
  - Skip any duplicate elements at `j` to avoid duplicate triplets.
  - Add `nums[j]` to the `seen` set.
Data Structures:

- Sorted array for efficient iteration and duplicate handling.
- Hash set to store encountered numbers for quick lookups.
Time Complexity:

- O(n^2), where n is the length of the input array. Sorting takes O(n log n), and the nested loops take O(n^2).

Space Complexity:

- O(n) in the worst case, where n is the length of the input array. This is due to the hash set storing up to n elements.

Trade-offs:

- The hash set approach avoids the need for two pointers but uses extra space to store encountered numbers.
- The time complexity is still O(n^2) due to the nested loops.

## Code

[Two Pointers Approach](./solution_two_pointers.py)
[Hash Set Approach](./solution_hashset.py)

## Notes

- The problem can also be solved using a brute-force approach (three nested loops), but it would have a time complexity of O(n^3) and is not efficient for large input arrays.
- The two-pointer and hash set approaches are generally preferred due to their better time complexity.
- When choosing between the two-pointer and hash set approaches, consider the trade-off between space complexity (hash set uses more space) and the complexity of implementation (two-pointer approach might be slightly more complex to implement).
- It is important to handle duplicate elements properly to avoid duplicate triplets in the result.
