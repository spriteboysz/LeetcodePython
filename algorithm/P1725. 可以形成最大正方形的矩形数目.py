#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 18:25:40
LastEditTime: 2022-01-23 18:27:36
Description:
FilePath: 1725.可以形成最大正方形的矩形数目.py
"""
#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#

# @lc code=start
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        side = list(map(lambda el: min(el), rectangles))
        return side.count(max(side))

# @lc code=end
