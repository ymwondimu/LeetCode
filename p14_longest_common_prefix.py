class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        #Edge case: if the array of strings is empty
        if len(strs) == 0:
            return ""

        #Edge case if only one string, return the whole thing
        if len(strs) == 1:
            return strs[0]

        #Edge case if the first string is an empty string
        if strs[0] == "":
            return ""

        current_count = 0
        longest_count = 0
        longest_prefix = ""

        word1 = strs[0]
        word2 = strs[1]

        #Edge case: check if either of the first two words is an empty string, if so, return an empty string
        if word1 == "" or word2 == "":
            return ""

        #Check if first character of the first two words is unequal, if so, return empty string
        if word1[0] != word2[0]:
            return ""

        n1 = len(word1)
        n2 = len(word2)

        #Get longest common prefix between first two strings for comparison amongst the rest
        is_one_greater = n1 > n2
        if is_one_greater:
            for i in range(n2):
                # print (i)
                if word1[i] == word2[i]:
                    longest_count += 1
                    longest_prefix += word1[i]
        else:
            for i in range(n1):
                if word1[i] == word2[i]:
                    longest_count += 1
                    longest_prefix += word1[i]

        #compare rest of the strings with the current longest prefix and update it with the new longest_prefix value as we go
        for i in range(2, len(strs)):
            print(longest_prefix)
            print(longest_count)
            if longest_count == 0:
                return ""
            word = strs[i]
            if word == "":
                return ""

            n = len(longest_prefix) if len(longest_prefix) < len(word) else len(word)

            for j in range(n):
                if word[j] == longest_prefix[j]:
                    current_count += 1
            longest_count = current_count
            longest_prefix = longest_prefix[:longest_count]
            current_count = 0
        return longest_prefix