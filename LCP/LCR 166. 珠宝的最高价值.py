#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:31
FileName: LCP
Description:LCR 166. 珠宝的最高价值.py 
"""
from typing import List


class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        m, n = len(frame), len(frame[0])
        if m == 0 or n == 0:
            return 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    frame[i][j] += frame[i][j - 1]
                elif j == 0:
                    frame[i][j] += frame[i - 1][j]
                else:
                    frame[i][j] += max(frame[i - 1][j], frame[i][j - 1])
        return frame[m - 1][n - 1]


if __name__ == '__main__':
    print(Solution().jewelleryValue(frame=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
