#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/2/2 22:48
FileName: 剑指Offer/剑指 Offer 63. 股票的最大利润.py
Description: 
"""
from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, maximum = inf, 0
        for price in prices:
            maximum = max(price - minimum, maximum)
            minimum = min(price, minimum)
        return maximum


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
