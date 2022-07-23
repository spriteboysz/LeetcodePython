#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-24 23:07:18
LastEditTime: 2022-04-24 23:12:37
Description: 
FilePath: 1905.统计子岛屿.py
"""
#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, x, y):
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                grid[x][y] = 0
                dfs(grid, x + 1, y)
                dfs(grid, x - 1, y)
                dfs(grid, x, y + 1)
                dfs(grid, x, y - 1)

        n, m = len(grid1), len(grid1[0])
        for i in range(n):
            for j in range(m):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    count += 1
                    dfs(grid2, i, j)
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countSubIslands(
        grid1=[
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
        ],
        grid2=[
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ],
    )
    print(ans)
