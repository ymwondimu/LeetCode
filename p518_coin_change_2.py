class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        T = [0] * (amount + 1)
        T[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                T[i] += T[i - coin]

        return T[-1]