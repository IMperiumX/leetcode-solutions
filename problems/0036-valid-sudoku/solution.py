# Checking Rows, Columns, and Subgrids

"""
Rows: It iterates through each row and uses a set seen to keep track of the numbers encountered.
 If a number (other than '.') is already in the set, it means there's a repetition in the row, and the board is invalid.

Columns: Similarly, it iterates through each column and uses a set to check for repetitions within the column.

Subgrids: It iterates through the 9 3x3 subgrids. For each subgrid, it uses a set to ensure
that there are no repeated numbers within that subgrid. The outer loops with steps of 3
(for i in range(0, 9, 3), for j in range(0, 9, 3)) help to traverse the top-left corner of each subgrid.

If all rows, columns, and subgrids pass the repetition check, the function returns True, indicating a valid Sudoku board.

Time Complexity: O(1) - The function always operates on a 9x9 board, so the time complexity is constant.

"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid.

        It checks if each row, each column, and each 3x3 subgrid contains the digits 1-9 without repetition.
        """

        # Check rows
        for row in board:
            seen = set()
            for cell in row:
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)

        # Check subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        cell = board[row][col]
                        if cell != ".":
                            if cell in seen:
                                return False
                            seen.add(cell)

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid.

        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check box
                box_index = (r // 3) * 3 + c // 3
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True
