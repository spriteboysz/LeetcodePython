#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:43
FileName: LCP
Description:LCR 188. 买卖芯片的最佳时机.py 
"""
from math import inf
from typing import List


class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        minimum, maximum = inf, 0
        for price in prices:
            maximum = max(price - minimum, maximum)
            minimum = min(price, minimum)
        return maximum


if __name__ == '__main__':
    print(Solution().bestTiming(prices=[3, 6, 2, 9, 8, 5]))
