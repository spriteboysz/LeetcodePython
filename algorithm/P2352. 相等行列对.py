#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-09 22:58
FileName: algorithm/P2352. 相等行列对.py
Description: 
"""
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows, cols = ["" for _ in range(n)], ["" for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rows[i] += str(grid[i][j]) + "#"
                cols[j] += str(grid[i][j]) + "#"
        cnt = 0
        for row in rows:
            for col in cols:
                if row == col:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
