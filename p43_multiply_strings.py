def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    res = 0
    x1 = convert_to_int(num1)
    num2 = num2[::-1]

    place = 0

    for char in num2:
        y = ord(char) - ord('0')
        y_val = y * (10 ** place)
        res += x1 * y_val
        place += 1

    return str(res)


def convert_to_int(num):
    res = 0

    for char in num:
        x = ord(char) - ord('0')
        res = res * 10 + x

    return res


def main():
    print (multiply("123", "456"))


if __name__ == "__main__":
    main()