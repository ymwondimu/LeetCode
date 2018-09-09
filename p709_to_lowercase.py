def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """

    output = ""

    for char in str:
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            diff = ord(char) - ord('A')
            num = ord('a') + diff
            new_char = chr(num)
            output += new_char
        else:
            output += char

    return output


def main():
    output = toLowerCase("Hello")
    print (output)


if __name__ == "__main__":
    main()