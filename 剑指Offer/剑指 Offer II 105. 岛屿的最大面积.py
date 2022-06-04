#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 21:21
LastEditTime: 2022-06-04 21:21
Description:
FilePath: 剑指 Offer II 105. 岛屿的最大面积.py
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            area = 1
            grid[i][j] = 0
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    area += dfs(x, y)
            return area

        maximum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maximum = max(maximum, dfs(i, j))
        return maximum

if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    print(ans)
