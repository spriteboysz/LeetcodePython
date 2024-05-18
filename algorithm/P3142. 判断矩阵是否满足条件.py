#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-15 21:41
FileName: algorithm
Description:P3142. 判断矩阵是否满足条件.py 
"""
from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().satisfiesConditions(grid=[[1, 0, 2], [1, 0, 2]]))
