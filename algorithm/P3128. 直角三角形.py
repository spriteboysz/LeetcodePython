#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 16:24
FileName: algorithm
Description:P3128. 直角三角形.py 
"""
from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows, cols = [0] * len(grid), [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += (rows[i] - 1) * (cols[j] - 1)
        return cnt


if __name__ == '__main__':
    print(Solution().numberOfRightTriangles(grid=[[1, 0, 1], [1, 0, 0], [1, 0, 0]]))
