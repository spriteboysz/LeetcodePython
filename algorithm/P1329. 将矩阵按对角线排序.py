#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-22 21:36:36
LastEditTime: 2022-04-22 21:51:17
Description: 
FilePath: 1329.将矩阵按对角线排序.py
"""
#
# @lc app=leetcode.cn id=1329 lang=python3
#
# [1329] 将矩阵按对角线排序
#

# @lc code=start

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        init = [(i, 0) for i in range(row)] + [(0, j) for j in range(1, col)]
        for point in init:
            i, j = point
            cur = [
                mat[i + n][j + n]
                for n in range(0, min(row, col))
                if i + n < row and j + n < col
            ]
            cur.sort()

            for k in range(len(cur)):
                mat[i + k][j + k] = cur[k]

        return mat


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
    print(ans)
