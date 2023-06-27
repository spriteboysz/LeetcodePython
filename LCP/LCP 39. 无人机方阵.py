#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 23:40:56
LastEditTime: 2022-02-07 23:46:13
Description:
FilePath: 1000369.无人机方阵.py
"""
#
# @lc app=leetcode.cn id=1000369 lang=python3
#
# [LCP 39] 无人机方阵
#

# @lc code=start
from typing import List


class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        color = dict()
        for i in range(len(source)):
            for j in range(len(source[0])):
                if source[i][j] in color:
                    color[source[i][j]] += 1
                else:
                    color[source[i][j]] = 1
                if target[i][j] in color:
                    color[target[i][j]] -= 1
                else:
                    color[target[i][j]] = -1
        return sum(map(abs, color.values())) // 2
# @lc code=end
