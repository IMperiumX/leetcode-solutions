**Step 1: Problem Identification**

*   **Prompt 1:** The input is the URL "<https://leetcode.com/problems/employee-free-time/description/>".  This points directly to LeetCode problem 759, "Employee Free Time," which is a Hard problem.  Note: This problem requires a LeetCode premium subscription to access fully.

    *   **Output:** Problem Number: 759, Problem Name: Employee Free Time, Difficulty: Hard

**Step 2: Problem File Creation**

*   Create a directory named `0759-employee-free-time`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:**  I'll generate a Python solution. Since this problem involves merging intervals and finding gaps, sorting and a sweep-line-like approach are appropriate.

*File: 0759-employee-free-time/solution.py*

```python
# 759. Employee Free Time - Merge Intervals Approach

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

def employeeFreeTime(schedule):
    """
    Finds the common free time for a list of employee schedules.

    Args:
        schedule: A list of employee schedules, where each schedule is a list of Intervals.

    Returns:
        A list of Intervals representing the common free time.
    """

    # Flatten the schedule into a single list of intervals
    intervals = []
    for employee_schedule in schedule:
        for interval in employee_schedule:
            intervals.append(interval)

    # Sort intervals by start time
    intervals.sort(key=lambda x: x.start)

    # Merge overlapping intervals
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals or interval.start > merged_intervals[-1].end:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)

    # Find gaps between merged intervals (free time)
    free_time = []
    for i in range(len(merged_intervals) - 1):
        free_time.append(Interval(merged_intervals[i].end, merged_intervals[i + 1].start))

    return free_time
```

**Step 4: Create Related Topics Files**

*File: 0759-employee-free-time/Intervals.md*
```markdown
# Intervals

Interval problems are a common category on LeetCode and in coding interviews.  They involve working with ranges of values, typically represented as pairs (start, end).  Common tasks include merging overlapping intervals, finding intersections, inserting new intervals, and detecting conflicts.

## Key Concepts

*   **Interval:** A range of values defined by a start and end point. The end point might be inclusive or exclusive.  On LeetCode, intervals are often represented using a custom `Interval` class or simply as tuples/lists of two elements.
*   **Overlapping Intervals:** Two intervals overlap if they share at least one common point.
*   **Disjoint Intervals:** Two intervals are disjoint if they do not overlap.
*   **Sorted Intervals:**  Many interval problems become easier to solve if the intervals are sorted by their start times (or sometimes by their end times).

## Common Interval Operations and Patterns

*   **Sorting:** Sorting intervals by their start times is a crucial preprocessing step for many interval problems.
*   **Merging Overlapping Intervals:**  Combining overlapping intervals into a single, larger interval.  This is a fundamental operation in many interval problems.
*   **Inserting a New Interval:**  Adding a new interval to a set of existing intervals, potentially merging it with overlapping intervals.
*   **Finding Intersections:**  Determining the overlapping regions between intervals.
*   **Sweep Line Algorithm:** A technique where you imagine a "sweep line" moving across the intervals (usually from left to right). You process events (start and end points of intervals) as the sweep line encounters them.
* **Checking Conflicts**: Detecting if there is conflict between given intervals.

## Example: Merging Overlapping Intervals

Given a list of intervals, merge all overlapping intervals.

**Input:** `[[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`

**Algorithm (Merge Intervals):**

1.  **Sort:** Sort the intervals by their start times.
2.  **Iterate:** Iterate through the sorted intervals.
3.  **Merge:**
    *   If the current interval overlaps with the last merged interval, update the end time of the last merged interval.
    *   Otherwise, add the current interval to the list of merged intervals.

## Related LeetCode Problems

*   [759. Employee Free Time](./0759-employee-free-time)
*   [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
*   [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
*   [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Easy - can attend all meetings?)
*   [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Medium - minimum number of meeting rooms)
*   [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
*    [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
```

**Step 5: Problem README Generation**

*File: 0759-employee-free-time/README.md*

```markdown
# 759. Employee Free Time, Difficulty: Hard

## Problem Description

(Note: This problem description is based on the general understanding of the "Employee Free Time" problem, as the full problem statement requires a LeetCode premium subscription.)

We are given a list `schedule` of employees, which represents the working time of each employee.

Each employee has a list of non-overlapping `Intervals`, and these intervals are in sorted order.

Return the list of finite intervals representing *common, positive-length free time* for *all* employees, also in sorted order.

(Even though we are representing `Intervals` in the input as lists, they are in fact `Interval` objects.)

**Example (Conceptual):**

Input:  `schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]`
Output: `[[3,4]]`

Input:  `schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]`
Output: `[[5,6],[7,9]]`

**Constraints (Conceptual):**

*   `1 <= schedule.length , schedule[i].length <= 50`
*   `0 <= schedule[i].start < schedule[i].end <= 10^8`

## Approach(es)

### Merge Intervals Approach

Algorithm:

1.  **Flatten the Schedule:** Combine all employee schedules into a single list of `Interval` objects.
2.  **Sort Intervals:** Sort the intervals based on their start times.
3.  **Merge Overlapping Intervals:** Iterate through the sorted intervals and merge any overlapping intervals.  This results in a list of non-overlapping intervals representing *busy* times.
4.  **Find Gaps (Free Time):** Iterate through the merged busy intervals. The gaps between consecutive busy intervals represent the common free time. Create new `Interval` objects for these gaps and add them to the result list.
5.  **Return Free Time:** Return the list of free time `Interval` objects.

Data Structures:

*   List to store all intervals.
*   List to store merged intervals.
*   List to store free time intervals.

Time Complexity:

*   O(n log n), where n is the total number of intervals across all employees.  The dominant factor is sorting the intervals.  Merging and finding gaps takes linear time.

Space Complexity:

*   O(n) in the worst case, to store the flattened list of intervals and the merged intervals.

Trade-offs:

* This approach is efficient and clearly solves the problem by first merging all busy times and then identifying the free time slots.

## Code

[Merge Intervals Approach](./solution.py)

## Notes

This problem is a variation of the classic "Merge Intervals" problem. The key steps are to flatten the input, sort the intervals, merge overlapping intervals, and then identify the gaps between the merged intervals to represent the free time.  The problem's difficulty comes from handling the nested lists and correctly merging the intervals. Using a custom Interval class (as defined on LeetCode) makes the code more readable.
```

Final Folder Structure:
```
0759-employee-free-time/
├── solution.py
├── README.md
└── Intervals.md
```
