def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    if len(s) == 0 or len(s) == 1:
        return s

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    s_arr = list(s)

    s = 0
    e = len(s_arr) - 1

    while s < e:
        l1 = s_arr[s]
        l2 = s_arr[e]

        if l1 in vowels and l2 in vowels:
            s_arr[s], s_arr[e] = s_arr[e], s_arr[s]
            s += 1
            e -= 1
        else:
            if l1 not in vowels:
                s += 1
            if l2 not in vowels:
                e -= 1

    return ''.join(s_arr)


def main():
    s = "leetcode"
    print (reverseVowels(s))


if __name__ == "__main__":
    main()