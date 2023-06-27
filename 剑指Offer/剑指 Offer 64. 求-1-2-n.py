#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-05 22:14:38
LastEditTime: 2022-02-05 22:17:06
Description:
FilePath: 100345.求-1-2-n.py
"""
#
# @lc app=leetcode.cn id=100345 lang=python3
#
# [剑指 Offer 64] 求1+2+…+n
#

# @lc code=start


class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(1, n + 1))
# @lc code=end
