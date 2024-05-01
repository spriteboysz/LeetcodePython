#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 20:21
FileName: algorithm
Description:P1605. 给定行和列的和求可行矩阵.py 
"""
from typing import List


class Solution:
    def restoreMatrix(self, row_sum: List[int], col_sum: List[int]) -> List[List[int]]:
        m, n = len(row_sum), len(col_sum)
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = min(row_sum[i], col_sum[j])
                row_sum[i] -= grid[i][j]
                col_sum[j] -= grid[i][j]
        return grid


if __name__ == '__main__':
    print(Solution().restoreMatrix(row_sum=[3, 8], col_sum=[4, 7]))
