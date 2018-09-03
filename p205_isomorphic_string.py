def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_dic = {}
    t_dic = {}

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        if s_char not in s_dic:
            s_dic[s_char] = t_char

        if t_char not in t_dic:
            t_dic[t_char] = s_char

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        if s_dic[s_char] != t_char or t_dic[t_char] != s_char:
            return False

    return True


def main():
    print (isIsomorphic("hello", "patti"))


if __name__ == "__main__":
    main()