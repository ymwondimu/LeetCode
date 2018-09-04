def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """

    res = x ^ y
    count = 0
    while res != 0:
        res = res & (res - 1)
        count += 1

    return count


def main():
    print (hammingDistance(1,4))


if __name__ == "__main__":
    main()