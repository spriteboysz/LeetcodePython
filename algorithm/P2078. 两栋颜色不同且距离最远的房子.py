#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 23:12:21
LastEditTime: 2022-01-21 23:14:56
Description:
FilePath: 2078.两栋颜色不同且距离最远的房子.py
"""
#
# @lc app=leetcode.cn id=2078 lang=python3
#
# [2078] 两栋颜色不同且距离最远的房子
#

# @lc code=start
from typing import List 
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 0
        for i in range(len(colors) - 1):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    if abs(i - j) > distance:
                        distance = abs(i - j)
        return distance
    
# @lc code=end

