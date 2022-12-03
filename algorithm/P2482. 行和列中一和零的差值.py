#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022/12/3 21:58
FileName: algorithm/P2482. 行和列中一和零的差值.py
Description: 
"""
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onerow, onecol = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                onerow[i] += (grid[i][j] == 1)
                onecol[j] += (grid[i][j] == 1)
        for i in range(m):
            for j in range(n):
                # grid[i][j] = onerow[i] + onecol[j] - (n-onerow[i]) - (m - onecol[j])
                grid[i][j] = 2 * onerow[i] + 2 * onecol[j] - m - n
        return grid


if __name__ == '__main__':
    print(Solution().onesMinusZeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
