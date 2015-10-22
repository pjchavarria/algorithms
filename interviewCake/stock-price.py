# https://www.interviewcake.com/question/stock-price
# Greedy

def get_max_profit(stock_prices_yesterday):

    if len (stock_prices_yesterday) < 2:
        raise IndexError("Getting a profit requires at least 2 items")

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - min_price

    for index, current_price in enumerate(stock_prices_yesterday):
        if index == 0:
            continue
        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price
        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit


print get_max_profit([200, 100, 500, 90, 100]), 400
print get_max_profit([200, 100, 90, 80, 1]), -10
print get_max_profit([1,1,1,1]), 0