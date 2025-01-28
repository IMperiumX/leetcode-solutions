# Divide and Conquer

Divide and Conquer is an algorithmic paradigm that solves a problem by recursively breaking it down into smaller subproblems of the same type, solving those subproblems, and then combining their solutions to solve the original problem.

## Key Concepts

- **Divide:** Divide the problem into smaller subproblems of the same type.
- **Conquer:** Solve the subproblems recursively. If the subproblem is small enough (base case), solve it directly.
- **Combine:** Combine the solutions of the subproblems to get the solution to the original problem.

## Algorithm Template

```

function solve(problem):
  if problem is small enough:
    solve problem directly (base case)
    return solution

  divide problem into subproblems

  for each subproblem in subproblems:
    solution_subproblem = solve(subproblem)

  combine solution_subproblem to get solution for problem
  return solution

```

## Applications

- **Merge Sort:** Sorts an array by dividing it into two halves, recursively sorting each half, and then merging the sorted halves.
- **Quick Sort:** Sorts an array by picking a pivot element, partitioning the array into two subarrays (elements less than the pivot and elements greater than the pivot), recursively sorting the subarrays, and then combining them.
- **Binary Search:** Searches for an element in a sorted array by repeatedly dividing the search interval in half.
- **Strassen's Matrix Multiplication:** Multiplies two matrices more efficiently than the naive algorithm by recursively dividing the matrices into submatrices.
- **Closest Pair of Points:** Finds the closest pair of points in a set of points in a plane by recursively dividing the set of points into two halves, finding the closest pair in each half, and then considering the points near the dividing line.

## Time Complexity

The time complexity of a divide and conquer algorithm is often expressed using a recurrence relation. The Master Theorem can be used to solve many common recurrence relations.

- **Example (Merge Sort):**
  - `T(n) = 2T(n/2) + O(n)`
  - `a = 2` (number of subproblems)
  - `b = 2` (size of each subproblem relative to the original problem)
  - `f(n) = O(n)` (time to divide and combine)
  - By the Master Theorem, the time complexity is `O(n log n)`.

## Space Complexity

The space complexity depends on the depth of the recursion and the space used in the divide and combine steps.

- **Example (Merge Sort):**
  - Recursion depth: `O(log n)`
  - Space used in merge step: `O(n)`
  - Overall space complexity: `O(n)` (can be optimized to `O(n log n)` or `O(log n)` in some implementations)

## Trade-offs

- **Advantages:**
  - Can lead to efficient algorithms (e.g., `O(n log n)` for sorting).
  - Often amenable to parallelization.
- **Disadvantages:**
  - Recursive calls can have overhead.
  - Can be more complex to implement than iterative solutions.

## Related LeetCode Problems

- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (can be solved with divide and conquer)
- [169. Majority Element](https://leetcode.com/problems/majority-element/) (can be solved with divide and conquer)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (can be solved with QuickSelect, which is related to QuickSort)
- [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) (can be solved with modified merge sort)
- [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) (can be solved with modified merge sort)
