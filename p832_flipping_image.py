def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    if len(A) == 0:
        return A

    for i in range(len(A)):
        A[i] = A[i][::-1]
        row = A[i]
        for j in range(len(row)):
            A[i][j] = A[i][j] ^ 1

    return A


def main():
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print (flipAndInvertImage(A))

if __name__ == "__main__":
    main()