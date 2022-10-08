#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-25 23:28:59
LastEditTime: 2022-04-25 23:31:20
Description: 
FilePath: 746.使用最小花费爬楼梯.py
"""
#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[1] = min(cost[0], cost[1])
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i - 1])
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minCostClimbingStairs([10, 15, 20])
    print(ans)
    ans = solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(ans)
