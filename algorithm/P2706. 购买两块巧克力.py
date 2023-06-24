#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:42
FileName: algorithm/P2706. 购买两块巧克力.py
Description: 
"""
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        return money if money < prices[0] + prices[1] else money - prices[0] - prices[1]


if __name__ == '__main__':
    print(Solution().buyChoco(prices=[2, 2, 1], money=3))
