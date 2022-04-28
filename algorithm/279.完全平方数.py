#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-28 22:55:56
LastEditTime: 2022-04-28 22:57:04
Description: 
FilePath: 279.完全平方数.py
"""
#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [inf] * n
        for i in range(1, int(n ** 0.5) + 1):
            cur = i * i
            for j in range(cur, n + 1):
                dp[j] = min(dp[j], dp[j - cur] + 1)
        return dp[n]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSquares(12)
    print(ans)
