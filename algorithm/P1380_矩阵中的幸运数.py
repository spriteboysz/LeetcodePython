#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 22:38:15
LastEditTime: 2022-01-26 22:41:47
Description: 
FilePath: 1380.矩阵中的幸运数.py
'''
#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minimum, maximum = [], []
        for row in matrix:
            minimum.append(min(row))
        for column in zip(*matrix):
            maximum.append(max(column))
        return list(set(minimum) & set(maximum))
# @lc code=end
