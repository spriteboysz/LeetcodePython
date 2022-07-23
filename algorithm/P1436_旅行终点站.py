#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 23:21:14
LastEditTime: 2022-01-25 23:24:32
Description: 
FilePath: 1436.旅行终点站.py
'''
#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = []
        for path in paths:
            src.append(path[0])
        for path in paths:
            if path[1] not in src:
                return path[1]
# @lc code=end
