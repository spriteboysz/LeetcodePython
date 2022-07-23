#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 23:42:14
LastEditTime: 2022-02-09 23:44:14
Description: 
FilePath: 73.矩阵置零.py
'''
#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 1
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# @lc code=end
