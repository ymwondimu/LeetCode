def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    output = ""

    mapping = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
               (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    while num > 0:
        for entry in mapping:
            x = entry[0]
            letter = entry[1]

            if num - x >= 0:
                output += letter
                num = num - x
                break

    return output


def main():
    print (intToRoman(1994))


if __name__ == "__main__":
    main()
