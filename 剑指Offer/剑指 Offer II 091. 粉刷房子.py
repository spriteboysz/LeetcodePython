#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 21:49
LastEditTime: 2022-06-05 21:49
Description:
FilePath: 剑指 Offer II 091. 粉刷房子.py
"""

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n, m = len(costs), len(costs[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            dp[0][j] = costs[0][j]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        return min(dp[n - 1][j] for j in range(m))

if __name__ == '__main__':
    solution = Solution()
    ans = solution.minCost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]])
    print(ans)
