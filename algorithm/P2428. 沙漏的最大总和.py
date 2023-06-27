#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-24 00:03
FileName: algorithm/P2428. 沙漏的最大总和.py
Description: 
"""
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        offsets = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
        maximum = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                cur = 0
                for di, dj in offsets:
                    cur += grid[i + di][j + dj]
                maximum = max(maximum, cur)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]])
    print(solution)
