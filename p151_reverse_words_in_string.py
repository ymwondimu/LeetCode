def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    s = s.strip()
    word_arr = s.split()

    word_arr = word_arr[::-1]
    return " ".join(word_arr)


def main():
    print (reverseWords("The sky is blue"))


if __name__ == "__main__":
    main()