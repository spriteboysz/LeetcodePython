#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-08 15:12:23
LastEditTime: 2022-01-08 15:37:07
Description:
FilePath: 463.岛屿的周长.py
"""
#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        matrix = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            matrix[i][1:m + 1] = grid[i - 1]

        count = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i][j]:
                    count += 4 - (matrix[i - 1][j] + matrix[i + 1]
                                  [j] + matrix[i][j - 1] + matrix[i][j + 1])
        return count
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter(
        [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
    print(s.islandPerimeter([[1]]))
    print(s.islandPerimeter([[1, 0]]))
    print(s.islandPerimeter([[0, 1]]))
