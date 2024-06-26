#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-26 22:34
FileName: algorithm
Description:P3195. 包含所有 1 的最小矩形面积 I.py 
"""
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x1, x2, y1, y2 = len(grid), -1, len(grid[0]), -1
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    x1 = min(x1, i)
                    x2 = max(x2, i)
                    y1 = min(y1, j)
                    y2 = max(y2, j)
        return (x2 - x1 + 1) * (y2 - y1 + 1)


if __name__ == '__main__':
    print(Solution().minimumArea(grid=[[0, 1, 0], [1, 0, 1]]))
