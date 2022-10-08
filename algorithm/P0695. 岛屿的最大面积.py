#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-24 21:32:10
LastEditTime: 2022-04-24 21:37:46
Description: 
FilePath: 695.岛屿的最大面积.py
"""
#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            if 0 <= x < n and 0 <= y < m and grid[x][y]:
                grid[x][y] = 0
                nonlocal area
                area += 1
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
                return area

        maximum = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = 0
                    maximum = max(maximum, dfs(i, j))
        return maximum


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    print(ans)
