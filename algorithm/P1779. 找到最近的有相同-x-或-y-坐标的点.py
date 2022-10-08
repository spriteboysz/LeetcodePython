#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-01 22:42:01
LastEditTime: 2022-02-01 22:54:02
Description: 
FilePath: 1779.找到最近的有相同-x-或-y-坐标的点.py
'''
#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid = list(filter(lambda el: el[0] == x or el[1] == y, points))
        if len(valid) == 0:
            return -1
        else:
            distance = list(
                map(lambda el: abs(el[0] - x) + abs(el[1] - y), valid))
            return points.index(valid[distance.index(min(distance))])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.nearestValidPoint(x=3, y=4, points=[[3, 4]]))
    print(s.nearestValidPoint(x=3, y=4, points=[[2, 3]]))
