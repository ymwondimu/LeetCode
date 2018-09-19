def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    output = []
    for i in range(numRows):
        output.append([1] * (i + 1))
        if i > 1:
            for j in range(1, i):
                output[i][j] = output[i - 1][j - 1] + output[i - 1][j]

    return output


def main():
    print (generate(5))


if __name__ == "__main__":
    main()
