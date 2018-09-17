def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    output = []
    dfs(0, 0, matrix, output, False)
    return output


def dfs(i, j, board, output, up):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    else:
        if board[i][j] != "#":
            # print ((i,j))
            # print (board[i][j])
            output.append(board[i][j])
            board[i][j] = "#"
            if up:
                dfs(i - 1, j, board, output, True)
            dfs(i, j + 1, board, output, False)
            dfs(i + 1, j, board, output, False)
            dfs(i, j - 1, board, output, False)
            dfs(i - 1, j, board, output, True)
        else:
            return


def main():
    matrix =[ [1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    print (spiralOrder(matrix))


if __name__ == "__main__":
    main()
