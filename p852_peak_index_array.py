def peakIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """

    max_val = -float('inf')
    max_index = 0

    for i in range(len(A)):
        val = A[i]
        if val > max_val:
            max_val = val
            max_index = i

    return max_index


def main():
    arr = [0, 2, 1, 0]
    print (peakIndexInMountainArray(arr))


if __name__ == "__main__":
    main()