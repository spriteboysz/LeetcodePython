#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-24 23:13:39
LastEditTime: 2022-02-24 23:18:07
Description: 
FilePath: 2141.同时运行-n-台电脑的最长时间.py
"""
#
# @lc app=leetcode.cn id=2141 lang=python3
#
# [2141] 同时运行 N 台电脑的最长时间
#

# @lc code=start
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = sorted(batteries, reverse=True)
        total = sum(batteries)
        for battery in batteries:
            if battery > total // n:
                n -= 1
                total -= battery
            else:
                return total // n


# @lc code=end
