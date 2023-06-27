#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 14:29:31
LastEditTime: 2022-02-04 14:54:04
Description:
FilePath: 100275.数组中重复的数字.py
"""
#
# @lc app=leetcode.cn id=100275 lang=python3
#
# [剑指 Offer 03] 数组中重复的数字
#

# @lc code=start
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        number = set()
        for num in nums:
            if num in number:
                return num
            else:
                number.add(num)
        return -1
# @lc code=end
