#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-02 20:44
FileName: algorithm
Description:P0059. 螺旋矩阵 II.py 
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num, target = 1, n * n
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                grid[top][j] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                grid[i][right] = num
                num += 1
            right -= 1
            for j in range(right, left - 1, -1):
                grid[bottom][j] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                grid[i][left] = num
                num += 1
            left += 1

        return grid


if __name__ == '__main__':
    print(Solution().generateMatrix(4))
