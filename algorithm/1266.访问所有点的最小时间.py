#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-27 23:54:33
LastEditTime: 2022-01-28 00:10:26
Description: 
FilePath: 1266.访问所有点的最小时间.py
'''
#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
from typing import List


class Solution:
    def calcDistance(self, point1, point2):
        return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points) - 1):
            count += self.calcDistance(points[i], points[i + 1])

        return count


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
    print(s.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
