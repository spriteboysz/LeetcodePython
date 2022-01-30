#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 23:32:32
LastEditTime: 2022-01-30 23:41:48
Description: 
FilePath: 1232.缀点成线.py
'''
#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = a * x + b
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        for i in range(2, len(coordinates)):
            if coordinates[i][1] - a * coordinates[i][0] - b > 0.001:
                return False
        return True
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.checkStraightLine(
        [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(s.checkStraightLine(
        [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
