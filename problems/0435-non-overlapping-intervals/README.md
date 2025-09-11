Okay, let's generate the LeetCode solution repository for problem 435, "Non-overlapping Intervals".

**Step 1: Problem Identification**

*   **Problem Number:** 435
*   **Problem Name:** Non-overlapping Intervals
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

We'll create a directory named `0435-non-overlapping-intervals`.

**Step 3: Solution File Generation**

Since no solution was provided, I'll generate a Python solution using the greedy approach, sorting by end times. This is the standard and most efficient way to solve this problem.

```python
# 0435-non-overlapping-intervals/solution_greedy.py
# 435. Non-overlapping Intervals - Greedy (Sort by End Times)

def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    """
    Finds the minimum number of intervals to remove to make the rest non-overlapping.
    """
    if not intervals:
        return 0

    # Sort intervals by their end times.
    intervals.sort(key=lambda x: x[1])

    removed_count = 0
    end_time = intervals[0][1]  # Initialize with the end time of the first interval

    for i in range(1, len(intervals)):
        # If the current interval overlaps with the previous one (start time < previous end time),
        # we need to remove one.  We *keep* the one that ends earlier (already sorted).
        if intervals[i][0] < end_time:
            removed_count += 1
        else:
            # No overlap, update the end_time
            end_time = intervals[i][1]

    return removed_count

```

**Step 4: Problem README Generation**

```markdown
# 435. Non-overlapping Intervals, Difficulty: Medium

## Problem Description

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the *minimum number of intervals* you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only *touch* at a point are non-overlapping. For example, `[1, 2]` and `[2, 3]` are non-overlapping.

**Example 1:**

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

**Example 2:**

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

**Example 3:**

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

**Constraints:**

*   1 <= intervals.length <= 10<sup>5</sup>
*   intervals[i].length == 2
*   -5 * 10<sup>4</sup> <= start<sub>i</sub> < end<sub>i</sub> <= 5 * 10<sup>4</sup>

## Approach(es)

### Greedy (Sort by End Times)

Algorithm:

1.  **Sort by End Times:** Sort the input `intervals` array based on the *end times* of the intervals in ascending order. This is crucial for the greedy approach.
2.  **Initialize:** Initialize `removed_count` to 0 and `end_time` to the end time of the first interval (after sorting).
3.  **Iterate:** Iterate through the sorted intervals starting from the second interval.
4.  **Overlap Check:** For each interval:
    *   If the current interval's start time is *less than* `end_time`, there's an overlap.  Increment `removed_count` (we're removing the current interval because we want to keep the interval with smaller end-time).
    *   Otherwise (no overlap), update `end_time` to the current interval's end time.
5.  **Return:** Return `removed_count`.

Data Structures:

*   None (we're working directly with the sorted input array).

Time Complexity:

*   O(N log N):  Dominated by the sorting step.  The iteration takes O(N) time.

Space Complexity:

*   O(1): We sort in place (most sorting algorithms have O(1) or, at most, O(log N) space complexity, but for the purpose of LeetCode problem analysis, we typically consider in-place sorts as O(1) space, the important aspect is that it doesn't scale with N). If we cannot modify input it can be O(N) to make a copy.

Trade-offs:

-   The greedy approach, combined with sorting by end times, provides an optimal solution to this problem.
-   Sorting is the most expensive operation.
- Why Sort by ending time:
    - Our aim is to maximize the number of non-overlapping intervals.
    - If we have two intervals, one ends earlier than the other, we keep the earlier, because it will allow us to accommodate more intervals.

## Code

[Greedy (Sort by End Times)](./solution_greedy.py)

## Notes (Optional)

*   This problem is a classic example of an "Interval Scheduling" problem, where the goal is to maximize the number of non-overlapping activities (or, in this case, minimize the number of removed intervals).
*   Sorting by start times would *not* lead to an optimal solution.  Consider the example `[[1, 10], [2, 3], [3, 4]]`.
* The greedy choice property holds: at each step, we choose the interval that ends earliest among the remaining intervals, and this leads to a globally optimal solution.
```

**Step 5: Topic Extraction and Files**

The main topics for this problem are:

1.  **Greedy Algorithms:** The core strategy used.
2.  **Sorting:**  Essential for the greedy approach.
3. **Interval Scheduling:**  A specific problem category that this falls under.

Let's generate `Greedy_Algorithms.md`, and `Interval_Scheduling.md`. We already have `Sorting.md`.
```markdown
# Greedy Algorithms

## Explanation

A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. In many problems, a greedy strategy does not produce an optimal solution, but a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

Key Characteristics:

*   **Local Optimization:**  At each step, the algorithm makes the choice that looks best *at that moment*, without considering the long-term consequences.
*   **No Backtracking:**  Once a choice is made, it's not reconsidered.
*   **Greedy Choice Property:**  A globally optimal solution can be obtained by making a locally optimal (greedy) choice.
*   **Optimal Substructure:**  An optimal solution to the problem contains within it optimal solutions to subproblems.

Advantages:

*   **Simplicity:** Greedy algorithms are often easy to design and implement.
*   **Efficiency:** Greedy algorithms are often very efficient, with linear or near-linear time complexity.

Disadvantages:

*   **Not Always Optimal:**  Greedy algorithms don't always find the globally optimal solution.  It's crucial to prove that the greedy choice property holds for the problem.
*   **Proof of Correctness:**  Proving the correctness of a greedy algorithm can be challenging.

Common Uses:

*   **Interval Scheduling:**  Finding the maximum number of non-overlapping intervals (like in this LeetCode problem).
*   **Huffman Coding:**  A greedy algorithm for data compression.
*   **Dijkstra's Algorithm:**  Finding the shortest paths in a graph with non-negative edge weights.
*   **Kruskal's Algorithm and Prim's Algorithm:** Finding minimum spanning trees in a graph.
*   **Activity Selection Problem.**
*   **Fractional Knapsack Problem.**

## Example (Python - Fractional Knapsack):

```python
def fractional_knapsack(capacity, items):
    # items is a list of (value, weight) tuples
    # Calculate value-to-weight ratio
    for i in range(len(items)):
        items[i] = (items[i][0], items[i][1], items[i][0] / items[i][1]) # (value,weight,ratio)

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for value, weight, ratio in items:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            break  # Knapsack is full

    return total_value

# Example Usage:
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value: {max_value}") #240.0
```

## Related LeetCode Problems:

* [435. Non-overlapping Intervals](0435-non-overlapping-intervals/README.md)
* [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
* [55. Jump Game](https://leetcode.com/problems/jump-game/)
* [134. Gas Station](https://leetcode.com/problems/gas-station/)
* [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)
* [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
```

```markdown
# Interval Scheduling

## Explanation

Interval scheduling is a class of problems in computer science, particularly in the field of algorithm design and operations research.  The general problem involves selecting a set of non-overlapping intervals from a collection of intervals, often with the goal of maximizing the number of selected intervals or maximizing the total value (or weight) of the selected intervals.

Key Concepts:

*   **Intervals:**  Represented by a start time and an end time (or a start time and a duration).
*   **Non-overlapping:** Two intervals are non-overlapping if they do not share any common time period. Intervals that only touch at endpoints are considered non-overlapping (e.g., [1, 2] and [2, 3]).
*   **Objective Function:**  Typically to maximize the number of selected intervals (unweighted) or the sum of their values/weights (weighted).

Common Variations:

*   **Unweighted Interval Scheduling:**  Maximize the *number* of non-overlapping intervals.
*   **Weighted Interval Scheduling:**  Maximize the *total value* (or weight) of non-overlapping intervals, where each interval has an associated value.  This is often solved using dynamic programming.
*   **Multiple Resource Scheduling:** Scheduling intervals on multiple resources (e.g., rooms, machines).
* **Job Shop Scheduling:** A complex scheduling problem involving multiple operations and machines.

Common Solution Approaches:

*   **Greedy (Sort by End Time):**  For the unweighted case, sorting intervals by their end times and greedily selecting non-overlapping intervals is optimal.
*   **Dynamic Programming:**  For the weighted case, dynamic programming is typically used.
* **Earliest Deadline First**: Sort intervals by their deadlines (end times) in ascending order and select them greedily.

## Example (Python - Unweighted Interval Scheduling, Sort by End Time):

```python
def unweighted_interval_scheduling(intervals):
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])

    selected_intervals = []
    if intervals:
        end_time = intervals[0][1]  #end time of first interval
        selected_intervals.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time:
                selected_intervals.append(intervals[i])
                end_time = intervals[i][1]
    return selected_intervals
# Example usage
intervals = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11]]
non_overlapping = unweighted_interval_scheduling(intervals)
print(non_overlapping)  # Output: [[1, 4], [5, 7], [8, 11]]
```
## Related Leetcode problems:

*   [435. Non-overlapping Intervals](0435-non-overlapping-intervals/README.md)
*   [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons)
* [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii)
* [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms) (A simpler version: can a person attend all meetings?)
* [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
```
```markdown
# Sorting

## Explanation

Sorting is a fundamental operation in computer science that arranges the elements of a list (or array) in a specific order, typically numerical or lexicographical (alphabetical).  There are many different sorting algorithms, each with its own advantages and disadvantages in terms of time complexity, space complexity, stability, and ease of implementation.

Key Concepts:

*   **In-Place Sorting:**  Sorts the elements within the original array without requiring significant extra space (typically O(log n) or O(1) auxiliary space).
*   **Stable Sorting:**  Maintains the relative order of equal elements.  If two elements have the same value, their order in the sorted output is the same as their order in the original input.
*   **Comparison-Based Sorting:**  Sorts by comparing pairs of elements.  Comparison-based sorting algorithms have a lower bound of O(n log n) time complexity in the average and worst cases.
*   **Non-Comparison-Based Sorting:**  Sorts without directly comparing elements (e.g., counting sort, radix sort).  These can achieve linear time complexity under certain conditions.

Common Sorting Algorithms:

*   **Bubble Sort:**  Simple but inefficient (O(n<sup>2</sup>)).  Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
*   **Selection Sort:**  Also O(n<sup>2</sup>), but generally performs fewer swaps than bubble sort.  Finds the minimum element and places it at the beginning, then repeats for the remaining unsorted portion.
*   **Insertion Sort:**  O(n<sup>2</sup>) in the worst and average cases, but O(n) in the best case (already sorted input).  Efficient for small datasets or nearly sorted data.  Builds the sorted array one element at a time.
*   **Merge Sort:**  O(n log n) in all cases.  A divide-and-conquer algorithm that recursively divides the array, sorts the subarrays, and then merges them.  Stable and efficient, but requires O(n) auxiliary space.
*   **Quicksort:**  O(n log n) on average, but O(n<sup>2</sup>) in the worst case (rare with good pivot selection).  A divide-and-conquer algorithm that partitions the array around a pivot element.  Generally very efficient in practice, but can be unstable.
*   **Heapsort:** O(n log n) in all cases. Uses a binary heap data structure.  In-place, but not stable.
*   **Counting Sort:**  O(n + k), where k is the range of input values.  Non-comparison-based.  Efficient when k is not significantly larger than n.
*   **Radix Sort:** O(nk), where k is the number of digits (or "passes"). Non-comparison-based.  Efficient for sorting integers or strings with fixed-length keys.

## Example (Python - Merge Sort and Quick Sort)
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr): #In-place
    def partition(arr, low, high):
        pivot = arr[high]  # Choose the last element as the pivot
        i = low - 1  # Index of the smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
# Example Usage:
arr_merge = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr_merge) #Creates a new sorted array
print(f"Merge Sorted array: {arr_merge}")

arr_quick = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr_quick) #Sorts inplace
print(f"Quick Sorted array: {arr_quick}")
```

## Related Leetcode problems
*   [435. Non-overlapping Intervals](0435-non-overlapping-intervals/README.md)
*   [148. Sort List](0148-sort-list/README.md)
*   [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
*   [179. Largest Number](https://leetcode.com/problems/largest-number/)
* [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
* [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms)
```

This completes the repository for LeetCode problem 435.  It includes a detailed explanation of the greedy approach, sorting, time/space complexity, and separate topic files for "Greedy Algorithms" and "Interval Scheduling," and "Sorting". The code implements the efficient sort-by-end-times strategy.
