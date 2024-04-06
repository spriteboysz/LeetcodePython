#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 17:29
FileName: algorithm
Description:P3033. 修改矩阵.py 
"""
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        columns = []
        for j in range(len(matrix[0])):
            maximum = matrix[0][j]
            for i in range(len(matrix)):
                maximum = max(maximum, matrix[i][j])
            columns.append(maximum)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = columns[j]
        return matrix


if __name__ == '__main__':
    print(Solution().modifiedMatrix(matrix=[[1, 2, -1], [4, -1, 6], [7, 8, 9]]))
