#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 21:51:04
LastEditTime: 2022-05-21 21:51:05
Description: 
FilePath: 剑指 Offer 47. 礼物的最大价值.py
"""

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        value = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    value[i][j] = grid[i][j]
                elif i == 0:
                    value[i][j] = grid[i][j] + value[i][j - 1]
                elif j == 0:
                    value[i][j] = grid[i][j] + value[i - 1][j]
                else:
                    value[i][j] = grid[i][j] + max(value[i - 1][j], value[i][j - 1])
        return max(value[-1])


if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(ans)
