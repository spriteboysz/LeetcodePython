#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 16:11
FileName: algorithm
Description:P1072. 按列翻转得到最大值等行数.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 1:
                for j in range(n):
                    matrix[i][j] = 1 - matrix[i][j]
        count = defaultdict(int)
        for row in matrix:
            count[''.join(map(str, row))] += 1
        return max(count.values())


if __name__ == '__main__':
    print(Solution().maxEqualRowsAfterFlips(matrix=[[0, 0, 0], [0, 0, 1], [1, 1, 0]]))
