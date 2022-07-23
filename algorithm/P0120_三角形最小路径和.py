#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 14:32:15
LastEditTime: 2022-04-10 14:37:08
Description: 
FilePath: 120.三角形最小路径和.py
"""
#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        path = [[0] * n for _ in range(n)]
        path[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                path[i][j] = triangle[i][j]
                if j == 0:
                    path[i][j] += path[i - 1][j]
                elif j == i:
                    path[i][j] += path[i - 1][j - 1]
                else:
                    path[i][j] += min(path[i - 1][j - 1], path[i - 1][j])

        return min(path[-1])


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(ans)
