#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/30 23:10
FileName: algorithm/P0714. 买卖股票的最佳时机含手续费.py
Description: 
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
