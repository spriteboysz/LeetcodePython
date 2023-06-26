#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 22:37:45
LastEditTime: 2022-04-10 22:47:33
Description:
FilePath: 84.柱状图中最大的矩形.py
"""
#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left, right, area = 0, len(heights) - 1, 0
        pass

# @lc code=end
