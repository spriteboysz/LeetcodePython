#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-02 23:35:05
LastEditTime: 2022-02-02 23:42:28
Description: 
FilePath: 812.最大三角形面积.py
'''
#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        #s = abs((x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1))/2
        maximum = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    cur = abs((x1 * y2 + x2 * y3 + x3 * y1 -
                              y1 * x2 - y2 * x3 - y3 * x1)) / 2
                    if cur > maximum:
                        maximum = cur
        return maximum
# @lc code=end
