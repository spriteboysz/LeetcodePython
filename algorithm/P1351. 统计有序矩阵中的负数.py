#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 22:59:13
LastEditTime: 2022-01-26 23:00:48
Description:
FilePath: 1351.统计有序矩阵中的负数.py
"""
#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += len(list(filter(lambda el: el < 0, row)))
        return count
# @lc code=end
