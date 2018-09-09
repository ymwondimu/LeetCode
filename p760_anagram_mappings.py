def anagramMappings(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """

    d = {}

    for i in range(len(A)):
        num = A[i]
        if num not in d:
            d[num] = [i]

    for i in range(len(B)):
        num = B[i]
        if len(d[num]) == 1:
            d[num].append(i)

    output = [-1] * len(A)

    for i in range(len(B)):
        num = A[i]
        indices = d[num]
        output[i] = indices[1]

    return output


def main():
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    output = anagramMappings(A,B)

    print (output)


if __name__ == "__main__":
    main()
