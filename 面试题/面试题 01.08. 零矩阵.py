#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 19:58:43
LastEditTime: 2022-05-02 19:58:43
Description: 
FilePath: 面试题 01.08. 零矩阵.py
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for y in range(m):
                        if matrix[i][y] != 0:
                            matrix[i][y] = "a"
                    for x in range(n):
                        if matrix[x][j] != 0:
                            matrix[x][j] = "a"

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0

        print(matrix)


if __name__ == "__main__":
    solution = Solution()
    solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
