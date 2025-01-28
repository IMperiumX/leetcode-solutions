# 2657. Find the Prefix Common Array of Two Arrays, Difficulty: Medium

## Problem Description

You are given two 0-indexed integer permutations `A` and `B` of length `n`.

A prefix common array of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return the prefix common array of `A` and `B`.

A sequence of `n` integers is called a permutation if it contains all integers from 1 to `n` exactly once.

**Example 1:**

```
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation:
At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
```

**Example 2:**

```
Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation:
At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
```

**Constraints:**

- `1 <= A.length == B.length == n <= 50`
- `1 <= A[i], B[i] <= n`
- It is guaranteed that `A` and `B` are both a permutation of `n` integers.

## Approach(es)

### Set Intersection Approach

**Algorithm:**

1. Initialize an array `C` of size `n` filled with 0s.
2. Iterate through the arrays `A` and `B` from index `i = 0` to `n-1`:
    - Create a set `setA` containing the elements of `A` from index 0 to `i`.
    - Create a set `setB` containing the elements of `B` from index 0 to `i`.
    - Find the intersection of `setA` and `setB` using the `intersection()` method.
    - The size of the intersection represents the number of common elements up to index `i`.
    - Store the size of the intersection in `C[i]`.
3. Return the `C` array.

**Data Structures:**

- `C` array (list of integers)
- `setA` (set of integers)
- `setB` (set of integers)

**Time Complexity:**

- O(n^2) in the worst case, where n is the length of the arrays. Creating the sets and finding the intersection can take up to O(i) time for each index `i`.

**Space Complexity:**

- O(n) to store the `C` array and the sets `setA` and `setB` in the worst case.

**Trade-offs:**

- This approach is relatively easy to implement and understand.
- The use of sets makes the common element check efficient.
- The time complexity could be improved if we could avoid recreating the sets in each iteration, but given the small constraints, this solution is sufficient.

## Code

[Set Intersection Approach](./solution.py)

## Notes

- This problem demonstrates a simple application of sets for finding common elements between arrays.
- The problem can also be solved using other approaches, such as using frequency counters or nested loops, but the set intersection approach is generally more concise and efficient for this specific problem.
- Given the small constraints (n <= 50), even less optimized solutions would likely pass the tests. However, for larger constraints, optimizing the time complexity would become more important.
