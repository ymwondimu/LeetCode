from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1

        d = defaultdict(int)
        for char in s:
            d[char] += 1

        for i, char in enumerate(s):
            if d[char] == 1:
                return i

        return -1