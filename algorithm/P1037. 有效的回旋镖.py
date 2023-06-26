#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-29 23:21:32
LastEditTime: 2022-01-29 23:34:07
Description:
FilePath: 1037.有效的回旋镖.py
"""
#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
from typing import List


class Solution:
    def calcDistance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def isBoomerang(self, points: List[List[int]]) -> bool:
        ab = self.calcDistance(points[0], points[1])
        ac = self.calcDistance(points[0], points[2])
        bc = self.calcDistance(points[1], points[2])
        ab, ac, bc = sorted([ab, ac, bc])
        print(ab, ac, bc)
        print(ab + ac)
        return True if ab + ac - bc > 0.00001 else False

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isBoomerang([[1, 1], [2, 3], [3, 2]]))
    print(s.isBoomerang([[1, 1], [2, 2], [7, 7]]))
