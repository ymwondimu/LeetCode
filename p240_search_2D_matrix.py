def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False

    i = 0
    j = len(matrix[0]) - 1

    while i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1

        elif matrix[i][j] > target:
            j -= 1

    return False


def main():
    arr = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5

    print (searchMatrix(arr, target))


if __name__ == "__main__":
    main()