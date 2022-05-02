#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 19:43:32
LastEditTime: 2022-05-02 19:43:33
Description: 
FilePath: 面试题 01.07. 旋转矩阵.py
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = list(map(list, zip(*matrix[::-1])))

        matrix[:] = matrix[::-1]
        for i in range(len(matrix)):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.rotate(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    )
    print(ans)
    ans = solution.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ans)
