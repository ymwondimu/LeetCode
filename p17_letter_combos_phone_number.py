def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    d = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    if len(digits) == 0:
        return []

    if len(digits) == 1:
        return list(d[digits])

    first_char = digits[0]
    rest = digits[1:]

    rest_values = letterCombinations(rest)
    head_values = d[first_char]

    return [s + f for f in rest_values for s in head_values]


def main():
    output = letterCombinations("35")
    print (output)


if __name__ == "__main__":
    main()
