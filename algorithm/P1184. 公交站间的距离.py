#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 21:40:03
LastEditTime: 2022-01-28 21:43:40
Description:
FilePath: 1184.公交站间的距离.py
"""
#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        dis = sum(distance[start:destination])
        return min(dis, sum(distance) - dis)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 2))
    print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 3))
