class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        output = 0

        conversions = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                       (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        while len(s) > 0:
            for conv in conversions:
                roman = conv[1]
                integer = conv[0]
                n = len(roman)
                if s.startswith(roman):
                    output += integer
                    s = s[n:]

        return output