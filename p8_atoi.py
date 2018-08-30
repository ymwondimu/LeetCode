def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    s = discard_whitespace(str)
    if len(s) == 0:
        return 0
    if len(s) == 1 and (s[0] == "-" or s[0] == "+"):
        return 0

    neg = 1
    if s[0] == "-" or s[0] == "+":
        if s[0] == "+":
            s = s[1:]
        else:
            neg = -1
            s = s[1:]

    if not s[0].isdigit():
        return 0

    count = 0
    val = 0
    for char in s:
        if char.isdigit():
            num = ord(char) - ord('0')
            # print (num)
            val = val * 10 + num
            count += 1
        else:
            break

    if val * neg > (2 ** 31) - 1:
        return (2 ** 31) - 1

    if val * neg < (2 ** 31) * -1:
        return (2 ** 31) * -1

    return val * neg


def discard_whitespace(s):
    s = s.strip()
    return s


def main():
    print (myAtoi("-42"))


if __name__ == "__main__":
    main()
