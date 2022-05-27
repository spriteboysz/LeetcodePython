#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-26 23:46
LastEditTime: 2022-05-26 23:46
Description: 
FilePath: xx.py
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for i in range(n + 2)]
        for i in range(2, n + 1):
            cur_max = 0
            for j in range(1, i):
                cur_max = max(cur_max, max(j * (i - j), j * dp[i - j]))
            dp[i] = cur_max
        return dp[i]
