#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 23:49:06
LastEditTime: 2022-01-27 23:52:30
Description:
FilePath: 1287.有序数组中出现次数超过-25-的元素.py
"""
#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for item in set(arr):
            if arr.count(item) > n / 4:
                return item
# @lc code=end
