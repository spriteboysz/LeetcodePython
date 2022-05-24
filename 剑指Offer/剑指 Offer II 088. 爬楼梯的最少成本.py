#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-24 22:53
LastEditTime: 2022-05-24 22:53
Description:
FilePath: 剑指 Offer II 088. 爬楼梯的最少成本.py
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minCostClimbingStairs(
        cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(ans)
