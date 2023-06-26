#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-06 23:32:58
LastEditTime: 2022-02-06 23:34:59
Description:
FilePath: 1886.判断矩阵经轮转后是否一致.py
"""
#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#

# @lc code=start
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        target = [tuple(row) for row in target]
        for _ in range(3):
            mat = list(zip(*mat))[::-1]
            if mat == target:
                return True
        else:
            return False

# @lc code=end
