#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-21 22:50:09
LastEditTime: 2022-03-21 22:51:54
Description:
FilePath: 41.缺失的第一个正数.py
"""
#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

from math import inf
# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minimum = inf
        for num in filter(lambda el: el > 0, nums):
            minimum = min(minimum, num)
        return minimum - 1
# @lc code=end
