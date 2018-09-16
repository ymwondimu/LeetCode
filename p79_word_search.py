def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if dfs(i, j, board, word):
                return True

    return False


def dfs(i, j, board, word):
    if len(word) == 0:
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False
    else:
        temp = board[i][j]
        board[i][j] = "#"
        res = dfs(i - 1, j, board, word[1:]) or dfs(i, j - 1, board, word[1:]) or dfs(i + 1, j,board, word[1:]) or dfs(i, j + 1, board, word[1:])
        board[i][j] = temp
        return res


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ABCCED"

    print (exist(board, word))

if __name__ == "__main__":
    main()