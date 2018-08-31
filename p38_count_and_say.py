def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """

    if n == 1:
        return "1"

    if n == 2:
        return "11"

    curr = "11"
    for i in range(3, n + 1):
        output = ""
        count = 1
        for i in range(1, len(curr)):
            prev = curr[i - 1]
            char = curr[i]

            if prev == char:
                count += 1
            else:
                output += str(count)
                output += prev
                count = 1

        output += str(count)
        output += char
        curr = output

    return curr


def main():
    print (countAndSay(5))


if __name__ == "__main__":
    main()