#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 18:01:16
LastEditTime: 2022-02-12 18:04:23
Description: 
FilePath: 1637.两点之间不包含任何点的最宽垂直面积.py
'''
#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        width = list(sorted(map(lambda el: el[0], points)))
        maximum = 0
        for i in range(1, len(width)):
            maximum = max(maximum, width[i] - width[i - 1])
        return maximum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxWidthOfVerticalArea(
        [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
