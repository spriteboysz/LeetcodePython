#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 22:15:30
LastEditTime: 2022-02-10 22:24:44
Description:
FilePath: 1503.所有蚂蚁掉下来前的最后一刻.py
"""
#
# @lc app=leetcode.cn id=1503 lang=python3
#
# [1503] 所有蚂蚁掉下来前的最后一刻
#

from math import inf
# @lc code=start
from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.append(0)
        right.append(inf)
        return max(max(left), n - min(right))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.getLastMoment(4, [4, 3], [0, 1]))
    print(s.getLastMoment(7, [], [0, 1, 2, 3, 4, 5, 6, 7]))
    print(s.getLastMoment(7, [0, 1, 2, 3, 4, 5, 6, 7], []))
    print(s.getLastMoment(9, [5], [4]))
    print(s.getLastMoment(6, [6], [0]))
