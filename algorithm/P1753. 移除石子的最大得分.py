#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-18 23:32:48
LastEditTime: 2022-04-18 23:33:13
Description: 
FilePath: 1753.移除石子的最大得分.py
"""


#
# @lc app=leetcode.cn id=1753 lang=python3
#
# [1753] 移除石子的最大得分
#

# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b <= c:
            return a + b
        else:
            return (a + b + c) // 2

# @lc code=end
