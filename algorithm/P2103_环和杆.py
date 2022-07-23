#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-21 22:12:37
LastEditTime: 2022-01-21 22:25:42
Description: 
FilePath: 2103.环和杆.py
'''
#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#

# @lc code=start


class Solution:
    def countPoints(self, rings: str) -> int:
        rod = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            rod[int(rings[int(i + 1)])].add(rings[int(i)])
        return list(map(len, rod)).count(3)

# @lc code=end
