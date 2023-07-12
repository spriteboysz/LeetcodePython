#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-11 23:05
FileName: algorithm/P2133. 检查是否每一行每一列都包含全部整数.py
Description: 
"""
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = [i for i in range(1, n + 1)]
        for row in matrix:
            if sorted(row) != target:
                return False
        for row in zip(*matrix):
            if sorted(list(row)) != target:
                return False
        return True


if __name__ == '__main__':
    print(Solution().checkValid(matrix=[[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
