#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 19:27:25
LastEditTime: 2022-03-14 19:31:08
Description: 
FilePath: 931.下降路径最小和.py
"""
#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        falling = [[0] * m for _ in range(n)]
        falling[0] = matrix[0]
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    falling[i][j] = matrix[i][j] + min(
                        falling[i - 1][j], falling[i - 1][j + 1]
                    )
                elif j == m - 1:
                    falling[i][j] = matrix[i][j] + min(
                        falling[i - 1][j - 1], falling[i - 1][j]
                    )
                else:
                    falling[i][j] = matrix[i][j] + min(
                        falling[i - 1][j - 1], falling[i - 1][j], falling[i - 1][j + 1]
                    )

        return min(falling[-1])


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]])
    print(ans)
    ans = solution.minFallingPathSum(matrix = [[-19,57],[-40,-5]])
    print(ans)
