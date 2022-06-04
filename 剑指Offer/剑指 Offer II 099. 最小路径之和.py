#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 22:11
LastEditTime: 2022-06-04 22:11
Description:
FilePath: 剑指 Offer II 099. 最小路径之和.py
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(ans)
