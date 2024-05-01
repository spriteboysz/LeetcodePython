#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 20:05
FileName: algorithm
Description:P0861. 翻转矩阵后的得分.py 
"""
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] = 1 - grid[i][j]
        for j in range(len(grid[0])):
            column = [grid[i][j] for i in range(len(grid))]
            if column.count(0) > column.count(1):
                for i in range(len(grid)):
                    grid[i][j] = 1 - grid[i][j]
        return sum([int(''.join(map(str, row)), 2) for row in grid])


if __name__ == '__main__':
    print(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
