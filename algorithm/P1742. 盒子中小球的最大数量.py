#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 22:25:13
LastEditTime: 2022-01-30 22:27:19
Description:
FilePath: 1742.盒子中小球的最大数量.py
"""
#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#

# @lc code=start


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = [0] * 50
        for i in range(lowLimit, highLimit + 1):
            box[sum(map(int, str(i)))] += 1
        return max(box)
# @lc code=end
