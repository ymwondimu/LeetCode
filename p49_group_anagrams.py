def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    d = {}

    for s in strs:
        s_sorted = ''.join(sorted(s))
        if s_sorted in d:
            d[s_sorted].append(s)
        else:
            d[s_sorted] = [s]

    output = []
    for val in d.values():
        output.append(val)

    return output


def main():
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]

    output = groupAnagrams(input)
    print (output)


if __name__ == "__main__":
    main()
