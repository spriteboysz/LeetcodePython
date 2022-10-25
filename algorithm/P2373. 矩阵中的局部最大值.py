#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 23:22
FileName: algorithm/P2373. 矩阵中的局部最大值.py
Description: 
"""
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        largest = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                cur = []
                for di in range(-1, 2):
                    cur.extend(grid[i + di][j - 1:j + 2])
                largest[i - 1][j - 1] = max(cur)
        return largest


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    solution = Solution().largestLocal(grid)
    print(solution)
