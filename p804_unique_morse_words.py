def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """

    mapping = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    d = {}
    total = 0

    for word in words:
        output = ""
        for char in word:
            num = ord(char) - ord('a')
            output += mapping[num]

        print(output)
        if output not in d:
            total += 1
            d[output] = 1

    return total


def main():
    words = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations(words))


if __name__ == "__main__":
    main()