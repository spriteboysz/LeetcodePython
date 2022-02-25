#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-25 23:09:33
LastEditTime: 2022-02-25 23:15:42
Description: 
FilePath: 2120.执行所有后缀指令.py
"""
#
# @lc app=leetcode.cn id=2120 lang=python3
#
# [2120] 执行所有后缀指令
#

# @lc code=start
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        counts = [0] * len(s)
        direction = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        for i in range(len(s)):
            x, y = startPos
            for operator in s[i:]:
                x, y = x + direction[operator][0], y + direction[operator][1]
                if 0 <= x < n and 0 <= y < n:
                    counts[i] += 1
                else:
                    break
        return counts


# @lc code=end
