#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:11
FileName: LCP
Description:LCR 035. 最小时间差.py 
"""
from typing import List


class Solution:
    def findMinDifference(self, time_points: List[str]) -> int:
        if len(set(time_points)) < len(time_points):
            return 0
        minutes = list(
            sorted(map(lambda el: int(el[0]) * 600 + int(el[1]) * 60 + int(el[3]) * 10 + int(el[4]), time_points)))
        minimum = 1440
        for i in range(len(time_points) - 1):
            minimum = min(minimum, minutes[i + 1] - minutes[i])
        return min(minimum, minutes[0] + 1440 - minutes[-1])


if __name__ == '__main__':
    print(Solution().findMinDifference(time_points=["00:00", "23:59", "00:00"]))
    print(Solution().findMinDifference(time_points=["00:10", "23:59", "00:00"]))
