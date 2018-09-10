class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        T = [float('inf')] * (amount + 1)
        T[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                T[i] = min(T[i], T[i - coin] + 1)

        return T[-1] if T[-1] != float('inf') else -1