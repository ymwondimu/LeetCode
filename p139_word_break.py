def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    T = [False] * (len(s) + 1)
    T[0] = True

    for i in range(1, len(s) + 1):
        for word in wordDict:
            if T[i - len(word)] and word == s[i - len(word):i]:
                T[i] = True

    return T[-1]


def main():
    s = "leetcode"
    word_dict = ["leet","code"]

    print (wordBreak(s, word_dict))


if __name__ == "__main__":
    main()