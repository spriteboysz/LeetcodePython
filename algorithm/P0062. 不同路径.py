#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-18 23:34:31
LastEditTime: 2022-02-18 23:43:09
Description: 
FilePath: 62.不同路径.py
"""


#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0] = [1] * n
        for i in range(m):
            grid[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.uniquePaths(3, 7)
    print(ans)
    ans = solution.uniquePaths(3, 2)
    print(ans)
    ans = solution.uniquePaths(3, 3)
    print(ans)
