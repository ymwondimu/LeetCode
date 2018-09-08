def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    min_price, max_profit = float('inf'), 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


def main():
    print (maxProfit([7,1,5,3,6,4]))


if __name__ == "__main__":
    main()
