#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-14 23:37:56
LastEditTime: 2022-02-14 23:46:18
Description:
FilePath: 121.买卖股票的最佳时机.py
"""
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

from math import inf
# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = inf
        dp = [0] * len(prices)
        for i, price in enumerate(prices):
            minprice = min(minprice, price)
            dp[i] = max(dp[i], price - minprice)
        return max(dp)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
    for i, args in enumerate(arguments):
        print("=== *{:02d} INPUT* ===".format(i + 1))
        print(args)
        print("=== *DEBUG* ===")
        answer = solution.maxProfit(args)
        print("=== *{:02d} OUTPUT* ===".format(i + 1))
        print(answer)
