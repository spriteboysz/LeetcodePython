#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 19:52
FileName: algorithm
Description:P3127. 构造相同颜色的正方形.py 
"""
from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                square = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
                if square.count('W') >= 3 or square.count('B') >= 3:
                    return True
        return False


if __name__ == '__main__':
    print(Solution().canMakeSquare(grid=[["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]))
