#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-06 22:25:26
LastEditTime: 2022-02-06 22:31:39
Description: 
FilePath: 1260.二维网格迁移.py
'''
#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        for _ in range(k):
            cur = [[0] * m for _ in range(n)]
            for row in range(n):
                for col in range(m - 1):
                    cur[row][col + 1] = grid[row][col]
            for row in range(n - 1):
                cur[row + 1][0] = grid[row][m - 1]

            cur[0][0] = grid[n - 1][m - 1]
            grid = cur
        return grid

# @lc code=end
