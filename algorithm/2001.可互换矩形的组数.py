#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-11 23:49:14
LastEditTime: 2022-02-11 23:55:39
Description: 
FilePath: 2001.可互换矩形的组数.py
'''
#
# @lc app=leetcode.cn id=2001 lang=python3
#
# [2001] 可互换矩形的组数
#

# @lc code=start
from typing import List
from math import gcd
from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = defaultdict(int)
        for item in rectangles:
            counts[(item[0]//gcd(*item), item[1]//gcd(*item))] += 1
        count = 0
        for item in filter(lambda el: el > 1, counts.values()):
            count += item * (item - 1)
        return count // 2
# @lc code=end
