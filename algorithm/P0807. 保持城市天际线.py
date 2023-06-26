#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-15 22:44:14
LastEditTime: 2022-02-15 22:50:09
Description:
FilePath: 807.保持城市天际线.py
"""
#
# @lc app=leetcode.cn id=807 lang=python3
#
# [807] 保持城市天际线
#

# @lc code=start
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxrow = [max(row) for row in grid]
        maxcol = [max(col) for col in zip(*grid)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += min(maxrow[i], maxcol[j]) - grid[i][j]
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
    print(s.maxIncreaseKeepingSkyline([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
