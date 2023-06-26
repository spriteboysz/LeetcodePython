#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 22:35:32
LastEditTime: 2022-01-28 22:43:21
Description:
FilePath: 821.字符的最短距离.py
"""
#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        position = []
        for i, item in enumerate(s):
            if item == c:
                position.append(i)
        shortest = []
        for i, item in enumerate(s):
            shortest.append(min(map(lambda el: abs(el - i), position)))
        return shortest
# @lc code=end
