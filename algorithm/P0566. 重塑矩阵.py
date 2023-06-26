#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-13 23:10:38
LastEditTime: 2022-01-13 23:21:15
Description:
FilePath: 566.重塑矩阵.py
"""
#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat[0]), len(mat)
        if m * n == r * c:
            matrix1, matrix2 = [], [[0] * c for _ in range(r)]
            for i in range(n):
                matrix1.extend(mat[i])
            k = 0
            for i in range(r):
                for j in range(c):
                    matrix2[i][j] = matrix1[k]
                    k += 1
            return matrix2
        else:
            return mat
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape([[1, 2, 3], [3, 4, 5]], 3, 2))
