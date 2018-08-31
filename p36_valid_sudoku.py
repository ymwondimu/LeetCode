class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row_check = is_valid_row(board, i)
            col_check = is_valid_column(board, i)
            if row_check == False or col_check == False:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_check = is_valid_square(board, i, j)
                if square_check == False:
                    return False

        return True


def is_valid_row(board, row):
    d = {}
    for i in range(9):
        if board[row][i] != '.':
            val = board[row][i]
            if val in d:
                return False
            else:
                d[val] = 1

    return True


def is_valid_column(board, col):
    d = {}
    for i in range(9):
        if board[i][col] != '.':
            val = board[i][col]
            if val in d:
                return False
            else:
                d[val] = 1

    return True


def is_valid_square(board, row_start, col_start):
    d = {}
    for i in range(3):
        for j in range(3):
            row_index = row_start + i
            col_index = col_start + j

            if board[row_index][col_index] != '.':
                val = board[row_index][col_index]
                if val in d:
                    return False
                else:
                    d[val] = 1

    return True