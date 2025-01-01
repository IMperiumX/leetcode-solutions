# Backtracking

## Introduction

**Backtracking** is a general algorithmic technique that tries to build a solution incrementally, one piece at a time. It explores all possible configurations of a solution space by making a choice, exploring the consequences of that choice, and then undoing the choice (backtracking) if it doesn't lead to a valid or desired solution. It's like navigating a maze by trying different paths and turning back when you hit a dead end.

## Key Concepts

1. **Choice:** At each step, there is a set of choices to make. For example, in the "Subsets" problem, the choice is whether to include or exclude an element in the current subset.

2. **Constraints:** There might be constraints that limit the valid choices. For example, in the N-Queens problem, you cannot place two queens in the same row, column, or diagonal.

3. **Goal:** The goal is to find a valid solution that satisfies all constraints and potentially meets some optimization criteria (e.g., finding the shortest path or the minimum cost).

## How Backtracking Works

1. **Start with an initial state:** This is usually an empty solution or a starting configuration.

2. **Make a choice:** Select one of the available choices at the current step.

3. **Explore the consequences:** Recursively call the backtracking function to explore the consequences of the current choice. This leads to a new state.

4. **Check for a valid solution:**
    * If the new state represents a valid solution (meets all constraints and the goal), record it or return it.
    * If the new state is not a valid solution and there are no more choices to explore, backtrack.

5. **Backtrack:** Undo the current choice (go back to the previous state) and try a different choice.

6. **Repeat steps 2-5:** Continue this process until all possible configurations have been explored or the desired solution has been found.

## Backtracking Algorithm (Pseudocode)

```text

function backtrack(state):
  if is_valid_solution(state):
    record_solution(state)
    return

  for each choice in get_choices(state):
    if is_valid_choice(choice, state):
      make_choice(choice, state)
      backtrack(state)  // Explore consequences
      undo_choice(choice, state)  // Backtrack

```

## Example: Subsets Problem

**Problem:** Given a set of unique integers, return all possible subsets (the power set).

**Solution (Python):**

```python
def subsets(nums):
    result = []

    def backtrack(index, current_subset):
        result.append(current_subset[:])  # Add a copy of the current subset to the result

        for i in range(index, len(nums)):
            current_subset.append(nums[i])  # Make a choice: include the current number
            backtrack(i + 1, current_subset)  # Explore consequences
            current_subset.pop()  # Backtrack: undo the choice

    backtrack(0, [])
    return result
```

**Explanation:**

1. **Choice:** Include or exclude the element at the current index (`nums[i]`).

2. **Constraints:** None in this particular problem.

3. **Goal:** Generate all possible subsets.

4. **`backtrack(index, current_subset)`:**
    * `result.append(current_subset[:])`: Adds a copy of the current subset to the result (this is when a valid subset is found).
    * `for i in range(index, len(nums))`: Iterates through the remaining elements.
    * `current_subset.append(nums[i])`: Makes a choice (include).
    * `backtrack(i + 1, current_subset)`: Explores further.
    * `current_subset.pop()`: Backtracks (undoes the choice).

## Advantages of Backtracking

* **Systematic Exploration:** Guarantees that all possible solutions will be considered.
* **Flexibility:** Can be adapted to solve a wide range of problems with different constraints and goals.
* **Conceptual Simplicity:** The basic idea of making choices, exploring, and undoing is relatively easy to grasp.

## Disadvantages of Backtracking

* **Time Complexity:** Can be very slow for problems with a large search space (often exponential time complexity).
* **Space Complexity:** Can use a significant amount of memory due to recursion (though techniques like iterative deepening can mitigate this).

## Common Applications of Backtracking

* **Combinatorial Problems:** Generating permutations, combinations, subsets, etc.
* **Constraint Satisfaction Problems:** Sudoku, N-Queens, map coloring.
* **Game Playing:** Chess, checkers, other board games (often combined with techniques like Minimax).
* **Graph Algorithms:** Finding paths, cycles, Hamiltonian cycles.

## A general approach to backtracking questions in Python \(Subsets, Permutations, Combination Sum, Palindrome Partitioning\)

```python
def subsets(nums):
    """
    https://leetcode.com/problems/subsets/
    Finds all subsets of a set (no duplicates in the input).
    """
    res = []
    nums.sort()  # Sorting is optional for subsets without duplicates

    def backtrack(start, current_subset):
        res.append(current_subset[:])  # Add a copy of the current subset
        for i in range(start, len(nums)):
            current_subset.append(nums[i])  # Include the current element
            backtrack(i + 1, current_subset)  # Explore subsets with this element
            current_subset.pop()  # Backtrack: remove the element for other combinations

    backtrack(0, [])
    return res
```

```python
def subsets_with_dup(nums):
    """
    https://leetcode.com/problems/subsets-ii/
    Finds all subsets of a set (may contain duplicates in the input).
    """
    res = []
    nums.sort()  # Sorting is important to handle duplicates

    def backtrack(start, current_subset):
        res.append(current_subset[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return res
```

```python

def permute(nums):
    """
    https://leetcode.com/problems/permutations/
    Finds all permutations of a set (no duplicates in the input).
    """
    res = []

    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            res.append(current_permutation[:])
            return

        for i in range(len(nums)):
            if nums[i] in current_permutation:
                continue  # Skip if element is already used
            current_permutation.append(nums[i])
            backtrack(current_permutation)
            current_permutation.pop()

    backtrack([])
    return res
```

```python

def permute_unique(nums):
    """
    https://leetcode.com/problems/permutations-ii/
    Finds all unique permutations of a set (may contain duplicates).
    """
    res = []
    nums.sort()  # Sorting helps with duplicate handling
    used = [False] * len(nums)  # Keep track of used elements

    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            res.append(current_permutation[:])
            return

        for i in range(len(nums)):
            # Skip if:
            # 1. Element is already used
            # 2. It's a duplicate of the previous element AND the previous wasn't used
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue

            used[i] = True
            current_permutation.append(nums[i])
            backtrack(current_permutation)
            used[i] = False  # Backtrack: mark as unused
            current_permutation.pop()

    backtrack([])
    return res
```

```python

def combination_sum(nums, target):
    """
    https://leetcode.com/problems/combination-sum/
    Finds combinations that sum to a target (can reuse elements).
    """
    res = []
    nums.sort()  # Optional but can help with pruning

    def backtrack(start, current_combination, remaining):
        if remaining < 0:
            return  # Exceeded target
        if remaining == 0:
            res.append(current_combination[:])
            return

        for i in range(start, len(nums)):
            current_combination.append(nums[i])
            # Stay at the same index (i) to allow reuse of elements
            backtrack(i, current_combination, remaining - nums[i])
            current_combination.pop()

    backtrack(0, [], target)
    return res
```

```python

def combination_sum2(nums, target):
    """
    https://leetcode.com/problems/combination-sum-ii/
    Finds combinations that sum to a target (cannot reuse elements).
    """
    res = []
    nums.sort()  # Important for handling duplicates

    def backtrack(start, current_combination, remaining):
        if remaining < 0:
            return
        if remaining == 0:
            res.append(current_combination[:])
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            current_combination.append(nums[i])
            backtrack(i + 1, current_combination, remaining - nums[i])  # Move to the next index (i+1)
            current_combination.pop()

    backtrack(0, [], target)
    return res
```

```python

def partition(s):
    """
    https://leetcode.com/problems/palindrome-partitioning/
    Partitions a string into palindromic substrings.
    """
    res = []

    def is_palindrome(sub):
        return sub == sub[::-1]  # Efficient palindrome check

    def backtrack(start, current_partition):
        if start == len(s):
            res.append(current_partition[:])
            return

        for i in range(start, len(s)):
            if is_palindrome(s[start:i + 1]):
                current_partition.append(s[start:i + 1])
                backtrack(i + 1, current_partition)
                current_partition.pop()

    backtrack(0, [])
    return res

```

## Problems Related to Backtracking

1. [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
2. [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
3. [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
4. [46. Permutations](https://leetcode.com/problems/permutations/)
5. [51. N-Queens](https://leetcode.com/problems/n-queens/)
6. [78. Subsets](./../problems/0078-subsets/README.md)
7. [79. Word Search](https://leetcode.com/problems/word-search/)
8. [90. Subsets II](https://leetcode.com/problems/subsets-ii/)
9. [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
