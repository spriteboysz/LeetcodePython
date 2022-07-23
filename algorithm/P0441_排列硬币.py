#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-27 23:26:11
Description: 排列硬币
FilePath: 441.排列硬币.py
'''
#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(n + 1):
            s = int((1 + i) * i * 0.5)
            if s == n:
                return i
            elif s > n:
                return i - 1
            
# @lc code=end

