def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    L = [[0 for x in range(len(s)+1)] for y in range(len(s)+1)]

    #for i in range(len(s)):
    #    L[i][i+1] = 1

    for i in range(len(s)+1):
        for j in range(len(s)+1):
            char = s[j-1]
            if j-i == 1:
                L[i][j] = 1
            elif j - i >= 2:
                temp = s[i:j-1]
                if char not in temp:
                    L[i][j] = 1 + L[i][j-1]
                else:
                    L[i][j] = 1

    max1 = max(map(max,L))

    return max1


def efficient_length(s):
    current_length = 1
    max_length = 1

    ht = {}
    ht[s[0]] = 0

    for i in range(1, len(s)):

        if s[i] not in ht.keys() or (i - ht[s[i]] > current_length):
            current_length+=1

        else:

            if max_length < current_length:
                max_length = current_length

            current_length = i - ht[s[i]]

        ht[s[i]] = i

    if max_length < current_length:
        max_length = current_length

    return max_length




def main():
    #max = lengthOfLongestSubstring("abca")
    max = efficient_length("abca")
    print (max)

if __name__ == "__main__":
    main()