```python
# 37. Sudoku Solver - Backtracking

def solveSudoku(board: list[list[str]]) -> None:
    """
    Solves a Sudoku puzzle using backtracking.  Modifies the board in place.
    """

    def is_valid(row, col, num):
        """Checks if placing 'num' at board[row][col] is valid."""

        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def solve():
        """Recursive helper function to solve the Sudoku."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":  # Find an empty cell
                    for num in map(str, range(1, 10)):  # Try numbers 1-9
                        if is_valid(row, col, num):
                            board[row][col] = num  # Place the number

                            if solve():  # Recursively try to solve the rest of the board
                                return True  # Solution found
                            else:
                                board[row][col] = "."  # Backtrack: Undo the placement

                    return False  # No valid number found for this cell

        return True  # All cells filled (base case for successful solution)

    solve()  # Start the solving process

```

```markdown
# 37. Sudoku Solver, Difficulty: Hard

## Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy *all* of the following rules:

1.  Each of the digits `1-9` must occur exactly once in each row.
2.  Each of the digits `1-9` must occur exactly once in each column.
3.  Each of the digits `1-9` must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The `'.'` character indicates empty cells.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

## Approach(es)

### Backtracking

Algorithm:

1.  **`is_valid(row, col, num)` Function:**
    *   Checks if placing the digit `num` (as a string) at `board[row][col]` is valid according to Sudoku rules.
    *   Checks for duplicates in the same row, column, and 3x3 subgrid.
    *   Returns `True` if valid, `False` otherwise.

2.  **`solve()` Function (Recursive):**
    *   Iterate through each cell `(row, col)` of the board:
        *   If the cell is empty (`board[row][col] == "."`):
            *   Try placing digits '1' through '9' in the cell:
                *   For each digit `num` (as a string):
                    *   If `is_valid(row, col, num)` returns `True`:
                        *   Place `num` in the cell: `board[row][col] = num`
                        *   Recursively call `solve()` to try to solve the rest of the board.
                        *   If the recursive call returns `True` (solution found), return `True`.
                        *   Otherwise (recursive call failed), backtrack:  `board[row][col] = "."` (remove the number and try the next one).
            *   If no digit from '1' to '9' can be placed in the current cell, return `False` (this branch is a dead end).
    *   If all cells are filled (the loop completes without finding any empty cells), return `True` (base case for a successful solution).
3. Call the recursive function `solve()`.

Data Structures:

*   2D List (the Sudoku board)

Time Complexity:

*   O(9^(m)), where m is the number of empty cells. In the worst case, for each empty cell, we try 9 possible digits. While this looks exponential, the constraints of the Sudoku puzzle significantly prune the search space, making it much faster in practice than the worst-case suggests.

Space Complexity:

*   O(m), where m is the number of empty cells.  The space is primarily used by the recursion stack, which can go as deep as the number of empty cells in the worst case. O(1) considering that the board is always 9x9.

Trade-offs:
* Backtracking can be computationally expensive for very large or complex problems, but Sudoku's constraint significantly reduce the complexity.

## Code

```python
def solveSudoku(board: list[list[str]]) -> None:
    """
    Solves a Sudoku puzzle using backtracking.  Modifies the board in place.
    """

    def is_valid(row, col, num):
        """Checks if placing 'num' at board[row][col] is valid."""

        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def solve():
        """Recursive helper function to solve the Sudoku."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":  # Find an empty cell
                    for num in map(str, range(1, 10)):  # Try numbers 1-9
                        if is_valid(row, col, num):
                            board[row][col] = num  # Place the number

                            if solve():  # Recursively try to solve the rest of the board
                                return True  # Solution found
                            else:
                                board[row][col] = "."  # Backtrack: Undo the placement

                    return False  # No valid number found for this cell

        return True  # All cells filled (base case for successful solution)

    solve()  # Start the solving process
```

## Notes

* This problem is a classic example of using backtracking to solve a constraint satisfaction problem.
* The `is_valid` function is crucial for enforcing the Sudoku rules.
* The recursive `solve` function systematically explores possible solutions, backtracking when a dead end is reached.
* The board is modified in place, so there's no need to return a new board.
* The time complexity, while exponential in the absolute worst case, is manageable in practice due to the constraints of the Sudoku puzzle.

```

**Step 5: Topic Extraction and Files**

*Prompt:* Topic Extraction
*Analysis*: Relevant topics are "Array", "Backtracking", and "Hash Table" (although we don't *explicitly* use a hash table, the `is_valid` function could be optimized using hash sets to store the seen numbers in each row, column, and subgrid, this optimization is often not necessary for the given constraints).

* `Arrays.md`: (already exists, reuse)
* Create a new file `Backtracking.md`

```markdown
# Backtracking

Backtracking is a general algorithmic technique for finding all (or some) solutions to computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## Key Concepts

*   **Candidate Solutions:**  Partial solutions that are built incrementally.
*   **Constraints:** Rules that define valid solutions.
*   **Choice Points:**  Points in the algorithm where we have multiple options to explore.
*   **Backtracking:**  When a partial solution violates a constraint, we "backtrack" to a previous choice point and try a different option.

## Algorithm (Recursive)

1.  **Base Case:**  If the current candidate solution is complete and satisfies all constraints, add it to the set of solutions (or return it if we're only looking for one solution).
2.  **Choice Point:**  For each possible choice at the current step:
    *   **Make the Choice:**  Extend the current candidate solution by making the choice.
    *   **Recursive Call:** Recursively call the backtracking function with the extended candidate solution.
    *   **Undo the Choice (Backtrack):** After the recursive call returns, undo the choice to restore the previous state. This is crucial for exploring other possibilities.

## When to Use Backtracking

*   **Constraint Satisfaction Problems:** Problems where you need to find solutions that satisfy a set of constraints (e.g., Sudoku, N-Queens).
*   **Combinatorial Search:** Problems where you need to find all possible combinations or permutations that meet certain criteria.
*   **Decision Problems:** Problems where you need to make a series of decisions to reach a goal.

## Advantages of Backtracking

*   **Systematic Exploration:**  Backtracking systematically explores the search space, ensuring that all possible solutions are considered (if necessary).
*   **Handles Constraints Effectively:**  Backtracking can efficiently handle complex constraints by abandoning partial solutions that violate those constraints.

## Disadvantages of Backtracking

*   **Exponential Time Complexity (in the worst case):**  For some problems, the search space can be very large, leading to exponential time complexity. However, pruning the search space with constraints can often make it practical.

## Examples

*   **Sudoku Solver:** Finding a valid solution to a Sudoku puzzle.
*   **N-Queens Problem:**  Placing N chess queens on an N×N chessboard so that no two queens threaten each other.
*   **Generating Permutations:**  Generating all possible permutations of a set of elements.
*   **Generating Subsets:**  Generating all possible subsets of a set.
*   **Graph Coloring:**  Assigning colors to vertices of a graph such that no two adjacent vertices have the same color.

## LeetCode problems related to Backtracking

*   [37. Sudoku Solver](0037-sudoku-solver/README.md)
*   [51. N-Queens](https://leetcode.com/problems/n-queens/)
*   [46. Permutations](https://leetcode.com/problems/permutations/)
* [78. Subsets](https://leetcode.com/problems/subsets/)
*   [79. Word Search](https://leetcode.com/problems/word-search/)
*   [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
*   [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
* [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
```
This creates the complete repository, including a backtracking solution, a detailed README, and a new "Backtracking.md" topic file, along with appropriate links to other files. It covers all aspects of the prompt and follows best practices.
