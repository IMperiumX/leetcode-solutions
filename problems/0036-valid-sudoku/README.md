
# 36. Valid Sudoku , Difficulty: Medium

**Link:** [https://leetcode.com/problems/valid-sudoku/](https://leetcode.com/problems/valid-sudoku/)

## Problem Description

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

**Note:**

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

## Solution Approach (Hash Sets)

The `solution.py` file contains a Python solution that uses hash sets to efficiently check the validity of the Sudoku board.

1. **Initialization:**
    * Create three arrays of hash sets: `rows`, `cols`, and `boxes`. Each array has a length of 9 to represent the 9 rows, 9 columns, and 9 sub-boxes of the Sudoku board.

2. **Iteration:**
    * Iterate through each cell of the Sudoku board using nested loops (rows and columns).
    * For each cell with a value (not '.'):
        * **Check Row:** Check if the value already exists in the hash set corresponding to the current row. If it does, the Sudoku is invalid, so return `False`. Otherwise, add the value to the row's hash set.
        * **Check Column:** Check if the value already exists in the hash set corresponding to the current column. If it does, the Sudoku is invalid, so return `False`. Otherwise, add the value to the column's hash set.
        * **Check Sub-box:** Calculate the index of the 3x3 sub-box to which the current cell belongs. Check if the value already exists in the hash set corresponding to that sub-box. If it does, the Sudoku is invalid, so return `False`. Otherwise, add the value to the sub-box's hash set.

3. **Return True:** If all cells are processed without finding any violations, it means the Sudoku board is valid, so return `True`.
