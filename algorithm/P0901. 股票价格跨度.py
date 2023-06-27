#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-09 22:30:23
LastEditTime: 2022-03-09 22:30:46
Description: 
FilePath: 901.股票价格跨度.py
"""


#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#

# @lc code=start
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        day = 1
        while self.stack and self.stack[-1][0] <= price:
            day += self.stack.pop()[1]
        self.stack.append((price, day))
        return day

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
