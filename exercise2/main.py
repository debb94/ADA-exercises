# Authors: Daniel Bolivar and Jeremy Astaiza
# Solution of problem: "Stock Maximize" HackerRank https://www.hackerrank.com/challenges/stockmax/problem

prices1 = [5, 3, 2]
prices2 = [1, 2, 100]
prices3 = [1, 3, 1, 2]


def stockmax(prices):
    n = len(prices)
    max_future = 0
    profit = 0
    for i in range(n - 1, -1, -1):
        price = prices[i]
        if price > max_future:
            max_future = price
        else:
            profit += max_future - price
    return profit


print(stockmax(prices1))
print(stockmax(prices2))
print(stockmax(prices3))