#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-14 22:49:10
LastEditTime: 2022-02-14 22:58:51
Description:
FilePath: 200.岛屿数量.py
"""
#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = "0"
            for position in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx, ny = x + position[0], y + position[1]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                    dfs(nx, ny)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]]
    for i, args in enumerate(arguments):
        print("=== *{:02d} INPUT* ===".format(i + 1))
        print(args)
        print("=== *DEBUG* ===")
        answer = solution.numIslands(args)
        print("=== *{:02d} OUTPUT* ===".format(i + 1))
        print(answer)
