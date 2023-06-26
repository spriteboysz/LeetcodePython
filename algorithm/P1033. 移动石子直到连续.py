#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 22:06:56
LastEditTime: 2022-02-10 22:12:16
Description:
FilePath: 1033.移动石子直到连续.py
"""
#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

# @lc code=start
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if c - a == 2:
            minimum = 0
        elif c - b <= 2 or b - a <= 2:
            minimum = 1
        else:
            minimum = 2
        return [minimum, c - a - 2]
# @lc code=end
