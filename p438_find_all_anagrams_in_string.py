from collections import Counter

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    m = len(p)
    n = len(s)

    if m > n:
        return []

    if s == p:
        return [0]

    substring_dict = Counter(p)
    sliding_window_dict = Counter(s[:m - 1])
    output = []

    for i in range(m - 1, n):
        sliding_window_dict[s[i]] += 1
        if sliding_window_dict == substring_dict:
            output.append(i - m + 1)

        sliding_window_dict[s[i - m + 1]] -= 1

        if sliding_window_dict[s[i - m + 1]] == 0:
            del sliding_window_dict[s[i - m + 1]]

    return output


def main():
    s = "cbaebabacd"
    p = "abc"

    print (findAnagrams(s,p))


if __name__ == "__main__":
    main()