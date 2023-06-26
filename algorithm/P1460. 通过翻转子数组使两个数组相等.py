#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:09:57
LastEditTime: 2022-01-25 23:10:35
Description:
FilePath: 1460.通过翻转子数组使两个数组相等.py
"""
#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#

# @lc code=start
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
# @lc code=end
