def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    max_profit = 0
    for i in range(1, len(prices)):
        profit = max(prices[i] - prices[i - 1], 0)
        max_profit += profit

    return max_profit


def main():
    print (maxProfit([1,2,3,4,5]))


if __name__ == "__main__":
    main()