import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        s = paragraph.split(" ")
        special = "!?',;."

        d = {}
        max_word = ""
        max_count = 0

        for word in s:
            word = word.lower()
            word = re.sub("[^a-zA-Z]+", "", word)
            # print (word)

            if word not in banned:
                if word in d:
                    d[word] += 1
                    if d[word] > max_count:
                        max_count = d[word]
                        max_word = word
                else:
                    d[word] = 1
                    if d[word] > max_count:
                        max_count = d[word]
                        max_word = word

        # print (d)
        return max_word