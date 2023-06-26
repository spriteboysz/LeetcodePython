#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 22:49:15
LastEditTime: 2022-03-15 23:09:13
Description:
FilePath: 939.最小面积矩形.py
"""
#
# @lc app=leetcode.cn id=939 lang=python3
#
# [939] 最小面积矩形
#

from math import inf
# @lc code=start
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        st = set([tuple(point) for point in points])
        area = float(inf)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (x1, y1), (x2, y2) = points[i], points[j]
                if x1 != x2 and y1 != y2 and (x1, y2) in st and (x2, y1) in st:
                    area = min(area, abs((x1 - x2) * (y1 - y2)))
        return 0 if area == float(inf) else area


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
    print(ans)
