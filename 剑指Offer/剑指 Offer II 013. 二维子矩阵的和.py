#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 23:51
LastEditTime: 2022-06-05 23:51
Description:
FilePath: 剑指 Offer II 013. 二维子矩阵的和.py
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.presum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for x in range(n):
            for y in range(m):
                self.presum[x + 1][y + 1] = self.presum[x + 1][y] + self.presum[x][y + 1] - self.presum[x][y] + \
                                            matrix[x][y]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2 + 1][col2 + 1] - self.presum[row2 + 1][col1] - self.presum[row1][col2 + 1] + \
            self.presum[row1][col1]
