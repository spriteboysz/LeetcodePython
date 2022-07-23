#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 22:45:46
LastEditTime: 2022-01-28 22:47:59
Description: 
FilePath: 766.托普利茨矩阵.py
'''
#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True
# @lc code=end
