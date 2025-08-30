def maxProfit(prices: list[int]) -> int:
    toBuy = 0
    toSell = 1
    diffMax = 0
    while toSell < len(prices):
        if prices[toSell] <= prices[toBuy]:
            toBuy = toSell
        else:
            diffMax = max(diffMax, prices[toSell] - prices[toBuy])
        toSell += 1
    return diffMax


def maxProfit_back(prices: list[int]) -> int:
    valueMax = prices[-1]
    diffMax = 0
    for i in reversed(range(len(prices))):
        if prices[i] < valueMax:
            diffMax = max(diffMax, valueMax - prices[i])
        else:
            valueMax = prices[i]
    return diffMax


def get_max_profit_bruteforce(prices: list[int]) -> int:
    profit_max = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current_profit = prices[j] - prices[i]
            profit_max = max(profit_max, current_profit)
    return profit_max


def get_max_profit_structures(prices: list[int]) -> int:
    res = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        else:
            res = max(res, price - lowest)
    return res


def get_max_profit_backward(prices: list[int]) -> int:
    res = 0
    max_price = prices[-1]
    for i in reversed(range(len(prices))):
        cur_price = prices[i]
        if cur_price < max_price:
            res = max(res, max_price - cur_price)
        else:
            max_price = cur_price
    return res


if __name__ == "__main__":
    stocks = [7, 1, 5, 3, 6, 4]
    print(get_max_profit_backward(stocks))
