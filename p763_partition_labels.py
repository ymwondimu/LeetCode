from collections import defaultdict


def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """

    last_index = defaultdict(lambda: int)

    for i in range(len(S)):
        last_index[S[i]] = i

    output = []
    start = 0
    all_last = 0
    for i in range(len(S)):
        all_last = max(last_index[S[i]], all_last)
        if all_last == i:
            output.append(i - start + 1)
            start = i + 1
    return output


def main():
    s = "ababcbacadefegdehijhklij"
    print (partitionLabels(s))



if __name__ == "__main__":
    main()
