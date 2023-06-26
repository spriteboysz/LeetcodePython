#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 00:08:43
LastEditTime: 2022-01-27 00:10:19
Description:
FilePath: 1051.高度检查器.py
"""
#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sequence = list(sorted(heights))
        count = 0
        for h, s in zip(heights, sequence):
            if h != s:
                count += 1
        return count
# @lc code=end
