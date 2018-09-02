class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        output = A

        max_bound = (len(B) / len(A)) + 1

        count = 1
        while B not in output:
            if count > max_bound:
                return -1
            output += A
            count += 1

        return count