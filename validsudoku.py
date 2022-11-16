""" Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules."""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hash sets of rows and columns and squares to determine if any duplicate values

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue

                # check if rows/cols/squares already in set
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3),(c//3)]:
                    return False
                # otherwise add num to the set
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3),(c//3)].add(board[r][c])
        return True
                