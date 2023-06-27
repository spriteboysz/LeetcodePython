#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-15 22:42:58
LastEditTime: 2022-02-15 22:43:34
Description:
FilePath: 1689.十-二进制数的最少数目.py
"""


#
# @lc app=leetcode.cn id=1689 lang=python3
#
# [1689] 十-二进制数的最少数目
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, n))
# @lc code=end
