#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-19 17:24
FileName: algorithm
Description:P1901. 寻找峰值 II.py 
"""
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0]) if n != 0 else 0
        for i in range(n):
            for j in range(m):
                flag1 = flag2 = flag3 = flag4 = True
                if i != 0:
                    flag1 = (mat[i - 1][j] < mat[i][j])
                if j != 0:
                    flag2 = (mat[i][j - 1] < mat[i][j])
                if i != n - 1:
                    flag3 = (mat[i + 1][j] < mat[i][j])
                if j != m - 1:
                    flag4 = (mat[i][j + 1] < mat[i][j])
                if flag1 and flag2 and flag3 and flag4:
                    return [i, j]
        return []


if __name__ == '__main__':
    print(Solution().findPeakGrid(mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
