#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-01 22:34:25
LastEditTime: 2022-04-01 22:41:27
Description: 
FilePath: 64.最小路径和.py
"""
#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        path = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    path[i][j] = grid[i][j]
                elif i == 0:
                    path[i][j] = path[i][j - 1] + grid[i][j]
                elif j == 0:
                    path[i][j] = path[i - 1][j] + grid[i][j]
                else:
                    path[i][j] = min(path[i - 1][j], path[i][j - 1]) + grid[i][j]

        return path[-1][-1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(ans)
    ans = solution.minPathSum([[1, 2, 3], [4, 5, 6]])
    print(ans)
