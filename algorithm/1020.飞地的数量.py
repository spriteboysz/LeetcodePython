#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-24 21:51:30
LastEditTime: 2022-04-24 21:54:46
Description: 
FilePath: 1020.飞地的数量.py
"""
#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                grid[x][y] = 0
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        n, m = len(grid), len(grid[0])
        for i in [0, n - 1]:
            for j in range(0, m):
                dfs(i, j)
        for i in range(0, n):
            for j in [0, m - 1]:
                dfs(i, j)

        return sum([sum(row) for row in grid])


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numEnclaves(
        grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    )
    print(ans)
    ans = solution.numEnclaves(
        grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    )
    print(ans)
    ans = solution.numEnclaves(
        [
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        ]
    )
    print(ans)
