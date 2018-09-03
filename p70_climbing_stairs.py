class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return fib(n + 1)


def fib(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = a + b, a

    return a