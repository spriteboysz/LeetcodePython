#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:52
FileName: algorithm/P2639. 查询网格图中每一列的宽度.py
Description: 
"""
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        width = []
        for col in zip(*grid):
            width.append(max(map(lambda el: len(str(el)), col)))
        return width


if __name__ == '__main__':
    print(Solution().findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))
