class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        i_arr = []
        j_arr = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in i_arr:
                        i_arr.append(i)
                    if j not in j_arr:
                        j_arr.append(j)

        for i in i_arr:
            set_row(i, matrix)

        for j in j_arr:
            set_column(j, matrix)


def set_row(i, arr):
    arr[i][:] = [0] * len(arr[0])


def set_column(j, arr):
    for i in range(len(arr)):
        arr[i][j] = 0