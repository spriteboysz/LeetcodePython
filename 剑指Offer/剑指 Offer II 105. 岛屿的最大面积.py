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

        def dfs(x: int, y: int) -> int:
            area = 1
            grid[x][y] = 0
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy]:
                    area += dfs(dx, dy)
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
