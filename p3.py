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

def main():
    max = lengthOfLongestSubstring("abca")
    print (max)

if __name__ == "__main__":
    main()