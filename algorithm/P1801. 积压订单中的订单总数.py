#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 17:03
LastEditTime: 2022-06-12 17:03
Description:
FilePath: 1801.积压订单中的订单总数.py
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []
        for price, amount, type in orders:
            if type == 0:
                match = sell and sell[0][0]
                while amount > 0 and sell and sell[0][0] <= price:
                    match, delta = heappop(sell)
                    amount -= delta
                if amount < 0:
                    heappush(sell, (match, -amount))
                if amount > 0:
                    heappush(buy, (-price, amount))
            else:
                match = buy and -buy[0][0]
                while amount > 0 and buy and -buy[0][0] >= price:
                    match, delta = heappop(buy)
                    amount -= delta
                if amount < 0:
                    heappush(buy, (match, -amount))
                if amount > 0:
                    heappush(sell, (price, amount))

        return (sum(list(map(lambda el: el[1], buy))) +
                sum(list(map(lambda el: el[1], sell)))) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.getNumberOfBacklogOrders(
        orders=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]])
    print(ans)
