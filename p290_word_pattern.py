class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        p_arr = list(pattern)
        str_arr = str.split(" ")
        if len(p_arr) != len(str_arr):
            return False

        print(p_arr)
        print(str_arr)

        char_key = {}
        word_key = {}

        for i in range(len(p_arr)):
            char = p_arr[i]
            word = str_arr[i]

            if char not in char_key:
                char_key[char] = word
            else:
                char_val = char_key[char]
                if char_val != word:
                    return False
            if word not in word_key:
                word_key[word] = char
            else:
                word_val = word_key[word]
                if word_val != char:
                    return False

        return True