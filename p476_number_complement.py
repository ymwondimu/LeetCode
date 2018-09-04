def findComplement(num):
    """
    :type num: int
    :rtype: int
    """

    l = len(bin(num)) - 2
    x = 1 << l

    xor_num = x - 1

    return (num ^ xor_num)


def main():
    print (findComplement(5))


if __name__ == "__main__":
    main()
