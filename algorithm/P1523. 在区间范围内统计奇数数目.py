#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-29 22:32:15
LastEditTime: 2022-01-29 22:34:08
Description:
FilePath: 1523.在区间范围内统计奇数数目.py
"""
#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high += high % 2
        return (high - low + 1) // 2
# @lc code=end

