def maxProfit(prices):
    profit = 0

    if not prices:
        return profit

    n = len(prices)

    for i in range(0, n - 1):
        profit = profit + max(0, prices[i + 1] - prices[i])

    return profit


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(maxProfit(a))