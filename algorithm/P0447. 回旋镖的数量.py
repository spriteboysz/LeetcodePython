#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 22:21:27
LastEditTime: 2022-02-26 22:27:32
Description: 
FilePath: 447.回旋镖的数量.py
"""
#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

from collections import defaultdict
# @lc code=start
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance2(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        count = 0
        for i in range(len(points)):
            dis = defaultdict(int)
            for j in range(len(points)):
                dis[distance2(points[i], points[j])] += 1
            for v in dis.values():
                count += v * (v - 1)
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numberOfBoomerangs(points=[[0, 0], [1, 0], [2, 0]])
    print(ans)
