#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:11
FileName: algorithm/P2500. 删除每行中的最大值.py
Description: 
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        ans = 0
        for row in zip(*grid):
            ans += max(row)
        return ans


if __name__ == '__main__':
    print(Solution().deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]]))
