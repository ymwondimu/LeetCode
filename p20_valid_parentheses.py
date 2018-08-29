class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        d = {')': '(', ']': '[', '}': '{'}

        stack = []

        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    output = stack.pop()
                if output != d[char]:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False