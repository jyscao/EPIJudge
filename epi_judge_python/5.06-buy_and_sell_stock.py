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


def longest_subarray(ints: List[int]) -> int:
    curr_elem, curr_len, max_len = ints[0], 0, 0
    for i in ints:
        if i == curr_elem:
            curr_len += 1
        else:
            curr_elem, curr_len = i, 1
        max_len = max(max_len, curr_len)
    return max_len
