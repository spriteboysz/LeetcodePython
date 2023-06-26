#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 21:54:30
LastEditTime: 2022-02-07 21:56:04
Description:
FilePath: 5984.拆分数位后四位数字的最小和.py
"""
#
# @lc app=leetcode.cn id=5984 lang=python3
#
# [5984] 拆分数位后四位数字的最小和
#

# @lc code=start


class Solution:
    def minimumSum(self, num: int) -> int:
        a, b, c, d = sorted(map(int, str(num)))
        return 10 * (a + b) + c + d
# @lc code=end
