Okay, let's generate the LeetCode solution repository for problem 621, "Task Scheduler."

**Step 1: Problem Identification**

The input clearly defines:

*   **Problem Number:** 621
*   **Problem Name:** Task Scheduler
*   **Difficulty:** Medium

**Step 2: Problem File Creation**

We will create a directory named `0621-task-scheduler`.

**Step 3: Solution File Generation**

Since a solution wasn't provided, we will generate a Python solution. The most efficient approach involves calculating the idle slots based on the frequency of the most frequent tasks.

```python
# 0621. Task Scheduler - Greedy Approach with Frequency Counting

def leastInterval(tasks, n):
    frequencies = [0] * 26  # Count frequency of each task (A-Z)
    for task in tasks:
        frequencies[ord(task) - ord('A')] += 1

    frequencies.sort()
    max_frequency = frequencies[25]  # Frequency of the most frequent task
    idle_slots = (max_frequency - 1) * n

    for i in range(24, -1, -1):  # Iterate backwards through frequencies
        idle_slots -= min(max_frequency - 1, frequencies[i])

    idle_slots = max(0, idle_slots)  # Idle slots can't be negative
    return idle_slots + len(tasks)
```

This code will be saved as `0621-task-scheduler/solution.py`. We also provide a more detailed explanation version.

```python
# 0621. Task Scheduler - Greedy Approach with Frequency Counting (Detailed Explanation)

def leastInterval(tasks, n):
    """
    Calculates the minimum number of CPU intervals required to complete all tasks.

    Args:
        tasks: A list of task labels (uppercase English letters).
        n: The cooling interval between tasks with the same label.

    Returns:
        The minimum number of CPU intervals.
    """

    # 1. Count the frequency of each task.
    frequencies = [0] * 26  # Assuming tasks are uppercase English letters (A-Z)
    for task in tasks:
        frequencies[ord(task) - ord('A')] += 1

    # 2. Sort the frequencies in descending order.  This makes it easier to
    #    calculate the idle slots based on the most frequent task.
    frequencies.sort()

    # 3. Calculate the maximum frequency (frequency of the most frequent task).
    max_frequency = frequencies[25]

    # 4. Calculate the initial number of idle slots.
    #    The most frequent task determines the basic structure.  If the most
    #    frequent task appears 'max_frequency' times, there will be
    #    'max_frequency - 1' gaps between these occurrences.  Each gap needs
    #    to be at least 'n' intervals long.
    idle_slots = (max_frequency - 1) * n

    # 5. Reduce idle slots based on other tasks.
    #    Iterate through the frequencies of the *other* tasks (in descending
    #    order). We can fill in the idle slots with these other tasks.
    for i in range(24, -1, -1):
        # We can fill at most 'max_frequency - 1' slots with each of the
        # other tasks.  For example, if max_frequency is 4 and n is 2:
        #   A _ _ A _ _ A _ _ A   (idle_slots = (4-1)*2 = 6)
        # If we have another task 'B' that appears 3 times, we can fill 3
        # of the idle slots:
        #   A B _ A B _ A B _ A   (idle_slots = 6 - 3 = 3)
        # If 'B' appears only twice:
        #   A B _ A B _ A _ _ A
        # The number of idle slots we can fill is the minimum of the
        # number of occurrences of the task and (max_freq-1).
        idle_slots -= min(max_frequency - 1, frequencies[i])

    # 6. Ensure idle slots are not negative.
    #    If we have enough different tasks to fill all the idle slots,
    #    the result might be negative.  In that case, we just need the
    #    total number of tasks.
    idle_slots = max(0, idle_slots)

    # 7. Return the total number of intervals.
    #    This is the sum of the tasks and the idle slots.
    return idle_slots + len(tasks)
```
This code is saved as `0621-task-scheduler/solution_detailed.py`.
**Step 4: Problem README Generation**

```markdown
# 621. Task Scheduler, Difficulty: Medium

## Problem Description

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least `n` intervals between two tasks with the same label.

Return the *minimum number of CPU intervals* required to complete all tasks.

**Example 1:**

Input: `tasks = ["A","A","A","B","B","B"], n = 2`
Output: `8`
Explanation: A possible sequence is: `A -> B -> idle -> A -> B -> idle -> A -> B`.

**Example 2:**

Input: `tasks = ["A","C","A","B","D","B"], n = 1`
Output: `6`
Explanation: A possible sequence is: `A -> B -> C -> D -> A -> B`.

**Example 3:**

Input: `tasks = ["A","A","A", "B","B","B"], n = 3`
Output: `10`
Explanation: A possible sequence is: `A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B`.

**Constraints:**

*   `1 <= tasks.length <= 104`
*   `tasks[i]` is an uppercase English letter.
*   `0 <= n <= 100`

## Approach(es)

### Greedy Approach with Frequency Counting

The key idea is to prioritize the most frequent tasks. The number of idle slots is primarily determined by the most frequent task and the cooling interval `n`.

**Algorithm:**

1.  **Frequency Counting:** Count the frequency of each task using an array of size 26 (for uppercase English letters).
2.  **Sort Frequencies:** Sort the frequencies in descending order.
3.  **Calculate Idle Slots:**
    *   The most frequent task will have a frequency `max_frequency`.
    *   There will be `max_frequency - 1` gaps between occurrences of the most frequent task.
    *   Each gap must have at least `n` idle slots.  So, initially, `idle_slots = (max_frequency - 1) * n`.
4.  **Fill Idle Slots:** Iterate through the remaining frequencies (from the second most frequent to the least frequent):
    *   For each task, we can fill at most `max_frequency - 1` of the idle slots.
    *   Subtract `min(max_frequency - 1, frequency_of_current_task)` from `idle_slots`.
5.  **Handle Negative Idle Slots:** If `idle_slots` becomes negative (meaning we have enough different tasks to fill all the gaps), set `idle_slots` to 0.
6.  **Total Intervals:** The minimum number of intervals is the sum of the number of tasks and the number of idle slots: `len(tasks) + idle_slots`.

**Data Structures:**

*   Array (of size 26): To store the frequencies of the tasks.

**Time Complexity:**

*   O(N) for counting frequencies, where N is the number of tasks.
*   O(1) for sorting the frequencies array (since it has a fixed size of 26).
*   O(1) for iterating through the frequencies array (again, fixed size).
*   Overall: O(N)

**Space Complexity:**

*   O(1), since we are using a fixed-size array (of size 26) for frequencies, regardless of the input size.

**Trade-offs:**

*   This approach is very efficient (O(N) time and O(1) space).
*   It relies on the observation that the most frequent task and the cooling interval determine the structure of the optimal schedule.

## Code

[Greedy Approach with Frequency Counting](./solution_detailed.py)

## Notes

- The problem can also be solved using a Priority Queue (Max Heap), but the time complexity would be O(N log 26), which is essentially the same as O(N), but the constant factors would be larger.  The frequency counting approach is the most efficient.
- This is a classic scheduling problem with a clever greedy solution. Understanding why the greedy approach works is important.

```

**Step 5: Topics Extraction:**

Since we use a greedy approach, we create `Greedy.md` file.
```markdown
# Greedy Algorithms

Greedy algorithms are a class of algorithms that make locally optimal choices at each step with the hope of finding a global optimum.  They are often used for optimization problems where you need to find the best solution (maximum, minimum, shortest, longest, etc.).  Greedy algorithms don't always guarantee the *best* solution, but they are often simple to implement and efficient.

## Key Concepts

*   **Locally Optimal Choice:** At each step, a greedy algorithm makes the choice that looks best *at that moment*, without considering the future consequences.
*   **No Backtracking:** Once a choice is made, it's not reconsidered.  Greedy algorithms don't backtrack or revise previous decisions.
*   **Greedy Choice Property:**  A problem has the *greedy choice property* if a globally optimal solution can be obtained by making a sequence of locally optimal choices. This is the key property that justifies using a greedy algorithm.
*   **Optimal Substructure:** Like dynamic programming, greedy algorithms often rely on the *optimal substructure* property: an optimal solution to the problem contains within it optimal solutions to subproblems.  However, unlike dynamic programming, greedy algorithms don't explore all subproblems; they commit to a single choice at each step.

## How Greedy Algorithms Work

1.  **Make a Greedy Choice:** Select the best option available at the current step based on some criteria (e.g., the largest value, the shortest distance, the earliest deadline).
2.  **Reduce the Problem:**  After making the choice, reduce the problem to a smaller subproblem.
3.  **Repeat:** Repeat steps 1 and 2 until a solution is reached (e.g., all items are selected, the target is reached, the entire graph is traversed).

## When to Use Greedy Algorithms

*   **Optimization Problems:** Greedy algorithms are well-suited for problems where you're trying to find the maximum, minimum, shortest, longest, etc.
*   **Greedy Choice Property:** The most important consideration is whether the problem has the greedy choice property.  If making the locally optimal choice at each step *always* leads to a globally optimal solution, then a greedy algorithm is likely to work.  Proving the greedy choice property can sometimes be challenging.
*   **Efficiency:** Greedy algorithms are often very efficient (often linear or near-linear time complexity).  If efficiency is a primary concern, and you suspect a greedy approach might work, it's worth exploring.

## Common Greedy Algorithm Patterns

*   **Activity Selection:**  Selecting the maximum number of non-overlapping activities from a set of activities with start and end times.
*   **Fractional Knapsack:**  Choosing items with the highest value-to-weight ratio to maximize the total value within a given capacity (you can take fractions of items).
*   **Huffman Coding:**  Constructing a prefix code with minimum average codeword length for data compression.
*   **Minimum Spanning Tree (MST):**  Finding a tree that connects all vertices in a graph with the minimum total edge weight (Prim's and Kruskal's algorithms are greedy).
*   **Shortest Path (Dijkstra's Algorithm):** Finding the shortest path between two nodes in a graph with non-negative edge weights (Dijkstra's algorithm is a greedy algorithm).
* **Task Scheduling:** Schedule task to optimize some criteria (time, resources ..etc), e.g ([621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)).

## Example LeetCode Problems (with links)

*   **Jump Game:** [55. Jump Game](https://leetcode.com/problems/jump-game/) (Medium)
*   **Jump Game II:** [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) (Medium)
*   **Gas Station:** [134. Gas Station](https://leetcode.com/problems/gas-station/) (Medium)
*   **Activity Selection:** (Not a specific LeetCode problem, but a common pattern)
*   **Fractional Knapsack:** (Not a specific LeetCode problem, but a common pattern)
*    **Task Scheduler:** [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium)

## Tips for LeetCode Greedy Problems

*   **Look for Optimization:** Greedy algorithms are almost always used for optimization problems.
*   **Identify the Greedy Choice:** Determine what the locally optimal choice is at each step.  What criteria should you use to make the best decision at each point?
*   **Prove (or Disprove) Correctness:** Try to convince yourself (or formally prove) that the greedy choice property holds.  If you can't, consider counterexamples.  Sometimes, a seemingly greedy approach might not be correct.
*   **Sort:**  Sorting the input data is often a crucial step in greedy algorithms (e.g., sorting activities by finish time, sorting items by value-to-weight ratio).
*   **Practice:** The best way to get good at greedy algorithms is to practice. Try to identify the greedy choice and prove (or at least convince yourself) that it leads to an optimal solution.

Greedy algorithms are a powerful tool for solving optimization problems efficiently. However, it's important to verify that the greedy choice property holds to ensure that the algorithm produces a correct solution.
```

This is saved as `Greedy.md`. All files have been created.
