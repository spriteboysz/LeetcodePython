#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-04 23:32
FileName: algorithm
Description:P2923. 找到冠军 I.py 
"""
from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(zip(*grid)):
            if sum(row) == 0:
                return i


if __name__ == '__main__':
    print(Solution().findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]))
