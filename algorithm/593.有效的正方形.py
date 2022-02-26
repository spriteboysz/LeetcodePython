#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 21:43:48
LastEditTime: 2022-02-26 21:49:14
Description: 
FilePath: 593.有效的正方形.py
"""
#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#

# @lc code=start
from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def distance2(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        points = [p1, p2, p3, p4]
        dis2 = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dis2.append(distance2(points[i], points[j]))
        a, b, c, d, ac, bd = sorted(dis2)
        return a == b == c == d and ac == bd and a + c == ac


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.validSquare([0, 0], [1, 1], [1, 0], [0, 1])
    print(ans)
    ans = solution.validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 12])
    print(ans)
    ans = solution.validSquare(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1])
    print(ans)
