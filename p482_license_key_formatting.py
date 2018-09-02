import re


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        s = re.sub('[-]', '', S)
        if s == "":
            return ""
        print(s)
        output = ""

        remainder = len(s) % K
        if remainder != 0:
            output = s[:remainder].upper()
            s = s[remainder:]
            output += "-"

        count = 0
        for i in range(len(s)):
            output += s[i].upper()
            count += 1
            if count == K:
                output += "-"
                count = 0

        print(output)
        if output[-1] == "-":
            output = output[:-1]
        return output
