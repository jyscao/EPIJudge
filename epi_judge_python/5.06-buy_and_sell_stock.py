from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    curr_min, max_profit = float("inf"), 0
    for p in prices:
        if p < curr_min:
            curr_min = p
        max_profit = max(max_profit, p - curr_min)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
