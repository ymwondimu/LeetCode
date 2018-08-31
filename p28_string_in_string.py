def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if len(needle) == 0:
        return 0

    if len(needle) > len(haystack):
        return -1

    n = len(needle)

    for i in range(len(haystack) - n + 1):
        val = haystack[i:i + n]
        if val == needle:
            return i

    return -1


def main():
    res1 = strStr("hello", "ll")
    print (res1)


if __name__ == "__main__":
    main()