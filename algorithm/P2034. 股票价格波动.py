#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-20 20:44:17
LastEditTime: 2022-02-20 20:47:02
Description: 
FilePath: 2034.股票价格波动.py
"""
#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] 股票价格波动
#

# @lc code=start
from sortedcontainers import SortedList,SortedDict
from sortedcontainers import SortedList


class StockPrice:
    def __init__(self):
        self.price = dict()
        self.cur = 0

    def update(self, timestamp: int, price: int) -> None:
        self.price[timestamp] = price
        self.cur = max(self.cur, timestamp)

    def current(self) -> int:
        return self.price[self.cur]

    def maximum(self) -> int:
        return max(self.price.values())

    def minimum(self) -> int:
        return min(self.price.values())


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end
